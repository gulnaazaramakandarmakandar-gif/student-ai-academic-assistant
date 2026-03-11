import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Timetable", layout="centered")

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
# Timetable UI
# -------------------------

st.title("📅 Class Timetable (Semester IV)")

day = st.selectbox(
    "Select Day",
    ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
)

# -------------------------
# Load Notifications
# -------------------------

try:
    notifications = pd.read_csv("data/notifications.csv")
except:
    notifications = pd.DataFrame(columns=["message","semester","subject","time","type"])

# -------------------------
# Timetable Data
# -------------------------

timetable = {

"Monday":[
("9:15-10:15","UHV"),
("10:15-11:15","DMS"),
("11:30-12:30","BIO"),
("12:30-1:30","MC"),
("2:30-3:30","LAB"),
("3:30-4:30","LAB"),
("4:30-5:15","NPTEL")
],

"Tuesday":[
("9:15-10:15","MC"),
("10:15-11:15","ADA"),
("11:30-12:30","DMS"),
("12:30-1:30","DBMS"),
("2:30-3:30","LAB"),
("3:30-4:30","LAB"),
("4:30-5:15","NPTEL")
],

"Wednesday":[
("9:15-10:15","BIO"),
("10:15-11:15","DMS"),
("11:30-12:30","ADA"),
("12:30-1:30","DBMS"),
("2:30-3:30","LAB"),
("3:30-4:30","LAB"),
("4:30-5:15","NPTEL")
],

"Thursday":[
("9:15-10:15","DBMS"),
("10:15-11:15","MC"),
("11:30-12:30","ADA"),
("12:30-1:30","DMS"),
("2:30-3:30","LAB LATEX"),
("3:30-4:30","LAB LATEX"),
("4:30-5:15","NPTEL")
],

"Friday":[
("9:15-10:15","AICTE Idea Lab"),
("10:15-11:15","AICTE Idea Lab"),
("11:30-12:30","LAB LATEX"),
("12:30-1:30","LAB LATEX"),
("2:30-3:30","LAB LATEX"),
("3:30-4:30","LAB LATEX")
],

"Saturday":[
("9:15-10:15","AICTE Activity/NSS"),
("10:15-11:15","AICTE Activity/NSS"),
("11:30-12:30","AICTE Activity/NSS"),
("2:30-4:30","Domain Skills")
]

}

# -------------------------
# Display Timetable
# -------------------------

st.subheader(f"📖 Timetable for {day}")

for time,subject in timetable[day]:

    status = ""

    for _,row in notifications.iterrows():

        if row["subject"] == subject and row["time"] == time:

            if row["type"] == "Cancelled":
                status = "❌ Cancelled"

            elif row["type"] == "Rescheduled":
                status = "⏰ Rescheduled"

    if status == "❌ Cancelled":

        st.error(f"{time} → {subject} {status}")

    elif status == "⏰ Rescheduled":

        st.warning(f"{time} → {subject} {status}")

    else:

        st.success(f"{time} → {subject}")