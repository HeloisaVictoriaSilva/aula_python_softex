.tables
.schema Aluno
.schema Turma
.schema Curso

---1
SELECT
COUNT() AS quantidade_alunos
FROM Aluno;

---2
SELECT 
MIN(mensalidade) AS mensalidade_me
FROM Curso;

---3
SELECT
MAX(mensalidade) AS mensalidade_ma
FROM Curso;

---4
SELECT
SUM(mensalidade) AS mensalidade_soma
FROM Curso;

---5
SELECT
AVG(nota2) AS media_nota2
FROM Aluno