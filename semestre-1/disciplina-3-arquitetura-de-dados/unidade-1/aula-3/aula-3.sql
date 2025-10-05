-- =================================================================
-- SIMULAÇÃO SQL: ARQUITETURA DE DADOS (TRANSAÇÃO NO VAREJO)
-- O foco é a integridade ACID (Atomicidade, Consistência, Isolamento)
-- garantida pelo SGBD (o Servidor), independente da arquitetura.
-- =================================================================

-- 1. CRIAÇÃO DA ESTRUTURA (O ESQUEMA CENTRAL NA NUVEM)
-- A tabela INVENTARIO é o dado que precisa ser sincronizado em tempo real.

CREATE TABLE INVENTARIO (
    sku VARCHAR(10) PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    estoque_global INT NOT NULL CHECK (estoque_global >= 0) -- Garante Consistência (estoque >= 0)
);

CREATE TABLE LOG_TRANSACOES (
    id_transacao INT IDENTITY(1,1) PRIMARY KEY,
    sku_vendido VARCHAR(10) REFERENCES INVENTARIO(sku),
    quantidade INT NOT NULL,
    local_venda VARCHAR(50) NOT NULL, -- Simula o nó (cliente) que realizou a operação
    data_hora DATETIME DEFAULT GETDATE(),
    status_transacao VARCHAR(10) -- 'SUCESSO' ou 'FALHA'
);

-- 2. POPULANDO O INVENTÁRIO (DADOS INICIAIS NO SERVIDOR)
INSERT INTO INVENTARIO (sku, nome_produto, estoque_global) VALUES
('SKU-100', 'Camiseta Básica', 500),
('SKU-201', 'Calça Jeans Premium', 250);

-- 3. CONSULTA AO INVENTÁRIO (Ação do Cliente/Nó Distribuído)
-- O Cliente (Loja ou E-commerce) solicita o estoque atual.
SELECT 
    sku, 
    nome_produto, 
    estoque_global 
FROM INVENTARIO 
WHERE sku = 'SKU-100';

-- =================================================================
-- 4. TRANSAÇÃO DE VENDA (Garantindo Atomicidade e Isolamento)
-- Loja-SP faz uma venda de 200 unidades (Deve passar)
-- =================================================================

-- O BEGIN TRANSACTION é crucial para a Atomicidade: todas as etapas devem ocorrer ou nenhuma.
-- O SGBD garante que, durante esta transação, o dado esteja Isolado de outras leituras/escritas.

BEGIN TRANSACTION VendaLojaSP
    DECLARE @sku_sp VARCHAR(10) = 'SKU-100';
    DECLARE @quantidade_sp INT = 200;
    DECLARE @estoque_atual_sp INT;

    -- 1. Verifica o estoque atual (Isolamento)
    SELECT @estoque_atual_sp = estoque_global FROM INVENTARIO WHERE sku = @sku_sp;

    IF @estoque_atual_sp >= @quantidade_sp
    BEGIN
        -- 2. Atualiza o estoque (Ação Principal)
        UPDATE INVENTARIO 
        SET estoque_global = estoque_global - @quantidade_sp
        WHERE sku = @sku_sp;

        -- 3. Loga o sucesso
        INSERT INTO LOG_TRANSACOES (sku_vendido, quantidade, local_venda, status_transacao)
        VALUES (@sku_sp, @quantidade_sp, 'Loja-SP', 'SUCESSO');
        
        -- 4. Confirma todas as etapas (Atomicidade: TUDO ou NADA)
        COMMIT TRANSACTION VendaLojaSP;
        SELECT '✅ Transação Loja-SP: SUCESSO! Estoque atualizado globalmente.' AS Resultado;
    END
    ELSE
    BEGIN
        -- 4. Desfaz todas as etapas se falhar
        ROLLBACK TRANSACTION VendaLojaSP;
        INSERT INTO LOG_TRANSACOES (sku_vendido, quantidade, local_venda, status_transacao)
        VALUES (@sku_sp, @quantidade_sp, 'Loja-SP', 'FALHA');
        SELECT '⛔ Transação Loja-SP: FALHA! Estoque insuficiente.' AS Resultado;
    END
GO

-- =================================================================
-- 5. SEGUNDA TRANSAÇÃO (Teste de Consistência e Atomicidade)
-- E-commerce tenta uma venda grande (251 unidades) (Deve falhar, 500 - 200 = 300 restantes)
-- =================================================================

BEGIN TRANSACTION VendaEcommerce
    DECLARE @sku_ecomm VARCHAR(10) = 'SKU-100';
    DECLARE @quantidade_ecomm INT = 251;
    DECLARE @estoque_atual_ecomm INT;

    -- 1. Verifica o estoque atual (Sincronizado)
    SELECT @estoque_atual_ecomm = estoque_global FROM INVENTARIO WHERE sku = @sku_ecomm;

    IF @estoque_atual_ecomm >= @quantidade_ecomm
    BEGIN
        -- Atualiza, loga e Comita
        UPDATE INVENTARIO SET estoque_global = estoque_global - @quantidade_ecomm WHERE sku = @sku_ecomm;
        INSERT INTO LOG_TRANSACOES (sku_vendido, quantidade, local_venda, status_transacao)
        VALUES (@sku_ecomm, @quantidade_ecomm, 'E-commerce', 'SUCESSO');
        COMMIT TRANSACTION VendaEcommerce;
        SELECT '✅ Transação E-commerce: SUCESSO! Estoque atualizado globalmente.' AS Resultado;
    END
    ELSE
    BEGIN
        -- 4. Desfaz todas as etapas se falhar (ROLLBACK)
        ROLLBACK TRANSACTION VendaEcommerce;
        INSERT INTO LOG_TRANSACOES (sku_vendido, quantidade, local_venda, status_transacao)
        VALUES (@sku_ecomm, @quantidade_ecomm, 'E-commerce', 'FALHA');
        SELECT '⛔ Transação E-commerce: FALHA! Estoque insuficiente.' AS Resultado;
    END
GO

-- 6. VERIFICAÇÃO FINAL
SELECT '--- Estoque Final Global ---' AS Status;
SELECT 
    sku, 
    estoque_global 
FROM INVENTARIO 
WHERE sku = 'SKU-100'; -- Deve mostrar 300 - 0 = 300 (A segunda transação falhou e fez rollback)

SELECT '--- Log de Transações ---' AS Status;
SELECT * FROM LOG_TRANSACOES;