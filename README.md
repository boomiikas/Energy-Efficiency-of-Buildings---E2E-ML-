# 🏠 Energy Efficiency Prediction App

This project is a **Streamlit web application** that predicts **Heating Load (Y1)** using an optimized **XGBoost Regressor** model.  
The dataset includes building characteristics such as compactness, wall area, roof area, and glazing properties.

---

## 📊 Features Used
- **X1 Relative Compactness**
- **X3 Wall Area**
- **X5 Overall Height**
- **X6 Orientation**
- **X7 Glazing Area**
- **X8 Glazing Area Distribution**

## 🎯 Target Variable
- **Y1 Heating Load**

---

## 🚀 Tech Stack
- **Python**
- **Scikit-learn**
- **XGBoost**
- **Streamlit**
- **Pickle** (for model deployment)

---

## 📌 How to Run the App

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd <your-repo-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Live App Link
[Energy Efficiency Prediction App](https://energy-efficiency-prediction-b5.streamlit.app/)

---

## 🖼️ App Screenshot
<img width="867" height="755" alt="image" src="https://github.com/user-attachments/assets/61c4c416-c61b-48b4-bd12-76539ea198a1" />


## 📈 Model Performance
- **Best Model:** XGBoost Regressor
- **MSE:** ~1.93
- **R² Score:** ~0.97

---

## 📂 Project Structure
```
├── app.py              # Streamlit app
├── model.pkl           # Trained XGBoost model
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ✨ Future Enhancements
- Add prediction for **Cooling Load (Y2)**
- Deploy app on **Streamlit Cloud / AWS / Azure**
- Add visualizations for energy efficiency insights
