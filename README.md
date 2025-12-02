📰 Fake News Detection System
🚀 Machine Learning + Streamlit UI

A modern machine learning application that detects Fake News vs Real News using Natural Language Processing (NLP) and a clean, beautiful Streamlit interface.

This project uses:
TF-IDF Vectorization
Logistic Regression Classifier
NLP Preprocessing

Streamlit Web App

🌟 Features

✔ High Accuracy Model
✔ Beautiful Modern UI
✔ Real-time Text Prediction
✔ TF-IDF text vectorization
✔ Clean Code Structure
✔ Fast & Lightweight
✔ Beginner-friendly ML pipeline

📂 Project Structure

fake-news-project/
│
├── data/
│   ├── Fake.csv
│   ├── True.csv
│
├── models/
│   ├── model.pkl
│   ├── tfidf.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── app.py     # Streamlit UI
│
├── venv/
│
├── requirements.txt
└── README.md


🧠 How the Model Works

Loads True and Fake news datasets
Performs text preprocessing
Converts text into numerical vectors using TF-IDF
Trains a Logistic Regression classifier
Saves trained model as model.pkl
Saved vectorizer as tfidf.pkl
predict.py and the Streamlit app use the model to classify new text


✨ Technologies Used

Python
Streamlit
Scikit-learn
Pandas
NumPy
Pickle
NLP / TF-IDF

We will embed a gauge using Plotly, because it supports color zones + semi-circular meter like the image.


🔥 So what do you do tomorrow?

cd "C:\Users\puneet kumar\Desktop\fake-news-project"
.\venv\Scripts\activate
streamlit run src/app.py

sample news to test

narendra modi is prime minister of india

The United Nations announced today that it has approved a $200 million humanitarian relief program for regions affected by severe flooding in Southeast Asia. 
According to the official statement, the funds will be used to provide emergency food supplies, temporary housing, clean drinking water, and medical support. 
UN Secretary-General praised the international community for its cooperation and urged member nations to increase contributions to disaster-preparedness initiatives.




