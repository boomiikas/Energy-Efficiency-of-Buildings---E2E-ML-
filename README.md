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

## 📊 Exploratory Data Analysis (EDA)

To better understand the dataset before model training, we performed **EDA** using visualizations:

### 🔹 1. Feature Distributions (KDE Plots)  
- Kernel Density Estimation (KDE) plots were created for features: **X1–X8**.  
- These plots help visualize the **probability density** of each feature and check whether features are normally distributed or skewed.  
- **Key insights:**
  - Some features (like `X1` and `X5`) show concentrated distributions.  
  - Features like `X3` and `X4` are more spread out, indicating larger variability.
    <img width="1986" height="989" alt="image" src="https://github.com/user-attachments/assets/8982a7ac-294d-4110-bd35-dbe2765941f1" />
 

---

### 🔹 2. Outlier Detection (Box Plots)  
- Box plots were generated for **X1–X8** to detect potential **outliers**.  
- Outliers can increase residual errors in regression models, so this step helps identify values that may need scaling, transformation, or capping.  
<img width="1989" height="989" alt="image" src="https://github.com/user-attachments/assets/09de7f2e-48ba-4d21-9f7f-80b2b8b35ce3" />

---

### 🔹 3. Correlation Heatmap  
- A **heatmap of feature correlations** was plotted to analyze relationships among variables.  
- **Key findings:**
  - `X1 (Relative Compactness)` is negatively correlated with `X2 (Surface Area)` and `X3 (Wall Area)`.  
  - Strong correlations indicate possible **multicollinearity**, which should be considered in feature selection or dimensionality reduction.  
  - Target variable `y1 (Heating Load)` shows stronger dependency on features like `X1`, `X5`, and glazing-related variables.
    <img width="536" height="418" alt="image" src="https://github.com/user-attachments/assets/22d16dff-cce1-4d7b-8358-2d13ad91dd32" />


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
