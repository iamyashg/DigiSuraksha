from flask import Flask, render_template, request
from urllib.parse import urlparse
from datetime import datetime
import requests
import time

app = Flask(__name__)

def is_suspicious_url(virustotal_data):
    if virustotal_data:
        analysis_stats = virustotal_data.get('attributes', {}).get('last_analysis_stats', {})
        return analysis_stats.get('malicious', 0) > 2 or analysis_stats.get('suspicious', 0) > 2
    return False

def get_virustotal_data(url):
    headers = {
        'authority': 'www.virustotal.com',
        'accept': 'application/json',
        'accept-ianguage': 'en-US,en;q=0.9,es;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://www.virustotal.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-app-version': 'v1x246x0',
        'x-tool': 'vt-ui-main',
        'x-vt-anti-abuse-header': 'MTU3MTQ1NDMxNzQtWkc5dWRDQmlaU0JsZG1scy0xNzA3OTAxNDcyLjM3Nw==',
    }

    data = {
        'url': url,
    }

    response = requests.post('https://www.virustotal.com/ui/urls', headers=headers, data=data)

    if response.status_code == 200:
        params = {
            'limit': '20',
            'relationships[comment]': 'author,item',
            'query': url,
        }

        retry_count = 0
        while retry_count < 5:
            response = requests.get('https://www.virustotal.com/ui/search', params=params, headers=headers)

            if response.status_code == 200:
                result_data = response.json().get('data')
                if result_data:
                    analysis_result = result_data[0].get('attributes', {}).get('last_analysis_results', {})
                    if not analysis_result:
                        print("Analyzing the URL...")
                        return {'analyzing': True}
                    else:
                        return result_data[0]
                elif not result_data:
                    print("Analyzing the URL...")
                    return {'analyzing': True}
            else:
                print("Analyzing the URL...")
                return {'analyzing': True}
            retry_count += 1
            time.sleep(10)

    return None


def timestampformat(value, format='%d/%m/%Y'):
    if isinstance(value, int):
        value = datetime.utcfromtimestamp(value)

    if value is None:
        return ''
    return value.strftime(format)

app.jinja_env.filters['timestampformat'] = timestampformat

def normalize_url(url):
    parsed_url = urlparse(url)
  
    if parsed_url.scheme and parsed_url.netloc.startswith('www.'):
        return url

    if not parsed_url.scheme:
        url = 'http://' + url
    return url

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cyberthreats')
def cyberthreats():
    return render_template('cyberthreats.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/check_url', methods=['POST'])
def check_url():
    raw_url = request.form['url']
    url = normalize_url(raw_url)
    virustotal_data = get_virustotal_data(url)
  
    if virustotal_data and 'analyzing' in virustotal_data:
      return render_template('index.html', analyzing=True)

    is_suspicious = is_suspicious_url(virustotal_data)

    return render_template('result.html', url=url, is_suspicious=is_suspicious, response_data=virustotal_data)

if __name__ == '__main__':
    app.run(debug=True)
