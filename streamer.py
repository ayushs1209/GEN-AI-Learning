import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

st.set_page_config(page_title="Gemini Chat Agent", layout="centered")

st.title("💬 Gemini Chat Agent")

api_key = "AIzaSyDrjeH5J6BXvoRx0ll1lDSfauje7oYkzM4"

if not api_key:
    st.sidebar.warning("Please enter your Google AI Studio API Key to start chatting.")
    st.stop() # Stop execution if key is not provided

try:
    genai.configure(api_key=api_key)
    genai.list_models()
except Exception as e:
    st.sidebar.error(f"Error configuring Google Generative AI: {e}")
    st.sidebar.error("Please check your API key.")
    st.stop() # Stop execution if API key is invalid

if "model" not in st.session_state:
    try:
        st.session_state["model"] = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
    except Exception as e:
        st.error(f"Error initializing model: {e}")
        st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state or st.session_state.get("current_chat_api_key") != api_key:
     try:
         st.session_state.messages = []
         st.session_state["chat"] = st.session_state["model"].start_chat(history=st.session_state.messages)
         st.session_state["current_chat_api_key"] = api_key
     except Exception as e:
         st.error(f"Error starting chat session: {e}")
         st.session_state["chat"] = None # Clear chat state on error
         st.session_state["current_chat_api_key"] = None
         st.stop()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("model"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(prompt)
                model_response = response.text

                st.session_state.messages.append({"role": "model", "content": model_response})

                st.markdown(model_response)

            except Exception as e:
                st.error(f"Error sending message: {e}")
                st.session_state.messages.append({"role": "model", "content": f"Error: {e}"})
                st.markdown(f"Error: {e}")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with [Streamlit](https://streamlit.io/) and [Google Generative AI](https://ai.google.dev/docs/gemini_api_overview).")
st.sidebar.markdown("Get your API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).")