-- Tabela alunos
CREATE TABLE alunos (
    matr INT PRIMARY KEY,
    nome VARCHAR(100),
    sexo CHAR(1),
    cr DECIMAL(4,2)
) ENGINE=InnoDB;

-- Tabela disciplinas
CREATE TABLE disciplinas (
    cod VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(100),
    vagas INT
) ENGINE=InnoDB;

-- Tabela matriculas (COM FK)
CREATE TABLE matriculas (
    matr INT,
    cod_disc VARCHAR(10),
    semestre VARCHAR(10),

    PRIMARY KEY (matr, cod_disc),

    CONSTRAINT fk_matr FOREIGN KEY (matr)
        REFERENCES alunos(matr),

    CONSTRAINT fk_disc FOREIGN KEY (cod_disc)
        REFERENCES disciplinas(cod)

) ENGINE=InnoDB;

SHOW TABLES;

SHOW CREATE TABLE matriculas;

INSERT INTO alunos VALUES (1, 'Ana', 'F', 8.5);
INSERT INTO alunos VALUES (2, 'Bruno', 'M', 7.0);

INSERT INTO disciplinas VALUES ('BD', 'Banco de Dados', 1);

INSERT INTO disciplinas (cod, nome)
VALUES ('BD', 'Banco de Dados')
ON DUPLICATE KEY UPDATE nome = 'Banco de Dados';

INSERT INTO matriculas VALUES (999, 'BD', '2025.1');

INSERT INTO matriculas VALUES (1, 'BD', '2025.1');

SELECT * FROM matriculas;

START TRANSACTION;

SELECT vagas 
FROM disciplinas
WHERE cod = 'BD'
FOR UPDATE;

INSERT INTO matriculas VALUES (1, 'BD', '2025.1');

UPDATE disciplinas
SET vagas = vagas - 1
WHERE cod = 'BD';

COMMIT;

DROP USER IF EXISTS 'aluno'@'localhost';
DROP USER IF EXISTS 'professor'@'localhost';

CREATE USER 'aluno'@'localhost' IDENTIFIED BY '123';
CREATE USER 'professor'@'localhost' IDENTIFIED BY '123';

-- aluno: só consulta
GRANT SELECT ON universidade.* TO 'aluno'@'localhost';

-- professor: consulta e atualização
GRANT SELECT, UPDATE ON universidade.* TO 'professor'@'localhost';

FLUSH PRIVILEGES;