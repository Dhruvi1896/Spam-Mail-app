import streamlit as st
import pickle
try:
    model = pickle.load(open('spam_model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
st.title("📧 Spam Mail Detector")

input_mail = st.text_area("Enter your message")

if st.button("Predict"):
    if input_mail.strip() == "":
        st.warning("Enter some text")
    else:
        input_data = [input_mail]
        vectorized_input = vectorizer.transform(input_data)
        
        prediction = model.predict(vectorized_input)
        st.write("Prediction Value",prediction)
        
        if prediction[0] == 1:
            st.error("🚫 Spam Mail")
        else:
            st.success("✅ Not Spam")