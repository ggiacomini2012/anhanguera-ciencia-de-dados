--
-- Exemplo de Script SQL para uma Biblioteca
-- Este script demonstra a implementação do Modelo Físico
-- de um banco de dados simples.
--

-- 1. Criação das Tabelas
-- Aqui, traduzimos o modelo lógico (entidades e atributos)
-- para o modelo físico (tabelas e colunas).

-- Tabela para armazenar informações sobre os autores.
-- 'id_autor' é a chave primária.
CREATE TABLE Autores (
    id_autor INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
);

-- Tabela para armazenar informações sobre os livros.
-- 'id_livro' é a chave primária.
-- 'id_autor' é a chave estrangeira, ligando Livros a Autores.
CREATE TABLE Livros (
    id_livro INT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    ano_publicacao INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor)
);

-- Tabela para registrar os empréstimos.
-- 'id_emprestimo' é a chave primária.
-- 'id_livro' é a chave estrangeira, ligando Empréstimos a Livros.
CREATE TABLE Emprestimos (
    id_emprestimo INT PRIMARY KEY,
    id_livro INT,
    nome_usuario VARCHAR(100) NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE,
    FOREIGN KEY (id_livro) REFERENCES Livros(id_livro)
);

-- 2. Inserção de Dados
-- Após a criação das tabelas, podemos inserir dados de exemplo
-- para testar o funcionamento do banco.

-- Inserindo dados na tabela Autores
INSERT INTO Autores (id_autor, nome, nacionalidade) VALUES
(1, 'Machado de Assis', 'Brasileiro'),
(2, 'Clarice Lispector', 'Brasileira'),
(3, 'J.R.R. Tolkien', 'Britânico');

-- Inserindo dados na tabela Livros
-- Note que o 'id_autor' deve corresponder a um autor existente na tabela Autores.
INSERT INTO Livros (id_livro, titulo, ano_publicacao, id_autor) VALUES
(101, 'Dom Casmurro', 1899, 1),
(102, 'Memórias Póstumas de Brás Cubas', 1881, 1),
(103, 'A Hora da Estrela', 1977, 2),
(104, 'O Senhor dos Anéis', 1954, 3);

-- Inserindo dados na tabela Empréstimos
INSERT INTO Emprestimos (id_emprestimo, id_livro, nome_usuario, data_emprestimo) VALUES
(1, 101, 'João Silva', '2024-05-10'),
(2, 104, 'Maria Oliveira', '2024-05-15');

-- 3. Consultas de Exemplo (SELECT)
-- Demonstramos como recuperar dados do banco, testando a integridade.

-- Listar todos os livros e seus respectivos autores
SELECT 
    L.titulo,
    L.ano_publicacao,
    A.nome AS autor
FROM Livros AS L
JOIN Autores AS A ON L.id_autor = A.id_autor;

-- Encontrar o nome do usuário que pegou 'Dom Casmurro' emprestado
SELECT 
    E.nome_usuario,
    E.data_emprestimo
FROM Emprestimos AS E
JOIN Livros AS L ON E.id_livro = L.id_livro
WHERE L.titulo = 'Dom Casmurro';