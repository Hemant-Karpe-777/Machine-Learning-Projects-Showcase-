# 🧠 Loan Approval Prediction App

A full-stack machine learning web application that predicts whether a loan will be **approved or not** based on applicant details. Built with **Logistic Regression**, **Scikit-Learn Pipelines**, **Flask**, and deployed as a responsive and interactive web app.

[![Loan app Demo](https://github.com/Hemant-Karpe-777/Machine-Learning-Projects-Showcase/blob/main/AdvancedML%20%26%20Feature%20Drift/deploy/images/web%20page%20for%20loan%20input.png)](https://github.com/Hemant-Karpe-777/Machine-Learning-Projects-Showcase/blob/main/AdvancedML%20%26%20Feature%20Drift/deploy)

---

## 🚀 Project Overview

This project includes:

- 🧪 **Model Training in Jupyter Notebook**  
  Preprocesses data, builds a pipeline, and saves the trained model using `joblib`.

- 🌐 **Web App using Flask**  
  Interactive web interface to enter loan application details and get instant predictions.

- 📦 **Complete End-to-End Pipeline**  
  Trained using `StandardScaler`, `OneHotEncoder`, and `LogisticRegression` in a unified `Pipeline`.

- 📊 **Input Features**  
  Includes both categorical and numerical inputs such as age, income, education, loan amount, etc.

---

## 💡 Prediction Use Case

The model predicts:


Loan Status: 
1 → Loan Approved ✅  
0 → Loan Denied ❌

---

## 🏗️ Tech Stack
| Category          | Tools Used                                       |
| ----------------- | ------------------------------------------------ |
| Model             | Scikit-learn, Pandas, Joblib                     |
| Preprocessing     | ColumnTransformer, StandardScaler, OneHotEncoder |
| Frontend (Web UI) | HTML, CSS (Dark Theme, Tooltip, Icons)           |
| Backend (API)     | Python Flask                                     |
| Deployment        | Localhost (can be extended to Render/Heroku)     |
| IDEs              | Jupyter Notebook, VS Code, Colab                 |

---

## 🧰 Input Fields Used
{
  "person_age": 22.0,
  "person_gender": "female",
  "person_education": "Master",
  "person_income": 71948.0,
  "person_emp_exp": 0,
  "person_home_ownership": "RENT",
  "loan_amnt": 35000.0,
  "loan_intent": "PERSONAL",
  "loan_int_rate": 16.02,
  "loan_percent_income": 0.49,
  "cb_person_cred_hist_length": 3.0,
  "credit_score": 561,
  "previous_loan_defaults_on_file": "No"
}

---

## 📁 Project Structure
```Loan-Approval-App(deployment)/
│
├── train_model.ipynb          # 📊 Jupyter Notebook to train & save the model
├── loan_pipeline.pkl          # ✅ Trained model pipeline
├── app.py                     # 🌐 Flask backend
├── templates/
│   └── index.html             # 🎨 HTML form for input
├── static/                    # 💅 CSS, JS, Icons, Animations
├── README.md                  # 📘 Project description
└── requirements.txt           # 📦 Python dependencies
```
---

## 🔁 How It Works
1. Model Training (train_model.ipynb).
   - Preprocesses data using pipelines.
   - Encodes categories & scales numeric columns.
   - Trains LogisticRegression.
   - Saves entire pipeline with joblib.

2. Web App (app.py).
- Accepts user input via form.
- Converts input to proper types (float/categorical).
- Runs prediction using loaded pipeline.
- Displays prediction with visual output.

3. Run App (app.py) locally 
- Open terminal inside the /deployment/ folder:
- python app.py  #run app file
- Running on http://127.0.0.1:5000/
- fill the fields and see prediction.

---

## ✨ Final Output
✅ Loan Approved
OR
❌ Loan Denied

---

## 🎯 Key Features
- 🔒 Does not reset form on submit — fields retain values
- 🌗 Dark Theme with icons and tooltips
- 📱 Responsive layout (horizontal, small-size form)
- 🎉 Smooth animations for better interactivity
- 🧩 Decimals and data types auto-handled in backend

---

## 📌 Future Improvements
- Deploy on Render / HuggingFace Spaces
- Add SHAP explainability
- Multi-model comparison with XGBoost, LightGBM
- Database storage for user input history
- Add PDF report download of prediction

---

Author

