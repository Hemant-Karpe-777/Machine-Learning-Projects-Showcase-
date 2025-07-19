# 🔗 Loan Approval Prediction using Stacking Ensemble & SHAP

This project demonstrates a powerful machine learning pipeline for classifying loan approvals using a **stacking ensemble** of Random Forest, XGBoost, and LightGBM, combined with **SHAP** for interpretability.

---

## 📌 Problem Statement

Predict whether a loan will be approved based on customer and financial details, and **explain model decisions using SHAP** to ensure interpretability.

---

## 🧠 Techniques Used

| Component       | Description                                      |
|----------------|--------------------------------------------------|
| Data Cleaning   | Drop NAs, handle missing Loan_ID                |
| Preprocessing   | One-Hot Encoding of categorical features        |
| Models Used     | RandomForest, XGBoost, LightGBM                 |
| Meta Model      | Logistic Regression (for stacking)              |
| Evaluation      | Accuracy, F1-score, Classification Report       |
| Explainability  | SHAP summary & force plots for XGB & LGBM       |

---

## 📁 Project Structure

```
StackedModel_Loan/
├── data/
│   └── loan_data.csv
├── models/
│   ├── rf_model.pkl
│   ├── xgb_model.pkl
│   ├── lgb_model.pkl
│   └── stacked_meta_model.pkl
├── shap/
│   ├── shap_summary_xgb.png
│   ├── shap_summary_lgbm.png
│   └── shap_force_individual.html
├── images/
│   └── stacking_architecture.png
├── notebooks/
│   ├── Day4_Stacking_Intro.ipynb
│   └── Day5_Stacking_Train_Meta.ipynb
│   └── Day6_SHAP_Interpretation.ipynb
├── README.md
```

---

## 🔗 Dataset

- **Source:** [Kaggle - Loan Approval Classification Data](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data?select=loan_data.csv)
- Target variable: `Loan_Status`

---

## 🔄 Workflow

### 1. Data Preprocessing
- Removed `Loan_ID`
- Encoded categorical columns using `pd.get_dummies()`
- Train/Test split using `stratify=y`

### 2. Base Learners
- Trained using 5-fold StratifiedKFold
- Used `predict_proba` for out-of-fold predictions
- Base models: `RandomForest`, `XGBoost`, `LightGBM`

### 3. Meta Learner
- Trained `LogisticRegression` on Level-1 predictions
- Combined all base predictions into a final stacked prediction

### 4. Model Evaluation

| Model     | Accuracy |
|-----------|----------|
| RF        | 0.9281    |
| XGBoost   | 0.9336    |
| LightGBM  | 0.9331    |
| **Stacked** | **0.9352** ✅ |

---

## 🔍 SHAP Model Explanation

### Global Feature Importance
- SHAP summary plot shows top features across all predictions
- Used for XGB and LGBM separately

### Local Interpretation
- SHAP force plot shows why a specific prediction was made
- E.g., `ApplicantIncome`, `Credit_History`, and `LoanAmount` were top drivers

---

## 📊 Visuals

- `stacking_architecture.png` - Flow of base → meta model
- `shap_summary_xgb.png` - Global SHAP plot for XGB
- `shap_force_individual.html` - Interactive force plot

---

## 🚀 Key Learnings

- Stacking boosts performance by leveraging multiple learners  
- SHAP enables model transparency (important in banking/finance)  
- Logistic regression is a simple yet effective meta learner  
- Model saving using `joblib` for reproducibility

---

## 🔮 Future Improvements

- Hyperparameter tuning with Optuna  
- Add CatBoost and NeuralNet to the stack  
- Deploy as an API with FastAPI or Streamlit  
- Perform feature selection and correlation filtering

---

## 🙌 Author

**Hemant Karpe**   
🌐 [GitHub Portfolio](https://github.com/your-username)
📧 Email: hemant.777karpe@gmail.com  
🔗 LinkedIn: [Hemant-karpe](https://www.linkedin.com/in/hemant-karpe)

---

## 🏁 Final Note

This project reflects a real-world pipeline with reproducibility, performance, and interpretability – ideal for portfolio or production-grade systems.
