-- aula-2.sql
-- Exemplo em SQL: Implementação do Modelo Lógico de Repositório (MLR) e MLC para Varejo.

-- O SQL define a ESTRUTURA LÓGICA que os repositórios (DW/DM) irão utilizar.

-- --- 1. MODELO LÓGICO CORPORATIVO (MLC) - Tabelas de Dimensão (DIM) ---

-- DIMENSÃO CLIENTE (MLC: Entidade Cliente)
CREATE TABLE DIM_CLIENTE (
    ID_CLIENTE INT PRIMARY KEY,              -- Chave Primária (Identificação Única)
    NOME VARCHAR(100) NOT NULL,
    REGIAO VARCHAR(50) NOT NULL,             -- Usado pela Área de Interesse Marketing
    DATA_CADASTRO DATE
);

-- DIMENSÃO PRODUTO (MLC: Entidade Produto)
CREATE TABLE DIM_PRODUTO (
    ID_PRODUTO INT PRIMARY KEY,              -- Chave Primária
    NOME_PRODUTO VARCHAR(100) NOT NULL,
    PRECO_UNITARIO DECIMAL(10, 2) NOT NULL,
    CATEGORIA VARCHAR(50)
);

-- --- 2. MODELO LÓGICO DE REPOSITÓRIO (MLR) - Tabela de Fato (FAT) ---

-- FATO VENDA (MLC: Relacionamento Venda)
-- Esta é a tabela central (FATO) no nosso Data Warehouse lógico.
CREATE TABLE FATO_VENDA (
    ID_VENDA INT PRIMARY KEY,
    ID_CLIENTE INT,                         -- Chave Estrangeira (Relacionamento com DIM_CLIENTE)
    ID_PRODUTO INT,                         -- Chave Estrangeira (Relacionamento com DIM_PRODUTO)
    QUANTIDADE INT NOT NULL,
    DATA_VENDA DATE NOT NULL,
    VALOR_TOTAL DECIMAL(10, 2),             -- Valor já calculado

    -- Definição dos Relacionamentos (Integridade dos Dados)
    FOREIGN KEY (ID_CLIENTE) REFERENCES DIM_CLIENTE(ID_CLIENTE),
    FOREIGN KEY (ID_PRODUTO) REFERENCES DIM_PRODUTO(ID_PRODUTO)
);

-- --- 3. POPULAÇÃO DE DADOS (Simulação de Inserção) ---

-- Inserção na Dimensão Cliente
INSERT INTO DIM_CLIENTE (ID_CLIENTE, NOME, REGIAO, DATA_CADASTRO) VALUES
(101, 'Ana Silva', 'Sul', '2023-01-15'),
(102, 'Bruno Costa', 'Norte', '2023-02-20'),
(103, 'Carla Meirelles', 'Sul', '2023-03-01'),
(104, 'David Lopes', 'Norte', '2023-04-10');

-- Inserção na Dimensão Produto
INSERT INTO DIM_PRODUTO (ID_PRODUTO, NOME_PRODUTO, PRECO_UNITARIO, CATEGORIA) VALUES
(501, 'Celular X', 1500.00, 'Eletronicos'),
(502, 'Notebook Y', 4500.00, 'Eletronicos'),
(503, 'Fone Z', 250.00, 'Acessorios');

-- Inserção no Fato Venda
INSERT INTO FATO_VENDA (ID_VENDA, ID_CLIENTE, ID_PRODUTO, QUANTIDADE, DATA_VENDA, VALOR_TOTAL) VALUES
(1, 101, 501, 1, '2024-09-01', 1500.00 * 1),
(2, 102, 503, 2, '2024-09-02', 250.00 * 2),
(3, 101, 502, 1, '2024-09-03', 4500.00 * 1),
(4, 104, 501, 3, '2024-09-04', 1500.00 * 3),
(5, 103, 503, 1, '2024-09-05', 250.00 * 1),
(6, 102, 502, 1, '2024-09-06', 4500.00 * 1);

-- --- 4. CONSULTA ANALÍTICA (Simulação da Área de Interesse Vendas/Marketing) ---

-- Problema: A empresa quer saber o faturamento total por região e o número de clientes únicos.
-- Esta consulta cruza a FATO (VENDAS) com a DIMENSÃO (CLIENTE),
-- utilizando o MODELO LÓGICO para obter insights.

SELECT
    DC.REGIAO,
    COUNT(DISTINCT FV.ID_CLIENTE) AS NUMERO_CLIENTES_UNICO,
    SUM(FV.VALOR_TOTAL) AS FATURAMENTO_TOTAL_REGIAO
FROM
    FATO_VENDA FV
JOIN
    DIM_CLIENTE DC ON FV.ID_CLIENTE = DC.ID_CLIENTE
GROUP BY
    DC.REGIAO
ORDER BY
    FATURAMENTO_TOTAL_REGIAO DESC;

-- Resultado esperado (exemplo):
/*
| REGIAO | NUMERO_CLIENTES_UNICO | FATURAMENTO_TOTAL_REGIAO |
|--------|-----------------------|--------------------------|
| Norte  | 2                     | 9500.00                  |
| Sul    | 2                     | 6250.00                  |
*/