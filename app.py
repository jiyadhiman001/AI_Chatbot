import streamlit as st
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/bot.png", width=80)
    st.title("AI Chatbot")
    st.markdown("---")
    st.markdown("**🧠 Model:** Llama 3.3 70B")
    st.markdown("**⚡ Powered by:** Groq")
    st.markdown("**👩‍💻 Built by:** Jiya Dhiman")
    st.markdown("---")
  
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
   


st.markdown("<h1 style='text-align:center;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Ask me anything — I'm here to help!</p>", unsafe_allow_html=True)
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

system_prompt = {
    "role": "system",
    "content": "You are a helpful, friendly and intelligent AI assistant. Answer clearly and concisely."
}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)



    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[system_prompt] + st.session_state.messages
            )
        reply = response.choices[0].message.content
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})