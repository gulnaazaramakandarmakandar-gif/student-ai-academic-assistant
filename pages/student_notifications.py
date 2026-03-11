import streamlit as st
import pandas as pd
import os
import base64

st.set_page_config(page_title="Notifications", layout="centered")
import streamlit as st

def hide_sidebar():

    hide = """
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
    </style>
    """

    st.markdown(hide, unsafe_allow_html=True)
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
# Page Title
# -------------------------

st.title("🔔 Class Notifications")

file_path = "data/notifications.csv"

# -------------------------
# Create File if Missing
# -------------------------

if not os.path.exists(file_path):

    df = pd.DataFrame(columns=["message", "semester", "subject", "time"])

    df.to_csv(file_path, index=False)

# -------------------------
# Load Notifications
# -------------------------

data = pd.read_csv(file_path)

# -------------------------
# Student Semester Selection
# -------------------------

semester = st.selectbox(
    "Select Your Semester",
    ["1","2","3","4"]
)

st.subheader("📢 Notifications")

# -------------------------
# Filter Notifications
# -------------------------

filtered = data[data["semester"].astype(str) == semester]

# -------------------------
# Display Notifications
# -------------------------

if filtered.empty:

    st.info("No notifications for your semester.")

else:

    for index, row in filtered.iterrows():

        st.warning(f"""
📢 **{row['subject']}**

{row['message']}

⏰ {row['time']}
""")