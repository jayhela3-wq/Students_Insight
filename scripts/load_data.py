import pandas as pd
from sqlalchemy import create_engine

connection_string = (
    "mssql+pyodbc://localhost\\SQLEXPRESS/StudentInsights"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)
print("Connected to SQL Server successfully")