# 🏡 House Price Prediction - Machine Learning Project

This project predicts house sale prices using machine learning regression techniques. It includes full end-to-end steps — from data exploration and cleaning to model training, evaluation, and explainability using SHAP.

---

## 📌 Problem Statement

Given various features of residential homes (location, area, quality, garage, etc.), predict the `SalePrice` of a house.  
This is a regression task using the **Kaggle: House Prices - Advanced Regression Techniques** dataset.

---

## 📁 Project Structure

├── data/ # Raw dataset from Kaggle
├── cleaned_data/ # Cleaned CSV used for modeling
├── notebooks/ # All experiment notebooks (Day1 to Day6)
├── models/ # Saved model files (.pkl)
├── explainability/ # SHAP plots and analysis
├── images/ # EDA plots and visuals
├── README.md # This file


---

## 🔧 Tools Used

- Python, NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn (LinearRegression, RandomForest)
- XGBoost
- SHAP (model interpretability)
- Joblib (for saving model)
- Git + GitHub (version control)

---

## 📊 EDA Snapshots

### 🔹 Target Distribution: SalePrice
![Target](images/hist_target.png)

### 🔹 GrLivArea vs SalePrice
![Area vs Price](images/scatter_area_price.png)

---

## 🧼 Data Cleaning Steps

- Dropped high-null columns (`Alley`, `PoolQC`, etc.)
- Imputed missing numerical values using median
- Imputed categorical variables using mode
- One-hot encoded nominal categorical features
- Reduced skewness in highly skewed numerical columns

---

## 🤖 Models Trained

| Model | MAE | RMSE | R² Score |
|-------|-----|------|----------|
| Linear Regression | ✅ | ✅ | ✅ |
| Random Forest Regressor | ✅ | ✅ | ✅ |
| XGBoost Regressor | ✅ | ✅ | ✅ |

✅ Metrics were computed using scikit-learn's `mean_absolute_error`, `mean_squared_error`, and `r2_score`.

---

## 🔍 Model Explainability

SHAP (SHapley Additive exPlanations) was used to interpret model predictions.

- `explainability/shap_beeswarm.png` – Global feature importance
- `explainability/shap_waterfall.png` – Single prediction breakdown

---

## 📦 Final Deliverables

- Trained XGBoost model saved as `models/xgb_model.pkl`
- Complete notebook: `notebooks/Day1_to_Day5.ipynb`
- Plots and insights saved in `/images/` and `/explainability/`
- GitHub repository with all files

---

## 📈 Future Improvements

- Feature engineering: polynomial features, feature selection
- Hyperparameter tuning with Optuna or GridSearchCV
- Streamlit-based web app deployment
