.tables
.schema Aluno
.schema Turma
.schema Curso

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
FROM Curso
WHERE mensalidade > 600;

---6
SELECT nome, ano
FROM Turma
ORDER BY ano ASC;

---7
SELECT ano, 
COUNT() AS quantidade_turmas
FROM Turma
GROUP BY ano;

---8
SELECT id_turma,
SUM(nota1) / COUNT(nota1) AS media_nota1
FROM Aluno
GROUP BY id_turma;

---9
SELECT ano,
COUNT() AS quantidade_turmas
FROM Turma
GROUP BY ano
HAVING quantidade_turmas > 2;

---10
SELECT nome, mensalidade
FROM Curso
ORDER BY mensalidade DESC;