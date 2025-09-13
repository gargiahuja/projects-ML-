import streamlit as st
from extractor import extract_text
from nlp_extractor import extract_params
from utils.analyzer import check_abnormal
import joblib
from utils.disease_model import predict_disease
import pandas as pd
from lifestyle import generate_full_suggestions

st.image(r"F:\ML\Medical\data\photo.png")
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>Medical Assistant</h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <p style='text-align: center; font-style: italic;'>Your Medical Partner</p>
    """,
    unsafe_allow_html=True
)
st.divider()

st.set_page_config(page_title="🩺Medical Assistant",layout="centered")
tab1,tab2,tab3=st.tabs(["Home","📄 Report Analysis", "💡 Symptom Checker"])

with tab1:
    st.markdown("""
        <h1 style='text-align: center; color: #4CAF50;'>Welcome to Medical Assistant 🏥</h1>
        <h3 style='text-align: center; color: gray;'>Your Health Companion for Early Diagnosis</h3>
        <hr style="border: 1px solid #4CAF50;">
    """, unsafe_allow_html=True)
    st.markdown("""
                
        ### 📄 Problem Statement
        Medical reports are often difficult for common people to understand. Patients cannot easily identify abnormal values or predict diseases from symptoms, leading to delays in diagnosis and treatment

        ---
                     
        ### 💡 About the App

        Medical Assistant is an AI-based healthcare application designed to support early diagnosis and awareness.
 
        - 📄 Report Analysis – Users can upload their medical reports, and the app will highlight which parameters are high or low, along with simple lifestyle suggestions to improve health.

        - 💡 Symptom Checker – Users can enter their symptoms, and the app will predict possible diseases using Machine Learning models.

        - ⚡ Easy Insights – Provides clear, easy-to-understand outputs for better decision-making without needing medical expertise.

        - 🏥 Acts as a personal health companion to guide users before consulting a doctor.
    

        ---
                

        ### 🎯 Objectives

        - 📄 To help users understand their medical reports easily.

        - ⚠ To automatically highlight abnormal parameters and suggest simple lifestyle changes.

        - 💡 To predict possible diseases based on user’s symptoms using ML models.

        - ⏳ To support early diagnosis and reduce delays in treatment.

        - 👩‍⚕ To act as a health companion before consulting a doctor.
                
        ---
                
        ### 🔍 Key Features
        - 📄 Report Analysis – Upload your medical reports (PDF/Image) and instantly see which parameters are high or low, along with health suggestions.

        - 💡 Symptom Checker – Enter your symptoms to get quick AI-powered predictions of possible diseases.
                
        - ⚡ User Friendly – Simple interface designed for anyone, even without medical knowledge.

        
        ---
                
        ### ⚙ Workflow
           Tab1:
        - Upload Report - User can upload their medical report in PDF, PNG, JPG and JPEG format.
        - Data Extraction – App reads and extracts parameters from the report.
        - Abnormal Detection - The Abnormal Parametres will be shown.
        - Lifestyle Change - Along with Abnormal Parametres, System will also suggest some suitable lifestyle changes.
        
        Tab2:
        - Symptom Input – User enters symptoms manually in Symptom Checker.
        - Disease Prediction – ML model predicts possible diseases based on symptoms.
        - Results Display – Clear, color-coded insights for easy understanding. 



        ---

        ### ⚙ Technologies Used
        - Frontend: Streamlit (Python-based UI)
        - Backend: Python
        - Report Processing: pdfplumber,pytesseract
        - Data Handling: Pandas, NumPy
        - Machine Learning: Scikit-learn, Random Forest Algorithim for disease prediction.
        - Model Management: Joblib (for saving & loading models)

        ---

        ### 📈 Future Enhancements
        - Multilingual support (Hindi, Regional languages)
        - Voice input for symptoms
        - Ask AI Health Assistant – Users can directly ask health-related queries (diet, symptoms, precautions) and get instant AI-driven guidance.
        - Cloud Storage – Securely store past reports and health history.

        ---

        ### 👩‍💻 Developed By
        - Name: Vanshika Nagpal(22AI301) and Gargi Ahuja(22AI009)
        - College: Anand International College of Engineering,Jaipur
        - Year: 4th Year (2022–2026)
        - Department: B.Tech - CS(AI)
        

        <p style='text-align: center;'>✨ Thank you for using Medical Assistant! ✨</p>
    """, unsafe_allow_html=True)

with tab2:
    uploaded = st.file_uploader("Upload report (PDF/Image):", type=['pdf','png','jpg','jpeg'])
    if uploaded:
        with open("temp", "wb") as f:
            f.write(uploaded.read())
    
        text = extract_text("temp")
        st.subheader("📄 Report Preview")
        
        params = extract_params(text)
        
        st.subheader("⚠ Health Status")
        st.dataframe(check_abnormal(params))
        params = extract_params(text)

        st.divider()
        st.subheader("🧘Lifestyle Changes")
        st.dataframe(generate_full_suggestions(params))

with tab3:
    st.header("Select Your Symptoms")
    description=pd.read_csv(r"D:\Downloads\archive\symptom_Description.csv")

    model = joblib.load("models/disease_model.pkl")
    symptom_encoder = joblib.load("models/symptom_encoder.pkl")
    label_encoder = joblib.load("models/label_encoder.pkl")
    precaution=joblib.load("F:\ML\Medical\models\prescription.pkl")

    all_symptoms = symptom_encoder.classes_.tolist()

    selected_symptoms = st.multiselect("Select your symptoms:", all_symptoms)

    if st.button("Predict Disease"):
        if selected_symptoms:
            x_input = symptom_encoder.transform([selected_symptoms])
            probs = model.predict_proba(x_input)
            top_indices = probs[0].argsort()[::-1][:3]

            st.subheader("🩺 Top 3 Predicted Diseases")
            for i in top_indices:
                disease = label_encoder.inverse_transform([model.classes_[i]])[0]
                prob = probs[0][i]
                desc = description.loc[description['Disease'] == disease, 'Description'].values[0]
                pres=precaution.loc[description['Disease'] == disease]
                
                st.markdown(f":red[*{disease}*] - {prob:.2%}")
                st.markdown(f"📝Description\n - {desc}")
                pres = precaution.loc[description['Disease'] == disease]
                if not pres.empty:
                    pres_text = ", ".join(pres.values[0])  
                else:
                    pres_text = "No precaution found."
                st.markdown(f"**😷Precaution:**\n {pres_text}")
            st.divider(width=52)
        else:
            st.warning("Please select at least one symptom.")