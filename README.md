# 🛍️ ShopEase: Customer Sentiment Analysis System

## 📖 Project Overview
This project is an end-to-end Machine Learning pipeline that automatically classifies customer feedback into **Positive**, **Neutral**, or **Negative** sentiments.

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
