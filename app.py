import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('trained_model.sav','rb'))

st.set_page_config(page_title="Heating Load Prediction", page_icon="🔥", layout="centered")

st.title("Heating Load Prediction (y1)")
st.write("Predict **Heating Load (y1)** using building features")


X1 = st.number_input("Relative Compactness (X1)", value=0.75, min_value=0.0)
X3 = st.number_input("Wall Area (X3)", value=200.0, min_value=0.0)
X5 = st.number_input("Overall Height (X5)", value=3.5, min_value=0.0)
X6 = st.number_input("Orientation (X6)", value=2, min_value=0, max_value=4, step=1)
X7 = st.number_input("Glazing Area (X7)", value=0.25, min_value=0.0, max_value=1.0)
X8 = st.number_input("Glazing Area Distribution (X8)", value=3, min_value=0, max_value=5, step=1)


features = np.array([[X1, X3, X5, X6, X7, X8]])


if st.button("Predict Heating Load (y1)"):
    prediction = model.predict(features)
    st.success(f"Predicted Heating Load (y1): **{prediction[0]:.4f}**")
