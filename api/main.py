from fastapi import FastAPI
from pydantic import BaseModel
import joblib, spacy, re

app = FastAPI(title="ShopEase Sentiment API")
nlp = spacy.load("en_core_web_sm")

# FIXED PATHS: Look directly into the models folder from the root
try:
    classifier = joblib.load("models/lr_model.pkl")
    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
    print("✅ Models loaded successfully!")
except Exception as e:
    print(f"❌ Error loading models: {e}")
    classifier, vectorizer = None, None

class SentimentRequest(BaseModel): text: str

def clean_and_lemmatize(text):
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", " ", str(text).lower())
    return " ".join([token.lemma_.strip() for token in nlp(text) if not token.is_stop and token.lemma_.strip()])

@app.post("/predict")
def predict(req: SentimentRequest):
    if classifier is None:
        return {"sentiment": "Error: Models missing or path is wrong!"}
    
    cleaned = clean_and_lemmatize(req.text)
    pred = classifier.predict(vectorizer.transform([cleaned]))[0] if cleaned else "neutral"
    return {"sentiment": pred}