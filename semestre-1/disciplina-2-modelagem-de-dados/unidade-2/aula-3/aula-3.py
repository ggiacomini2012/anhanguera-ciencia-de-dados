# A superclasse 'Funcionario' representa a generalização de todos os tipos de funcionários
class Funcionario:
    def __init__(self, id, nome, salario):
        self.id = id
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Salário: R${self.salario:.2f}"

# A subclasse 'Gerente' é uma especialização de 'Funcionario'
# Ela herda os atributos de Funcionario e adiciona o seu próprio 'departamento'.
class Gerente(Funcionario):
    def __init__(self, id, nome, salario, departamento):
        super().__init__(id, nome, salario)
        self.departamento = departamento

    def __str__(self):
        return super().__str__() + f", Departamento: {self.departamento}"

# A subclasse 'Engenheiro' é outra especialização de 'Funcionario'
# Ela herda os atributos de Funcionario e adiciona o seu próprio 'especializacao'.
class Engenheiro(Funcionario):
    def __init__(self, id, nome, salario, especializacao):
        super().__init__(id, nome, salario)
        self.especializacao = especializacao

    def __str__(self):
        return super().__str__() + f", Especialização: {self.especializacao}"

# A subclasse 'Tecnico' é mais uma especialização de 'Funcionario'
# Ela herda os atributos de Funcionario e adiciona o seu próprio 'area_atuacao'.
class Tecnico(Funcionario):
    def __init__(self, id, nome, salario, area_atuacao):
        super().__init__(id, nome, salario)
        self.area_atuacao = area_atuacao

    def __str__(self):
        return super().__str__() + f", Área de Atuação: {self.area_atuacao}"

# Criando instâncias (objetos) de cada tipo de funcionário
gerente1 = Gerente(101, "Ana Silva", 8500.00, "Vendas")
engenheiro1 = Engenheiro(201, "Carlos Mendes", 7200.00, "Software")
tecnico1 = Tecnico(301, "Beatriz Costa", 4500.00, "Manutenção")

# Imprimindo os dados de cada funcionário
print("--- Exemplos de Especialização/Generalização ---")
print(gerente1)
print(engenheiro1)
print(tecnico1)

# Exemplo de Relacionamento (Entidades Associativas) e Cardinalidade
# Vamos criar um relacionamento "Atende" entre 'Medico' e 'Paciente'
class Medico:
    def __init__(self, crm, nome):
        self.crm = crm
        self.nome = nome
        self.pacientes_atendidos = []

    def __str__(self):
        return f"Médico: {self.nome} (CRM: {self.crm})"

class Paciente:
    def __init__(self, cpf, nome, tipo_sanguineo):
        self.cpf = cpf
        self.nome = nome
        self.tipo_sanguineo = tipo_sanguineo

    def __str__(self):
        return f"Paciente: {self.nome} (CPF: {self.cpf}, Tipo Sanguíneo: {self.tipo_sanguineo})"

# Entidade Associativa: 'Atendimento'
# Representa um relacionamento 'muitos para muitos' (N:N)
class Atendimento:
    def __init__(self, medico, paciente, data, diagnostico):
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.diagnostico = diagnostico

    def __str__(self):
        return (f"Atendimento em {self.data}: "
                f"Médico: {self.medico.nome} atendeu Paciente: {self.paciente.nome}. "
                f"Diagnóstico: {self.diagnostico}")

print("\n--- Exemplo de Relacionamento N:N e Entidade Associativa ---")
medico_joao = Medico("CRM-123", "Dr. João")
paciente_maria = Paciente("CPF-456", "Maria", "A+")
paciente_pedro = Paciente("CPF-789", "Pedro", "O-")

# Um médico pode atender muitos pacientes (1:N)
atendimento1 = Atendimento(medico_joao, paciente_maria, "2025-09-10", "Gripe")
atendimento2 = Atendimento(medico_joao, paciente_pedro, "2025-09-11", "Dor de cabeça")

# Um paciente pode ser atendido por muitos médicos (N:1, se considerarmos um atendimento por vez)
# Ou por muitos médicos em diferentes atendimentos (N:N)
# O relacionamento 'Atendimento' surge para conectar ambos
print(atendimento1)
print(atendimento2)