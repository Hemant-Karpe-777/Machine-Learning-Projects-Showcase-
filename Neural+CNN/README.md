# 🧠 Digit Recognizer using Convolutional Neural Network (CNN)

This project uses a deep learning CNN model to classify handwritten digits from the MNIST dataset. It includes both a baseline Multi-Layer Perceptron (MLP) model and an improved CNN architecture trained and evaluated using TensorFlow/Keras.

---

## 📌 Problem Statement

Build an image classifier that accurately predicts digits (0–9) from 28×28 pixel grayscale images.  
Use the MNIST dataset and implement both a baseline MLP and an optimized CNN model with regularization.

---

## 🧠 Dataset

- 📦 **MNIST**: 70,000 images of handwritten digits (28x28 grayscale)  
- 🔁 60,000 training + 10,000 testing  
- Built-in via `tensorflow.keras.datasets`

---

## ⚙️ Technologies Used

- Python, NumPy, Matplotlib  
- TensorFlow & Keras (`Sequential`, `Conv2D`, `Dropout`, `Dense`)  
- scikit-learn (`classification_report`, `confusion_matrix`)  
- Git & GitHub

---

## 🧪 Models Built

### 🔹 Baseline: MLP (Multi-Layer Perceptron)
- `Flatten` → `Dense(128)` → `Dense(64)` → `Dense(10)`  
- Achieved ~98% accuracy on test set

### 🔹 Optimized: CNN Architecture

Conv2D(32) → MaxPooling → Dropout  
Conv2D(64) → MaxPooling → Dropout  
Flatten → Dense(128) → Dropout → Dense(10)

---

## 🔍 Model Comparison

| Model | Accuracy | F1-Score |
|-------|----------|----------|
| MLP   | 98.0%    | 0.98     |
| CNN   | 98.7%    | 0.987    |

### 🧠 Takeaway:
- CNN outperforms MLP on image data due to spatial learning
- Dropout and MaxPooling helped reduce overfitting
- Model ready for deployment via `.h5`

---

## 🧠 Key Learnings

- ✅ **CNNs outperform MLPs** on spatial image data like MNIST
- ✅ **Pooling and Dropout** help reduce overfitting
- ✅ **EarlyStopping & ModelCheckpoint** improve model stability
- ✅ Final trained **model exported in `.h5`** format for deployment

---

## 🔮 Future Improvements

- 🔁 Add **Data Augmentation** (rotation, shifting, zoom)
- 🧱 Train **deeper CNNs** (e.g., VGG-style architecture)
- 🌐 **Deploy model** via Streamlit or Flask web app
- 🔄 Try **Transfer Learning** using EfficientNet or MobileNet for similar image tasks

---

## 📦 Final Deliverables

| ✅ Deliverable                  | Description                            |
|-------------------------------|----------------------------------------|
| `cnn_best_model.h5`           | Trained & optimized CNN model          |
| Accuracy / Loss plots         | Visual performance evaluation          |
| Sample Predictions            | Sample outputs of digit predictions    |
| `README.md`                   | GitHub-ready documentation             |
| `MLP_vs_CNN_Notebooks.ipynb`  | Two side-by-side model training files  |

---
## 📬 Contact

📧 Email: hemant.777karpe@gmail.com  
🔗 LinkedIn: [Hemant-karpe](https://www.linkedin.com/in/hemant-karpe)
