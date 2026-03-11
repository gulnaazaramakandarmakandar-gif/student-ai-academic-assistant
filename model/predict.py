import joblib
import numpy as np

model = joblib.load("model/model.pkl")

def attendance_marks(attended_days):

    percentage = (attended_days / 90) * 100

    if percentage >= 90:
        return 15
    elif percentage >= 80:
        return 12
    elif percentage >= 70:
        return 9
    elif percentage >= 60:
        return 6
    else:
        return 0


def calculate_internal(ia1, ia2, assignment, lab, attended_days):

    att_marks = attendance_marks(attended_days)

    internal_total = ia1 + ia2 + assignment + lab + att_marks

    return internal_total


def predict_marks(ia1, ia2, assignment, lab, attended_days):

    internal = calculate_internal(ia1, ia2, assignment, lab, attended_days)

    data = np.array([[attended_days, internal]])

    prediction = model.predict(data)

    return round(prediction[0],2), internal