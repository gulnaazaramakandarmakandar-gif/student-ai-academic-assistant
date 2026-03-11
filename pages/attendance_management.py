import streamlit as st
import pandas as pd
import os
import base64

st.set_page_config(page_title="Attendance Management", layout="wide")

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
# PAGE TITLE
# -------------------------

st.title("📋 Attendance Management")

file_path = "data/attendance.csv"

# Ensure attendance file exists
if not os.path.exists(file_path):

    df = pd.DataFrame(columns=["subject","date","usn","status"])

    df.to_csv(file_path, index=False)

# -------------------------
# Tabs
# -------------------------

tab1, tab2 = st.tabs(["Faculty Entry", "Student Attendance"])

# -------------------------------
# FACULTY ATTENDANCE ENTRY
# -------------------------------

with tab1:

    st.subheader("Faculty Attendance Entry")

    subject = st.text_input("Subject")
    date = st.date_input("Date")

    st.write("Enter all student USNs (one per line)")
    usn_list = st.text_area("Student USNs")

    st.write("Enter present students USNs (one per line)")
    present_students = st.text_area("Present Students")

    if st.button("Save Attendance"):

        all_students = usn_list.split("\n")
        present = present_students.split("\n")

        records = []

        for usn in all_students:

            status = "Present" if usn in present else "Absent"

            records.append({
                "subject": subject,
                "date": date,
                "usn": usn.strip(),
                "status": status
            })

        df = pd.DataFrame(records)

        df.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )

        st.success("Attendance saved successfully!")

# -------------------------------
# STUDENT ATTENDANCE VIEW
# -------------------------------

with tab2:

    st.subheader("Check My Attendance")

    usn = st.text_input("Enter Your USN")

    if st.button("Check Attendance"):

        data = pd.read_csv(file_path)

        student_data = data[data["usn"] == usn]

        if student_data.empty:

            st.warning("No attendance records found")

        else:

            st.dataframe(student_data)

            total_classes = len(student_data)

            present_classes = len(
                student_data[student_data["status"] == "Present"]
            )

            percentage = (present_classes / total_classes) * 100

            st.write(f"Total Classes: {total_classes}")
            st.write(f"Classes Attended: {present_classes}")

            st.success(f"Attendance Percentage: {round(percentage,2)}%")

            st.progress(int(percentage))

            if percentage < 75:
                st.error("⚠ Warning: Attendance below 75%")
            else:
                st.success("Good attendance record")