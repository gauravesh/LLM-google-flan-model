from langchain import HuggingFaceHub
import streamlit as st
from config import set_environment


st.set_page_config(page_title="Q and A Demo ")

set_environment()
def get_response(question):
    llm = HuggingFaceHub(repo_id='google/flan-t5-xxl')
    raw_response = llm.predict(question, raw_response=True)
    return raw_response

st.header('Langchain Application ')

inp = st.text_input('Input :' , key='input')
submit = st.button('Ask the question')

if submit:
    response = get_response(inp)
    st.subheader('Response is ')
    st.write(response)
