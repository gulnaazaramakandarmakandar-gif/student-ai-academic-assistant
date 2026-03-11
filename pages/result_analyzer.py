import streamlit as st
import base64

st.set_page_config(page_title="VTU Result Analyzer", layout="centered")

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

# ---------------------------
# PAGE TITLE
# ---------------------------

st.title("📊 VTU Result Analyzer & SGPA Calculator")

# ---------------------------
# USN INPUT
# ---------------------------

st.subheader("Check VTU Results")

usn = st.text_input("Enter your USN")

if st.button("Open VTU Result Portal"):

    if usn:

        st.link_button(
            "Click here to open VTU Results",
            "https://results.vtu.ac.in/"
        )

        st.info("Enter your USN on the VTU portal to view your results.")

    else:

        st.warning("Please enter your USN")


# ---------------------------
# ENTER SUBJECT MARKS
# ---------------------------

st.subheader("Enter Subject Marks to Calculate SGPA")

num_subjects = st.number_input(
    "Number of Subjects",
    min_value=1,
    max_value=10,
    value=5
)

subjects = []

for i in range(int(num_subjects)):

    st.write(f"### Subject {i+1}")

    col1, col2 = st.columns(2)

    with col1:
        marks = st.number_input(
            f"Marks (Subject {i+1})",
            0,
            100,
            key=f"marks{i}"
        )

    with col2:
        credit = st.number_input(
            f"Credits (Subject {i+1})",
            1,
            5,
            key=f"credit{i}"
        )

    subjects.append((marks, credit))


# ---------------------------
# GRADE POINT FUNCTION
# ---------------------------

def grade_point(marks):

    if marks >= 90:
        return 10, "O"

    elif marks >= 80:
        return 9, "A+"

    elif marks >= 70:
        return 8, "A"

    elif marks >= 60:
        return 7, "B+"

    elif marks >= 55:
        return 6, "B"

    elif marks >= 50:
        return 5, "C"

    elif marks >= 40:
        return 4, "P"

    else:
        return 0, "F"


# ---------------------------
# SGPA CALCULATION
# ---------------------------

if st.button("Calculate SGPA"):

    total_points = 0
    total_credits = 0

    st.subheader("Subject Grades")

    for i, (marks, credit) in enumerate(subjects):

        gp, grade = grade_point(marks)

        st.write(
            f"Subject {i+1} → Marks: {marks} | Grade: {grade} | Grade Point: {gp}"
        )

        total_points += gp * credit
        total_credits += credit

    sgpa = total_points / total_credits

    st.success(f"🎓 Your SGPA: {round(sgpa,2)}")

    # Performance message

    if sgpa >= 9:

        st.success("Excellent Performance! Keep it up!")

    elif sgpa >= 8:

        st.info("Very Good Performance!")

    elif sgpa >= 7:

        st.info("Good Performance. You can improve further.")

    elif sgpa >= 6:

        st.warning("Average Performance. Focus more on studies.")

    else:

        st.error("Low SGPA. Need serious improvement.")