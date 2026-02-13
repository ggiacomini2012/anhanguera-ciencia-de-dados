-- 1. DADOS ESTRUTURADOS: Criação da Tabela de Clientes

-- A tabela de clientes é o exemplo clássico de dados estruturados. 
-- Cada coluna tem um tipo de dado fixo (INT, VARCHAR, DECIMAL), e a estrutura é rígida.
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    data_cadastro DATE,
    satisfacao_media DECIMAL(3, 2) -- Média de 0.00 a 5.00
);

-- Inserção de Dados Estruturados
INSERT INTO clientes (id_cliente, nome, cpf, data_cadastro, satisfacao_media) VALUES
(1, 'Mario de Souza', '111.111.111-11', '2023-01-15', 4.50),
(2, 'Anderson Inácio', '222.222.222-22', '2023-03-20', 3.80),
(3, 'Marina Silva', '333.333.333-33', '2024-05-10', 5.00);

-- Consulta (Query) de Dados Estruturados (rápida e precisa)
SELECT nome, satisfacao_media 
FROM clientes
WHERE satisfacao_media > 4.00;

-----------------------------------------------------------

-- 2. INTEGRAÇÃO com DADOS NÃO ESTRUTURADOS e PARCIALMENTE ESTRUTURADOS

-- Embora o SQL seja para dados estruturados, podemos USÁ-LO para gerenciar metadados 
-- e referências aos outros tipos de dados, que geralmente ficam em Data Lakes (arquivos) 
-- ou Bancos NoSQL (JSON).

CREATE TABLE avaliacoes_produtos (
    id_avaliacao INT PRIMARY KEY,
    id_produto VARCHAR(50) NOT NULL,
    id_cliente INT, -- Chave estrangeira para dados estruturados (tabela clientes)
    estrelas INT NOT NULL, -- DADO ESTRUTURADO (Rating fixo 1-5)
    
    -- Coluna para DADOS NÃO ESTRUTURADOS (o texto do comentário)
    comentario_texto_livre TEXT, 
    
    -- Coluna para DADOS PARCIALMENTE ESTRUTURADOS (o JSON com detalhes adicionais)
    -- Em alguns SGBDs (PostgreSQL, MySQL >= 5.7), existe um tipo nativo JSON.
    -- Aqui, usamos um TEXT ou VARCHAR longo para compatibilidade.
    dados_flexiveis_json TEXT
);

-- Inserção mostrando a combinação dos dados:
INSERT INTO avaliacoes_produtos (
    id_avaliacao, id_produto, id_cliente, estrelas, comentario_texto_livre, dados_flexiveis_json
) VALUES
(
    101, 
    'PROD-X', 
    1, 
    5, 
    'Produto excelente, exatamente como na foto. A cor é incrível!', -- DADO NÃO ESTRUTURADO
    '{ "data_postagem": "2024-10-12", "versao_produto": "v2.0", "link_video_unboxing": "https://data.com/video1" }' -- DADO PARCIALMENTE ESTRUTURADO (JSON)
),
(
    102, 
    'PROD-Y', 
    2, 
    2, 
    'Extremamente decepcionado. A entrega atrasou e o material é frágil.', 
    '{ "data_postagem": "2024-10-13", "motivo_atraso": "logistica", "tags_analise": ["atraso", "fragil"] }'
);


-- Consulta para identificar clientes que deram poucas estrelas (Estruturado) e ler o texto (Não Estruturado)
SELECT 
    c.nome, 
    ap.estrelas, 
    ap.comentario_texto_livre 
FROM clientes c
JOIN avaliacoes_produtos ap ON c.id_cliente = ap.id_cliente
WHERE ap.estrelas <= 2;

-- Exemplo de consulta que manipularia o JSON (dados parcialmente estruturados)
-- Nota: A sintaxe exata depende do SGBD (ex: JSON_EXTRACT no MySQL ou ->> no PostgreSQL)
-- Simulação (usando JSON_EXTRACT, comum em alguns SGBDs):
-- SELECT id_avaliacao, JSON_EXTRACT(dados_flexiveis_json, '$.link_video_unboxing') AS link_externo FROM avaliacoes_produtos;