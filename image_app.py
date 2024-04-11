from openai import OpenAI
import os
import webbrowser

import streamlit as st
st.set_page_config(layout="wide")

st.image('DSU_Logo.tif', width=750)

st.header('ARTIFICIAL INTELLIGENCE IN ORGANIZATIONS (BS)', divider='rainbow')

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 30px;">The future of business</p>'
st.markdown(new_title, unsafe_allow_html=True)


st.write('**Students will learn to understand what artificial intelligence is, and what AI means for businesses and organizations and develop skills for applying artificial intelligence tools and methods in a variety of industries. With these skills, they will be prepared to help make data-driven decisions in their companies, optimize business processes and workflows, minimize costs, and maximize revenues by utilizing AI tools and applications. They will also be able to successfully navigate AI-related issues, challenges, and ethics in workplaces and be AI-aware in society.**')

st.title('🦜🔗 Image Generator')

prompt_input = st.text_input('Please enter a prompt in the textbox')
 
if prompt_input:
    client = OpenAI()


    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_input,
        size="1024x1024",
        quality="hd",
        n=1,)

    url = response.data[0].url
 
    webbrowser.open(url, new=1, autoraise=True)
