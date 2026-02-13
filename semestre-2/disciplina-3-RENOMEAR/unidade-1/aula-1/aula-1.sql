-- Arquivo: aula-1.sql
-- Aula 1: Introdução à Arquitetura de Dados - Modelagem Relacional e DIKW em SQL

-- ----------------------------------------------------------------------
-- PASSO 1: CRIAÇÃO DO ESQUEMA FÍSICO E MODELO RELACIONAL
-- O Arquiteto de Dados define as tabelas (Relações) e suas colunas (Atributos).
-- Utilizaremos o Modelo Relacional, ideal para a integridade de Clientes e Transações.
-- ----------------------------------------------------------------------

-- Tabela 1: Cliente (Entidade)
CREATE TABLE Cliente (
    cliente_id VARCHAR(5) PRIMARY KEY, -- Chave Primária
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50)
);

-- Tabela 2: Produto (Entidade)
CREATE TABLE Produto (
    produto_id INT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    cor VARCHAR(20)
);

-- Tabela 3: Transacao (Fato / Relacionamento 1:N com Cliente e Produto)
CREATE TABLE Transacao (
    transacao_id INT PRIMARY KEY,
    cliente_id VARCHAR(5), -- Chave Estrangeira (FK) -> Cliente
    produto_id INT,        -- Chave Estrangeira (FK) -> Produto
    valor DECIMAL(10, 2) NOT NULL,
    data_transacao DATE,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);

-- ----------------------------------------------------------------------
-- PASSO 2: DADOS (Data) BRUTOS
-- Inserção dos registros (Instâncias do Banco de Dados em um ponto no tempo).
-- ----------------------------------------------------------------------

-- Clientes
INSERT INTO Cliente (cliente_id, nome, cidade) VALUES
('C001', 'Alice Silva', 'Sao Paulo'),
('C002', 'Bruno Souza', 'Rio de Janeiro'),
('C003', 'Carla Mendes', 'Sao Paulo');

-- Produtos
INSERT INTO Produto (produto_id, nome_produto, cor) VALUES
(101, 'Camisa Polo', 'azul'),
(102, 'Calca Jeans', 'verde'),
(103, 'Tenis Casual', 'vermelho'),
(104, 'Moletom', 'verde');

-- Transações (Dados Brutos)
INSERT INTO Transacao (transacao_id, cliente_id, produto_id, valor, data_transacao) VALUES
(1001, 'C001', 101, 150.00, '2023-09-01'), -- Azul
(1002, 'C002', 102, 50.00, '2023-09-01'),  -- Verde
(1003, 'C001', 104, 200.00, '2023-09-02'), -- Verde (Cliente C001 compra Azul e Verde)
(1004, 'C003', 101, 80.00, '2023-09-02'),  -- Azul
(1005, 'C002', 103, 120.00, '2023-09-03'); -- Vermelho

-- ----------------------------------------------------------------------
-- PASSO 3: INFORMAÇÃO (Information)
-- Refino dos dados brutos: agregação e contextualização.
-- Transforma fatos isolados em contexto de cliente (Total Gasto, Compras).
-- ----------------------------------------------------------------------

SELECT
    C.cliente_id,
    C.nome,
    COUNT(T.transacao_id) AS num_compras,
    SUM(T.valor) AS total_gasto,
    SUM(T.valor) / COUNT(T.transacao_id) AS ticket_medio  -- Novo Contexto
FROM
    Cliente C
JOIN
    Transacao T ON C.cliente_id = T.cliente_id
GROUP BY
    C.cliente_id, C.nome
ORDER BY
    total_gasto DESC;

-- ----------------------------------------------------------------------
-- PASSO 4: CONHECIMENTO (Knowledge)
-- Cruzamento de informações para encontrar padrões (o "COMO").
-- Exemplo: Encontrar clientes que realizaram 'Cross-selling' (compraram Azul E Verde).
-- ----------------------------------------------------------------------

SELECT
    C.cliente_id,
    C.nome
FROM
    Cliente C
JOIN
    Transacao T ON C.cliente_id = T.cliente_id
JOIN
    Produto P ON T.produto_id = P.produto_id
WHERE
    P.cor IN ('azul', 'verde')
GROUP BY
    C.cliente_id, C.nome
-- Condição de Conhecimento: O cliente deve ter COMPRADO pelo menos uma vez 'azul' E pelo menos uma vez 'verde'.
HAVING
    COUNT(DISTINCT CASE WHEN P.cor = 'azul' THEN P.cor END) > 0 AND
    COUNT(DISTINCT CASE WHEN P.cor = 'verde' THEN P.cor END) > 0;

-- Resultado (Conhecimento): Cliente C001 comprou Azul e Verde. Isto gera o insight de Cross-selling.

-- ----------------------------------------------------------------------
-- PASSO 5: SABEDORIA (Wisdom) - Comentário
-- Ação Estratégica (o "POR QUE"): Aplicação do Conhecimento para Ação de Negócio.
-- O SQL é a ferramenta para ISOLAR a informação que dará suporte à Sabedoria.
-- ----------------------------------------------------------------------

-- SABEDORIA 1 (Baseada no CONHECIMENTO de Cross-selling):
-- A equipe de marketing deve criar uma regra para disparar cupons de desconto
-- em produtos verdes para clientes que acabaram de comprar azul (C001).

-- SABEDORIA 2 (Baseada na INFORMAÇÃO de Ticket Médio):
-- Clientes com Ticket Médio acima de R$150.00 (Cliente C001, Ticket Médio R$175.00)
-- devem ser incluídos em um programa de fidelidade VIP para retenção.