import streamlit as st
import pandas as pd
import os
import base64

st.set_page_config(page_title="AI Student Academic Assistant", layout="centered")

# ---------- Background Function ----------
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

    /* Calligraphy heading */
    .main-title {{
        font-family: "Brush Script MT", "Lucida Handwriting", cursive;
        font-size: 60px;
        text-align: center;
        color: #2f2f2f;
        margin-bottom: 30px;
    }}

    /* Warning style */
    .warning-text {{
        background-color: rgba(255, 200, 0, 0.2);
        padding: 12px;
        border-radius: 8px;
        font-size: 18px;
        color: #7a4f01;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }}

    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)


# Apply background
set_bg("assets/background.jpg")

# ---------- Custom Title ----------
st.markdown(
"""
<div class="main-title">
🎓 AI Student Academic Assistant
</div>
""",
unsafe_allow_html=True
)

# ---------- Login Input ----------
usn = st.text_input("Enter your USN").upper()

# ---------- Login Button ----------
if st.button("Login"):

    if usn == "":

        st.markdown(
        """
        <div class="warning-text">
        ⚠ Please enter your USN
        </div>
        """,
        unsafe_allow_html=True
        )

    else:

        file_path = "data/students.csv"

        if not os.path.exists(file_path):

            st.error("Student database not found")

        else:

            data = pd.read_csv(file_path)

            if usn in data["usn"].astype(str).values:

                st.session_state["usn"] = usn

                st.success(f"Login successful. Welcome {usn}!")

                st.switch_page("pages/dashboard.py")

            else:

                st.error("USN not found")