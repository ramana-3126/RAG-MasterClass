question = st.text_input("Ask a question")

if question:
    answer = ask_bot(question)
    st.write(answer)
