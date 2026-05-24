# 🏥 Hospital Appointment No-Show Prediction System

## 📌 Project Overview
This project is a machine learning-based web application designed to predict whether a patient will miss their hospital appointment ("No-Show") based on historical appointment data and patient attributes.

The system helps hospitals reduce missed appointments, optimize scheduling, and improve healthcare resource management.

---

## 🎯 Objective
The main goal of this project is to build a predictive model that identifies patients who are likely to not attend their scheduled appointments using features such as:

- Age
- Gender
- Neighborhood
- Medical conditions (Hypertension, Diabetes, Alcoholism, Handicap)
- SMS reminders
- Waiting time
- Appointment day
- Socio-economic indicators (Scholarship)

---

## 🧠 Machine Learning Approach

### 📊 Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Feature engineering (e.g., Age Groups, Waiting Days)
- Data normalization where required

### 🤖 Models Used
- Random Forest Classifier
- Decision Tree Classifier
- StandardScaler for feature scaling

### 📈 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## 🌐 Web Application (Flask)
A Flask-based web application was developed to provide an interactive user interface.

### Features:
- User input form for patient details
- Real-time prediction of no-show probability
- Simple and clean UI using HTML templates

### Technologies:
- Python
- Flask
- HTML / CSS
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📷 Project Visualizations
The following visualizations were generated during analysis:

- Correlation Heatmap
- Count Plots (No-show distribution)
- Feature Importance Plot (from Random Forest)
- Data distribution graphs

---

## ⚠️ Important Notes
- The model is trained on historical data and predictions are probabilistic, not absolute.
- Model version compatibility between scikit-learn versions may affect loading saved models.

---

## 👨‍💻 Authors
- **Omar Hisham**

- **Under Supervision of:**
  - Dr. Mohamed El Sayah

---

## 🚀 How to Run the Project

```bash
pip install -r requirements.txt
python app.py
