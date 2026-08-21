import pandas as pd
from sqlalchemy import create_engine

connection_string = (
    "mssql+pyodbc://localhost\\SQLEXPRESS/StudentInsights"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)
print("Connected to SQL Server successfully")

students_df = pd.read_csv("data/students.csv")
print("CSV loaded")
print(students_df.head())

students_df.to_sql(
    "students",
    con = engine,
    if_exists = "append",
    index = False
)

print("Students data inserted successfully")

academic_df = pd.read_csv("data/academic_data.csv") 
print("\nAcademic Data")
print(academic_df.head())

academic_df.to_sql(
    "academic_data",
    con = engine,
    if_exists = "append",
    index = False
)

print("Academic data inserted successfully")

attendance_df = pd.read_csv("data/attendance.csv")

print("\nAttendance data:")
print(attendance_df.head())

attendance_df.to_sql(
    "attendance",
    con = engine,
    if_exists = "append",
    index = False
)

print("Attendance data inserted successfully")

feedback_df = pd.read_csv("data/feedback.csv")

print("\nFeedback data:")
print(feedback_df.head())

feedback_df.to_sql(
    "feedback",
    con = engine,
    if_exists = "append",
    index = False
)

print("Feedback data inserted")


skills_df = pd.read_csv("data/skills.csv")

print("Skills data:")
print(skills_df.head())

skills_df.to_sql(
    "skills",
    con = engine,
    if_exists = "append",
    index = False
)

print("Skills data inserted")

placement_df = pd.read_csv("data/placement.csv")

print("Placement data:")
print(placement_df.head())

placement_df.to_sql(
    "placement",
    con = engine,
    if_exists = "append",
    index = False
)

print("Placement data inserted")