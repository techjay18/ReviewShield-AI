
import streamlit as st
import pickle

model = pickle.load(open("C:/Users/jayde/OneDrive/Desktop/Fake review detector/fake_review_model.pkl","rb"))
vectorizer = pickle.load(open("C:/Users/jayde/OneDrive/Desktop/Fake review detector/vectorizer.pkl","rb"))

st.title("ReviewShield-AI")

review = st.text_area("Enter a product review")

if st.button("Check Review"):
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)

    if prediction[0] == "CG":
        st.error("This review is FAKE")
    else:
        st.success("This review is REAL")