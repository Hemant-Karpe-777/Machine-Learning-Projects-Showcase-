# 🧠 Mental Health Depression Analysis

This project presents an end-to-end analysis of a mental health dataset from Kaggle to understand patterns in depression across different professions and demographics. It uses data preprocessing, cleaning, and visualizations to highlight important trends.

---

## 📌 Objective

Analyze the relationship between **profession** and **depression**, using a cleaned dataset to uncover insights and display results visually.

---

## 📂 Dataset

**Source:** [Kaggle - Playground Series - Season 4, Episode 11](https://www.kaggle.com/competitions/playground-series-s4e11)

- `train.csv`: Contains user data and target (`Depression`)
- `test.csv`: Provided but mainly unused in this visual-focused analysis

---

## 🔍 Key Columns

- `id`: Unique identifier
- `Name`: Individual's name
- `Profession`: Job title (some noisy data cleaned)
- `Age`: Age of the individual
- `Depression`: Target label (1 = Depressed, 0 = Not Depressed)

---

## 🔧 Preprocessing & Cleaning

- ✅ Removed rows where `Profession == Name`
- ✅ Dropped obvious outliers in profession (e.g. "Nagpur", "Yogesh")
- ✅ Converted all profession values to strings to avoid type mismatch
- ✅ Focused analysis on **top 15 most frequent professions**

---

## 📊 Visual Analysis

### ✔️ Top Professions by Frequency
- A barplot showing the 30 most common professions in the dataset.

### ✔️ Profession-wise Depression Analysis
- A grouped barplot (hue = Depression) for the top 15 professions
- Shows the distribution of depression cases by job type

---

## 🧰 Tools Used

- `Python`
- `Pandas` & `NumPy` for data manipulation
- `Seaborn` & `Matplotlib` for plotting
- `Scikit-learn` for preprocessing
- `opendatasets` for loading Kaggle data

---

---

## 🚀 Future Enhancements

- Add ML classification models to predict depression
- Clean profession column using NLP (e.g., spaCy or fuzzy matching)
- Include demographic-based analysis (e.g., age groups)
- Explore correlation between age, profession, and depression

---

## ✅ Conclusion

This project demonstrates how data cleaning and visualization can reveal hidden trends in mental health data. It emphasizes the importance of clean feature engineering, especially for real-world fields like `Profession`.

---

## 🙌 Acknowledgements

- Data Source: Kaggle Playground Series (S4E11)
- Developed as part of a personal Data Science & ML portfolio

