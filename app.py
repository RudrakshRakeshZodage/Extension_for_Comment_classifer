import streamlit as st
import joblib
import os

# Set page configuration
st.set_page_config(page_title="AI vs Human Comment Classifier", page_icon="🧠")

# Load models
@st.cache_resource
def load_models():
    vectorizer_path = os.path.join("..", "models", "vectorizer.pkl")
    clf_path = os.path.join("..", "models", "clf.pkl")

    if not os.path.exists(vectorizer_path) or not os.path.exists(clf_path):
        st.error("Model files not found. Make sure vectorizer.pkl and clf.pkl are in the models directory.")
        return None, None

    vectorizer = joblib.load(vectorizer_path)
    clf = joblib.load(clf_path)
    return vectorizer, clf

vectorizer, clf = load_models()

# Page title
st.markdown("<h1 style='text-align: center;'>📝 AI vs Human Comment Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem;'>Enter a comment and the model will predict if it's Human or AI-generated.</p>", unsafe_allow_html=True)

# Input area
user_input = st.text_area("💬 Enter your comment:", height=150)

if st.button("🚀 Predict"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a valid comment.")
    elif vectorizer and clf:
        X = vectorizer.transform([user_input])
        prediction = clf.predict(X)[0]
        confidence = max(clf.predict_proba(X)[0])

        if prediction == 0:
            st.success("🧑‍💻 **Prediction: Human-generated**")
        else:
            st.success("🤖 **Prediction: AI-generated**")
            st.markdown(f"<div style='text-align: center; margin-top: 10px;'>🔒 <strong>Confidence Level:</strong> {confidence*100:.2f}%</div>", unsafe_allow_html=True)
