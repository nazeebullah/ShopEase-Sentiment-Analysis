import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Create a mini dataset
texts = [
    "I absolutely love this, it is amazing, wonderful, perfect, highly recommend!",
    "Terrible, broken, worst thing ever, late delivery, nightmare, hate it.",
    "It is okay, average, does the job, fine, not bad."
]
labels = ["positive", "negative", "neutral"]

# 2. Train a fresh model
print("Training new models for Python 3.12...")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

classifier = LogisticRegression()
classifier.fit(X, labels)

# 3. Save them into the models folder
os.makedirs("models", exist_ok=True)
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
joblib.dump(classifier, "models/lr_model.pkl")
print("✅ Models successfully fixed and saved!")