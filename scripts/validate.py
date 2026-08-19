import pandas as pd

DATA_PATH = "data"

students = pd.read_csv(f"{DATA_PATH}/students.csv")
academic = pd.read_csv(f"{DATA_PATH}/academic_data.csv")
attendance = pd.read_csv(f"{DATA_PATH}/attendance.csv")
skills = pd.read_csv(f"{DATA_PATH}/skills.csv")
placement = pd.read_csv(f"{DATA_PATH}/placement.csv")
feedback = pd.read_csv(f"{DATA_PATH}/feedback.csv")


datasets = {
    "Students": students,
    "Academic":academic,
    "Attendance":attendance,
    "Skills":skills,
    "Placement":placement,
    "Feedback":feedback
}

print("\nRow Counts:")
for name, df in datasets.items():
    print(f"{name}:{len(df)}")

print("\nNull Values:")
for name, df in datasets.items():
    print(f"\n{name}")
    print(df.isnull().sum())

print("\nDuplicates:")
for name, df in datasets.items():
    print(f"{name}:{df.duplicated().sum()}")

print("\nRange Checks:")
print("Invalid Age:", ((students["Age"]<18) | (students["Age"]>25)).sum())
print("Invalid CGPA:", ((academic["CGPA"]<4) | (academic["CGPA"]>10)).sum())
print("Invalid Attendance:",((attendance["AttendancePercentage"]<40) | (attendance["AttendancePercentage"]>100)).sum())
print("Invalid Skill Scores:", ((skills.iloc[:,1]<0) | (skills.iloc[:,1]>100)).sum())
print("Invalid Ratings:", ((feedback["Rating"]<1) | (feedback["Rating"]>5)).sum())

student_ids = set(students["StudentID"])
print("\nForeign Key Check:")

for name, df in datasets.items():
    if "StudentID" in df.columns:
        missing_ids = set(df["StudentID"]) - student_ids
        print(f"{name}:{len(missing_ids)} invalid StudentIDs")
