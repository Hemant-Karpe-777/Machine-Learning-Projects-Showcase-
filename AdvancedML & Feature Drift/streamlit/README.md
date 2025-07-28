# 🏦 Loan Approval Prediction App – Streamlit + ML Pipeline

This project is a full-stack Machine Learning web app that predicts whether a loan will be approved based on applicant and loan details. Built with **Scikit-learn**, **Streamlit**, and a model trained on real-world loan approval data from Kaggle.

---

## 📌 Project Highlights

- ✅ End-to-end ML pipeline using `scikit-learn`
- ✅ Categorical & numerical preprocessing handled via pipeline
- ✅ Interactive UI built with `streamlit`
- ✅ User-friendly input forms with real-time predictions
- ✅ Ready for local or cloud deployment (e.g. Streamlit Cloud)

---

## 🧠 ML Model Overview

- **Dataset**: [Loan Approval Classification](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)
- **Algorithm**: Logistic Regression / XGBoost (selectable)
- **Preprocessing**: OneHotEncoding, Scaling, ColumnTransformer
- **Saved As**: `model.pkl` using full pipeline

---

## 🎯 Prediction Features

| Feature Name                      | Description                            |
|----------------------------------|----------------------------------------|
| `person_age`                     | Age of applicant                       |
| `person_gender`                  | Gender: male / female                  |
| `person_education`               | Education level                        |
| `person_income`                  | Monthly income                         |
| `person_emp_exp`                | Employment experience (in years)       |
| `person_home_ownership`          | Home ownership: RENT, OWN, MORTGAGE    |
| `loan_amnt`                      | Loan amount requested                  |
| `loan_intent`                    | Purpose of the loan                    |
| `loan_int_rate`                  | Interest rate for the loan             |
| `loan_percent_income`            | Loan % of income                       |
| `cb_person_cred_hist_length`     | Credit history length                  |
| `credit_score`                   | Credit score (300–850)                 |
| `previous_loan_defaults_on_file`| Whether previous defaults exist        |

---

## 📦 File Structure
```
loan-approval-streamlit-app/
├── app.py                 # Streamlit frontend
├── model.pkl              # Trained ML pipeline
├── loan_data.csv          # (Optional) Source dataset
├── README.md
├── requirements.txt
```
---

## 🖥 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/loan-approval-streamlit-app.git
cd loan-approval-streamlit-app
```

### 2. Install Requirements
```pip install streamlit pandas scikit-learn joblib```

### 3. Run the App
```streamlit run app.py```

-Then open in your browser:
-📍 http://localhost:8501

---

## 🔑 Key Features

- 🧠 **ML Pipeline Deployment**: End-to-end Scikit-learn pipeline with scaling + encoding + model.
- 🌐 **Streamlit Web App**: Intuitive UI for real-time loan prediction.
- 🗃️ **Form-based Inputs**: Collects user data via dropdowns, sliders, and number fields.
- ⚙️ **Model Inference in Real-Time**: Predicts using `.pkl` model loaded from disk.
- 💾 **Reusability**: Can be deployed locally or hosted on the cloud.
- 📦 **Portable**: Only `app.py` and `model.pkl` needed for deployment.
---

## 🧠 Future Enhancements
- Add model probability scores (via predict_proba)
- Add SHAP-based model explanation
- Store prediction logs in a database
- Add login/authentication for users

---

## 📜 License
This project is licensed under the MIT License.
Feel free to fork and build your own ML apps!

---

## 👨‍💻 Author
### **Hemant Karpe**
- Machine Learning Developer
- 📧 Email: hemant.777karpe@gmail.com 
- 🌐 [GitHub Portfolio](https://github.com/Hemant-Karpe-777) | 🔗 [Hemant-karpe](https://www.linkedin.com/in/hemant-karpe)
 
