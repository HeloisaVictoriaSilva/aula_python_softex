#1
import sqlite3 
from pathlib import Path

db_connection= sqlite3.connect('bancodados/escola_v2.db')

cursor= db_connection.cursor()

#2
cursor.execute("""
SELECT * 
FROM Aluno
               """)

query_result = cursor.fetchall()
print(query_result)

#3

db_connection.close()