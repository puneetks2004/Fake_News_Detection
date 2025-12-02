# src/train.py
import os
import pandas as pd
import numpy as np
import nltk
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- 1) load dataset ---
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
fake = pd.read_csv(os.path.join(DATA_DIR, "Fake.csv"))
true = pd.read_csv(os.path.join(DATA_DIR, "True.csv"))

# If CSVs don't have 'text' column but 'title' exists, combine
def get_text_column(df):
    if "text" in df.columns:
        return df["text"].astype(str)
    if "title" in df.columns:
        return df["title"].astype(str)
    raise ValueError("CSV must have 'text' or 'title' column")

fake_text = get_text_column(fake)
true_text = get_text_column(true)

fake_df = pd.DataFrame({"text": fake_text, "label": 0})
true_df = pd.DataFrame({"text": true_text, "label": 1})

data = pd.concat([fake_df, true_df], ignore_index=True)
data = data.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle

# --- 2) basic preprocessing ---
nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = str(text).lower()
    tokens = text.split()
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    return " ".join(tokens)

data["text_clean"] = data["text"].apply(clean_text)

# --- 3) features and split ---
X = data["text_clean"]
y = data["label"]

tfidf = TfidfVectorizer(max_features=5000)
X_vect = tfidf.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vect, y, test_size=0.2, random_state=42, stratify=y
)

# --- 4) train model ---
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --- 5) evaluate ---
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# --- 6) save model and vectorizer ---
MODELS_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(MODELS_DIR, exist_ok=True)
with open(os.path.join(MODELS_DIR, "tfidf.pkl"), "wb") as f:
    pickle.dump(tfidf, f)
with open(os.path.join(MODELS_DIR, "model.pkl"), "wb") as f:
    pickle.dump(model, f)

print("Saved tfidf and model to", MODELS_DIR)
