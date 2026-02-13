/*
Arquivo: aula-4.sql

Descrição:
Este script SQL demonstra a criação de tabelas e o estabelecimento
de relacionamentos com chaves primárias e estrangeiras. Ele traduz
os conceitos do modelo de entidade-relacionamento (MER) para o
SQL, o que é fundamental na prática do desenvolvimento de bancos de dados.

As tabelas 'Areas' e 'Livros' simulam o cenário de uma biblioteca.
A tabela 'Areas' é a entidade forte, com a chave primária `id_area`.
A tabela 'Livros' é a entidade fraca, com a chave primária `id_livro`
e a chave estrangeira `id_area`, que se relaciona com a tabela 'Areas'.

O script inclui:
1. Criação das tabelas com suas chaves.
2. Comentários explicando cada parte do código.
3. Inserção de dados para exemplificar o funcionamento.
4. Uma consulta `JOIN` que ilustra como as chaves conectam as tabelas,
   permitindo buscar informações de forma combinada.
*/

-- Criação da tabela de áreas (Entidade Forte)
-- Esta tabela é independente e não precisa de outras para existir.
CREATE TABLE Areas (
    -- Chave primária: identifica unicamente cada área.
    -- `INT` é o tipo de dado para números inteiros.
    -- `PRIMARY KEY` define a coluna como a chave primária.
    id_area INT PRIMARY KEY,
    
    -- `VARCHAR(100)` armazena uma string de até 100 caracteres.
    -- `NOT NULL` impede que o campo fique vazio.
    nome_area VARCHAR(100) NOT NULL
);

-- Inserindo dados na tabela 'Areas'
INSERT INTO Areas (id_area, nome_area) VALUES
(1, 'Ficção Científica'),
(2, 'Fantasia'),
(3, 'História');


-- Criação da tabela de livros (Entidade Fraca)
-- Esta tabela depende da existência da tabela 'Areas'.
CREATE TABLE Livros (
    -- Chave primária: identifica unicamente cada livro.
    id_livro INT PRIMARY KEY,
    
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    
    -- Chave Estrangeira: `id_area` se conecta à chave primária da
    -- tabela `Areas`. Isso estabelece um relacionamento entre as tabelas.
    id_area INT NOT NULL,
    
    -- A instrução `FOREIGN KEY` define a chave estrangeira.
    -- `REFERENCES Areas(id_area)` indica que o valor de `id_area`
    -- nesta tabela deve corresponder a um valor existente na
    -- coluna `id_area` da tabela `Areas`.
    FOREIGN KEY (id_area) REFERENCES Areas(id_area)
);

-- Inserindo dados na tabela 'Livros'
-- Note que o `id_area` para cada livro deve ser um valor
-- válido que já existe na tabela 'Areas'.
INSERT INTO Livros (id_livro, titulo, autor, id_area) VALUES
(101, 'Duna', 'Frank Herbert', 1),
(102, 'O Senhor dos Anéis', 'J.R.R. Tolkien', 2),
(103, 'Neuromancer', 'William Gibson', 1),
(104, 'Sapiens: Uma Breve História da Humanidade', 'Yuval Noah Harari', 3);


-- Consulta para demonstrar o relacionamento (Cardinalidade 1:M)
-- A relação é: Uma Área (1) pode ter Muitos Livros (M).
-- Usamos `JOIN` para combinar dados de ambas as tabelas
-- e mostrar o nome da área de cada livro.
SELECT
    L.titulo,
    L.autor,
    A.nome_area
FROM
    Livros L
JOIN
    Areas A ON L.id_area = A.id_area
ORDER BY
    A.nome_area, L.titulo;