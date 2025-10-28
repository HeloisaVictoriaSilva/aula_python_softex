.tables
.schema Aluno
---1
SELECT * FROM Aluno;
---2
SELECT 
    nome,
    nota1
FROM Aluno;

---3
SELECT nome, nota1
FROM Aluno
WHERE nota1 >= 8;

---4
SELECT nome, data_nascimento
FROM Aluno
WHERE data_nascimento >= 2000;

---5
SELECT nome, mensalidade
FROM Aluno
WHERE mensalidade > 600;