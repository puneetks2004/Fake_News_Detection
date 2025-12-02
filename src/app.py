# import streamlit as st
# import plotly.graph_objects as go
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import pandas as pd
# from predict import predict

# st.set_page_config(page_title="Fake News Detector", layout="wide")

# # ---- HEADER ----
# st.markdown("""
#     <h1 style="text-align:center;">
#   <span style="color:#FF5533;">📰 Fake</span>
#   <span style="color:#FFFFFF;">News</span>
#   <span style="color:#00ff00;">Detector</span>
# </h1>
#     <p style='text-align:center; font-size:18px;'>
#         An interactive AI-powered system to check if news is Real or Fake
#     </p>
# """, unsafe_allow_html=True)

# # ---- SIDEBAR (Website Sections) ----
# st.sidebar.title("📌 Navigation")
# section = st.sidebar.radio("Go to", ["Home", "Fake News Detector", "About Project", "Technologies Used", "Dataset Info"])

# # ------------------------------------
# # HOME PAGE
# # ------------------------------------
# if section == "Home":
#     st.markdown("""
#         <h2>Welcome 👋</h2>
#         <p style='font-size:17px;'>
#             This tool uses Machine Learning and Natural Language Processing 
#             to detect whether a news article is <b>Real</b> or <b>Fake</b>.
#             <br><br>
#             Navigate using the left sidebar to explore features.
#         </p>
#     """, unsafe_allow_html=True)

# # ------------------------------------
# # DETECTOR PAGE (Main Function)
# # ------------------------------------
# elif section == "Fake News Detector":
#     st.header("🔍 Fake News Detector")

#     text = st.text_area("Paste News Text Here", height=200)

#     if st.button("Check Credibility"):
#         if text.strip() == "":
#             st.warning("Please enter some news text.")
#         else:
#             with st.spinner("Analyzing the news..."):
#                 result = predict(text)
            
#             label = result['label']
#             prob = result['probability']

#             # ---- CUSTOM GAUGE METER ----
#             gauge_val = prob * 100 if label == "REAL" else (100 - prob * 100)

#             fig = go.Figure(go.Indicator(
#                 mode = "gauge+number",
#                 value = gauge_val,
#                 title = {'text': "Credibility Meter"},
#                 gauge = {
#                     'axis': {'range': [0, 100]},
#                     'bar': {'color': "black"},
#                     'steps': [
#                         {'range': [0, 40], 'color': "red"},
#                         {'range': [40, 70], 'color': "yellow"},
#                         {'range': [70, 100], 'color': "green"},
#                     ],
#                 }
#             ))

#             st.plotly_chart(fig, use_container_width=True)

#             # ---- TEXT OUTPUT ----
#             if label == "REAL":
#                 st.success(f"Prediction: REAL NEWS (Confidence: {prob:.2f})")
#             else:
#                 st.error(f"Prediction: FAKE NEWS (Confidence: {prob:.2f})")

#             st.markdown("---")

#             # -----------------------------------------------------
#             #   WORD CLOUD SECTION
#             # -----------------------------------------------------
#             st.subheader("☁️ Word Cloud (Important Words in the News)")
#             wc = WordCloud(width=800, height=400, background_color='black').generate(text)

#             fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
#             ax_wc.imshow(wc, interpolation='bilinear')
#             ax_wc.axis("off")
#             st.pyplot(fig_wc)

#             st.markdown("---")

#             # -----------------------------------------------------
#             #   REAL vs FAKE PROBABILITY BAR CHART
#             # -----------------------------------------------------
#             st.subheader("📊 Real vs Fake Probability Chart")

#             df = pd.DataFrame({
#                 'Label': ['Real', 'Fake'],
#                 'Probability': [prob if label == "REAL" else (100 - gauge_val)/100,
#                                 1-prob if label == "REAL" else gauge_val/100]
#             })

#             st.bar_chart(df.set_index('Label'))

