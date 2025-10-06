-- Nome do arquivo: aula-4.sql
-- MODELO FÍSICO: Comandos SQL para criação das tabelas da Livraria
-- Este script define a estrutura do banco de dados, incluindo tipos de dados (VARCHAR, INT, DECIMAL)
-- e as Restrições (PRIMARY KEY e FOREIGN KEY).

-- --------------------------------------
-- 1. TABELA EDITORA (Entidade Forte)
-- --------------------------------------
-- Relacionamento 1:N com LIVRO
CREATE TABLE Editora (
    -- Cod_editora é a Chave Primária (PK)
    cod_editora INT NOT NULL PRIMARY KEY,
    nome        VARCHAR(100) NOT NULL UNIQUE
);

-- --------------------------------------
-- 2. TABELA CLIENTE (Entidade Forte)
-- --------------------------------------
-- Relacionamento 1:N com PEDIDO
CREATE TABLE Cliente (
    -- Cod_cliente é a Chave Primária (PK)
    cod_cliente INT NOT NULL PRIMARY KEY,
    nome        VARCHAR(150) NOT NULL,
    endereco    VARCHAR(255)
);

-- --------------------------------------
-- 3. TABELA LIVRO
-- --------------------------------------
-- Relacionamento N:1 com EDITORA
-- Relacionamento 1:1 com ESTOQUE
-- Relacionamento N:M com PEDIDO (via ITENS_PEDIDO)
CREATE TABLE Livro (
    -- Cod_livro é a Chave Primária (PK)
    cod_livro         INT NOT NULL PRIMARY KEY,
    titulo            VARCHAR(200) NOT NULL,
    ano_publicacao    INT,
    -- cod_editora é a Chave Estrangeira (FK) que aponta para a tabela Editora
    cod_editora_fk    INT NOT NULL,

    CONSTRAINT fk_livro_editora
        FOREIGN KEY (cod_editora_fk)
        REFERENCES Editora (cod_editora)
);

-- --------------------------------------
-- 4. TABELA ESTOQUE
-- --------------------------------------
-- Relacionamento 1:1 com LIVRO (cod_livro_fk é PK e FK)
CREATE TABLE Estoque (
    -- cod_livro_fk é Chave Primária (PK) e Estrangeira (FK)
    cod_livro_fk          INT NOT NULL PRIMARY KEY,
    quantidade_disponivel INT NOT NULL DEFAULT 0,

    CONSTRAINT fk_estoque_livro
        FOREIGN KEY (cod_livro_fk)
        REFERENCES Livro (cod_livro)
);

-- --------------------------------------
-- 5. TABELA PEDIDO
-- --------------------------------------
-- Relacionamento N:1 com CLIENTE
-- Relacionamento 1:N com ITENS_PEDIDO
CREATE TABLE Pedido (
    -- Num_pedido é a Chave Primária (PK)
    num_pedido      INT NOT NULL PRIMARY KEY,
    data_pedido     DATE NOT NULL,
    valor_total     DECIMAL(10, 2) NOT NULL,
    -- cod_cliente_fk é a Chave Estrangeira (FK) que aponta para a tabela Cliente
    cod_cliente_fk  INT NOT NULL,

    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (cod_cliente_fk)
        REFERENCES Cliente (cod_cliente)
);

-- --------------------------------------
-- 6. TABELA ITENS_PEDIDO (Tabela Associativa)
-- --------------------------------------
-- Esta tabela resolve o relacionamento Muitos-para-Muitos (N:M) entre PEDIDO e LIVRO.
CREATE TABLE Itens_pedido (
    -- As duas FKs juntas formam a Chave Primária Composta (PK)
    num_pedido_fk  INT NOT NULL,
    cod_livro_fk   INT NOT NULL,
    quantidade     INT NOT NULL CHECK (quantidade > 0),
    preco_unitario DECIMAL(10, 2) NOT NULL,

    -- Define a Chave Primária Composta
    PRIMARY KEY (num_pedido_fk, cod_livro_fk),

    -- Define a primeira Chave Estrangeira para PEDIDO
    CONSTRAINT fk_itens_pedido_pedido
        FOREIGN KEY (num_pedido_fk)
        REFERENCES Pedido (num_pedido),

    -- Define a segunda Chave Estrangeira para LIVRO
    CONSTRAINT fk_itens_pedido_livro
        FOREIGN KEY (cod_livro_fk)
        REFERENCES Livro (cod_livro)
);

-- --------------------------------------
-- Exemplo de inserção de dados (Modelo Físico em ação)
-- --------------------------------------

INSERT INTO Editora (cod_editora, nome) VALUES
(101, 'Atlas Publishing'),
(102, 'Tech Books Inc.');

INSERT INTO Cliente (cod_cliente, nome, endereco) VALUES
(500, 'Mariana Silva', 'Rua A, 123');

INSERT INTO Livro (cod_livro, titulo, ano_publicacao, cod_editora_fk) VALUES
(1, 'Aventura em Python', 2023, 102),
(2, 'SQL Avançado', 2022, 102),
(3, 'Modelagem de Dados', 2021, 101);

INSERT INTO Estoque (cod_livro_fk, quantidade_disponivel) VALUES
(1, 50),
(2, 30),
(3, 25);

INSERT INTO Pedido (num_pedido, data_pedido, valor_total, cod_cliente_fk) VALUES
(1000, '2024-10-01', 150.00, 500);

-- Inserindo os itens do pedido 1000
INSERT INTO Itens_pedido (num_pedido_fk, cod_livro_fk, quantidade, preco_unitario) VALUES
(1000, 1, 1, 80.00), -- 1x Aventura em Python
(1000, 3, 1, 70.00); -- 1x Modelagem de Dados

-- --------------------------------------
-- Consulta para verificar o JOIN (Relacionamento N:N)
-- --------------------------------------

SELECT
    P.num_pedido,
    C.nome AS nome_cliente,
    L.titulo AS titulo_livro,
    I.quantidade,
    I.preco_unitario
FROM Pedido P
JOIN Cliente C ON P.cod_cliente_fk = C.cod_cliente
JOIN Itens_pedido I ON P.num_pedido = I.num_pedido_fk
JOIN Livro L ON I.cod_livro_fk = L.cod_livro
WHERE P.num_pedido = 1000;