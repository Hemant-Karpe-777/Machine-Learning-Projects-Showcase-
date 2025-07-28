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
- 📂 [View Project](https://github.com/Hemant-Karpe-777/Machine-Learning-Projects-Showcase/tree/main/AdvancedML%20%26%20Feature%20Drift/report)

---

### 2. 🔁 Experiment Tracking with MLflow

| Task                            | Status |
|----------------------------------|--------|
| Set up MLflow locally (Jupyter)  | ✅ Done |
| Track parameters, metrics, models| ✅ Done |
| Used `mlflow.sklearn` for saving runs | ✅ Done |

**Alternative**: You also tried running it via `ngrok` and decided to switch to Jupyter/PyCharm due to Colab limitations.
- 📂 [View Project](https://github.com/Hemant-Karpe-777/Machine-Learning-Projects-Showcase/tree/main/AdvancedML%20%26%20Feature%20Drift/mlflow)
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

- 📂 [View Project](https://github.com/Hemant-Karpe-777/Machine-Learning-Projects-Showcase/tree/main/AdvancedML%20%26%20Feature%20Drift/deploy)
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

  - 📂 [View Project](https://github.com/Hemant-Karpe-777/Machine-Learning-Projects-Showcase/tree/main/AdvancedML%20%26%20Feature%20Drift/streamlit)

---

## 📁 Project Structure
```
AdvancedML & Feature Drift/
├── data/
│   └── loan_data.csv  #training data
├── notebooks/
│   ├── drift_analysis.ipynb
│   ├── AdvancedML_&_Feature_Drift_notebooks.ipynb
│   └── train_model.ipynb
├── mlflows/                # mlflow for version control and model experiments 
│   ├── mlflow_tracking.ipynb
│   └──  mlflow_tracking.csv
├── report/                # EVIDENTLY for data drift detection 
│   ├── notebook.ipynb
│   └──  report image      
├── deploy/                # Flask App (LocalHost : 5000)
│   ├── app.py            
│   └──  model.pkl         
├── streamlit/             # streamlit_app
│   └── app.py            
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

## 👨‍💻 Author
### **Hemant Karpe**
- Machine Learning Developer
- 📧 Email: hemant.777karpe@gmail.com 
- 🌐 [GitHub Portfolio](https://github.com/Hemant-Karpe-777) | 🔗 [Hemant-karpe](https://www.linkedin.com/in/hemant-karpe)
