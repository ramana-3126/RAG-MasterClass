import streamlit as st

st.set_page_config(page_title="NIAT RAG Challenge")

st.title("NIAT RAG Challenge")

question = st.text_input("Ask a question")

if question:
    st.write("Bot is working")
