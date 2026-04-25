from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from main import load_data
import streamlit as st
import joblib


df=load_data("data.csv")

X=df["shop"]
Y=df["description"]

vectorizer=CountVectorizer()
X_vectorized=vectorizer.fit_transform(X)
model=MultinomialNB()
model.fit(X_vectorized,Y)

def predict_category(shop):
    vector=vectorizer.transform([shop])
    prediction=model.predict(vector)
    return prediction[0]


