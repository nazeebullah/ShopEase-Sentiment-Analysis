# 🛍️ ShopEase: Customer Sentiment Analysis System

## 📖 Project Overview
This project is an end-to-end Machine Learning pipeline that automatically classifies customer feedback into **Positive**, **Neutral**, or **Negative** sentiments, allowing the business to quickly identify areas for product and service improvements.

## 🚀 How to Run the Application
1. Install dependencies: `pip install -r requirements.txt`
2. Download NLP model: `python -m spacy download en_core_web_sm`
3. Start the API: `cd api && uvicorn main:app --reload`
4. Start the UI: `cd ui && streamlit run app.py`

## 🐳 Docker Deployment
This application is fully containerized. You can pull and run the backend API from anywhere using Docker.

**1. Pull the image from Docker Hub:**
`docker pull nazeeb3776/shopease-api:latest`

**2. Run the container:**
`docker run -p 8000:8000 nazeeb3776/shopease-api:latest`

The API will instantly be available at `http://localhost:8000`.

## 🏗️ System Architecture
This project implements a decoupled, microservices-style architecture:
* **Frontend:** Streamlit provides an intuitive web interface for customer service reps to input text or upload batch CSV files.
* **Backend:** FastAPI serves the machine learning model via RESTful endpoints (`/predict`).
* **Machine Learning:** `scikit-learn` and `spaCy` process text and predict sentiment using a trained Logistic Regression model and TF-IDF vectorization.
* **Deployment:** The backend is fully containerized using **Docker**, ensuring consistency across development and production environments.

## 💼 Business Impact
By deploying the ShopEase Sentiment Analysis System, the business achieves:
1. **Automated Triage:** Thousands of daily reviews are instantly categorized without manual human reading.
2. **Rapid Issue Resolution:** Negative feedback is immediately flagged, allowing customer service to prioritize dissatisfied customers and prevent churn.
3. **Data-Driven Product Improvement:** Aggregated sentiment data provides the product team with quantifiable metrics on how new releases are received by the market.
