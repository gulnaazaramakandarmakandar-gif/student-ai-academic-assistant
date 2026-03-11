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

st.title("📂 Faculty Assignment & Attendance Panel")

# -------------------------
# Load Students
# -------------------------

students_file = "data/students.csv"

if os.path.exists(students_file):
    students_df = pd.read_csv(students_file)
    usn_list = students_df["usn"].tolist()
else:
    usn_list = []

# -------------------------
# Subjects List
# -------------------------

subjects = [
    "ADA",
    "DBMS",
    "Microcontrollers",
    "Biology",
    "Maths",
    "Operating Systems",
    "Java"
]

# -------------------------
# Files
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

subject = st.selectbox("Select Subject", subjects)

usn = st.selectbox("Select Student USN", usn_list)

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

subject_att = st.selectbox("Subject for Attendance", subjects, key="att")

attendance_date = st.date_input("Select Date", value=date.today())

selected_students = st.multiselect(
    "Mark Present Students",
    usn_list
)

if st.button("Save Attendance"):

    records = []

    for usn_val in usn_list:

        status = "Present" if usn_val in selected_students else "Absent"

        records.append({
            "subject":subject_att,
            "usn":usn_val,
            "date":attendance_date,
            "status":status
        })

    df = pd.DataFrame(records)

    df.to_csv(
        attendance_file,
        mode="a",
        header=False,
        index=False
    )

    st.success("Attendance saved successfully")