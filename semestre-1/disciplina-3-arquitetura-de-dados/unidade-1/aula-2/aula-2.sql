-- aula-2.sql
-- Exemplificando as Linguagens de Arquitetura de Dados (DDL/DML)
-- Foco na Camada Conceitual (Tabelas) e Camada Externa (Views)

-- =========================================================================
-- 1. LINGUAGEM DE DEFINIÇÃO DE DADOS (DDL)
-- Criação da Estrutura (Camada Conceitual e Interna)
-- =========================================================================

-- Criação da Tabela principal de Funcionários (Conceito Lógico do Negócio)
CREATE TABLE Funcionarios (
    id_func INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    salario DECIMAL(10, 2) -- Dado sensível
);

-- Criação da Tabela de Projetos (Exemplo de outra entidade)
CREATE TABLE Projetos (
    id_projeto INT PRIMARY KEY,
    nome_projeto VARCHAR(100) NOT NULL,
    orcamento DECIMAL(15, 2)
);


-- =========================================================================
-- 2. LINGUAGEM DE MANIPULAÇÃO DE DADOS (DML)
-- Inserção de Dados (Camada Conceitual)
-- =========================================================================

-- Inserindo dados na tabela Funcionarios
INSERT INTO Funcionarios (id_func, nome, departamento, salario) VALUES
(10, 'Aline Silva', 'RH', 6200.00),
(20, 'Bruno Costa', 'Financeiro', 7500.00),
(30, 'Carla Mendes', 'Vendas', 4800.00),
(40, 'David Rocha', 'Vendas', 5100.00),
(50, 'Erica Luz', 'Financeiro', 7000.00);


-- =========================================================================
-- 3. CAMADA EXTERNA (VIEWS) - A SOLUÇÃO DA ARQUITETURA ANSI/SPARC
-- Resolvendo o problema de personalização e segurança
-- =========================================================================

-- PROBLEMA DA EMPRESA: Dificuldade na personalização de dados por departamento.
-- SOLUÇÃO: Criar Views específicas (Camada Externa) para cada grupo de usuários.

-- 3.1. VIEW para o Departamento FINANCEIRO
-- O Financeiro precisa de informações sensíveis (Nome, Salário)
CREATE VIEW View_Dados_Financeiro AS
SELECT
    f.nome,
    f.departamento,
    f.salario
FROM
    Funcionarios f
WHERE
    f.departamento = 'Financeiro';

-- Teste da View Financeiro: Acesso personalizado
SELECT * FROM View_Dados_Financeiro;


-- 3.2. VIEW para o Departamento de VENDAS (Operacional)
-- O Vendas NÃO deve ver o salário, apenas dados operacionais (Nome, ID)
CREATE VIEW View_Dados_Vendas_Operacional AS
SELECT
    f.id_func,
    f.nome,
    f.departamento
FROM
    Funcionarios f
WHERE
    f.departamento = 'Vendas';

-- Teste da View Vendas: Acesso personalizado (Salário é omitido)
SELECT * FROM View_Dados_Vendas_Operacional;


-- 3.3. VIEW para o Departamento de RH
-- O RH precisa de uma visão geral de todos, incluindo salário
CREATE VIEW View_Dados_RH_Geral AS
SELECT
    f.id_func,
    f.nome,
    f.departamento,
    f.salario
FROM
    Funcionarios f;

-- Teste da View RH: Acesso a todos os dados
SELECT * FROM View_Dados_RH_Geral;


-- =========================================================================
-- 4. CONCLUSÃO DA SOLUÇÃO
-- =========================================================================

-- A VIEW é uma tabela virtual da Camada Externa.
-- Ela permite que diferentes usuários (ou aplicações) acessem o mesmo 
-- conjunto de dados brutos (Camada Interna/Conceitual) de forma personalizada
-- (apenas as colunas e linhas que lhes são relevantes),
-- resolvendo o problema de ineficiência operacional por falta de personalização.

-- Limpeza (DDL):
DROP VIEW View_Dados_Financeiro;
DROP VIEW View_Dados_Vendas_Operacional;
DROP VIEW View_Dados_RH_Geral;
DROP TABLE Funcionarios;
DROP TABLE Projetos;