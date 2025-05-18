# 📩 SMS Spam Detection

This project is an end-to-end machine learning solution to detect whether an SMS message is spam or not. It uses Natural Language Processing (NLP) techniques along with the **Naive Bayes theorem** to classify text messages.

## 📌 Overview

SMS spam is a major concern that affects communication and productivity. This project uses a dataset of labeled SMS messages to build a text classification model using the **Multinomial Naive Bayes** algorithm.

### 🔍 Objective

- Preprocess the SMS text data  
- Extract features using CountVectorizer  
- Train a Naive Bayes model  
- Evaluate its performance  
- Deploy the model using Streamlit

---

## 🧠 Algorithm Used

- **Multinomial Naive Bayes**
  - Based on Bayes' Theorem and suited for classification with discrete features like word counts.
  - Assumes independence between features (bag-of-words model).

---

## 📁 Dataset

- The dataset contains two columns:
  - `label`: spam or ham (non-spam)
  - `message`: the actual SMS text

You can download the dataset from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection) or use the one provided in this repository.

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- CountVectorizer
- Streamlit (for deployment)
- Matplotlib / Seaborn (for visualization)

---

## 🚀 How to Run

1. **Clone the repository**  
```bash
git clone https://github.com/aliahmad552/SMS-Spam-Detection.git
cd SMS-Spam-Detection

---

## 📊 Model Evaluation
Accuracy: ~98%

Confusion Matrix, Precision, Recall, and F1-score used for detailed evaluation.

