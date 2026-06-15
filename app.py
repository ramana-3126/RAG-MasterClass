import streamlit as st

st.title("NIAT RAG Challenge")

def ask_bot(question):
    return f"You asked: {question}"

question = st.text_input("Ask a question")

if question:
    answer = ask_bot(question)
    st.write(answer)
