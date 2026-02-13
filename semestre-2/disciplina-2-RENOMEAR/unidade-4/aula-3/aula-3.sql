-- Exemplificação das Formas Normais de Boyce-Codd (FNBC) e 4FN em SQL

-- Este script demonstra a aplicação das formas normais avançadas
-- na criação e estruturação de tabelas de um banco de dados.

-- =================================================================
-- Cenário 1: Forma Normal de Boyce-Codd (FNBC)
-- =================================================================
-- Problema: Uma única tabela 'FILHO_ESCOLA' que armazena informações
-- redundantes sobre a relação entre sala e professor. A dependência funcional
-- 'NumeroSala' -> 'NomeProfessor' não é baseada na chave primária da tabela.

-- Antes da FNBC (Tabela ANÔMALA)
-- NOTE: Esta tabela não deve ser criada na prática, é apenas para fins ilustrativos.
/*
CREATE TABLE FILHO_ESCOLA_ANOMALO (
    NomeFilho VARCHAR(100),
    EnderecoFilho VARCHAR(200),
    DataNascimento DATE,
    NomeEscola VARCHAR(100),
    NumeroSala VARCHAR(50),
    NomeProfessor VARCHAR(100),
    PRIMARY KEY (NomeFilho, EnderecoFilho) -- Chave primária composta
);
*/

-- Solução: Normalizar para a FNBC, dividindo a tabela em duas entidades.
-- A entidade 'Filho' contém os dados do aluno.
-- A entidade 'Sala' contém a relação entre sala, escola e professor.

-- Tabela FILHO (na FNBC)
CREATE TABLE FILHO (
    id_filho INT PRIMARY KEY AUTO_INCREMENT,
    nome_filho VARCHAR(100) NOT NULL,
    endereco_filho VARCHAR(200),
    data_nascimento DATE,
    numero_sala VARCHAR(50),
    FOREIGN KEY (numero_sala) REFERENCES SALA(numero_sala)
);

-- Tabela SALA (na FNBC)
CREATE TABLE SALA (
    numero_sala VARCHAR(50) PRIMARY KEY,
    nome_escola VARCHAR(100) NOT NULL,
    nome_professor VARCHAR(100)
);

-- Inserindo dados para demonstrar a ausência de redundância
INSERT INTO SALA (numero_sala, nome_escola, nome_professor) VALUES
('101', 'Escola X', 'Prof. Ana'),
('205', 'Escola Y', 'Prof. Carlos');

INSERT INTO FILHO (nome_filho, endereco_filho, data_nascimento, numero_sala) VALUES
('João', 'Rua A', '2015-01-10', '101'),
('Pedro', 'Rua C', '2017-09-20', '101'), -- Pedro e João compartilham a mesma sala.
('Maria', 'Rua B', '2016-05-15', '205');

-- Para ver a relação, usamos um JOIN
SELECT
    F.nome_filho,
    F.endereco_filho,
    S.nome_escola,
    S.nome_professor
FROM
    FILHO F
JOIN
    SALA S ON F.numero_sala = S.numero_sala;

-- =================================================================
-- Cenário 2: Quarta Forma Normal (4FN)
-- =================================================================
-- Problema: Uma tabela 'COMPRA' que mistura dois fatos independentes e multivalorados:
-- 1. Quais produtos um fornecedor oferece.
-- 2. Quais compradores um fornecedor atende.

-- Antes da 4FN (Tabela ANÔMALA)
/*
CREATE TABLE COMPRA_ANOMALA (
    CodFornecedor INT,
    CodProduto VARCHAR(50),
    CodComprador VARCHAR(50),
    PRIMARY KEY (CodFornecedor, CodProduto, CodComprador)
);
*/

-- Solução: Normalizar para a 4FN, dividindo a tabela em duas.
-- A entidade 'FORNECEDOR_PRODUTO' para a relação entre fornecedor e produto.
-- A entidade 'FORNECEDOR_COMPRADOR' para a relação entre fornecedor e comprador.

-- Tabela FORNECEDOR_PRODUTO (na 4FN)
CREATE TABLE FORNECEDOR_PRODUTO (
    cod_fornecedor INT,
    cod_produto VARCHAR(50),
    PRIMARY KEY (cod_fornecedor, cod_produto)
);

-- Tabela FORNECEDOR_COMPRADOR (na 4FN)
CREATE TABLE FORNECEDOR_COMPRADOR (
    cod_fornecedor INT,
    cod_comprador VARCHAR(50),
    PRIMARY KEY (cod_fornecedor, cod_comprador)
);

-- Inserindo dados para demonstrar a separação dos fatos
INSERT INTO FORNECEDOR_PRODUTO (cod_fornecedor, cod_produto) VALUES
(101, 'BA3'),
(102, 'CJ10'),
(110, '88A'),
(530, 'BA3');

INSERT INTO FORNECEDOR_COMPRADOR (cod_fornecedor, cod_comprador) VALUES
(101, '01'),
(102, '05'),
(110, '25'),
(530, '01'),
(101, '25'); -- Agora podemos associar o fornecedor 101 a outro comprador sem repetir a info do produto.

-- Consultando as tabelas normalizadas
SELECT * FROM FORNECEDOR_PRODUTO;
SELECT * FROM FORNECEDOR_COMPRADOR;

-- Conclusão: A normalização avança a estrutura de dados para o nível de integridade e eficiência ideal,
-- evitando redundâncias e anomalias de forma clara e estruturada.