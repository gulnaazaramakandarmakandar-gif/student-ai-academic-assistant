import streamlit as st
import pandas as pd
import base64
import os
from datetime import date

st.set_page_config(page_title="Faculty Assignment Upload", layout="centered")

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

set_bg("assets/background.jpg")

# -------------------------
# Page Title
# -------------------------

st.title("📂 Faculty Assignment & Attendance Panel")

# -------------------------
# File Setup
# -------------------------

assignment_file = "data/assignment_list.csv"
attendance_file = "data/attendance.csv"

if not os.path.exists(assignment_file):
    pd.DataFrame(columns=["subject","usn","marks"]).to_csv(assignment_file,index=False)

if not os.path.exists(attendance_file):
    pd.DataFrame(columns=["subject","usn","date","status"]).to_csv(attendance_file,index=False)

# -------------------------
# Assignment Marks Entry
# -------------------------

st.subheader("📑 Enter Assignment Marks")

subject = st.text_input("Subject")

usn = st.text_input("Student USN")

marks = st.number_input("Assignment Marks",0,100)

if st.button("Save Assignment Marks"):

    data = pd.DataFrame([{
        "subject":subject,
        "usn":usn,
        "marks":marks
    }])

    data.to_csv(
        assignment_file,
        mode="a",
        header=False,
        index=False
    )

    st.success("Assignment marks saved successfully")

# -------------------------
# Attendance Entry
# -------------------------

st.subheader("📅 Attendance Entry")

subject_att = st.text_input("Subject for Attendance")

attendance_date = st.date_input("Select Date", value=date.today())

st.write("Mark Attendance")

usn1 = st.text_input("Student USN 1")
present1 = st.checkbox("Present", key="p1")

usn2 = st.text_input("Student USN 2")
present2 = st.checkbox("Present", key="p2")

usn3 = st.text_input("Student USN 3")
present3 = st.checkbox("Present", key="p3")

if st.button("Save Attendance"):

    records = []

    students = [
        (usn1,present1),
        (usn2,present2),
        (usn3,present3)
    ]

    for usn_val, status in students:

        if usn_val != "":

            records.append({
                "subject":subject_att,
                "usn":usn_val,
                "date":attendance_date,
                "status":"Present" if status else "Absent"
            })

    df = pd.DataFrame(records)

    df.to_csv(
        attendance_file,
        mode="a",
        header=False,
        index=False
    )

    st.success("Attendance saved successfully")