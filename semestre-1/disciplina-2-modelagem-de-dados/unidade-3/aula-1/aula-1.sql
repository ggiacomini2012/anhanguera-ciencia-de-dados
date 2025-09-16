-- Este script SQL cria a estrutura do banco de dados para o sistema da editora,
-- com base no Diagrama Entidade-Relacionamento (DER) fornecido na aula.

-- Criação da tabela de Áreas
CREATE TABLE Areas (
    codigo_area INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao VARCHAR(255) NOT NULL
);

-- Criação da tabela de Formatos
CREATE TABLE Formatos (
    codigo_formato INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao VARCHAR(255) NOT NULL,
    altura_cm DECIMAL(5, 2),
    largura_cm DECIMAL(5, 2)
);

-- Criação da tabela de Encadernações
CREATE TABLE Encadernacoes (
    codigo_encadernacao INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao VARCHAR(255) NOT NULL
);

-- Criação da tabela de Autores
CREATE TABLE Autores (
    codigo_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo VARCHAR(255) NOT NULL,
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado CHAR(2),
    cpf VARCHAR(14) UNIQUE NOT NULL,
    rg VARCHAR(20) UNIQUE,
    telefone VARCHAR(20),
    data_nascimento DATE,
    genero VARCHAR(50),
    estado_civil VARCHAR(50),
    local_trabalho VARCHAR(255)
);

-- Criação da tabela de Livros
-- Esta tabela contém chaves estrangeiras que implementam os relacionamentos M:1
CREATE TABLE Livros (
    isbn VARCHAR(13) PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    numero_paginas INTEGER,
    peso_gramas DECIMAL(10, 2),
    custo DECIMAL(10, 2),
    preco_venda DECIMAL(10, 2),
    edicao INTEGER,
    ano_edicao INTEGER,
    numero_reimpressao INTEGER,
    numero_contrato VARCHAR(50),
    
    -- Chaves Estrangeiras para relacionamentos M:1
    area_id INTEGER NOT NULL,
    formato_id INTEGER NOT NULL,
    encadernacao_id INTEGER NOT NULL,
    
    FOREIGN KEY (area_id) REFERENCES Areas(codigo_area),
    FOREIGN KEY (formato_id) REFERENCES Formatos(codigo_formato),
    FOREIGN KEY (encadernacao_id) REFERENCES Encadernacoes(codigo_encadernacao)
);

-- Tabela de Associação para o relacionamento M:N entre Autores e Livros
-- Esta tabela é necessária para representar que vários autores podem escrever vários livros.
CREATE TABLE Autor_Livro (
    autor_id INTEGER NOT NULL,
    livro_isbn VARCHAR(13) NOT NULL,
    
    PRIMARY KEY (autor_id, livro_isbn),
    FOREIGN KEY (autor_id) REFERENCES Autores(codigo_autor),
    FOREIGN KEY (livro_isbn) REFERENCES Livros(isbn)
);
