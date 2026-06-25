from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model and preprocessing files with error handling
model = None
columns = None
scaler = None
encoder = None

try:
    model_path = 'SVM_heart.pkt'
    with open(model_path, 'rb') as f: 
        model = pickle.load(f)
    
    columns_path = 'columns.pkl'
    with open(columns_path, 'rb') as f:
        columns = pickle.load(f)
    
    scaler_path = 'scaler.pkl'
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    
    encoder_path = 'df_encode.pkl'
    with open(encoder_path, 'rb') as f:
        encoder = pickle.load(f)
    
    print("[OK] All model files loaded successfully")
except FileNotFoundError as e:
    print(f"[ERROR] Missing model file - {e}")
except Exception as e:
    print(f"[ERROR] Loading model files - {e}")

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/predict-form')
def predict_form():
    return render_template('predict.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if model is loaded
        if model is None or columns is None or scaler is None:
            return jsonify({'error': 'Model not loaded. Please check server configuration.'}), 500
        
        data = request.json
        
        # Validate that all required columns are present
        missing_cols = [col for col in columns if col not in data]
        if missing_cols:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_cols)}'}), 400
        
        # Extract and validate features
        try:
            input_data = []
            for col in columns:
                value = float(data[col])
                input_data.append(value)
        except ValueError as e:
            return jsonify({'error': f'Invalid input values: All fields must be numeric. {str(e)}'}), 400
        
        # Convert to numpy array and reshape
        input_array = np.array(input_data).reshape(1, -1)
        
        # Scale the input
        scaled_input = scaler.transform(input_array)
        
        # Make prediction
        prediction = model.predict(scaled_input)[0]
        
        # Get probability/decision function
        try:
            probability = model.decision_function(scaled_input)[0]
        except:
            # Fallback if decision_function is not available
            probability = 0
        
        # Convert probability to percentage (safely)
        try:
            risk_percentage = (1 / (1 + np.exp(-probability))) * 100
            risk_percentage = max(0, min(100, risk_percentage))  # Clamp between 0-100
        except:
            risk_percentage = 50.0  # Default fallback
        
        result = {
            'prediction': int(prediction),
            'risk_percentage': round(risk_percentage, 2),
            'message': 'High Risk of Heart Attack' if prediction == 1 else 'Low Risk of Heart Attack'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
