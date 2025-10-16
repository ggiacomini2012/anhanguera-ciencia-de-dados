-- #############################################
-- ETAPA 1: CRIAÇÃO DA ESTRUTURA (DATA WAREHOUSE)
-- A tabela FATO_VENDA armazena as métricas para análise.
-- #############################################

-- Tabela de Fatos (Armazena os fatos/eventos e as métricas)
CREATE TABLE FATO_VENDA (
    data_venda DATE NOT NULL,
    regiao_venda VARCHAR(50) NOT NULL, -- Já padronizada pelo ETL
    nome_produto VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    receita_total DECIMAL(10, 2) NOT NULL
);

-- #############################################
-- ETAPA 2: CARGA DE DADOS (Simulando o "Load" do ETL)
-- Aqui inserimos os dados que foram extraídos do ODS e transformados.
-- Note que as regiões já estão limpas/padronizadas (ex: 'Sudeste', 'Norte', 'Sul').
-- #############################################

INSERT INTO FATO_VENDA (data_venda, regiao_venda, nome_produto, quantidade, receita_total) VALUES
('2025-09-01', 'Sudeste', 'TV 50', 1, 2500.50),
('2025-09-01', 'Sudeste', 'FONE Bluetooth', 2, 300.00),
('2025-09-02', 'Norte', 'TV 50', 1, 2500.50),
('2025-09-02', 'Norte', 'FONE Bluetooth', 3, 450.00),
('2025-09-03', 'Sul', 'TV 50', 1, 2500.50),
('2025-09-03', 'Sul', 'FONE Bluetooth', 4, 600.00);

-- Verifica os dados carregados no DW
SELECT * FROM FATO_VENDA;

-- #############################################
-- ETAPA 3: CONSULTAS SQL PARA RELATÓRIOS (GROUP BY e Agregação)
-- Essas consultas são a base para Dashboards e Relatórios de BI.
-- #############################################

-- Consulta 1: Relatório de Receita Total por Região (KPI de Vendas Geográficas)
-- Simula o agrupamento de dados para ver a performance de vendas em diferentes locais.
SELECT
    regiao_venda,
    SUM(receita_total) AS ReceitaTotal
FROM
    FATO_VENDA
GROUP BY
    regiao_venda
ORDER BY
    ReceitaTotal DESC;

-- Consulta 2: Relatório de Volume de Vendas por Produto (KPI de Popularidade)
-- Simula o agrupamento para identificar o produto com maior volume de unidades vendidas.
SELECT
    nome_produto,
    SUM(quantidade) AS TotalUnidadesVendidas,
    SUM(receita_total) AS ReceitaPorProduto
FROM
    FATO_VENDA
GROUP BY
    nome_produto
ORDER BY
    TotalUnidadesVendidas DESC;

-- Consulta 3: Relatório de Desempenho Diário
-- Simula o agrupamento para monitorar a tendência de vendas ao longo do tempo.
SELECT
    data_venda,
    SUM(receita_total) AS ReceitaDiaria,
    COUNT(*) AS TotalTransacoes
FROM
    FATO_VENDA
GROUP BY
    data_venda
ORDER BY
    data_venda ASC;

-- #############################################
-- TOMADA DE DECISÃO FINAL (Visão da Análise)
-- Se a "Receita Total por Região" mostrar que o Sudeste é líder, a
-- decisão será focar em otimizar a logística para essa região.
-- #############################################

-- Exemplo de consulta que pode alimentar um velocímetro de KPI de meta de receita (Ex: R$ 10.000)
SELECT
    SUM(receita_total) AS ReceitaAcumulada,
    10000.00 AS Meta,
    (SUM(receita_total) / 10000.00) * 100 AS PorcentagemAtingida
FROM
    FATO_VENDA;