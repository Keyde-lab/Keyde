# 🎓 Banco de Dados II – Atividade Prática

![MySQL](https://img.shields.io/badge/MySQL-Database-blue)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/license-academic-lightgrey)

---

## 📌 Sobre o Projeto

Este repositório apresenta a implementação prática dos conceitos de:

* 🔄 Controle de Concorrência
* 🔐 Segurança em Banco de Dados
* 📊 Integridade de Dados
* 💾 Recuperação (Backup e Restore)

A atividade simula um **sistema acadêmico**, com gerenciamento de alunos, disciplinas e matrículas.

---

## 🗂️ Estrutura do Banco

O banco de dados utilizado foi:

```sql id="l0qpxc"
CREATE DATABASE IF NOT EXISTS universidade;
USE universidade;
```

### 📊 Tabelas criadas

* `alunos`
* `disciplinas`
* `matriculas`

---

## 🧱 Modelagem das Tabelas

### 👨‍🎓 alunos

```sql id="10d62i"
CREATE TABLE alunos (
    matr INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sexo CHAR(1),
    cr DECIMAL(4,2)
);
```

---

### 📘 disciplinas

```sql id="9t0m5a"
CREATE TABLE disciplinas (
    cod VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    vagas INT,
    CHECK (vagas >= 0)
);
```

---

### 📝 matriculas

```sql id="szwy7h"
CREATE TABLE matriculas (
    matr INT,
    cod_disc VARCHAR(10),
    semestre VARCHAR(10),

    PRIMARY KEY (matr, cod_disc),

    FOREIGN KEY (matr) REFERENCES alunos(matr),
    FOREIGN KEY (cod_disc) REFERENCES disciplinas(cod)
);
```

---

## 📥 Inserção de Dados

```sql id="pcl00o"
INSERT INTO alunos VALUES 
(1, 'Ana', 'F', 8.5),
(2, 'Bruno', 'M', 7.0);

INSERT INTO disciplinas VALUES 
('BD', 'Banco de Dados', 1);
```

---

## 🔄 Controle de Concorrência

Implementação utilizando transações e bloqueio de registros:

```sql id="o0h2r9"
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
```

### ✔️ Objetivo:

Evitar que dois alunos ocupem a mesma vaga simultaneamente.

---

## 🔐 Segurança

Criação de usuários com permissões diferentes:

```sql id="7ahixd"
CREATE USER 'aluno'@'localhost' IDENTIFIED BY '123';
CREATE USER 'professor'@'localhost' IDENTIFIED BY '123';

GRANT SELECT ON universidade.* TO 'aluno'@'localhost';
GRANT SELECT, UPDATE ON universidade.* TO 'professor'@'localhost';

FLUSH PRIVILEGES;
```

| Usuário   | Permissões     |
| --------- | -------------- |
| aluno     | SELECT         |
| professor | SELECT, UPDATE |

---

## 📊 Integridade de Dados

Foram aplicadas:

* 🔑 **Integridade de Entidade** → PRIMARY KEY
* 🔗 **Integridade Referencial** → FOREIGN KEY
* 📏 **Integridade de Domínio** → CHECK (vagas ≥ 0)

---

## 💾 Backup e Recuperação

### 📤 Backup

```bash id="c7ap46"
mysqldump -u root -p universidade > backup.sql
```

### 📥 Restauração

```bash id="o32j92"
mysql -u root -p universidade < backup.sql
```

---

## ⚠️ Problemas Encontrados

* ❌ Tabela já existente
* ❌ Chave primária duplicada
* ❌ Comando `mysql` não reconhecido

✔️ Todos foram resolvidos durante o desenvolvimento.

---

## ✅ Conclusão

A atividade permitiu aplicar conceitos essenciais de banco de dados, garantindo:

* Consistência dos dados
* Controle de acesso
* Prevenção de erros de concorrência
* Segurança e recuperação

---

## 👨‍🏫 Referência

Material da disciplina **Banco de Dados II**
Controle de Concorrência, Segurança, Integridade e Recuperação de Dados

---
