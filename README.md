
# ❤️ Heart Failure Prediction App

A simple and interactive **Streamlit** web application to predict the likelihood of **heart failure** based on clinical features using a trained **XGBoost** model.

## 🚀 Overview

This app allows healthcare professionals or users to input key medical measurements:

- **Follow-up Period (time)** in days  
- **Ejection Fraction (%)** – the percentage of blood pumped out of the heart during each contraction  
- **Serum Creatinine (mg/dL)** – a measure of kidney function  

Based on these features, the app predicts whether the patient is at high or low risk of heart failure.

---

## 🔧 Technologies Used

- **Python**
- **Streamlit** – for web interface
- **XGBoostClassifier** – for the prediction model
- **RobustScaler** – to preprocess input data
- **Joblib** – to save and load the model and scaler

---

## 📁 Project Structure

```
heart_failure_app/
│
├── heart_failure_app.py          # Streamlit application
├── xgb_model.joblib              # Trained XGBoost model
├── robust_scaler.joblib          # Fitted RobustScaler
├── README.md                     # Project documentation
└── requirements.txt              # Required Python packages
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/heart-failure-predictor.git
cd heart-failure-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run heart_failure_app.py
```

---

## 📊 Model Details

- **Model**: XGBoost Classifier
- **Input Features**:
  - `time`
  - `ejection_fraction`
  - `serum_creatinine`
- **Preprocessing**: RobustScaler used to reduce the impact of outliers

---

## 📌 Example

![App Screenshot](https://via.placeholder.com/600x300.png?text=Insert+Your+Screenshot+Here)

---

## ✍️ Author

Ahmed Mohamed Kamel  
[LinkedIn](https://www.linkedin.com/) • [GitHub](https://github.com/)

---

## 📃 License

This project is open-source and available under the MIT License.
