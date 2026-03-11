import streamlit as st
import pandas as pd
import base64
import os

st.set_page_config(page_title="Assignment Submission", layout="centered")

# -------------------------
# Background Function
# -------------------------

def set_bg(image_file):

    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)


# Apply background
set_bg("assets/background.jpg")

# -------------------------
# Ensure folders exist
# -------------------------

os.makedirs("uploads", exist_ok=True)
os.makedirs("data", exist_ok=True)

file_path = "data/assignments.csv"

if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["usn","subject","assignment","file"])
    df.to_csv(file_path, index=False)
subjects = [
    "ADA",
    "DBMS",
    "Microcontrollers",
    "Biology",
    "Maths",
    "Operating Systems",
    "Java"
]
titles = [
    "Module 1",
    "Module 2",
    "Module 3",
    "Module 4",
    "Module 5"
]

# -------------------------
# Page UI
# -------------------------

st.title("📚 Assignment Submission")

usn = st.text_input("Enter USN")

subject = st.selectbox("Select Subject", subjects)

assignment_title = st.selectbox("Assignment Title", titles)

Submission = st.text_input("Enter Submission date")
# -------------------------
# Submit Assignment
# -------------------------

st.button("Submit ")

    
        