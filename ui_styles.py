import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    body {
        background-color: #1a1410;
        color: #3b2f2f;
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        color: #5c4033;
        text-align: center;
    }

    .box {
        background-color: #2a1f1a;
        padding: 20px;
        border-radius: 15px;
        color: #d2b48c;
    }
    </style>
    """, unsafe_allow_html=True)