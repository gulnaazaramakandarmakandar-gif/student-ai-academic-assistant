import streamlit as st
import pandas as pd
import os
import base64

# -------- BACKGROUND FUNCTION --------
def add_bg():

    with open("assets/background.jpg", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """

    st.markdown(bg_style, unsafe_allow_html=True)

# Apply background
add_bg()
st.set_page_config(layout="wide")

hide_pages = """
<style>
[data-testid="stSidebarNav"] {display: none;}
</style>
"""
st.markdown(hide_pages, unsafe_allow_html=True)

st.title("🎓 Student Dashboard")

# ----------------------------
# PERSONALIZATION
# ----------------------------

if "usn" in st.session_state:

    usn = st.session_state["usn"]

    st.subheader(f"Welcome {usn}")

else:

    st.warning("Please login first")
    st.switch_page("app.py")


# ----------------------------
# STUDENT DATA
# ----------------------------

student_file = "data/students.csv"

if os.path.exists(student_file):

    data = pd.read_csv(student_file)

    student = data[data["usn"] == usn]

    if not student.empty:

        col1, col2, col3 = st.columns(3)

        with col1:
            st.info(f"Branch: {student.iloc[0]['branch']}")

        with col2:
            st.info(f"Semester: {student.iloc[0]['semester']}")

        with col3:
            st.info(f"College: {student.iloc[0]['college']}")

# ----------------------------
# SMART DASHBOARD
# ----------------------------

st.subheader("📊 Academic Overview")

attendance_percent = 0
study_progress = 0
assignments = 0

# Attendance calculation
attendance_file = "data/attendance.csv"

if os.path.exists(attendance_file):

    attendance_data = pd.read_csv(attendance_file)

    student_att = attendance_data[attendance_data["usn"] == usn]

    if not student_att.empty:

        total = len(student_att)

        present = len(student_att[student_att["status"] == "Present"])

        attendance_percent = round((present/total)*100,2)

# Assignments count
assignment_file = "data/assignments.csv"

if os.path.exists(assignment_file):

    assignment_data = pd.read_csv(assignment_file)

    student_assign = assignment_data[assignment_data["usn"] == usn]

    assignments = len(student_assign)

# Example study progress
study_progress = 60

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Attendance", f"{attendance_percent}%")

with col2:
    st.metric("Study Progress", f"{study_progress}%")

with col3:
    st.metric("Assignments Submitted", assignments)

# ----------------------------
# FEATURE NAVIGATION
# ----------------------------

st.subheader("Select a Feature")

col1, col2 = st.columns(2)

if col1.button("Predict Internal Marks"):
    st.switch_page("pages/prediction.py")

if col2.button("AI Study Assistant"):
    st.switch_page("pages/ai_assistant.py")

col3, col4 = st.columns(2)

if col3.button("Self Study Tracker"):
    st.switch_page("pages/self_study_tracker.py")

if col4.button("Result Analyzer"):
    st.switch_page("pages/result_analyzer.py")

col5, col6 = st.columns(2)

if col5.button("Notifications"):
    st.switch_page("pages/student_notifications.py")

if col6.button("Assignment Submission"):
    st.switch_page("pages/assignment_submission.py")

col7, col8 = st.columns(2)

if col7.button("Attendance Management"):
    st.switch_page("pages/attendance_management.py")

if col8.button("Timetable"):
    st.switch_page("pages/timetable.py")