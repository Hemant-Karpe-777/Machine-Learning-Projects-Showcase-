# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JX3_tosTb0hcTr5yLjqh4XgpDhVkhD89
"""

from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)
pipeline = joblib.load("loan_pipeline.pkl")

# 🏠 Route to load HTML form
@app.route('/')
def home():
    return render_template('index.html')  # renders HTML form

# 📤 Route to handle prediction from form
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()  # Get form data as dictionary

        # Convert numeric fields
        for key in data:
            try:
                data[key] = float(data[key])
            except:
                pass  # Leave as string for categorical columns

        df = pd.DataFrame([data])  # Single row DataFrame
        prediction = pipeline.predict(df)
        result = int(prediction[0])
        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)