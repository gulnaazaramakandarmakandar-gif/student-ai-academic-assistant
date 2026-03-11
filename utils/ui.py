import streamlit as st

def hide_sidebar():

    hide = """
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
    </style>
    """

    st.markdown(hide, unsafe_allow_html=True)