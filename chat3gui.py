from freeGPT import gpt3
import streamlit as st
chat = []
def send_prompt(prompt):
    response = gpt3.Completion.create(prompt=prompt, chat=chat)
    st.write("""Response:""", response.text)
    chat.append({"question": prompt, "answer": response.text})

st.write("""# GPT3miniGUI""")
prompt = st.text_input("Prompt: ")
if st.button('Send'): send_prompt(prompt)