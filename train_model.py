"""
Heart Attack Prediction Model Training Script
Generates SVM model and preprocessing files for the web application
"""

import pickle
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Set random seed for reproducibility
np.random.seed(42)

print("=" * 60)
print("  Heart Attack Prediction Model Training")
print("=" * 60)

# Create synthetic training dataset based on UCI Heart Disease dataset
print("\n[1/5] Generating synthetic training data...")

n_samples = 300

# Generate realistic feature values
data = {
    'age': np.random.randint(29, 77, n_samples),
    'sex': np.random.randint(0, 2, n_samples),  # 0=Female, 1=Male
    'cp': np.random.randint(0, 4, n_samples),   # Chest Pain Type (0-3)
    'trestbps': np.random.randint(94, 200, n_samples),  # Resting BP
    'chol': np.random.randint(126, 564, n_samples),     # Cholesterol
    'fbs': np.random.randint(0, 2, n_samples),  # Fasting Blood Sugar
    'restecg': np.random.randint(0, 3, n_samples),      # Resting ECG (0-2)
    'thalach': np.random.randint(60, 202, n_samples),   # Max Heart Rate
    'exang': np.random.randint(0, 2, n_samples),        # Exercise Angina
    'oldpeak': np.random.uniform(0, 6.2, n_samples),    # ST Depression
    'slope': np.random.randint(0, 3, n_samples),        # ST Slope (0-2)
    'ca': np.random.randint(0, 4, n_samples),           # Coronary Artery Calc (0-3)
    'thal': np.random.randint(0, 3, n_samples),         # Thalassemia (0-2)
}

X = pd.DataFrame(data)

# Create target variable with realistic distribution
# Higher values of certain features correlate with higher risk
risk_score = (
    (X['age'] > 55) * 0.3 +
    (X['sex'] == 1) * 0.2 +
    (X['cp'] > 1) * 0.3 +
    (X['trestbps'] > 140) * 0.4 +
    (X['chol'] > 240) * 0.3 +
    (X['fbs'] == 1) * 0.2 +
    (X['restecg'] > 0) * 0.2 +
    (X['thalach'] < 100) * 0.3 +
    (X['exang'] == 1) * 0.4 +
    (X['oldpeak'] > 2) * 0.4 +
    (X['slope'] == 2) * 0.3 +
    (X['ca'] > 0) * 0.5 +
    (X['thal'] > 0) * 0.3 +
    np.random.uniform(0, 0.5, n_samples)  # Random noise
)

y = (risk_score > 2.0).astype(int)

print(f"✓ Generated {n_samples} samples with {len(data)} features")
print(f"  - Class distribution: {sum(y==0)} healthy, {sum(y==1)} at-risk")

# Split data
print("\n[2/5] Splitting data into train/test sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"✓ Training: {len(X_train)} samples, Testing: {len(X_test)} samples")

# Scale features
print("\n[3/5] Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✓ Features scaled using StandardScaler")

# Train SVM model
print("\n[4/5] Training SVM model...")
model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True)
model.fit(X_train_scaled, y_train)
print("✓ SVM model trained successfully")

# Evaluate model
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n  Model Performance:")
print(f"  - Accuracy: {accuracy:.2%}")
print(f"\n{classification_report(y_test, y_pred, target_names=['Low Risk', 'High Risk'])}")

# Save model files
print("\n[5/5] Saving model files...")

# Get column names
columns = list(X.columns)

# Save model
with open('SVM_heart.pkt', 'wb') as f:
    pickle.dump(model, f)
print("✓ SVM_heart.pkt saved")

# Save columns
with open('columns.pkl', 'wb') as f:
    pickle.dump(columns, f)
print("✓ columns.pkl saved")

# Save scaler
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print("✓ scaler.pkl saved")

# Create dummy encoder (for compatibility)
encoder = {'status': 'no_encoding_needed'}
with open('df_encode.pkl', 'wb') as f:
    pickle.dump(encoder, f)
print("✓ df_encode.pkl saved")

# Verify files
print("\n" + "=" * 60)
print("  File Verification")
print("=" * 60)

import os
files = ['SVM_heart.pkt', 'columns.pkl', 'scaler.pkl', 'df_encode.pkl']
for fname in files:
    if os.path.exists(fname):
        size = os.path.getsize(fname)
        print(f"✓ {fname:<20} ({size:>8} bytes)")
    else:
        print(f"✗ {fname:<20} FAILED")

print("\n" + "=" * 60)
print("  Training Complete!")
print("=" * 60)
print("\nThe model is ready for the Flask application.")
print("Start the server with: python app.py")
print("Access the web app at: http://localhost:5000")
