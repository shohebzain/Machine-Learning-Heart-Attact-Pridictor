# ❤️ Heart Attack Risk Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn)
![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

A web-based **Heart Attack Risk Prediction System** that leverages **Machine Learning** to estimate the probability of heart disease based on patient medical information. The application uses a trained **Support Vector Machine (SVM)** model and provides a simple, responsive interface for healthcare demonstrations, research, and educational purposes.

> **⚠️ Disclaimer:** This application is intended for educational and research purposes only and should not replace professional medical advice or diagnosis.

---

# 📖 Overview

The application accepts various clinical parameters, preprocesses the data using trained encoders and scalers, and predicts the likelihood of heart disease using a machine learning model. It demonstrates the integration of Machine Learning with a Flask-based web application.

---

# ✨ Features

* ❤️ Heart attack risk prediction
* 🤖 Machine Learning powered by Support Vector Machine (SVM)
* 📊 Percentage-based risk assessment
* 📋 Patient medical data input form
* 📱 Fully responsive interface
* ⚡ Fast Flask backend
* 🔄 Automated data preprocessing
* 🎨 Modern and user-friendly design

---

# 🛠️ Tech Stack

| Category             | Technologies            |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Backend              | Flask                   |
| Machine Learning     | Scikit-learn            |
| Data Processing      | NumPy, Pandas           |
| Frontend             | HTML5, CSS3, JavaScript |
| Model Serialization  | Pickle (.pkl)           |

---

# 📂 Project Structure

```text
Heart-Attack-Risk-Prediction/
│
├── app.py                  # Flask application
├── requirements.txt        # Dependencies
├── SVM_heart.pkl           # Trained ML model
├── scaler.pkl              # Feature scaler
├── columns.pkl             # Feature columns
├── df_encode.pkl           # Label encoder
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── README.md
└── LICENSE
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/yourusername/heart-attack-risk-prediction.git
```

Navigate to the project

```bash
cd heart-attack-risk-prediction
```

---

## Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open your browser:

```text
http://localhost:5000
```

---

# 🩺 Input Parameters

The prediction model uses the following medical attributes:

* Age
* Gender
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol Level
* Fasting Blood Sugar
* Resting ECG Results
* Maximum Heart Rate
* Exercise-Induced Angina
* ST Depression (Oldpeak)
* ST Segment Slope
* Number of Major Vessels
* Thalassemia Type

---

# 📊 Prediction Output

| Risk Level   | Description                 |
| ------------ | --------------------------- |
| ✅ Low Risk   | Probability below 50%       |
| ⚠️ High Risk | Probability of 50% or above |

The system displays:

* Risk percentage
* Prediction result
* User-friendly interface
* Easy-to-understand output

---

# 🧠 Machine Learning Pipeline

```text
Patient Data
      │
      ▼
Data Preprocessing
      │
      ▼
Encoding
      │
      ▼
Feature Scaling
      │
      ▼
SVM Prediction Model
      │
      ▼
Risk Percentage
      │
      ▼
Prediction Result
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* Machine Learning model deployment
* Flask web development
* Data preprocessing
* Feature scaling
* Model serialization
* User interface development
* Integration of AI with healthcare applications

---

# 🚀 Future Enhancements

* 🗄️ Database integration
* 👤 User authentication
* 📈 Patient history dashboard
* 📄 PDF medical reports
* 📱 Mobile application
* ☁️ Cloud deployment
* 🤖 Deep Learning models
* 📊 Explainable AI (XAI)
* 🌐 Multi-language support
* 🔔 Email and SMS notifications

---

# 📸 Screenshots

Include screenshots of:

* Home Page
* Patient Form
* Prediction Result
* Mobile View

---

# ⚠️ Medical Disclaimer

This project is intended **only for educational, research, and demonstration purposes**.

The predictions generated by this application **must not be used for clinical diagnosis or medical treatment decisions**. Always consult a qualified healthcare professional for medical advice.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developer

**Mohammad Shoheb**

* AI & Full-Stack Developer
* Python • Flask • Machine Learning • React
* Passionate about AI, Healthcare Technology, and Software Development

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork it

💡 Contribute improvements

🚀 Happy Coding!
