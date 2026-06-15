import streamlit as st

st.title("NIAT RAG Challenge")

question = st.text_input("Ask a question")

if question:
    st.write("Bot is working!")
