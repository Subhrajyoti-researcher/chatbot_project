import streamlit as st
from langchain_helper import generate_response

def main():
    st.title("🤖 Chatbot Demo using LangChain and GPT-2")
    st.write("An end-to-end chatbot running locally on your MacBook.")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("You:", key="input")

    if st.button("Send") and user_input:
        with st.spinner("Generating response..."):
            prompt = f"The following is a conversation between a user and an AI assistant.\n\nUser: {user_input}\nAI:"
            response = generate_response(prompt)
            st.session_state.conversation.append((user_input, response))

    if st.session_state.conversation:
        for user_msg, bot_msg in reversed(st.session_state.conversation):
            st.markdown(f"**You:** {user_msg}")
            st.markdown(f"**Bot:** {bot_msg}")
            st.write("---")

if __name__ == "__main__":
    main()
