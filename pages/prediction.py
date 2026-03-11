import streamlit as st
import base64

st.set_page_config(page_title="VTU CIE Calculator", layout="centered")

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

st.title("📊 VTU CIE Marks Calculator")

subject_type = st.selectbox(
    "Select Subject Type",
    [
        "Non-Integrated Theory",
        "Integrated Theory + Lab",
        "External Lab Only"
    ]
)

# ---------------- NON INTEGRATED ----------------

if subject_type == "Non-Integrated Theory":

    ia1 = st.text_input("IA 1 (out of 15)")
    ia2 = st.text_input("IA 2 (out of 15)")
    assignment = st.text_input("Assignment / Other Assessment (out of 10)")

    if st.button("Calculate CIE"):

        try:

            ia1 = float(ia1)
            ia2 = float(ia2)
            assignment = float(assignment)

            test_scaled = (ia1 + ia2) / 2

            theory_cie = test_scaled + assignment

            st.success(f"Theory CIE = {round(theory_cie,2)} / 25")

            st.success(f"Total CIE (Scaled) = {round(theory_cie*2,2)} / 50")

        except:
            st.error("Enter valid marks")

# ---------------- INTEGRATED ----------------

elif subject_type == "Integrated Theory + Lab":

    st.subheader("Theory Component")

    ia1 = st.text_input("IA 1 (out of 15)")
    ia2 = st.text_input("IA 2 (out of 15)")
    assignment = st.text_input("Assignment (out of 10)")

    st.subheader("Practical Component")

    lab_record = st.text_input("Lab Record Evaluation (out of 15)")
    lab_test = st.text_input("Lab Test (out of 10)")

    if st.button("Calculate CIE"):

        try:

            ia1 = float(ia1)
            ia2 = float(ia2)
            assignment = float(assignment)
            lab_record = float(lab_record)
            lab_test = float(lab_test)

            theory_test = (ia1 + ia2) / 2

            theory = theory_test + assignment
            practical = lab_record + lab_test

            total_cie = theory + practical

            st.success(f"Theory CIE = {round(theory,2)} / 25")
            st.success(f"Practical CIE = {round(practical,2)} / 25")
            st.success(f"Total CIE = {round(total_cie,2)} / 50")

        except:
            st.error("Enter valid marks")

# ---------------- EXTERNAL LAB ----------------

else:

    procedure = st.text_input("Procedure (out of 15)")
    execution = st.text_input("Execution (out of 70)")
    viva = st.text_input("Viva (out of 15)")

    if st.button("Calculate External Lab Marks"):

        try:

            procedure = float(procedure)
            execution = float(execution)
            viva = float(viva)

            total = procedure + execution + viva

            st.success(f"External Lab Marks = {total} / 100")

        except:
            st.error("Enter valid marks")