# # ------------------------------------
# # ABOUT PROJECT SECTION
# # ------------------------------------
# elif section == "About Project":
#     st.header("📘 About the Project")
#     st.markdown("""
#         This project detects Fake or Real news using Machine Learning.
#         It learns patterns from real examples and analyzes writing style,
#         wording, sentiment, and structure to classify news credibility.
#     """)

# # ------------------------------------
# # TECH USED SECTION
# # ------------------------------------
# elif section == "Technologies Used":
#     st.header("🛠 Technologies Used")
#     st.markdown("""
#     ### ✔ Python  
#     ### ✔ Streamlit (Web UI)  
#     ### ✔ scikit-learn (Machine Learning)  
#     ### ✔ NLTK (Text Preprocessing)  
#     ### ✔ TF-IDF Vectorizer  
#     ### ✔ Logistic Regression Model  
#     ### ✔ Plotly (Gauge Meter Visualization)  
#     ### ✔ WordCloud & Matplotlib  
#     """) 

# # ------------------------------------
# # DATASET SECTION
# # ------------------------------------
# elif section == "Dataset Info":
#     st.header("📊 Dataset Information")
#     st.markdown("""
#         We used the **Fake and Real News Dataset** from Kaggle.
#         <ul>
#             <li><b>Fake.csv</b> — contains fake news articles</li>
#             <li><b>True.csv</b> — contains real news articles</li>
#         </ul>
#         During training:
#         <ul>
#             <li>Fake = label 0</li>
#             <li>Real = label 1</li>
#         </ul>
#     """, unsafe_allow_html=True)

# # ---- FOOTER ----
# st.markdown("""
#     <hr>
#     <p style='text-align:center; font-size:20px;'>
#         Puneet Kumar | Built using Streamlit & Machine Learning | Fake News Detector Project
#     </p>
# """, unsafe_allow_html=True)


import streamlit as st
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from predict import predict

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide"
)

# -----------------------------------------------------
# CUSTOM CSS FOR BEAUTIFUL UI
# -----------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: #0d1117;
    color: white;
}

/* HEADER DESIGN */
.title {
    text-align:center;
    font-size:60px;
    font-weight:700;
    margin-top: -20px;
    animation: fadeIn 1s ease-in-out;
}

.subtitle {
    text-align:center;
    font-size:20px;
    color:#d1d5db;
    margin-top:-20px;
}

/* NAV SIDEBAR */
.css-1d391kg {
    background-color: #111827 !important;
}

.sidebar-title {
    font-size:30px !important;
    font-weight:600;
    color:#00ffbf;
}

/* BUTTON */
.stButton>button {
    background-color:#00ffbf;
    color:black;
    border-radius:12px;
    padding:10px 22px;
    transition:0.3s;
    font-size:18px;
    border:none;
    font-weight:600;
}

.stButton>button:hover {
    background-color:#00cc99;
    transform:scale(1.05);
}

/* TEXTAREA */
textarea {
    background-color:#1f2937 !important;
    color:white !important;
    border-radius:12px !important;
    padding:15px !important;
}

/* CARD CONTAINER */
.card {
    background:#1f2937;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 0px 25px rgba(0,255,180,0.1);
    animation: fadeInUp 0.8s ease-in-out;
}

