import pandas as pd
import numpy as np
from faker import Faker
import random

np.random.seed(42)
random.seed(42)
Faker.seed(42)

faker = Faker()

NUM_STUDENTS = 1000

DEPARTMENTS = ['CSE', 'IT', 'ECE', 'EEE', 'MECH', 'AI_DS']

GENDERS = ['Male', 'Female']

students = []

for i in range(NUM_STUDENTS):
    student_id = f"ST{10001 + i}"
    name = faker.name()
    gender = random.choice(GENDERS)
    department = random.choice(DEPARTMENTS)
    admission_year = random.choice([2022, 2023, 2024])
    current_semester = random.randint(1, 8)
    age = random.randint(18, 25)

    students.append([
        student_id,
        name,
        gender,
        department,
        admission_year,
        current_semester,
        age
    ])

students_df = pd.DataFrame(
    students,
    columns = [
        "StudentID", "Name", "Gender", "Department", "AdmissionYear", "CurrentSemester", "Age"
    ]
)

students_df.to_csv("data/students.csv", index=False)

print("students.csv created")
print(students_df.head())

academic_data = []

for _, student in students_df.iterrows():
    student_id = student["StudentID"]
    department = student["Department"]

    for semester in range(1, 5):
        base_score = np.random.normal(70, 10)

        if department in ['CSE', 'IT', 'AI_DS']:
            programming_score = base_score + np.random.normal(5, 5)
            dsa_score = base_score + np.random.normal(5, 5)

        else:
            programming_score = base_score + np.random.normal(0, 7)
            dsa_score = base_score + np.random.normal(0, 7)

        math_score = base_score + np.random.normal(0, 7)
        project_score = base_score + np.random.normal(3, 6)

        programming_score = np.clip(programming_score, 0, 100)
        dsa_score = np.clip(dsa_score, 0, 100)
        math_score = np.clip(math_score, 0, 100)
        project_score = np.clip(project_score, 0, 100)

        average_score = (math_score + programming_score + dsa_score + project_score)/4

        cgpa = (average_score/10) + np.random.normal(0, 0.3)
        cgpa = np.clip(cgpa, 4.0, 10.0)

        academic_data.append([
            student_id,
            semester,
            round(cgpa, 2),
            round(math_score, 2),
            round(programming_score, 2),
            round(dsa_score, 2),
            round(project_score, 2)
        ])

academic_df = pd.DataFrame(
    academic_data,
    columns = ["StudentID", "Semester", "CGPA", "MathScore", "ProgrammingScore", "DSAScore", 'ProjectScore']
)

academic_df.to_csv("data/academic_data.csv", index=False)

print("academic_data.csv created")
print(academic_df.head())

attendance_data = []

for _, row in academic_df.iterrows():
    student_id = row["StudentID"]
    semester = row["Semester"]
    cgpa = row["CGPA"]

    attendance = 45 + (cgpa*5) + np.random.normal(0, 8)

    attendance = np.clip(attendance, 40, 100)

    attendance_data.append([
        student_id, semester, round(attendance, 2)
    ])
attendance_df = pd.DataFrame(
    attendance_data,
    columns = ["StudentID", "Semester", "AttendancePercentage"]
)
attendance_df.to_csv("data/attendance.csv", index=False)

print("attendance.csv created")
print(attendance_df.head())

skills_data = []

for _, student in students_df.iterrows():
    student_id = student["StudentID"]
    department = student["Department"]
    semester =  student["CurrentSemester"]

    student_academic = academic_df[academic_df["StudentID"]==student_id]
    avg_score = student_academic[["MathScore", "ProgrammingScore", "DSAScore", "ProjectScore"]].mean().mean()

    exp_bonus = semester*2

    base_skill = (avg_score*0.6) + exp_bonus

    if department in ["CSE", "IT"]:
        python_score = base_skill + np.random.normal(8, 7)
        java_score = base_skill + np.random.normal(6,7)
        dsa_score = base_skill + np.random.normal(8, 7)
        ml_score = base_skill + np.random.normal(5, 8)
        webdev_score = base_skill + np.random.normal(7, 7)

    elif department == "AI_DS":
        python_score = base_skill + np.random.normal(10, 6)
        java_score = base_skill + np.random.normal(3, 8)
        dsa_score = base_skill + np.random.normal(7, 7)
        ml_score = base_skill + np.random.normal(12, 6)
        webdev_score = base_skill + np.random.normal(3, 8)

    else :
        python_score = base_skill + np.random.normal(2, 8)
        java_score = base_skill + np.random.normal(2, 8)
        dsa_score = base_skill + np.random.normal(3, 8)
        ml_score = base_skill + np.random.normal(1, 9)
        webdev_score = base_skill + np.random.normal(2, 8)

    communication_score = base_skill + np.random.normal(5, 8)


    python_score = np.clip(python_score, 0, 100)
    java_score = np.clip(java_score, 0, 100)
    dsa_score = np.clip(dsa_score, 0, 100)
    ml_score = np.clip(ml_score, 0, 100)
    webdev_score = np.clip(webdev_score, 0, 100)
    communication_score = np.clip(communication_score, 0, 100)

    skills_data.append([
        student_id,
        round(python_score, 2),
        round(java_score, 2),
        round(dsa_score, 2),
        round(ml_score, 2),
        round(webdev_score, 2),
        round(communication_score, 2)

    ])

