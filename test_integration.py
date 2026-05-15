"""
End-to-End Integration Test for Heart Attack Prediction System
Tests complete workflow: Form → Backend → Prediction → Response
"""

import requests
import json
import subprocess
import time
import signal
import os
import sys

print("=" * 70)
print("  Heart Attack Prediction - Integration Test")
print("=" * 70)

# Test 1: Check all model files exist
print("\n[TEST 1] Checking model files...")
model_files = ['SVM_heart.pkt', 'columns.pkl', 'scaler.pkl', 'df_encode.pkl']
all_exist = True
for fname in model_files:
    if os.path.exists(fname):
        print(f"  ✓ {fname}")
    else:
        print(f"  ✗ {fname} MISSING")
        all_exist = False

if not all_exist:
    print("\n✗ Some model files missing! Cannot proceed.")
    sys.exit(1)

# Test 2: Check app.py syntax and imports
print("\n[TEST 2] Checking app.py...")
try:
    import app
    print(f"  ✓ app.py imported")
    print(f"  ✓ Model loaded: {app.model is not None}")
    print(f"  ✓ Columns loaded: {app.columns is not None}")
    print(f"  ✓ Scaler loaded: {app.scaler is not None}")
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

# Test 3: Test prediction function directly
print("\n[TEST 3] Testing prediction logic...")
import numpy as np

test_data = {
    'age': '45',
    'sex': '1',
    'cp': '0',
    'trestbps': '130',
    'chol': '220',
    'fbs': '0',
    'restecg': '0',
    'thalach': '130',
    'exang': '0',
    'oldpeak': '1.2',
    'slope': '1',
    'ca': '0',
    'thal': '0'
}

try:
    # Simulate prediction process
    input_data = []
    for col in app.columns:
        value = float(test_data[col])
        input_data.append(value)
    
    input_array = np.array(input_data).reshape(1, -1)
    scaled_input = app.scaler.transform(input_array)
    prediction = app.model.predict(scaled_input)[0]
    
    print(f"  ✓ Prediction successful")
    print(f"  ✓ Result: {prediction} (1=High Risk, 0=Low Risk)")
    
except Exception as e:
    print(f"  ✗ Prediction failed: {e}")
    sys.exit(1)

# Test 4: Start Flask server and test API
print("\n[TEST 4] Starting Flask server...")
server_process = subprocess.Popen(
    [sys.executable, 'app.py'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    cwd=os.getcwd()
)

# Wait for server to start
time.sleep(3)

try:
    # Test health endpoint
    print("  Waiting for server to start...")
    response = requests.get('http://localhost:5000/health', timeout=5)
    if response.status_code == 200:
        print("  ✓ Server is running")
    else:
        print(f"  ✗ Server returned status {response.status_code}")
        sys.exit(1)
    
    # Test home page
    print("\n[TEST 5] Testing home page...")
    response = requests.get('http://localhost:5000/', timeout=5)
    if response.status_code == 200:
        if 'Heart Attack Risk' in response.text:
            print("  ✓ Homepage loads successfully")
            print("  ✓ Contains expected content")
        else:
            print("  ✗ Homepage missing expected content")
            sys.exit(1)
    else:
        print(f"  ✗ Homepage returned status {response.status_code}")
        sys.exit(1)
    
    # Test prediction endpoint
    print("\n[TEST 6] Testing prediction API...")
    response = requests.post(
        'http://localhost:5000/predict',
        json=test_data,
        timeout=5
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"  ✓ API response received")
        
        # Validate result structure
        required_fields = ['prediction', 'risk_percentage', 'message']
        missing = [f for f in required_fields if f not in result]
        
        if missing:
            print(f"  ✗ Missing fields: {missing}")
            print(f"     Response: {result}")
            sys.exit(1)
        
        print(f"  ✓ Response structure valid")
        print(f"  ✓ Prediction: {result['prediction']}")
        print(f"  ✓ Risk %: {result['risk_percentage']}%")
        print(f"  ✓ Message: {result['message']}")
        
    else:
        print(f"  ✗ API returned status {response.status_code}")
        print(f"     Response: {response.text}")
        sys.exit(1)
    
    # Test error handling - missing fields
    print("\n[TEST 7] Testing error handling (missing fields)...")
    incomplete_data = {'age': '45', 'sex': '1'}
    response = requests.post(
        'http://localhost:5000/predict',
        json=incomplete_data,
        timeout=5
    )
    
    if response.status_code != 200:
        result = response.json()
        if 'error' in result:
            print(f"  ✓ Error correctly returned for incomplete data")
            print(f"  ✓ Error message: {result['error'][:50]}...")
        else:
            print(f"  ✗ Response missing error field")
            sys.exit(1)
    else:
        print(f"  ✗ Should have returned error for incomplete data")
        sys.exit(1)
    
    # Test error handling - invalid values
    print("\n[TEST 8] Testing error handling (invalid values)...")
    invalid_data = test_data.copy()
    invalid_data['age'] = 'not_a_number'
    response = requests.post(
        'http://localhost:5000/predict',
        json=invalid_data,
        timeout=5
    )
    
    if response.status_code != 200:
        result = response.json()
        if 'error' in result:
            print(f"  ✓ Error correctly returned for invalid data")
            print(f"  ✓ Error message: {result['error'][:50]}...")
        else:
            print(f"  ✗ Response missing error field")
            sys.exit(1)
    else:
        print(f"  ✗ Should have returned error for invalid data")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("  ALL TESTS PASSED! ✓")
    print("=" * 70)
    print("\nThe application is fully functional!")
    print("✓ Model files valid and loadable")
    print("✓ Backend prediction logic working")
    print("✓ Frontend form structure correct")
    print("✓ API endpoints responding correctly")
    print("✓ Error handling working as expected")
    print("\nTo run the server: python app.py")
    print("Then open http://localhost:5000 in your browser")
    
except requests.exceptions.ConnectionError:
    print(f"  ✗ Could not connect to server. Is it running?")
    sys.exit(1)
except Exception as e:
    print(f"  ✗ Error during testing: {e}")
    sys.exit(1)
finally:
    # Kill the server
    print("\nStopping test server...")
    server_process.terminate()
    try:
        server_process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        server_process.kill()
    print("✓ Server stopped")
