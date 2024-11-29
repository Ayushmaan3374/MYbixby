from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
def my_output(query):
    response = model.generate_content(query)
    return response.text


#### UI Development using streamlit


st.set_page_config(page_title = "BIXBY")
st.header("BIXBY")
input = st.text_input("Input ",key = "input")
submit = st.button("Just Ask... ")

if submit :
    response = my_output(input)
    #st.subheader("")
    st.write(response)

