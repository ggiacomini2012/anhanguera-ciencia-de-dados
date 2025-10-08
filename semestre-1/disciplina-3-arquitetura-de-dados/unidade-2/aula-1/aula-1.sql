-- aula-1.sql
-- Autor: Exemplificando Aula
-- Descrição: Este script define a arquitetura de dados padronizada para o
--            aplicativo de supermercado, servindo de base para os sistemas
--            da aplicação (mobile, distribuídos, etc.).

-- --- SEÇÃO 1: PADRONIZAÇÃO E ESTRUTURA BASE ---
-- A padronização aqui é crucial. Usamos:
-- - Nomes de tabelas e colunas em snake_case (ex: nome_coluna).
-- - Nomes de tabelas no singular (ex: usuario, produto).
-- - Chaves primárias claras (ex: id_usuario).
-- - Tipos de dados consistentes e restrições para garantir a integridade.

-- Tabela de Usuários
-- Armazena informações dos clientes do app.
CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY, -- SERIAL cria um ID numérico auto-incremental.
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE, -- UNIQUE garante que não haja e-mails duplicados.
    senha_hash VARCHAR(255) NOT NULL, -- NUNCA armazene senhas em texto plano!
    tipo_usuario VARCHAR(10) NOT NULL CHECK (tipo_usuario IN ('normal', 'premium')), -- Garante que o valor seja apenas 'normal' ou 'premium'.
    ultima_plataforma VARCHAR(10) CHECK (ultima_plataforma IN ('ios', 'android')), -- Útil para análises mobile.
    data_criacao TIMESTAMPTZ DEFAULT NOW() -- TIMESTAMPTZ armazena o timestamp com fuso horário.
);

-- Tabela de Produtos
-- O catálogo de produtos do supermercado.
CREATE TABLE produto (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL CHECK (preco >= 0), -- Garante que o preço não seja negativo.
    estoque INT NOT NULL DEFAULT 0 CHECK (estoque >= 0)
);


-- --- SEÇÃO 2: ESTRUTURANDO DADOS PARA OS SERVIÇOS (Carrinho e Histórico) ---
-- Estas tabelas suportam as funcionalidades dos nossos "microservices".

-- Tabela do Histórico de Compras
-- Essencial para o serviço de recomendação e para o negócio.
CREATE TABLE historico_compra (
    id_compra SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL REFERENCES usuario(id_usuario), -- Chave estrangeira ligando ao usuário.
    id_produto INT NOT NULL REFERENCES produto(id_produto), -- Chave estrangeira ligando ao produto.
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    data_compra TIMESTAMPTZ DEFAULT NOW()
);


-- --- SEÇÃO 3: PADRÕES DE DADOS PARA RECOMENDAÇÕES E PERSONALIZAÇÃO ---
-- Esta tabela demonstra um padrão para otimizar o desempenho do serviço de recomendação.
-- Em vez de calcular recomendações em tempo real (o que pode ser lento), podemos
-- pré-calcular e armazenar os resultados aqui.

CREATE TABLE recomendacao_gerada (
    id_recomendacao SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL REFERENCES usuario(id_usuario),
    id_produto_recomendado INT NOT NULL REFERENCES produto(id_produto),
    algoritmo_usado VARCHAR(50), -- Ex: 'comprados_juntos', 'tendencias_locais'
    score_confianca FLOAT, -- Um valor de 0 a 1 indicando a força da recomendação.
    data_geracao TIMESTAMPTZ DEFAULT NOW()
);


-- --- SEÇÃO 4: INSERINDO DADOS DE EXEMPLO ---
-- Populando as tabelas para que possamos visualizar a estrutura em ação.

INSERT INTO usuario (nome, email, senha_hash, tipo_usuario, ultima_plataforma) VALUES
('Ana Silva', 'ana.silva@email.com', 'hash_seguro_123', 'premium', 'ios'),
('Bruno Costa', 'bruno.costa@email.com', 'hash_seguro_456', 'normal', 'android');

INSERT INTO produto (nome, descricao, preco, estoque) VALUES
('Leite Integral Longa Vida', 'Caixa com 1L de leite integral', 5.99, 200),
('Café Especial em Grãos', 'Pacote de 500g, torra média', 25.50, 80),
('Vinho Tinto Seco', 'Garrafa de 750ml, safra 2022', 75.90, 50),
('Queijo Gorgonzola', 'Pedaço de 200g, importado', 35.00, 40);

-- Ana (premium) comprou Café e Queijo
INSERT INTO historico_compra (id_usuario, id_produto, quantidade, preco_unitario) VALUES
(1, 2, 1, 25.50),
(1, 4, 1, 35.00);

-- Bruno (normal) comprou Leite
INSERT INTO historico_compra (id_usuario, id_produto, quantidade, preco_unitario) VALUES
(2, 1, 6, 5.99);

-- Gerando uma recomendação para a Ana com base em suas compras
INSERT INTO recomendacao_gerada (id_usuario, id_produto_recomendado, algoritmo_usado, score_confianca) VALUES
(1, 3, 'comprados_juntos', 0.85); -- Recomenda Vinho para quem compra Queijo.

-- --- SEÇÃO 5: CONSULTA EXEMPLO (Lógica do Serviço de Recomendação) ---
-- Esta consulta simula a lógica para encontrar produtos frequentemente
-- comprados por usuários 'premium'.

SELECT
    p.nome,
    p.preco,
    COUNT(hc.id_compra) AS total_de_compras_premium
FROM
    historico_compra hc
JOIN
    produto p ON hc.id_produto = p.id_produto
JOIN
    usuario u ON hc.id_usuario = u.id_usuario
WHERE
    u.tipo_usuario = 'premium'
GROUP BY
    p.nome, p.preco
ORDER BY
    total_de_compras_premium DESC;