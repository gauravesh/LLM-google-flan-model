from langchain import HuggingFaceHub
import streamlit as st
from config import set_environment
import os
st.set_page_config(page_title="Q and A Demo ")
set_environment()

def get_response(question):
    llm = HuggingFaceHub(repo_id='google/flan-t5-xxl')
    response = str(llm.predict(question))
    return response



# Ensure you have set the environment variables correctly before running this script
    
# Example usage:




st.header('Langchain Application ')

inp = st.text_input('Input :' ,key='input')
 
response= get_response(inp)
submit=st.button('Ask the question')

if submit:
    st.subheader('Response is ')
    st.write(response)
