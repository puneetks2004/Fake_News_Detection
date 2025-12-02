# src/predict.py
import os
import pickle
import re
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))

MODELS_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

with open(os.path.join(MODELS_DIR, "tfidf.pkl"), "rb") as f:
    tfidf = pickle.load(f)
with open(os.path.join(MODELS_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

def clean_text(text):
    text = str(text).lower()
    tokens = text.split()
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    return " ".join(tokens)

def predict(text):
    c = clean_text(text)
    v = tfidf.transform([c])
    pred = model.predict(v)[0]
    proba = model.predict_proba(v)[0].max() if hasattr(model, "predict_proba") else None
    label = "REAL" if pred == 1 else "FAKE"
    return {"label": label, "probability": float(proba) if proba is not None else None}

if __name__ == "__main__":
    sample = "President announced a new stimulus package for students."
    print(predict(sample))
