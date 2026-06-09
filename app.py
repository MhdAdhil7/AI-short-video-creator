import streamlit as st
from ai_engine import generate_content
from ui_styles import apply_style

apply_style()

st.markdown("<div class='title'>AI Shorts Generator 🎬</div>", unsafe_allow_html=True)

topic = st.text_input("Enter your video idea")

if st.button("Generate"):
    with st.spinner("AI is thinking..."):
        result = generate_content(topic)

    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.write(result)
    st.markdown("</div>", unsafe_allow_html=True)