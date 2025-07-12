
# Loan Approval Prediction - ML Classifier

Predict loan approval status using RandomForest and XGBoost.  
Includes full pipeline + SHAP explainability.

## 📌 Dataset
Kaggle: [Loan Approval Classification Data](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)

## 🧪 Models Used
- Random Forest
- XGBoost (tuned with GridSearchCV)

## 🔍 Explainability
- SHAP Beeswarm: Top influencing features
- SHAP Waterfall: Individual predictions

## 🧼 Workflow
1. Cleaned and encoded data
2. Handled class imbalance (SMOTE & class weights)
3. Tuned models using GridSearchCV
4. Saved model with `joblib`
5. Pushed to GitHub

## 📊 Results
### 🔍 Tuned XGBoost Evaluation

| Metric     | Score |
|------------|-------|
| Accuracy   | 0.94  |
| Precision  | 0.89  |
| Recall     | 0.81  |
| F1-Score   | 0.85  |

#### 📊 Confusion Matrix

|                | Predicted: 0 | Predicted: 1 |
|----------------|--------------|--------------|
| **Actual: 0**  | 6810         | 190          |
| **Actual: 1**  | 387          | 1613         |


## 📁 Project Structure

LoanClassifier_ML/
├── data/                      
│   └── train.csv
├── models/
│   └── xgb_best_tuned.pkl
├── notebooks/
│   └── Day1_to_Day5.ipynb
├── explainability/
│   ├── shap_beeswarm.png
│   └── shap_waterfall_0.png
├── images/
│   └── confusion_matrix.png
├── README.md



## 🔮 Future Improvements
- Build a Streamlit web app for real-time predictions
- Add ROC-AUC and precision-recall evaluation
- Track data drift using evidently
- Try Optuna for advanced hyperparameter tuning
- Engineer new features from income, loan ratios
- Build a model card to describe ethical usage
