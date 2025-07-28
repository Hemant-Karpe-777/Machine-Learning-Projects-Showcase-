# 🚀 Week 4: ML Monitoring, Drift Detection & Deployment

This week focuses on deploying machine learning models and preparing them for production using best practices like **drift detection**, **model tracking**, and **serving with Flask and Streamlit**. You’ll build everything from tracking systems to real-time prediction APIs.

---

## 🔖 Key Learning Objectives

- ✅ Understand the differences between model drift, data drift, and concept drift
- ✅ Detect feature/data drift using visualization tools like Evidently
- ✅ Track experiments and metrics using MLflow
- ✅ Deploy models via Flask REST APIs and Streamlit interfaces
- ✅ Handle local hosting, versioning, and API testing like an ML engineer

---

## 📦 Projects Completed

### 1. 📊 Drift Detection with Evidently

| Task                        | Status |
|-----------------------------|--------|
| Analyze data drift visually | ✅ Done |
| Compare training vs test distributions | ✅ Done |
| Integrated Evidently into notebook | ✅ Done |

**Tools Used**: `evidently`, `pandas`, `matplotlib`

---

### 2. 🔁 Experiment Tracking with MLflow

| Task                            | Status |
|----------------------------------|--------|
| Set up MLflow locally (Jupyter)  | ✅ Done |
| Track parameters, metrics, models| ✅ Done |
| Used `mlflow.sklearn` for saving runs | ✅ Done |

**Alternative**: You also tried running it via `ngrok` and decided to switch to Jupyter/PyCharm due to Colab limitations.

---

### 3. 🌐 API Deployment with Flask

| Task                        | Status |
|-----------------------------|--------|
| Saved trained pipeline with `joblib` | ✅ Done |
| Built a local Flask app (`app.py`)   | ✅ Done |
| Tested POST requests using `requests` | ✅ Done |
| Local server hosted via `127.0.0.1:5000` | ✅ Done |

**Prediction API Endpoint**:

POST /predict
{
  "features": [22.0, "female", "Master", 71948.0, 0, "RENT", 35000.0, "PERSONAL", 16.02, 0.49, 3.0, 561, "No"]
}

---

### 4. 🖥️ Streamlit Dashboard App
| Task                               | Status |
| ---------------------------------- | ------ |
| Built Streamlit UI for predictions | ✅ Done |
| Handled input features from users  | ✅ Done |
| Loaded `.pkl` pipeline model       | ✅ Done |
| Matched inputs with model schema   | ✅ Done |

Streamlit Features:
- Form-based user inputs
- Real-time predictions
- Success/error message based on model output
- Clean interface & fully pipelined model use

---

## 📁 Project Structure
```
week_4_project/
├── data/
│   └── loan_data.csv
├── notebooks/
│   ├── drift_analysis.ipynb
│   ├── mlflow_tracking.ipynb
│   └── train_model.ipynb
├── deployment/
│   ├── app.py             # Flask API
│   ├── model.pkl          # Trained pipeline
│   └── requirements.txt
├── streamlit_app/
│   └── app.py             # Streamlit UI
└── README.md
```
---

## 🔧 Tech Stack
- Python, Pandas, Scikit-learn
- Streamlit, Flask, Joblib
- MLflow, Evidently
- Jupyter Notebook, PyCharm, VSCode

---

## 📚 Skills Mastered
- ✅ Drift vs. Concept Drift
- ✅ Feature Monitoring
- ✅ Experiment Tracking
- ✅ API Development
- ✅ Real-time Predictions
- ✅ Streamlit UI Design
- ✅ Handling Deployment Environments

---

## a
