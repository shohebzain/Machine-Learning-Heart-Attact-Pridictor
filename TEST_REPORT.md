# Heart Attack Prediction - ML Model Test Report

**Generated:** 2026-05-11 21:08:54  
**Overall Status:** ✅ ALL TESTS PASSED  
**Tests:** 31/31 passed

---

## 1. Model Training Summary 

| Parameter | Value |
|-----------|-------|
| Algorithm | Support Vector Machine (SVM) |
| Kernel | RBF (Radial Basis Function) |
| C | 1.0 |
| Gamma | scale |
| Training Samples | 240 |
| Test Samples | 60 |
| Total Features | 13 |
| Class Distribution | 53 Low Risk / 247 High Risk |

### Features Used
| # | Feature | Description |
|---|---------|-------------|
| 1 | age | Patient age in years |
| 2 | sex | Sex (0=Female, 1=Male) |
| 3 | cp | Chest pain type (0-3) |
| 4 | trestbps | Resting blood pressure (mmHg) |
| 5 | chol | Serum cholesterol (mg/dl) |
| 6 | fbs | Fasting blood sugar > 120 mg/dl |
| 7 | restecg | Resting ECG results (0-2) |
| 8 | thalach | Maximum heart rate achieved |
| 9 | exang | Exercise induced angina |
| 10 | oldpeak | ST depression induced by exercise |
| 11 | slope | Slope of peak exercise ST segment |
| 12 | ca | Number of major vessels (0-3) |
| 13 | thal | Thalassemia type (0-2) |

---

## 2. Model Performance Metrics

| Metric | Score |
|--------|-------|
| **Accuracy** | 88.33% |
| **Precision** | 87.93% |
| **Recall** | 100.00% |
| **F1-Score** | 93.58% |
| **AUC-ROC** | 0.8780 |

### Cross-Validation (5-Fold)
| Fold | Accuracy |
|------|----------|
| Fold 1 | 85.00% |
| Fold 2 | 90.00% |
| Fold 3 | 86.67% |
| Fold 4 | 81.67% |
| Fold 5 | 86.67% |
| **Mean ± Std** | **86.00% ± 2.71%** |

### Confusion Matrix
|  | Predicted Low Risk | Predicted High Risk |
|--|-------------------|-------------------|
| **Actual Low Risk** | 2 (TN) | 7 (FP) |
| **Actual High Risk** | 0 (FN) | 51 (TP) |

### Per-Class Report
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Low Risk | 100.00% | 22.22% | 36.36% | 9 |
| High Risk | 87.93% | 100.00% | 93.58% | 51 |

---

## 3. Test Results

### Unit Tests
| # | Test | Status | Details |
|---|------|--------|---------|
| 1 | File exists: SVM_heart.pkt | ✅ |  |
| 2 | File exists: columns.pkl | ✅ |  |
| 3 | File exists: scaler.pkl | ✅ |  |
| 4 | File exists: df_encode.pkl | ✅ |  |
| 5 | Model pickle loads | ✅ | SVC |
| 6 | Columns pickle loads | ✅ | 13 columns |
| 7 | Scaler pickle loads | ✅ | StandardScaler |
| 8 | Column count = 13 features | ✅ | got 13 |
| 9 | Prediction returns 0 or 1 | ✅ | got 0 |
| 10 | Probabilities sum to 1 | ✅ | sum=1.0000 |
| 11 | High-risk patient detected | ✅ | prediction=1 |
| 12 | Low-risk patient detected | ✅ | prediction=0 |
| 13 | Edge case: min values | ✅ |  |
| 14 | Edge case: max values | ✅ |  |
| 15 | Batch prediction (10 samples) | ✅ | got 10 results |
| 16 | Flask app imports | ✅ |  |
| 17 | Flask app instance exists | ✅ |  |
| 18 | Model loaded in app | ✅ |  |
| 19 | Columns loaded in app | ✅ |  |
| 20 | Scaler loaded in app | ✅ |  |
| 21 | Route '/' registered | ✅ |  |
| 22 | Route '/predict' registered | ✅ |  |
| 23 | Route '/health' registered | ✅ |  |
| 24 | GET / returns 200 | ✅ |  |
| 25 | GET /health returns 200 | ✅ |  |
| 26 | POST /predict valid data returns 200 | ✅ |  |
| 27 | Response has 'prediction' | ✅ |  |
| 28 | Response has 'risk_percentage' | ✅ |  |
| 29 | Response has 'message' | ✅ |  |
| 30 | Missing fields returns error | ✅ |  |
| 31 | Invalid values returns error | ✅ |  |

### Summary
- **Total Tests:** 31
- **Passed:** 31 ✅
- **Failed:** 0 
- **Pass Rate:** 100.0%

---

## 4. Sample Predictions

| Patient Profile | Age | Sex | BP | Chol | HR | Prediction | Risk |
|----------------|-----|-----|-----|------|-----|------------|------|
| Healthy Young Female | 30 | F | 110 | 180 | 170 | 0 | Low |
| Middle-aged Male | 45 | M | 130 | 220 | 130 | 0 | Low |
| High-risk Elder | 70 | M | 180 | 350 | 80 | 1 | High |

---

## 5. File Verification

| File | Size | Status |
|------|------|--------|
| SVM_heart.pkt | 17,150 bytes | ✅ |
| columns.pkl | 115 bytes | ✅ |
| scaler.pkl | 914 bytes | ✅ |
| df_encode.pkl | 45 bytes | ✅ |
| app.py | 3,317 bytes | ✅ |
| templates/index.html | 8,152 bytes | ✅ |
| static/style.css | 4,461 bytes | ✅ |
| static/script.js | 3,959 bytes | ✅ |
| requirements.txt | 50 bytes | ✅ |

---

## 6. Conclusion

The Heart Attack Prediction ML model has been **successfully trained, tested, and validated**.

- **Model Accuracy:** 88.33% on test data
- **Cross-Validation:** 86.00% mean accuracy across 5 folds
- **All 31/31 tests passed** including unit tests, Flask API tests, and edge case tests
- **All model files** are generated and valid
- **Flask web application** is fully functional with proper error handling

### Recommendations
1. For production use, train on real clinical datasets (e.g., UCI Heart Disease dataset)
2. Consider ensemble methods (Random Forest, XGBoost) for improved accuracy
3. Add feature importance analysis for model interpretability
4. Implement periodic model retraining with new patient data

---

*Report generated automatically by run_tests_and_report.py*
