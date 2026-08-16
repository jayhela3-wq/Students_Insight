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



