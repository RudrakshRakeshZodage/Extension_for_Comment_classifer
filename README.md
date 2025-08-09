# Extension_for_Comment_classifer


## Overview
This project is an AI-powered system designed to detect whether a given comment or review is **AI-generated** or **human-written**. It uses a combination of **Artificial Intelligence (AI)**, **Machine Learning (ML)**, and **Natural Language Processing (NLP)** techniques to analyze linguistic patterns, context, and style, achieving **99.40% accuracy** in classification.

AI-generated comments are highlighted in **red**, while human-written comments are highlighted in **green**, providing an intuitive interface for quick verification.

---

## Features
- **High Accuracy (99.40%)** on test datasets.
- Detection of **HumanizeAI**-modified AI content.
- **Color-coded visual output** for instant identification.
- Integration-ready for **web extensions** and **moderation tools**.
- Trained on **487,236 samples** of balanced AI and human comments.
- Supports deployment in **Google Chrome Extensions** using Python, HTML, CSS, and basic JavaScript.

---

## System Workflow
1. **Text Input** — User submits a comment or review.
2. **NLP Preprocessing** — Tokenization, cleaning, and feature extraction.
3. **ML Model Prediction** — Classification as AI-generated or human.
4. **Output Visualization** — Red highlight for AI text, green for human.
5. **Integration** — Result displayed in the browser via extension.

---

## Technology Stack
- **Python** — Model training and backend logic.
- **Scikit-learn / TensorFlow / PyTorch** — Machine learning framework.
- **NLP Tools** — NLTK, SpaCy, or custom feature extractors.
- **HTML / CSS / JavaScript** — Frontend for browser extension.
- **Google Chrome Extension API** — Integration point for deployment.

---

## Model Performance
**Confusion Matrix:**