/* ANIMATIONS */
@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}
@keyframes fadeInUp {
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HEADER SECTION
# -----------------------------------------------------
st.markdown("""
<h1 class="title">
    <span style="color:#FF5533;">📰 Fake</span>
    <span style="color:#FFFFFF;">News</span>
    <span style="color:#00FFBF;">Detector</span>
</h1>
<p class="subtitle">AI-powered system to detect Fake vs Real news</p>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------
st.sidebar.markdown("<h2 class='sidebar-title'>📌 Navigation</h2>", unsafe_allow_html=True)
section = st.sidebar.radio("Go to", ["Home", "Fake News Detector", "About Project", "Technologies Used", "Dataset Info"])

# -----------------------------------------------------
# PAGES
# -----------------------------------------------------

# HOME PAGE
if section == "Home":
    st.markdown("""
    <div class="card">
        <h2>👋 Welcome</h2>
        <p style='font-size:18px;'>
            This interactive AI-powered tool detects whether news content is 
            <b style='color:#00ffbf;'>Real</b> or 
            <b style='color:#FF5533;'>Fake</b>.
            <br><br>
            Use the sidebar to navigate through the features.
        </p>
    </div>
    """, unsafe_allow_html=True)

# DETECTOR PAGE
elif section == "Fake News Detector":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🔍 Fake News Detector")

    text = st.text_area("Paste News Text Here", height=200)

    if st.button("Check Credibility"):
        
        if text.strip() == "":
            st.warning("⚠ Please enter some news text to analyze.")
        
        else:
            with st.spinner("⚡ Analyzing the news..."):
                result = predict(text)

            label = result["label"]
            prob = result["probability"]

            # GAUGE VALUE
            gauge_val = prob * 100 if label == "REAL" else (100 - prob * 100)

            # BEAUTIFUL GAUGE METER
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=gauge_val,
                title={'text': "Credibility Meter"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "white"},
                    'steps': [
                        {'range': [0, 40], 'color': "red"},
                        {'range': [40, 70], 'color': "yellow"},
                        {'range': [70, 100], 'color': "green"},
                    ],
                }
            ))

            st.plotly_chart(fig, use_container_width=True)

            # TEXT OUTPUT
            if label == "REAL":
                st.success(f"🟢 REAL NEWS (Confidence: {prob:.2f})")
            else:
                st.error(f"🔴 FAKE NEWS (Confidence: {prob:.2f})")

            st.markdown("</div>", unsafe_allow_html=True)

            # WORD CLOUD
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("☁️ Word Cloud (Important Words)")
            wc = WordCloud(width=800, height=400, background_color='black').generate(text)
            fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
            ax_wc.imshow(wc, interpolation="bilinear")
            ax_wc.axis("off")
            st.pyplot(fig_wc)
            st.markdown("</div>", unsafe_allow_html=True)

            # BAR CHART
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("📊 Real vs Fake Probability")
            df = pd.DataFrame({
                "Label": ["Real", "Fake"],
                "Probability": [
                    prob if label == "REAL" else (100 - gauge_val)/100,
                    1 - prob if label == "REAL" else gauge_val/100
                ]
            })
            st.bar_chart(df.set_index("Label"))
            st.markdown("</div>", unsafe_allow_html=True)

# ABOUT SECTION
elif section == "About Project":
    st.markdown("""
    <div class="card">
    <h2>📘 About This Project</h2>
    <p style='font-size:18px;'>
        This project uses Machine Learning to detect the authenticity of news articles.
        It analyzes writing style, word patterns, semantics, and statistical features 
        to classify news as <b>Real</b> or <b>Fake</b>.
    </p>
    </div>
    """, unsafe_allow_html=True)

# TECHNOLOGIES
elif section == "Technologies Used":
    st.markdown("""
    <div class="card">
    <h2>🛠 Technologies Used</h2>
    <ul style='font-size:18px;'>
        <li>Python</li>
        <li>Streamlit</li>
        <li>scikit-learn</li>
        <li>NLTK</li>
        <li>TF-IDF Vectorizer</li>
        <li>Logistic Regression</li>
        <li>Plotly</li>
        <li>WordCloud</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# DATASET INFO
elif section == "Dataset Info":
    st.markdown("""
    <div class="card">
    <h2>📊 Dataset Information</h2>
    <p style='font-size:17px;'>
        Dataset used: <b>Fake and Real News Dataset</b> (Kaggle)
    </p>

    <ul>
        <li><b>Fake.csv</b> → Fake news articles</li>
        <li><b>True.csv</b> → Real news articles</li>
    </ul>

    <b>Labels:</b>
    <ul>
        <li>0 → Fake</li>
        <li>1 → Real</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


# FOOTER
st.markdown("""
<hr>
<p style='text-align:center; color:#888; font-size:16px;'>
    ⚡ Built by <b>Puneet Kumar</b> | Streamlit + Machine Learning | Fake News Detector  
</p>
""", unsafe_allow_html=True)
