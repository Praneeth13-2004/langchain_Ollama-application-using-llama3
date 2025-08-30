import os
from langchain_community.chat_models import ChatOllama
import streamlit as st

llm = ChatOllama(model="llama3")
st.title("Ask anything")
question = st.text_input("enter question: ")
if question:
    response = llm.invoke(question)
    st.write(response.content)
