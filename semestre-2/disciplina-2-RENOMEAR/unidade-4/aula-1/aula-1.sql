-- aula-1.sql

-- =======================================================================
-- SCRIPT SQL PARA EXEMPLIFICAR A NORMALIZAÇÃO DE UM BANCO DE DADOS
-- =======================================================================
-- Este script demonstra o resultado final do processo de normalização
-- de um formulário de registro de jogos de futebol. A única tabela
-- original, com redundâncias e dependências, foi decomposta em
-- tabelas menores, mais eficientes e organizadas, seguindo as Formas Normais (FN).

-- Passo 1: Criação da tabela LOCALIZACOES (Resultado da 3ª Forma Normal)
-- Esta tabela foi criada para remover a dependência transitiva, onde
-- a 'CidadeLocal' dependia de 'LocalJogo'. Agora, cada local tem uma
-- única cidade associada, eliminando a repetição de dados.
-- Chave Primária: LocalJogo
CREATE TABLE LOCALIZACOES (
    LocalJogo VARCHAR(255) PRIMARY KEY,
    CidadeLocal VARCHAR(255) NOT NULL
);

-- Inserção de dados na tabela LOCALIZACOES
INSERT INTO LOCALIZACOES (LocalJogo, CidadeLocal) VALUES
('Estádio Municipal', 'Santa Catarina'),
('Arena Olímpica', 'Rio de Janeiro'),
('Estádio do Morumbi', 'São Paulo');


-- Passo 2: Criação da tabela JOGOS (Resultado da 3ª Forma Normal)
-- Esta tabela foi separada da original para eliminar as dependências parciais
-- e transitivas. Ela armazena informações únicas sobre cada jogo.
-- A coluna 'LocalJogo' agora é uma Chave Estrangeira, que referencia a
-- tabela LOCALIZACOES, garantindo a integridade dos dados.
-- Chave Primária: NumeroJogo
-- Chave Estrangeira: LocalJogo -> LOCALIZACOES
CREATE TABLE JOGOS (
    NumeroJogo INT PRIMARY KEY,
    DataPartida DATE NOT NULL,
    LocalJogo VARCHAR(255),
    NomeOponente VARCHAR(255),
    FOREIGN KEY (LocalJogo) REFERENCES LOCALIZACOES(LocalJogo)
);

-- Inserção de dados na tabela JOGOS
INSERT INTO JOGOS (NumeroJogo, DataPartida, LocalJogo, NomeOponente) VALUES
(101, '2023-10-25', 'Estádio Municipal', 'Time A'),
(102, '2023-11-02', 'Arena Olímpica', 'Time B'),
(103, '2023-11-10', 'Estádio Municipal', 'Time C'),
(104, '2023-11-18', 'Estádio do Morumbi', 'Time D'),
(105, '2023-11-25', 'Arena Olímpica', 'Time E');


-- Passo 3: Criação da tabela JOGADORES (Resultado da 2ª Forma Normal)
-- Esta tabela foi criada para remover a dependência parcial, onde
-- o nome e a posição do jogador dependiam apenas de seu código, e não
-- da chave primária composta da tabela original.
-- Chave Primária: CodigoJogador
CREATE TABLE JOGADORES (
    CodigoJogador VARCHAR(50) PRIMARY KEY,
    NomeJogador VARCHAR(255) NOT NULL,
    PosicaoJogador VARCHAR(100)
);

-- Inserção de dados na tabela JOGADORES
INSERT INTO JOGADORES (CodigoJogador, NomeJogador, PosicaoJogador) VALUES
('J001', 'João Silva', 'Atacante'),
('J002', 'Maria Santos', 'Meio-campo'),
('J003', 'Pedro Rocha', 'Defensor');


-- Passo 4: Criação da tabela ATUACOES (Resultado da 2ª Forma Normal)
-- Esta é a tabela de ligação (ou de relacionamento), que mantém a chave
-- primária composta da tabela original, mas agora apenas com as chaves
-- estrangeiras e os atributos que dependem funcionalmente da chave inteira.
-- Chave Primária: (NumeroJogo, CodigoJogador)
-- Chaves Estrangeiras:
--  - NumeroJogo -> JOGOS
--  - CodigoJogador -> JOGADORES
CREATE TABLE ATUACOES (
    NumeroJogo INT,
    CodigoJogador VARCHAR(50),
    GolsMarcados INT,
    PRIMARY KEY (NumeroJogo, CodigoJogador),
    FOREIGN KEY (NumeroJogo) REFERENCES JOGOS(NumeroJogo),
    FOREIGN KEY (CodigoJogador) REFERENCES JOGADORES(CodigoJogador)
);

-- Inserção de dados na tabela ATUACOES
INSERT INTO ATUACOES (NumeroJogo, CodigoJogador, GolsMarcados) VALUES
(101, 'J001', 2),
(102, 'J002', 1),
(103, 'J001', 0),
(104, 'J003', 3),
(105, 'J002', 1);

-- =======================================================================
-- Consultas de Verificação
-- =======================================================================
-- Seleciona todos os jogadores e suas posições
SELECT * FROM JOGADORES;

-- Seleciona todos os jogos e os locais (agora com um join)
SELECT J.NumeroJogo, J.DataPartida, L.LocalJogo, L.CidadeLocal, J.NomeOponente
FROM JOGOS J
JOIN LOCALIZACOES L ON J.LocalJogo = L.LocalJogo;

-- Seleciona todos os gols marcados por jogadores em cada jogo
SELECT J.NumeroJogo, J.DataPartida, JD.NomeJogador, A.GolsMarcados
FROM ATUACOES A
JOIN JOGOS J ON A.NumeroJogo = J.NumeroJogo
JOIN JOGADORES JD ON A.CodigoJogador = JD.CodigoJogador;