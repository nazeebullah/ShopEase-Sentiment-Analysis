from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib, spacy, re

app = FastAPI(title="ShopEase Sentiment API")
nlp = spacy.load("en_core_web_sm")
try:
    classifier = joblib.load("../models/lr_model.pkl")
    vectorizer = joblib.load("../models/tfidf_vectorizer.pkl")
except:
    classifier, vectorizer = None, None

class SentimentRequest(BaseModel): text: str

def clean_and_lemmatize(text):
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", " ", str(text).lower())
    return " ".join([token.lemma_.strip() for token in nlp(text) if not token.is_stop and token.lemma_.strip()])

@app.post("/predict")
def predict(req: SentimentRequest):
    cleaned = clean_and_lemmatize(req.text)
    pred = classifier.predict(vectorizer.transform([cleaned]))[0] if cleaned else "neutral"
    return {"sentiment": pred}
