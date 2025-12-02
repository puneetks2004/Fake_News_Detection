📰 Fake News Detection System
🚀 Machine Learning + Streamlit UI

A modern machine learning application that detects Fake News vs Real News using Natural Language Processing (NLP) and a clean, beautiful Streamlit interface.

This project uses:<br>
TF-IDF Vectorization<br>
Logistic Regression Classifier<br>
NLP Preprocessing<br>

Streamlit Web App

🌟 Features

✔ High Accuracy Model<br>
✔ Beautiful Modern UI<br>
✔ Real-time Text Prediction<br>
✔ TF-IDF text vectorization<br>
✔ Clean Code Structure<br>
✔ Fast & Lightweight<br>
✔ Beginner-friendly ML pipeline<br>

📂 Project Structure

fake-news-project/
│
├── data/<br>
│   ├── Fake.csv<br>
│   ├── True.csv<br>
│<br><br>
├── models/<br>
│   ├── model.pkl<br>
│   ├── tfidf.pkl<br>
│<br><br>
├── src/<br>
│   ├── train.py<br>
│   ├── predict.py<br>
│   ├── app.py     # Streamlit UI<br>
│<br><br>
├── venv/<br>
│<br><br>
├── requirements.txt<br>
└── README.md<br>


🧠 How the Model Works
<br><br>
Loads True and Fake news datasets<br>
Performs text preprocessing<br>
Converts text into numerical vectors using TF-IDF<br>
Trains a Logistic Regression classifier<br>
Saves trained model as model.pkl<br>
Saved vectorizer as tfidf.pkl<br>
predict.py and the Streamlit app use the model to classify new text<br>


✨ Technologies Used

Python<br>
Streamlit<br>
Scikit-learn<br>
Pandas<br>
NumPy<br>
Pickle<br>
NLP / TF-IDF<br>
<br>
We will embed a gauge using Plotly, because it supports color zones + semi-circular meter like the image.

Img:

<img width="1919" height="915" alt="Image" src="https://github.com/user-attachments/assets/c149da8b-f064-4661-b1ea-4823c63a065f" />
<br>
<img width="1919" height="924" alt="Image" src="https://github.com/user-attachments/assets/1aaf6bbb-3b5d-4e6c-aac6-ed811761270a" />
<br>
- Using Plotly library
<br>
<img width="1567" height="703" alt="Image" src="https://github.com/user-attachments/assets/3f3e21bb-3aea-44a0-9fe4-8b0fbdcc8647" />
<br>
- Using WorldCloud
<br>
<img width="1598" height="800" alt="Image" src="https://github.com/user-attachments/assets/dee09a19-8f39-4c64-ad76-ade677525736" />
<br>
-Using Plotly library
<br>
<img width="1555" height="663" alt="Image" src="https://github.com/user-attachments/assets/982a5e2c-f1f1-433c-8f48-850bca4bbb3e" />


🔥 So what do you do tomorrow?

cd "C:\Users\puneet kumar\Desktop\fake-news-project"
.\venv\Scripts\activate
streamlit run src/app.py

sample news to test

narendra modi is prime minister of india

The United Nations announced today that it has approved a $200 million humanitarian relief program for regions affected by severe flooding in Southeast Asia. 
According to the official statement, the funds will be used to provide emergency food supplies, temporary housing, clean drinking water, and medical support. 
UN Secretary-General praised the international community for its cooperation and urged member nations to increase contributions to disaster-preparedness initiatives.




