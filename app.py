
import streamlit as st

st.set_page_config(
    page_title="Saleh Hweidi AI Studio",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Saleh Hweidi AI Studio")

st.subheader("AI Integration Platform")

st.write(
    "Welcome to the intelligent platform "
    "connecting MiniMax, OpenAI GPT, and Google Maps."
)

service = st.selectbox(
    "Choose an AI service",
    ["MiniMax H3", "OpenAI GPT", "Google Maps"]
)

st.write("Selected service:", service)

st.info(
    "The integration modules will be connected "
    "in the next development stage."
)
