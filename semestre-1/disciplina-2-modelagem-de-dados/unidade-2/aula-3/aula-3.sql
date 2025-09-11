-- Exemplo de Especialização/Generalização
-- Tabela 'Funcionario' (Superclasse)
-- Esta tabela armazena os dados comuns a todos os tipos de funcionários.
CREATE TABLE Funcionario (
    id_funcionario INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL
);

-- Tabela 'Gerente' (Subclasse)
-- Esta tabela armazena os dados específicos de gerentes e se relaciona com a tabela 'Funcionario'
-- A chave primária é também uma chave estrangeira, indicando a relação de herança.
CREATE TABLE Gerente (
    id_gerente INT PRIMARY KEY,
    departamento VARCHAR(50),
    FOREIGN KEY (id_gerente) REFERENCES Funcionario(id_funcionario)
);

-- Tabela 'Engenheiro' (Subclasse)
CREATE TABLE Engenheiro (
    id_engenheiro INT PRIMARY KEY,
    especializacao VARCHAR(50),
    FOREIGN KEY (id_engenheiro) REFERENCES Funcionario(id_funcionario)
);

-- Tabela 'Tecnico' (Subclasse)
CREATE TABLE Tecnico (
    id_tecnico INT PRIMARY KEY,
    area_atuacao VARCHAR(50),
    FOREIGN KEY (id_tecnico) REFERENCES Funcionario(id_funcionario)
);


-- Exemplo de Cardinalidade e Entidade Associativa
-- Relacionamento N:N (Muitos para Muitos) entre Medico e Paciente
-- Uma entidade associativa (tabela de junção) é necessária para resolver este relacionamento.

-- Tabela 'Medico'
CREATE TABLE Medico (
    crm VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela 'Paciente'
-- Relacionamento N:1 com Tipo_Sanguineo (um paciente tem um tipo, um tipo pode ter N pacientes)
CREATE TABLE Paciente (
    cpf VARCHAR(15) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_tipo_sanguineo INT,
    FOREIGN KEY (id_tipo_sanguineo) REFERENCES Tipo_Sanguineo(id_tipo_sanguineo)
);

-- Tabela 'Tipo_Sanguineo'
CREATE TABLE Tipo_Sanguineo (
    id_tipo_sanguineo INT PRIMARY KEY,
    tipo VARCHAR(5) NOT NULL UNIQUE
);

-- Tabela 'Atendimento' (Entidade Associativa)
-- Esta tabela resolve o relacionamento N:N entre Medico e Paciente.
-- Cada linha representa um evento de atendimento e tem suas próprias chaves estrangeiras.
CREATE TABLE Atendimento (
    id_atendimento INT PRIMARY KEY AUTO_INCREMENT,
    crm_medico VARCHAR(20),
    cpf_paciente VARCHAR(15),
    data_atendimento DATE,
    diagnostico TEXT,
    FOREIGN KEY (crm_medico) REFERENCES Medico(crm),
    FOREIGN KEY (cpf_paciente) REFERENCES Paciente(cpf)
);