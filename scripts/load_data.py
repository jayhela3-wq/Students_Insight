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