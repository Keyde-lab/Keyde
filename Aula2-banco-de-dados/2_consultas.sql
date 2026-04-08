-- Seleciona alunos do curso CC e mostra apenas o nome
SELECT Nome
FROM ALUNOS
WHERE Cr = 'CC';

-- Filtra mulheres do curso CC
SELECT Nome
FROM ALUNOS
WHERE Sexo = 'F' AND Cr = 'CC';

-- Junta alunos com cursos
SELECT A.Nome, C.Nome
FROM ALUNOS A
JOIN CURSOS C ON A.Cr = C.Cod;
-- Primeiro juntamos alunos com seus cursos usando a chave.
-- Depois selecionamos apenas os nomes que queremos mostrar.

-- Alunos que possuem matrícula no semestre 2026.1
SELECT DISTINCT A.Nome
FROM ALUNOS A
JOIN MATRICULAS M ON A.Matr = M.Matr
WHERE M.Sem = '2026.1';
-- Primeiro juntamos alunos com matrículas.
-- Depois filtramos o semestre e mostramos os nomes 

-- Nome do aluno e disciplina no semestre 2026.1
SELECT A.Nome, M.Disc
FROM ALUNOS A
JOIN MATRICULAS M ON A.Matr = M.Matr
WHERE M.Sem = '2026.1';
