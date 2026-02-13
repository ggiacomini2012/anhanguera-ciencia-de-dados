-- Exemplo de Armazenamento com SQL: DDL, DML, DTL e Funções Agregadas.
-- Estes comandos são a base para qualquer banco de dados relacional (MySQL, PostgreSQL, SQL Server, SQL Azure, etc.).

--------------------------------------------------------------------------------
-- 1. DDL (Data Definition Language) - O Arquiteto constrói a estrutura
--------------------------------------------------------------------------------

-- Comando para remover a tabela se ela já existir, garantindo um teste limpo
-- (Útil em ambientes de desenvolvimento e scripts de migração)
DROP TABLE IF EXISTS Projetos_Nuvem;

-- Criação da tabela (Define o esquema e os tipos de dados)
CREATE TABLE Projetos_Nuvem (
    -- Analogia: ID é a Chave Primária, a "matrícula" única do projeto
    id INT PRIMARY KEY IDENTITY(1,1), 
    
    -- Tipo CHAR/VARCHAR: Nome do projeto (TEXT), não pode ser nulo (NOT NULL)
    nome_projeto VARCHAR(100) NOT NULL, 
    
    -- Plataforma da Nuvem (Azure, AWS, GCP)
    plataforma_nuvem VARCHAR(50) NOT NULL, 
    
    -- Modelo de Serviço (IaaS, PaaS, SaaS)
    modelo_servico VARCHAR(10), 
    
    -- Tipo REAL/FLOAT: Custo mensal (moeda)
    custo_mensal DECIMAL(10, 2)
);

-- DDL Adicional: Adicionando uma coluna para demonstrar ALTER TABLE
ALTER TABLE Projetos_Nuvem ADD data_implantacao DATE;

--------------------------------------------------------------------------------
-- 2. DML (Data Manipulation Language) - Os Pedreiros inserem e manipulam
--------------------------------------------------------------------------------

-- Comando INSERT: Inserindo registros (o dado em si)
INSERT INTO Projetos_Nuvem (nome_projeto, plataforma_nuvem, modelo_servico, custo_mensal, data_implantacao) VALUES
('Data Lake Enterprise', 'Azure', 'PaaS', 450.75, '2023-01-15'),
('Servidor Web Principal', 'AWS', 'IaaS', 120.00, '2023-03-20'),
('Sistema de CRM', 'Azure', 'SaaS', 89.90, '2023-05-10'),
('Banco de Dados Backup', 'GCP', 'PaaS', 210.50, '2023-07-01'),
('Máquina Virtual Dev', 'Azure', 'IaaS', 35.00, '2024-02-28');

-- Comando UPDATE: Atualizando um registro existente
-- Exemplo: O custo do Data Lake Enterprise foi renegociado.
UPDATE Projetos_Nuvem
SET custo_mensal = 400.00
WHERE nome_projeto = 'Data Lake Enterprise';

--------------------------------------------------------------------------------
-- 3. DML (SELECT) e Funções Agregadas - O Analista consulta e resume
--------------------------------------------------------------------------------

-- Consulta Simples: Recuperando todos os dados
SELECT * FROM Projetos_Nuvem;

-- Consulta com Predicado (WHERE): Filtrando por Projetos na Azure
-- (SELECT com WHERE é a base da manipulação de dados)
SELECT 
    nome_projeto, 
    modelo_servico, 
    custo_mensal
FROM 
    Projetos_Nuvem
WHERE 
    plataforma_nuvem = 'Azure';

-- Funções Agregadas: Resumindo os dados
-- (Essencial para tomada de decisão e relatórios)
SELECT
    COUNT(id) AS Total_Projetos,              -- Conta o número de linhas (COUNT)
    SUM(custo_mensal) AS Custo_Total_Mensal,  -- Soma de todos os custos (SUM)
    AVG(custo_mensal) AS Custo_Medio_Projeto,  -- Média do custo (AVG)
    MAX(custo_mensal) AS Custo_Maximo
FROM
    Projetos_Nuvem;

-- Agrupamento com Funções Agregadas (GROUP BY): Média por Modelo de Serviço
SELECT
    modelo_servico,
    AVG(custo_mensal) AS Custo_Medio
FROM
    Projetos_Nuvem
GROUP BY
    modelo_servico
ORDER BY
    Custo_Medio DESC;
    
--------------------------------------------------------------------------------
-- 4. DTL (Data Transaction Language) - O Notário garante a integridade
--------------------------------------------------------------------------------

-- Inicia uma transação (garante que as operações abaixo sejam tratadas como uma única unidade)
BEGIN TRANSACTION;

-- Tentativa de exclusão
DELETE FROM Projetos_Nuvem WHERE nome_projeto = 'Servidor Web Principal';

-- Se houvesse um erro ou mudança de ideia, usaríamos ROLLBACK:
-- ROLLBACK;

-- Para salvar a alteração permanentemente, usamos COMMIT:
COMMIT TRANSACTION;