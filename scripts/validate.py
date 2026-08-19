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

print("\n Null Values:")
for name, df in datasets.items():
    print(f"\n{name}")
    print(df.isnull().sum())
