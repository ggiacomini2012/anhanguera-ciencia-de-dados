## Arquivo: universidade.py

# A classe Pessoa é a superclasse (generalização)
class Pessoa:
    def __init__(self, nome, endereco, rg, cpf, data_nascimento, nome_mae, nome_pai):
        self.nome = nome
        self.endereco = endereco
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai

    def __str__(self):
        return (f"Nome: {self.nome}\nEndereço: {self.endereco}\n"
                f"RG: {self.rg}\nCPF: {self.cpf}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Nome da Mãe: {self.nome_mae}\n"
                f"Nome do Pai: {self.nome_pai}")

# A classe Funcionario herda de Pessoa (especialização)
class Funcionario(Pessoa):
    def __init__(self, nome, endereco, rg, cpf, data_nascimento, nome_mae, nome_pai, data_admissao, data_demissao, salario):
        super().__init__(nome, endereco, rg, cpf, data_nascimento, nome_mae, nome_pai)
        self.data_admissao = data_admissao
        self.data_demissao = data_demissao
        self.salario = salario
    
    def __str__(self):
        return (f"--- Dados do Funcionário ---\n"
                f"{super().__str__()}\n"
                f"Data de Admissão: {self.data_admissao}\n"
                f"Data de Demissão: {self.data_demissao}\n"
                f"Salário: R${self.salario:,.2f}")

# A classe Professor herda de Pessoa (especialização)
class Professor(Pessoa):
    def __init__(self, nome, endereco, rg, cpf, data_nascimento, nome_mae, nome_pai, valor_hora_aula, horas_aula):
        super().__init__(nome, endereco, rg, cpf, data_nascimento, nome_mae, nome_pai)
        self.valor_hora_aula = valor_hora_aula
        self.horas_aula = horas_aula

    def __str__(self):
        return (f"--- Dados do Professor ---\n"
                f"{super().__str__()}\n"
                f"Valor da Hora/Aula: R${self.valor_hora_aula:,.2f}\n"
                f"Quantidade de Horas/Aula: {self.horas_aula}")

# A classe Aluno herda de Pessoa (especialização)
class Aluno(Pessoa):
    def __init__(self, nome, endereco, rg, cpf, data_nascimento, nome_mae, nome_pai, data_entrada, data_formatura):
        super().__init__(nome, endereco, rg, cpf, data_nascimento, nome_mae, nome_pai)
        self.data_entrada = data_entrada
        self.data_formatura = data_formatura
    
    def __str__(self):
        return (f"--- Dados do Aluno ---\n"
                f"{super().__str__()}\n"
                f"Data de Entrada na Faculdade: {self.data_entrada}\n"
                f"Data de Formatura: {self.data_formatura}")

# --- Criando e exibindo objetos para exemplificar ---

# Criando um objeto da classe Professor
prof_exemplo = Professor(
    nome="Carlos Martins",
    endereco="Rua das Rosas, 123",
    rg="12.345.678-9",
    cpf="123.456.789-00",
    data_nascimento="10/05/1980",
    nome_mae="Maria Silva",
    nome_pai="José Martins",
    valor_hora_aula=75.00,
    horas_aula=20
)

# Criando um objeto da classe Aluno
aluno_exemplo = Aluno(
    nome="Ana Souza",
    endereco="Avenida Brasil, 456",
    rg="98.765.432-1",
    cpf="987.654.321-00",
    data_nascimento="25/11/2000",
    nome_mae="Paula Lima",
    nome_pai="João Souza",
    data_entrada="03/02/2020",
    data_formatura="15/12/2024"
)

# Exibindo os dados
print(prof_exemplo)
print("\n" + "="*30 + "\n")
print(aluno_exemplo)