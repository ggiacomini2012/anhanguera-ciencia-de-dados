-- aula-2.sql

/**
 * Normalização de Dados em SQL
 *
 * Este script demonstra o processo de normalização de um banco de dados
 * através da criação de tabelas e inserção de dados. O objetivo é transformar
 * um modelo desorganizado, com redundâncias e dependências incorretas, em um
 * modelo mais eficiente, seguindo as regras da 1ª, 2ª e 3ª Forma Normal.
 */

-- -----------------------------------------------------------------------------
-- Passo 0: Criação da Tabela Original (Não Normalizada)
-- Esta tabela representa o ponto de partida, com dados desorganizados.
-- -----------------------------------------------------------------------------
-- Excluindo a tabela se ela já existir para evitar erros
DROP TABLE IF EXISTS Funcionarios_Nao_Normalizados;

CREATE TABLE Funcionarios_Nao_Normalizados (
    matriculaFunc VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idCargo INT,
    descCargo VARCHAR(100),
    cidade_depto VARCHAR(100), -- Campo não atômico com cidade e departamento
    dataAdmissao DATE
);

-- Inserindo os dados na tabela não normalizada
INSERT INTO Funcionarios_Nao_Normalizados (matriculaFunc, nome, idCargo, descCargo, cidade_depto, dataAdmissao) VALUES
('148-9', 'Jane Anne', 191, 'Analista Contábil I', 'Curitiba, Contabilidade', '2018-01-15'),
('721-4', 'Klaus Lins', 323, 'Assistente de Produção II', 'São Paulo, Produção', '2017-11-21'),
('673-2', 'Sandra Costa', 101, 'Auxiliar de DP', 'Santo André, RH', '2018-04-03'),
('502-1', 'Octávio Neto', 254, 'Analista de TI III', 'Rio de Janeiro, Tecnologia da Informação', '2018-05-29');

-- Exibindo a tabela original
SELECT * FROM Funcionarios_Nao_Normalizados;

-- -----------------------------------------------------------------------------
-- Passo 1: Normalização para a Primeira Forma Normal (1FN)
-- Problema: O campo 'cidade_depto' não é atômico.
-- Solução: Criar tabelas separadas para Cidades e Departamentos.
-- -----------------------------------------------------------------------------

-- Criando a tabela de Cidades
DROP TABLE IF EXISTS Cidades;

CREATE TABLE Cidades (
    idCidade INT PRIMARY KEY AUTO_INCREMENT,
    nomeCidade VARCHAR(50) NOT NULL
);

-- Inserindo as cidades únicas
INSERT INTO Cidades (nomeCidade) VALUES
('Curitiba'),
('São Paulo'),
('Santo André'),
('Rio de Janeiro');

-- Exibindo a nova tabela de Cidades
SELECT * FROM Cidades;

-- -----------------------------------------------------------------------------
-- Passo 2 e 3: Normalização para a Segunda e Terceira Forma Normal (2FN e 3FN)
-- Problema: A tabela 'Funcionarios_Nao_Normalizados' tem dependências transitivas.
-- 'descCargo' depende de 'idCargo', não da chave primária 'matriculaFunc'.
-- 'cidade_depto' já foi tratado na 1FN, mas a dependência transitiva ainda existe
-- de forma conceitual.
-- Solução: Criar uma tabela separada para Cargos e outra para Departamentos.
-- -----------------------------------------------------------------------------

-- Criando a tabela de Cargos
DROP TABLE IF EXISTS Cargos;

CREATE TABLE Cargos (
    idCargo INT PRIMARY KEY,
    descCargo VARCHAR(100) NOT NULL
);

-- Inserindo os cargos únicos
INSERT INTO Cargos (idCargo, descCargo) VALUES
(191, 'Analista Contábil I'),
(323, 'Assistente de Produção II'),
(101, 'Auxiliar de DP'),
(254, 'Analista de TI III');

-- Exibindo a nova tabela de Cargos
SELECT * FROM Cargos;

-- -----------------------------------------------------------------------------
-- Passo Final: Criação da Tabela de Funcionários Normalizada
-- Esta tabela agora contém apenas chaves estrangeiras para Cidades e Cargos,
-- eliminando todas as redundâncias.
-- -----------------------------------------------------------------------------

-- Criando a tabela de Funcionários normalizada
DROP TABLE IF EXISTS Funcionarios;

CREATE TABLE Funcionarios (
    matriculaFunc VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    dataAdmissao DATE,
    idCargo INT,
    idCidade INT,
    
    FOREIGN KEY (idCargo) REFERENCES Cargos(idCargo),
    FOREIGN KEY (idCidade) REFERENCES Cidades(idCidade)
);

-- Inserindo os dados na tabela normalizada, usando as chaves estrangeiras
INSERT INTO Funcionarios (matriculaFunc, nome, dataAdmissao, idCargo, idCidade) VALUES
('148-9', 'Jane Anne', '2018-01-15', 191, 1), -- idCidade 1 para Curitiba
('721-4', 'Klaus Lins', '2017-11-21', 323, 2), -- idCidade 2 para São Paulo
('673-2', 'Sandra Costa', '2018-04-03', 101, 3), -- idCidade 3 para Santo André
('502-1', 'Octávio Neto', '2018-05-29', 254, 4); -- idCidade 4 para Rio de Janeiro

-- Exibindo a tabela final, normalizada
SELECT * FROM Funcionarios;

-- -----------------------------------------------------------------------------
-- Exemplo de consulta que une as tabelas normalizadas
-- Podemos obter todas as informações originais sem redundância.
-- -----------------------------------------------------------------------------

SELECT
    f.matriculaFunc,
    f.nome,
    c.descCargo AS cargo,
    ci.nomeCidade AS cidade,
    f.dataAdmissao
FROM
    Funcionarios f
JOIN
    Cargos c ON f.idCargo = c.idCargo
JOIN
    Cidades ci ON f.idCidade = ci.idCidade;