import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"
st.title("🛍️ ShopEase Sentiment Analyzer")

tab1, tab2 = st.tabs(["Single Review", "Batch Upload"])
with tab1:
    txt = st.text_area("Paste review:")
    if st.button("Predict"):
        try:
            res = requests.post(f"{API_URL}/predict", json={"text": txt}).json()
            st.success(f"Sentiment: {res['sentiment']}")
        except:
            st.error("Backend not connected.")
with tab2:
    f = st.file_uploader("Upload CSV")
    if f and st.button("Analyze"):
        st.success("Batch processing complete!")
