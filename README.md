# 🛍️ ShopEase Sentiment Analysis System

## 📖 Project Overview

This project is an end-to-end Machine Learning application that analyzes customer reviews and classifies them into sentiments such as **Positive, Neutral, or Negative**.

The system is designed to simulate a real-world production pipeline where a trained model is tracked, deployed, and consumed through an API and user interface.

---

## 🚀 Features

* Real-time sentiment prediction
* Batch analysis via CSV upload
* MLflow model tracking using DagsHub
* REST API built with FastAPI
* Interactive UI using Streamlit
* Transformer-based NLP model (DistilBERT)

---

## 🏗️ System Architecture

```text
Streamlit UI → FastAPI → MLflow (DagsHub) → Model → Prediction
```

### Components:

* **Frontend:** Streamlit interface for entering reviews and uploading datasets
* **Backend:** FastAPI serving predictions through `/predict` endpoint
* **Model Tracking:** MLflow integrated with DagsHub for versioning and experiment tracking
* **Model:** Transformer-based sentiment model (DistilBERT)

---

## ⚙️ How to Run the Application

### 1. Clone the repository

```bash
git clone https://github.com/nazeebullah/ShopEase-Sentiment-Analysis.git
cd ShopEase-Sentiment-Analysis
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn streamlit mlflow dagshub transformers torch pandas requests
```

---

### 4. Run FastAPI backend

```bash
python -m uvicorn myapi.main:app --reload
```

---

### 5. Run Streamlit UI (new terminal)

```bash
streamlit run ui/streamlit_app.py
```

---

## 🌐 Access the Application

* API Docs: http://127.0.0.1:8000/docs
* UI: http://localhost:8501

---

## 📊 Example Output

Input:

```
This product is amazing
```

Output:

```
Positive (confidence ~0.99)
```

---

## 💼 Business Impact

* **Automated Feedback Analysis:** Instantly classify thousands of customer reviews
* **Improved Customer Experience:** Quickly identify negative sentiment and respond faster
* **Data-Driven Decisions:** Helps businesses understand customer perception at scale

---

## 🧠 Tech Stack

* Python
* FastAPI
* Streamlit
* MLflow
* DagsHub
* HuggingFace Transformers

---

## 📌 Author

**Nazeeb Ullah**
