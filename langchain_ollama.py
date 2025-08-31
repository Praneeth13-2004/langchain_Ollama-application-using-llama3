import os
from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain.prompts import PromptTemplate

# Page Config
st.set_page_config(page_title="Interview Tutor", layout="centered")

# App Heading / Intro
st.title("Interview Tutor")
st.markdown(
    """
    Welcome to **Interview Tutor**!  
    This app helps you **prepare for interviews** by generating **personalized tips**.  

    Just provide details about:
    - **Company** you are applying to  
    - **Position / Role** you are aiming for  
    - Your **Strengths** (what makes you a good fit)  
    - Your **Weaknesses** (areas you’re working on)  

    Then click **Enter** and get instant tailored interview guidance. 
    """
)

# Model + Prompt
llm = ChatOllama(model="llama3")
prompt_template = PromptTemplate(
    input_variables=["company", "position", "strengths", "weaknesses"],
    template="""
        You are a career coach. Provide tailored interview tips for the position of {position} at {company}.
        Highlight how to emphasize strengths in {strengths}, and prepare for potential questions
        about weaknesses such as {weaknesses}.
    """
)

# User Inputs
company = st.text_input("Company Name")
position = st.text_input("Position Title")
strengths = st.text_area("Your Strengths", height=100)
weaknesses = st.text_area(" Your Weaknesses", height=100)

# Generate Response
if company and position and strengths and weaknesses:
    with st.spinner("Generating tailored tips... ✨"):
        response = llm.invoke(
            prompt_template.format(
                company=company,
                position=position,
                strengths=strengths,
                weaknesses=weaknesses
            )
        )
    st.subheader("📌 Interview Preparation Tips")
    st.write(response.content)
