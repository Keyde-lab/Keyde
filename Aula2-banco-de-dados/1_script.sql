-- Comando para criar o banco de dados   
CREATE DATABASE aula2;
USE aula2;

-- Comando para criar as tabelas
CREATE TABLE CURSOS (
    Cod VARCHAR(10) PRIMARY KEY,
    Nome VARCHAR(50),
    Depto VARCHAR(50),
    Coord VARCHAR(50)
);

CREATE TABLE ALUNOS (
    Matr INT PRIMARY KEY,
    Nome VARCHAR(50),
    Sexo CHAR(1),
    Cr VARCHAR(10),
    FOREIGN KEY (Cr) REFERENCES CURSOS(Cod)
);

CREATE TABLE MATRICULAS (
    Matr INT,
    Disc VARCHAR(50),
    T VARCHAR(10),
    Sem VARCHAR(10),
    FOREIGN KEY (Matr) REFERENCES ALUNOS(Matr)
);

-- Inserir dados 
INSERT INTO CURSOS VALUES
('CC', 'Ciencia da Computacao', 'Exatas', 'Joao'),
('SI', 'Sistemas de Informacao', 'Exatas', 'Maria'),
('ADM', 'Administracao', 'Humanas', 'Carlos');

INSERT INTO ALUNOS VALUES
(1, 'Ana', 'F', 'CC'),
(2, 'Bruno', 'M', 'CC'),
(3, 'Carla', 'F', 'SI'),
(4, 'Daniel', 'M', 'SI'),
(5, 'Eva', 'F', 'ADM'),
(6, 'Felipe', 'M', 'CC'),
(7, 'Giovana', 'F', 'CC'),
(8, 'Henrique', 'M', 'ADM'),
(9, 'Isabela', 'F', 'SI'),
(10, 'Joao', 'M', 'CC');

INSERT INTO MATRICULAS VALUES
(1,'BD','A','2026.1'),
(2,'BD','A','2026.1'),
(3,'ED','A','2026.1'),
(4,'POO','A','2026.1'),
(5,'ADM','A','2026.1'),
(6,'BD','A','2026.1'),
(7,'ED','A','2026.1'),
(8,'ADM','A','2026.1'),
(9,'POO','A','2026.1'),
(10,'BD','A','2026.1'),
(1,'ED','A','2025.2'),
(2,'POO','A','2025.2'),
(3,'BD','A','2025.2'),
(4,'ED','A','2025.2'),
(5,'ADM','A','2025.2'),
(6,'POO','A','2025.2'),
(7,'BD','A','2025.2'),
(8,'ADM','A','2025.2'),
(9,'ED','A','2025.2'),
(10,'POO','A','2025.2');