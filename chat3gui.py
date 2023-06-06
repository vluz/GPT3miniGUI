from freeGPT import gpt3
import streamlit as st

def send_prompt(prompt):
    response = gpt3.Completion.create(prompt=prompt)
    st.write("""Response:""", str(response['text']))

st.write("""# GPT3 mini GUI""")
prompt = st.text_input("Prompt: ")
if st.button('Send'): send_prompt(prompt)
