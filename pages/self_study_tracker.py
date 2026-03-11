import streamlit as st
import base64

st.set_page_config(page_title="Self Study Tracker", layout="centered")

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

st.title("📚 StudentSelf Prep Tracker")

usn = st.text_input("Enter USN")

semester = st.selectbox(
    "Select Semester",
    ["1","2","3","4"]
)

# -------------------------
# Subject Data
# -------------------------

subjects_by_sem = {
    "1": {
        "Maths 1": 4,
        "Physics": 4,
        "C Programming": 3,
        "RES": 3,
        "Intro to CivilEng": 3,
        "Eng": 1,
        "IDT": 1
    },

    "2": {
        "Maths 2": 4,
        "Chemistry": 4,
        "Python": 3,
        "Intro to ELN": 3,
        "Constitution": 1,
        "Kannada": 1
    },

    "3": {
        "DSA": 3,
        "DDCO": 4,
        "Operating Systems": 4,
        "Java": 3,
        "Maths 3": 4
    },

    "4": {
        "ADA": 3,
        "Microcontrollers": 4,
        "Biology": 2,
        "DBMS": 4,
        "Maths 4": 4
    }
}

subjects = subjects_by_sem[semester]

# -------------------------
# External Prediction Logic
# -------------------------

def predict_external(progress, credit):

    weighted_score = progress + (credit * 5)

    if weighted_score >= 90:
        return "85 - 100"

    elif weighted_score >= 75:
        return "70 - 84"

    elif weighted_score >= 60:
        return "55 - 69"

    elif weighted_score >= 40:
        return "40 - 54"

    else:
        return "Below 40 (Risk)"


# -------------------------
# Module Tracking
# -------------------------

for subject, credit in subjects.items():

    st.write(f"### {subject} (Credits: {credit})")

    m1 = st.checkbox(f"{subject} - Module 1")
    m2 = st.checkbox(f"{subject} - Module 2")
    m3 = st.checkbox(f"{subject} - Module 3")
    m4 = st.checkbox(f"{subject} - Module 4")
    m5 = st.checkbox(f"{subject} - Module 5")

    completed = sum([m1, m2, m3, m4, m5])

    progress = (completed / 5) * 100

    st.write(f"Preparation: {progress}%")

    st.progress(int(progress))

    prediction = predict_external(progress, credit)

    st.write(f"Estimated External Marks: {prediction}")

    if progress < 40:

        st.error("⚠ High Risk – increase preparation")

    elif progress < 60:

        st.warning("Moderate preparation")

    else:

        st.success("Good preparation")