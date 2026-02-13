-- aula-5.sql
-- Exemplo em SQL (Linguagem do Modelo Físico)
-- Aplica os conceitos do Modelo Lógico e Normalização para um SGBD.

-- ----------------------------------------------------
-- 1. ESTRUTURAÇÃO DO BANCO DE DADOS (DDL)
-- Criação das tabelas com Chaves Primárias (PRIMARY KEY) e Tipos de Dados
-- ----------------------------------------------------

-- Tabela 1: AUTOR (Entidade principal)
-- Normalização: Garante que a informação do autor não se repita em cada livro.
CREATE TABLE Autor (
    ID_Autor INT PRIMARY KEY,               -- Chave Primária (PK)
    Nome VARCHAR(255) NOT NULL,
    Data_Nascimento DATE,
    Biografia TEXT
);

-- Tabela 2: ALUNO (Entidade principal)
CREATE TABLE Aluno (
    ID_Aluno INT PRIMARY KEY,               -- Chave Primária (PK)
    Nome VARCHAR(255) NOT NULL,
    Data_Matricula DATE NOT NULL
);

-- Tabela 3: LIVRO (Entidade principal)
-- Inclui uma Chave Estrangeira (FK) para relacionar com Autor.
CREATE TABLE Livro (
    ISBN VARCHAR(17) PRIMARY KEY,           -- Chave Primária (PK) para o Livro
    Titulo VARCHAR(255) NOT NULL,
    Ano_Publicacao INT,
    ID_Autor INT,                           -- Coluna que será a FK
    -- Definição da Chave Estrangeira: Referencia a coluna ID_Autor na tabela Autor
    FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor)
);

-- Tabela 4: EMPRÉSTIMO (Entidade de Relacionamento)
-- Esta tabela implementa o relacionamento N:N (Muitos para Muitos) entre Aluno e Livro.
-- Possui DUAS Chaves Estrangeiras, garantindo a integridade referencial.
CREATE TABLE Emprestimo (
    ID_Emprestimo INT PRIMARY KEY,
    ID_Aluno INT NOT NULL,                  -- Chave Estrangeira (FK) para Aluno
    ISBN VARCHAR(17) NOT NULL,              -- Chave Estrangeira (FK) para Livro
    Data_Emprestimo DATE NOT NULL,
    Data_Devolucao_Prevista DATE NOT NULL,
    
    -- Definições das Chaves Estrangeiras
    FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID_Aluno),
    FOREIGN KEY (ISBN) REFERENCES Livro(ISBN)
);


-- ----------------------------------------------------
-- 2. INSERÇÃO DE DADOS (DML)
-- Demonstração da aplicação da Normalização: 
-- Inserimos cada entidade uma única vez.
-- ----------------------------------------------------

-- Inserção de Autores
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES
(1, 'Fernando Machado', '1975-01-20'),
(2, 'Dennis Ritchie', '1941-09-09');

-- Inserção de Alunos
INSERT INTO Aluno (ID_Aluno, Nome, Data_Matricula) VALUES
(101, 'Maria da Silva', '2023-08-15'),
(102, 'João de Souza', '2024-01-20');

-- Inserção de Livros (Referenciando o ID_Autor como FK)
INSERT INTO Livro (ISBN, Titulo, Ano_Publicacao, ID_Autor) VALUES
('978-8575225409', 'Banco de Dados Avançado', 2020, 1),
('978-0131103627', 'A Linguagem C', 1978, 2);

-- Inserção de Empréstimos (Referenciando Aluno e Livro como FKs)
INSERT INTO Emprestimo (ID_Emprestimo, ID_Aluno, ISBN, Data_Emprestimo, Data_Devolucao_Prevista) VALUES
(1, 101, '978-8575225409', '2025-10-01', '2025-10-15'),
(2, 102, '978-0131103627', '2025-10-02', '2025-10-16');

-- ----------------------------------------------------
-- 3. CONSULTA DE DADOS (DEMONSTRAÇÃO DE RELACIONAMENTOS)
-- Simulação de um relatório que "junta" as informações separadas (JOINs)
-- ----------------------------------------------------

-- Objetivo: Listar quem pegou qual livro e a data.
SELECT 
    A.Nome AS Nome_Aluno,
    L.Titulo AS Titulo_Livro,
    E.Data_Emprestimo
FROM 
    Emprestimo E
JOIN 
    Aluno A ON E.ID_Aluno = A.ID_Aluno  -- Junção da FK ID_Aluno com a PK ID_Aluno
JOIN 
    Livro L ON E.ISBN = L.ISBN;          -- Junção da FK ISBN com a PK ISBN

-- Consulta para demonstrar o relacionamento Livro -> Autor
SELECT
    L.Titulo,
    AU.Nome AS Nome_Autor,
    L.Ano_Publicacao
FROM
    Livro L
JOIN
    Autor AU ON L.ID_Autor = AU.ID_Autor;