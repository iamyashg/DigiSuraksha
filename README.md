# Digi Suraksha - Cybersecurity Web Application

## ✨ Overview

Digi Suraksha is a web application designed to enhance cybersecurity awareness and provide users with tools to assess the safety of URLs. The application leverages the VirusTotal API to analyze URLs for potential threats, providing users with insights into the safety of websites they wish to visit.

## ✳️ Features

- **URL Analysis:** Users can input a URL, and the application retrieves information about the site's safety by querying the VirusTotal API.

- **Suspicious URL Detection:** The application identifies potentially suspicious URLs based on VirusTotal analysis results.

- **Crowdsourced Context:** Digi Suraksha incorporates crowdsourced information, offering additional insights into the cybersecurity status of a website.

- **Reporting Tool:** Users can contribute to the community by reporting suspicious websites through a dedicated form. The submitted data is collected in a Google Sheet for further analysis.

## 👨‍💻 Technologies Used

- **Backend:** Python with Flask web framework
- **Frontend:** HTML, CSS
- **API:** VirusTotal API for URL analysis
- **Charts:** Chart.js for visualizing analysis results
- **Google Sheets:** for collecting and managing reported URLs

## 🌐 Usage

Visit the [Digi Suraksha deployed on Render](https://digisuraksha.onrender.com/) to explore the application and analyze URLs.

## ☁️ Deployment

1. Clone the repository:

   ```bash
   git clone https://github.com/iamyashg/digi-suraksha.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your browser and go to [http://localhost:5000](http://localhost:5000) to access Digi Suraksha.

## 📸 Snapshots

### Home Page
![Home Page](https://github.com/iamyashg/DigiSuraksha/assets/72647281/9fe35971-7d5c-49c6-8619-2492b609636f)

### Results Page
![Results Page 1](https://github.com/iamyashg/DigiSuraksha/assets/72647281/b6660f1e-f5c4-4598-b359-eed27b7490dd)
![Results Page 2](https://github.com/iamyashg/DigiSuraksha/assets/72647281/d6b0dd0d-2dfb-4603-aceb-84120dabbee1)

### Report Page
![Report Page](https://github.com/iamyashg/DigiSuraksha/assets/72647281/3e600f13-d380-4c8d-ab56-35d92114a2d8)

## Contribution

- Cybersecurity Threats Page & Report Page Developed by [Vansh Sethi](https://github.com/vanshsethi23)

Contributions to Digi Suraksha are welcome! If you find a bug or have a feature request, please open an issue. If you'd like to contribute code, fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the [VirusTotal](https://www.virustotal.com) team for providing the API used in this project.
