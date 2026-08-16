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

students_df.to_csv("../data/students.csv", index=False)

print("students.csv created")
print(students_df.head())