skills_df = pd.DataFrame(
    skills_data,
    columns = ["StudentID", "PythonScore", "JavaScore", "DSAScore", "MLScore", "WebDevScore", "CommunicationScore"]

)

skills_df.to_csv("data/skills.csv", index=False)

print("skills.csv created")
print(skills_df.head())

placement_data = []

for _, student in students_df.iterrows():
    student_id = student["StudentID"]
    semester = student["CurrentSemester"]

    student_academic = academic_df[academic_df["StudentID"] == student_id]

    avg_cgpa = student_academic["CGPA"].mean()

    student_skills = skills_df[skills_df["StudentID"] == student_id].iloc[0]

    avg_technical_skill = student_skills[
        ["PythonScore", "JavaScore", "DSAScore", "MLScore", "WebDevScore"]
    ].mean()

    communication = student_skills["CommunicationScore"]

    internship_count = np.random.choice([0,1,2,3], p=[0.45, 0.35, 0.15, 0.05])

    hackathon_count = np.random.choice([0,1,2,3,4], p=[0.45, 0.30, 0.15, 0.07, 0.03])

    aptitude_score = (avg_cgpa*6 + avg_technical_skill*0.25 + np.random.normal(0, 8))
    aptitude_score = np.clip(aptitude_score, 0, 100)

    interview_score = (communication*0.5 + avg_technical_skill*0.3 + internship_count*4 + np.random.normal(0, 8))
    interview_score = np.clip(interview_score, 0, 100)

    resume_score = (avg_cgpa*5 + internship_count*8 + hackathon_count*3 + np.random.normal(0, 7))
    resume_score = np.clip(resume_score, 0, 100)

    placement_score = (avg_cgpa*0.20 + aptitude_score*0.20 + interview_score*0.25 + resume_score*0.15 + avg_technical_skill*0.15 + internship_count*1.5 + hackathon_count*0.5)

    probability = 1/(1 + np.exp(-(placement_score-48)/8))

    placement_status = ("Placed" if np.random.random() < probability else "Not Placed")

    placement_data.append([
        student_id,
        round(aptitude_score, 2),
        round(interview_score, 2),
        round(resume_score, 2),
        internship_count,
        hackathon_count,
        placement_status

    ])

placement_df = pd.DataFrame(
    placement_data,
    columns = ["StudentID", "AptitudeScore", "InterviewScore", "ResumeScore", "InternshipCount", "HackathonCount","PlacementStatus"]
)

placement_df.to_csv("data/placement.csv", index=False)

print("placement.csv created")
print(placement_df.head())

print("\nPlacement Distributions:")
print(placement_df["PlacementStatus"].value_counts())

feedback_data = []

positive_feedback = [
    "The courses are well structured and helpful.",
    "I am satisfied with the learning experience.",
    "The faculty members are very supportive.",
    "The placement training has been useful.",
    "The practical sessions are excellent.",
    "The academic resources are very helpful."
]

neutral_feedback = [
    "The overall experience is average.",
    "The courses are okay but could be improved.",
    "The facilities are satisfactor.",
    "The learning experience is neither good nor bad.",
    "Some aspects of the program are useful."
]

negative_feedback = [
    "The placment training needs serious improvement.",
    "The workload is too high.",
    "The faculty support could be better.",
    "The practical sessions need complete overhaul.",
    "The placement opportunities are not sufficient.",
    "The academic resources need improvement."
] 

feedback_data =[]

NUM_FEEDBACK = 5000

for i in range(NUM_FEEDBACK):
    student_id = random.choice(students_df["StudentID"].tolist())

    feedback_type = random.choices(["Positive", "Neutral", "Negative"], weights=[0.60, 0.20, 0.20])[0]

    if feedback_type == "Positive":
        feedback_text = random.chocie(positive_feedback)
        rating = random.randint(4, 5)

    elif feedback_type == "Neutral":
        feedback_text = random.choice(neutral_feedback)
        rating = 3

    else :
        feedback_text = random.choice(negative_feedback)

    feedback_date = faker.date_between(start_date = "-2y", end_date="today")

    feedback_data.append([
        f"FB{10001 + i}",
        student_id,
        feedback_date,
        rating,
        feedback_text
    ])

feedback_df = pd.DataFrame(
    feedback_data,
    columns = ["FeedbackID", "StudentID", "FeedbackDate", "Rating", "FeedbackText"] 
)

feedback_df.to_csv("data/feedback.csv", index=False)

print("feedback.csv created")
print(feedback_df.head())









