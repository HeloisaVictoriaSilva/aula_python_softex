#1
import sqlite3 
from pathlib import Path

db_connection= sqlite3.connect('bancodados/escola_v2.db')

cursor= db_connection.cursor()

# #2
cursor.execute("""
SELECT * 
FROM Aluno
               """)

query_result = cursor.fetchall()
print(query_result)

#3
cursor.execute("""
SELECT nota1, nota2,
(nota1+nota2)/2 AS media
FROM Aluno   
ORDER BY media DESC
LIMIT 10            
               """)

query_result = cursor.fetchall()
print(query_result)

#4
cursor.execute("""
SELECT *
FROM Aluno
LEFT JOIN Turma ON Aluno.id = Turma.id                       
               """)
query_result = cursor.fetchall()
print(query_result)

#5
cursor.execute("""
SELECT *
FROM Aluno
LEFT JOIN Turma ON Aluno.id = Turma.id
WHERE Turma.id = 2                       
               """)
query_result = cursor.fetchall()
print(query_result)

db_connection.close()