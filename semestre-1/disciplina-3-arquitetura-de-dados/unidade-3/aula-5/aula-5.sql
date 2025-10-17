/**
 * Arquivo: aula-5.sql
 * Tema: Arquitetura de Dados Corporativos, Modelagem Dimensional e Consultas OLAP em SQL
 *
 * 1. Criação de Tabelas (Esquema Estrela)
 * 2. Inserção de Metadados e Fatos
 * 3. Consultas Analíticas (Simulação OLAP)
 */

-- ==============================================================================
-- 1. CRIAÇÃO DAS TABELAS NO DATA WAREHOUSE (DW)
--    As chaves primárias (PK) e estrangeiras (FK) garantem a integridade.
-- ==============================================================================

-- Tabela Dimensão Produto (DIM_PRODUTO)
-- Contém atributos para análise (Categorias, Nomes, etc.)
CREATE TABLE DIM_PRODUTO (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    -- Metadado de Negócio: Descrição clara do produto
    descricao_negocio VARCHAR(255)
);

-- Tabela Dimensão Tempo (DIM_TEMPO)
-- Essencial para qualquer análise de tendências e sazonalidade.
CREATE TABLE DIM_TEMPO (
    data_id DATE PRIMARY KEY,
    ano SMALLINT NOT NULL,
    trimestre SMALLINT NOT NULL,
    mes SMALLINT NOT NULL
);

-- Tabela FATO VENDAS (FACT_VENDAS)
-- Contém as métricas (Fatos) e as chaves estrangeiras (FK) para as Dimensões.
CREATE TABLE FACT_VENDAS (
    id_transacao_pk INT PRIMARY KEY,
    fk_produto INT NOT NULL,  -- Chave para DIM_PRODUTO
    fk_data DATE NOT NULL,      -- Chave para DIM_TEMPO
    uf_localizacao CHAR(2) NOT NULL, -- Simplificando Dimensão Localização
    
    valor_bruto DECIMAL(10, 2) NOT NULL,
    valor_liquido DECIMAL(10, 2) NOT NULL, -- O FATO/MÉTRICA principal (calculado no ETL)
    quantidade INT NOT NULL,
    
    -- Metadado Operacional
    data_carga TIMESTAMP,
    
    FOREIGN KEY (fk_produto) REFERENCES DIM_PRODUTO(id_produto),
    FOREIGN KEY (fk_data) REFERENCES DIM_TEMPO(data_id)
);

-- ==============================================================================
-- 2. INSERÇÃO DE DADOS (Simulando a Carga 'L' do ETL)
-- ==============================================================================

-- Inserção na DIM_PRODUTO
INSERT INTO DIM_PRODUTO (id_produto, nome_produto, categoria, descricao_negocio) VALUES
(1001, 'Notebook X', 'Eletrônicos', 'Laptop de alta performance.'),
(1002, 'MousePad', 'Acessórios', 'Mousepad ergonômico.'),
(1003, 'Fone Pro', 'Áudio', 'Headset profissional com cancelamento de ruído.');

-- Inserção na DIM_TEMPO
INSERT INTO DIM_TEMPO (data_id, ano, trimestre, mes) VALUES
('2024-10-16', 2024, 4, 10),
('2024-10-17', 2024, 4, 10);

-- Inserção na FACT_VENDAS (Valores líquidos já transformados)
INSERT INTO FACT_VENDAS (id_transacao_pk, fk_produto, fk_data, uf_localizacao, valor_bruto, valor_liquido, quantidade, data_carga) VALUES
(1, 1001, '2024-10-16', 'SP', 1500.50, 1350.45, 1, CURRENT_TIMESTAMP),
(2, 1002, '2024-10-16', 'RJ', 50.00, 45.00, 1, CURRENT_TIMESTAMP),
(3, 1003, '2024-10-17', 'SP', 200.99, 180.89, 2, CURRENT_TIMESTAMP),
(4, 1001, '2024-10-17', 'MG', 1500.50, 1350.45, 1, CURRENT_TIMESTAMP),
(5, 1002, '2024-10-17', 'RJ', 100.00, 90.00, 2, CURRENT_TIMESTAMP);


-- ==============================================================================
-- 3. CONSULTAS ANALÍTICAS (Simulação OLAP)
--    Consultas que geram insights de negócio.
-- ==============================================================================

-- 3.1. Análise OLAP 1: Total de Vendas por Categoria e Mês (Drill-Down e Roll-Up)
-- O JOIN entre FATO e DIMENSÃO é o coração da consulta dimensional.
SELECT
    DP.categoria,
    DT.mes,
    SUM(FV.valor_liquido) AS total_vendas_liquidas, -- Agregação (ROLL-UP)
    SUM(FV.quantidade) AS total_itens_vendidos
FROM
    FACT_VENDAS FV
JOIN
    DIM_PRODUTO DP ON FV.fk_produto = DP.id_produto -- JOIN Fato com Dimensão Produto
JOIN
    DIM_TEMPO DT ON FV.fk_data = DT.data_id       -- JOIN Fato com Dimensão Tempo
GROUP BY
    DP.categoria, DT.mes
ORDER BY
    DT.mes, total_vendas_liquidas DESC;

-- 3.2. Análise OLAP 2: Vendas e Quantidade por UF (Slice)
-- Agregação simples sobre uma única Dimensão (Localização)
SELECT
    uf_localizacao,
    SUM(valor_liquido) AS vendas_por_uf
FROM
    FACT_VENDAS
GROUP BY
    uf_localizacao
ORDER BY
    vendas_por_uf DESC;

-- 3.3. Uso de Metadado Operacional: Verificação de Latência (Quando o dado foi carregado?)
SELECT
    MAX(data_carga) AS ultima_carga_dw,
    MIN(fk_data) AS dado_mais_antigo_na_carga
FROM
    FACT_VENDAS;

-- 3.4. Uso de Metadado de Negócio: Consulta rápida da definição da métrica
-- Em um ambiente real, esta consulta seria feita em um Catálogo de Dados.
SELECT 
    descricao_negocio
FROM 
    DIM_PRODUTO
WHERE 
    nome_produto = 'Notebook X';