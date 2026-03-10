import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets["Gemini"])


model = genai.GenerativeModel("gemini-2.5-flash")


st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title(" Gemini Chatbot")
st.caption("Powered by Google Gemini API")

user_input = st.text_input("Ask me anything:", placeholder="Type your question here...")

if st.button("Ask") and user_input.strip():
    with st.spinner("Thinking..."):
        response = model.generate_content(user_input)
        st.markdown(" Response:")
        st.write(response.text)