
import os
from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain.prompts import PromptTemplate


llm = ChatOllama(model="llama3")
prompt_template = PromptTemplate(
    input_variables = ["company", "position",
                       "strengths", "weaknesses"
                       ],
    template = """
        You are a career coach. Provide tailored interview tips for the position of {position} at {company}.
        Highlight your Strengths in {strengths} and prepare for question.
        about your weaknesses as {weaknesses}.
    """
)
st.title("Interview Tutor")
company = st.text_input("Company Name: ")
position = st.text_input("Position Title: ")
strengths = st.text_area("Your Strengths", height=100)
weaknesses = st.text_area("Your Weaknesses",height=100)

if company and position and strengths and weaknesses:
    response = llm.invoke(prompt_template.format(
        company = company,
        position = position,
        strengths = strengths,
        weaknesses = weaknesses
    ))
    st.write(response.content)


