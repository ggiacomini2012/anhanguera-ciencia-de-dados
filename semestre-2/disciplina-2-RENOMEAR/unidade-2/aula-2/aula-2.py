# Este script Python simula a modelagem de entidades e relacionamentos
# conforme a aula sobre MER. Ele utiliza uma abordagem orientada a objetos
# para representar as entidades e seus atributos.

class Entidade:
    """
    Representa uma entidade no modelo Entidade-Relacionamento.
    Uma entidade é algo que existe física ou virtualmente.
    """
    def __init__(self, nome, atributos=None):
        self.nome = nome
        self.atributos = atributos if atributos is not None else []
        self.instancias = []

    def adicionar_atributo(self, atributo):
        """Adiciona um atributo à entidade."""
        self.atributos.append(atributo)

    def adicionar_instancia(self, instancia):
        """Adiciona uma instância (registro) à entidade."""
        self.instancias.append(instancia)

    def __str__(self):
        return f"Entidade: {self.nome}\nAtributos: {', '.join(self.atributos)}"

class Relacionamento:
    """
    Representa um relacionamento entre duas entidades.
    """
    def __init__(self, nome, entidade1, entidade2):
        self.nome = nome
        self.entidade1 = entidade1
        self.entidade2 = entidade2
        self.instancias = []

    def adicionar_associacao(self, instancia1, instancia2):
        """Adiciona uma associação entre instâncias de entidades."""
        self.instancias.append((instancia1, instancia2))

    def __str__(self):
        return f"Relacionamento: {self.nome} entre {self.entidade1.nome} e {self.entidade2.nome}"

def simular_aula_mer():
    """
    Função principal que simula a aula de MER.
    """
    print("--- Simulação da Aula sobre MER ---")

    # Criando as entidades
    aluno = Entidade("Aluno", ["ID_Aluno", "Nome", "DataNascimento", "Email"])
    disciplina = Entidade("Disciplina", ["ID_Disciplina", "NomeDisciplina", "CargaHoraria"])
    instrutor = Entidade("Instrutor", ["ID_Instrutor", "Nome", "Salario"])
    dependente = Entidade("Dependente", ["ID_Dependente", "Nome"])
    
    # Adicionando atributos para o instrutor e dependente
    instrutor.adicionar_atributo("ID_Instrutor")
    instrutor.adicionar_atributo("Nome")
    dependente.adicionar_atributo("ID_Dependente")
    dependente.adicionar_atributo("Nome")

    print("\n--- Entidades Criadas ---")
    print(aluno)
    print(disciplina)
    print(instrutor)
    print(dependente)

    # Exemplo de instância da entidade Aluno
    aluno1 = {"ID_Aluno": 12345, "Nome": "Shankar", "DataNascimento": "10/05/2000", "Email": "shankar@email.com"}
    aluno.adicionar_instancia(aluno1)

    print("\n--- Instância da Entidade Aluno ---")
    print(aluno.instancias[0])

    # Criando relacionamentos
    matricula = Relacionamento("Matricula", aluno, disciplina)
    mentor = Relacionamento("Mentor", instrutor, aluno)

    print("\n--- Relacionamentos Criados ---")
    print(matricula)
    print(mentor)

    # Exemplo de instância do relacionamento Mentor
    instrutor_katz = {"ID_Instrutor": 45565, "Nome": "Katz", "Salario": 8000.00}
    mentor.adicionar_associacao(instrutor_katz, aluno1)

    print("\n--- Instância do Relacionamento Mentor ---")
    print(f"{mentor.instancias[0][0]['Nome']} é mentor de {mentor.instancias[0][1]['Nome']}")
    
    # Exemplo de atributo em relacionamento (como "nota")
    class Realiza(Relacionamento):
        def __init__(self, entidade1, entidade2):
            super().__init__("Realiza", entidade1, entidade2)
            self.atributos_descritivos = ["Nota", "Credito"]

        def adicionar_associacao(self, instancia1, instancia2, **atributos_descritivos):
            self.instancias.append((instancia1, instancia2, atributos_descritivos))

    realiza = Realiza(aluno, disciplina)
    
    disciplina_bd = {"ID_Disciplina": 101, "NomeDisciplina": "Banco de Dados", "CargaHoraria": 60}
    aluno_shankar_nota_bd = {"Nota": 9.5, "Credito": "Sim"}
    realiza.adicionar_associacao(aluno1, disciplina_bd, **aluno_shankar_nota_bd)
    
    print("\n--- Atributo em Relacionamento (Realiza) ---")
    associacao = realiza.instancias[0]
    print(f"O aluno {associacao[0]['Nome']} realizou a disciplina {associacao[1]['NomeDisciplina']} com nota {associacao[2]['Nota']}.")

# Executa a simulação
if __name__ == "__main__":
    simular_aula_mer()
