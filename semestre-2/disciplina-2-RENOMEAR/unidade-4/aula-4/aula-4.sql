-- Este script SQL simula o processo de engenharia reversa,
-- começando com a criação de um banco de dados legado e, em seguida,
-- usando comandos para "descobrir" sua estrutura, assim como um analista faria.

-- Vamos assumir que você está usando um SGBD como PostgreSQL, MySQL ou SQL Server.
-- Os comandos podem variar ligeiramente dependendo do SGBD.

-- --- Passo 1: Criação do Banco de Dados Legado (Simulação) ---

-- Crie o banco de dados e conecte-se a ele.
-- Este comando é um placeholder. Você executaria isso no seu terminal ou cliente SQL.
-- CREATE DATABASE biblioteca_legado;
-- USE biblioteca_legado; -- Ou \c biblioteca_legado para PostgreSQL

-- Criação das tabelas com nomes e estruturas não padronizadas, simulando um sistema legado.
CREATE TABLE livros_info (
    id_livro INT PRIMARY KEY,
    nome_livro VARCHAR(255) NOT NULL,
    nome_do_autor VARCHAR(255),
    ano_de_publ INT
);

CREATE TABLE membros_dados (
    identif VARCHAR(50) PRIMARY KEY,
    nome_membro VARCHAR(255) NOT NULL
);

CREATE TABLE emprestimos_registros (
    id_transacao INT PRIMARY KEY,
    livro_id INT,
    membro_identificacao VARCHAR(50),
    data_emprestimo DATE
);

-- Inserção de dados para que possamos "ver" as relações.
INSERT INTO livros_info (id_livro, nome_livro, nome_do_autor, ano_de_publ) VALUES
(1, 'Aventuras em SQL', 'Maria Joana', 2019),
(2, 'Modelagem de Dados para Iniciantes', 'João Silva', 2021);

INSERT INTO membros_dados (identif, nome_membro) VALUES
('M001', 'Paula Ferreira'),
('M002', 'Ricardo Alves');

INSERT INTO emprestimos_registros (id_transacao, livro_id, membro_identificacao, data_emprestimo) VALUES
(101, 1, 'M001', '2023-10-25'),
(102, 2, 'M002', '2023-10-26'),
(103, 1, 'M002', '2023-11-01');

-- --- Passo 2: O Processo de Engenharia Reversa com Comandos SQL ---
-- O analista não tem a documentação, então ele usa comandos para "investigar".

-- Comando para listar todas as tabelas no banco de dados.
-- MySQL: SHOW TABLES;
-- PostgreSQL: \dt
-- SQL Server: SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';

-- Comando para descrever a estrutura de uma tabela, mostrando colunas e tipos de dados.
-- MySQL: DESCRIBE livros_info;
-- PostgreSQL: \d livros_info
-- SQL Server: sp_help 'livros_info'

-- Exemplo de saída (simulada) para `DESCRIBE livros_info;`:
/*
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| id_livro       | int(11)      | NO   | PRI | NULL    |       |
| nome_livro     | varchar(255) | NO   |     | NULL    |       |
| nome_do_autor  | varchar(255) | YES  |     | NULL    |       |
| ano_de_publ    | int(11)      | YES  |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
*/

-- Comando para examinar os dados e inferir relacionamentos.
-- Analisando a tabela 'emprestimos_registros'.
SELECT * FROM emprestimos_registros;

-- Observação do Analista (Conclusão do Passo 2):
-- A coluna `livro_id` na tabela `emprestimos_registros` contém valores que parecem
-- corresponder à `id_livro` na tabela `livros_info`.
-- A coluna `membro_identificacao` na tabela `emprestimos_registros` contém valores que
-- parecem corresponder a `identif` na tabela `membros_dados`.
-- Isso sugere que estas são as **chaves estrangeiras** do sistema.

-- --- Passo 3: Criação de um Modelo Lógico (Representado por SQL) ---
-- Com as descobertas, o analista propõe um novo esquema mais claro e com restrições de integridade.

-- O novo modelo seria algo como:
-- CREATE TABLE livros (
--     id INT PRIMARY KEY,
--     titulo VARCHAR(255) NOT NULL,
--     autor VARCHAR(255),
--     ano_publicacao INT
-- );

-- CREATE TABLE membros (
--     id VARCHAR(50) PRIMARY KEY,
--     nome VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE emprestimos (
--     id INT PRIMARY KEY,
--     id_livro INT,
--     id_membro VARCHAR(50),
--     data_emprestimo DATE,
--     FOREIGN KEY (id_livro) REFERENCES livros(id),
--     FOREIGN KEY (id_membro) REFERENCES membros(id)
-- );

-- Este processo de engenharia reversa permite criar uma documentação
-- e um modelo de dados limpo a partir de um sistema existente,
-- facilitando futuras manutenções e migrações.