Atividade: Banco de Dados Distribuído - UEG
Disciplina
Bancos de Dados II
Instituição
Universidade Estadual de Goiás
Objetivo
Implementar um modelo simplificado de banco de dados distribuído, considerando os campi de Goianésia e Anápolis, utilizando conceitos de:
•	Fragmentação horizontal
•	Replicação
•	Transparência de dados (visões)
Estrutura do Banco de Dados
Foram criadas as seguintes tabelas principais:
•	alunos (matr, nome, cr, campus)
•	disciplinas (cod, nome)
•	matriculas (matr, cod_disc)
Tecnologias Utilizadas
•	MySQL
•	DBeaver
•	VSCode
Execução do Projeto
1. Criar banco de dados
CREATE DATABASE ueg_distribuido;
USE ueg_distribuido;
2. Criar tabelas
CREATE TABLE alunos (
    matr INT PRIMARY KEY,
    nome VARCHAR(100),
    cr DECIMAL(4,2),
    campus VARCHAR(50)
);

CREATE TABLE disciplinas (
    cod INT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE matriculas (
    matr INT,
    cod_disc INT,
    PRIMARY KEY (matr, cod_disc)
);
3. Inserir dados
INSERT INTO alunos VALUES
(1, 'Maria Silva', 8.5, 'Goianesia'),
(2, 'João Souza', 7.8, 'Anapolis'),
(3, 'Ana Lima', 9.1, 'Goianesia'),
(4, 'Carlos Mendes', 6.5, 'Anapolis');

INSERT INTO disciplinas VALUES
(101, 'Banco de Dados'),
(102, 'Algoritmos');

INSERT INTO matriculas VALUES
(1, 101),
(2, 102),
(3, 101);
Fragmentação Horizontal
A tabela alunos foi fragmentada com base no campus.
Fragmento Goianésia
CREATE TABLE alunos_goianesia AS
SELECT * FROM alunos
WHERE campus = 'Goianesia';
Fragmento Anápolis
CREATE TABLE alunos_anapolis AS
SELECT * FROM alunos
WHERE campus = 'Anapolis';
Objetivo: distribuir os dados entre os campi.
Visão Global (Transparência)
Foi criada uma VIEW para simular transparência de localização:
CREATE VIEW alunos_global AS
SELECT * FROM alunos_goianesia
UNION ALL
SELECT * FROM alunos_anapolis;
Permite consultar todos os alunos como se fosse uma única tabela.
Replicação de Dados
A tabela disciplinas foi replicada para os dois campi.
CREATE TABLE disciplinas_goianesia AS
SELECT * FROM disciplinas;

CREATE TABLE disciplinas_anapolis AS
SELECT * FROM disciplinas;
Justificativa
A replicação foi utilizada porque:
•	a tabela sofre poucas alterações
•	é muito consultada
•	melhora o desempenho local
Vantagens e Desvantagens da Replicação
Vantagens
•	Alta disponibilidade
•	Redução do tempo de consulta
•	Independência entre campi
Desvantagens
•	Necessidade de sincronização
•	Possibilidade de inconsistência temporária
•	Maior custo de atualização
Transação Distribuída (Exemplo)
Uma operação de matrícula pode envolver múltiplos nós:
INSERT INTO matriculas VALUES (4, 101);
Descrição
•	Inserção na tabela matriculas
•	Verificação do aluno em outro fragmento
•	Possível atualização em diferentes nós
Problemas possíveis
•	Falha de comunicação entre campi
•	Inconsistência de dados
•	Necessidade de rollback global
Conceitos Aplicados
•	Banco de dados distribuído
•	Fragmentação horizontal
•	Replicação
•	Transparência de localização
•	Consistência de dados
Organização do Projeto
projeto-bd-distribuido/
│
├── scripts/
│   ├── 01_create_tables.sql
│   ├── 02_insert_data.sql
│   ├── 03_fragmentacao.sql
│   ├── 04_view_global.sql
│   └── 05_replicacao.sql
│
└── README.md
Autora:
Keyde Taisa da Silva
