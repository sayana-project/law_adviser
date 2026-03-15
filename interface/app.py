import streamlit as st
from agents.main_agent import Agents

if "agent" not in st.session_state:
    st.session_state["agent"] = Agents()

if "message" not in st.session_state:
    st.session_state["message"] = []

with st.sidebar:
        st.write("History")

st.title("Law Adviser")
st.write("Bienvenue sur law adviser posez vos question d'ordre juridique")
prompt = st.chat_input("say something")
if prompt:
    st.session_state["message"].append({"role": "user", "content": prompt})
    prompt_assistant = st.session_state["agent"].llm_output(st.session_state["message"])
    st.session_state["message"].append({"role": "assistant", "content": prompt_assistant})

for message in st.session_state["message"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

    