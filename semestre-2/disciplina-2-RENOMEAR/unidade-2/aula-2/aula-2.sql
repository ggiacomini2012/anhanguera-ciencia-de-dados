-- Este script SQL exemplifica a criação de tabelas e a inserção de dados
-- baseados nos conceitos da aula sobre modelagem Entidade-Relacionamento.

-- Criação da Entidade Forte (Aluno)
-- Uma entidade forte existe independentemente de outras.
CREATE TABLE Aluno (
    id_aluno INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    email VARCHAR(100) UNIQUE
);

-- Criação da Entidade Forte (Disciplina)
-- Representa a entidade que pode ser cursada por vários alunos.
CREATE TABLE Disciplina (
    id_disciplina INT PRIMARY KEY,
    nome_disciplina VARCHAR(100) NOT NULL,
    carga_horaria INT
);

-- Criação da Entidade Forte (Instrutor)
-- Representa a entidade que pode ser mentora de um aluno.
CREATE TABLE Instrutor (
    id_instrutor INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2)
);

-- Criação da Entidade Fraca (Dependente)
-- Uma entidade fraca depende da existência de outra (neste caso, Instrutor).
-- A chave primária é composta por seu próprio ID e a chave estrangeira.
CREATE TABLE Dependente (
    id_dependente INT,
    nome VARCHAR(100) NOT NULL,
    id_instrutor INT,
    PRIMARY KEY (id_dependente, id_instrutor),
    FOREIGN KEY (id_instrutor) REFERENCES Instrutor(id_instrutor)
);

-- Criação da Entidade Associativa (Matricula)
-- Uma entidade associativa que representa o relacionamento entre Aluno e Disciplina.
-- Ela pode ter atributos próprios, como 'nota' e 'credito'.
CREATE TABLE Matricula (
    id_aluno INT,
    id_disciplina INT,
    data_matricula DATE,
    nota DECIMAL(4, 2),
    credito VARCHAR(10),
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id_disciplina)
);

-- Criação da Entidade Associativa (Mentor)
-- Representa o relacionamento entre Instrutor e Aluno.
CREATE TABLE Mentor (
    id_instrutor INT,
    id_aluno INT,
    data_inicio DATE,
    PRIMARY KEY (id_instrutor, id_aluno),
    FOREIGN KEY (id_instrutor) REFERENCES Instrutor(id_instrutor),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

-- Inserção de dados nas tabelas (instâncias)
INSERT INTO Aluno (id_aluno, nome, data_nascimento, email)
VALUES (12345, 'Shankar', '2000-05-10', 'shankar@email.com');

INSERT INTO Disciplina (id_disciplina, nome_disciplina, carga_horaria)
VALUES (101, 'Banco de Dados', 60);

INSERT INTO Instrutor (id_instrutor, nome, salario)
VALUES (45565, 'Katz', 8000.00);

-- Inserção de um relacionamento de mentoria
INSERT INTO Mentor (id_instrutor, id_aluno, data_inicio)
VALUES (45565, 12345, '2024-09-09');

-- Inserção de um relacionamento com atributos
INSERT INTO Matricula (id_aluno, id_disciplina, data_matricula, nota, credito)
VALUES (12345, 101, '2024-09-01', 9.5, 'Sim');
