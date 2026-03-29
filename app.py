from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("placement_model.pkl")


@app.route("/", methods=["GET","POST"])
def home():

    prediction = None

    if request.method == "POST":

        age = int(request.form["Age"])
        communication = int(request.form["Communication_Skills"])
        backlogs = int(request.form["Backlogs"])
        cgpa = float(request.form["CGPA"])
        projects = int(request.form["Projects"])
        coding = float(request.form["Coding_Skills"])
        certifications = float(request.form["Certifications"])
        aptitude = int(request.form["Aptitude_Test_Score"])
        internships = float(request.form["Internships"])
        soft = int(request.form["Soft_Skills_Rating"])

        gender = request.form["Gender"]
        degree = request.form["Degree"]

        student_id = 1

        gender_female = 1 if gender == "Female" else 0
        gender_male = 1 if gender == "Male" else 0

        degree_btech = 1 if degree == "B.Tech" else 0
        degree_bca = 1 if degree == "BCA" else 0
        degree_bscit = 1 if degree == "BSc_IT" else 0
        degree_mca = 1 if degree == "MCA" else 0

        data = pd.DataFrame({
            "Student_ID":[student_id],
            "Age":[age],
            "CGPA":[cgpa],
            "Internships":[internships],
            "Projects":[projects],
            "Coding_Skills":[coding],
            "Communication_Skills":[communication],
            "Aptitude_Test_Score":[aptitude],
            "Soft_Skills_Rating":[soft],
            "Certifications":[certifications],
            "Backlogs":[backlogs],
            "Degree_B.Tech":[degree_btech],
            "Degree_BCA":[degree_bca],
            "Degree_BSc_IT":[degree_bscit],
            "Degree_MCA":[degree_mca],
            "Gender_Female":[gender_female],
            "Gender_Male":[gender_male]
        })

        prediction_result = model.predict(data)

        prediction = "Student will likely be Placed!" if prediction_result[0] == 1 else "Student will likely be Not Placed!"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)