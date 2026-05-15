# Heart Attack Risk Prediction Website

A web-based application that uses machine learning to predict the risk of heart attack based on patient medical data.

## Features

- 🤖 **Machine Learning Model**: Support Vector Machine (SVM) algorithm for accurate predictions
- 🎨 **Beautiful UI**: Modern, responsive design with gradient backgrounds
- 📊 **Risk Assessment**: Provides percentage-based risk scores
- 💻 **User-Friendly**: Intuitive form with medical field inputs
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile devices

## Project Structure

```
heart attack prediction/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── SVM_heart.pkt         # Trained SVM model
├── columns.pkl           # Feature column names
├── scaler.pkl            # Data scaler for normalization
├── df_encode.pkl         # Encoder for categorical variables
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Styling
    └── script.js         # Frontend logic
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project directory:**
   ```bash
   cd "d:\heart attact prediction"
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. **Enter patient information** and click "Predict Risk" to get the assessment

## Input Fields

- **Age**: Patient's age in years
- **Sex**: Male or Female
- **Chest Pain Type**: Type of chest pain experienced
- **Resting Blood Pressure**: In mmHg
- **Cholesterol**: In mg/dl
- **Fasting Blood Sugar**: Whether blood sugar > 120 mg/dl
- **Resting ECG Results**: ECG findings
- **Max Heart Rate Achieved**: During stress test
- **Exercise Induced Angina**: Whether exercise causes chest pain
- **ST Depression (oldpeak)**: ST segment depression
- **ST Slope**: Slope of ST segment
- **Coronary Artery Calcification**: Number of vessels affected
- **Thalassemia Type**: Blood disorder type

## Understanding Results

- **✅ Low Risk**: Less than 50% probability of heart attack
- **⚠️ High Risk**: 50% or greater probability of heart attack

## Medical Disclaimer

⚠️ **IMPORTANT**: This application is for educational and informational purposes only. It should NOT be used as a substitute for professional medical advice. Always consult with a qualified healthcare professional before making any medical decisions.

## Model Information

- **Algorithm**: Support Vector Machine (SVM)
- **Training Data**: Historical cardiac patient data
- **Performance**: Validated with comprehensive test datasets

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify the last line in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to different port
```

### Missing Model Files
Ensure all `.pkl` files are in the project root directory:
- `SVM_heart.pkt`
- `columns.pkl`
- `scaler.pkl`
- `df_encode.pkl`

### Dependencies Issues
Reinstall requirements:
```bash
pip install --upgrade -r requirements.txt
```

## Future Enhancements

- [ ] User authentication and patient records
- [ ] Historical data visualization
- [ ] Export reports as PDF
- [ ] Multi-language support
- [ ] Integration with health monitoring devices
- [ ] Database for storing predictions
- [ ] Advanced analytics dashboard

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, please review the troubleshooting section or consult the code comments.

---

**Built with**: Flask, scikit-learn, NumPy, and modern web technologies
