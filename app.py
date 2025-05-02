import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import os

nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))
nltk.download('punkt', download_dir=os.path.join(os.path.dirname(__file__), "nltk_data"))


ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/Text Spam Classifier")
input_sms = st.text_area("Enter the message ")


if st.button('Predict'):
    transformed_text = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_text])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")