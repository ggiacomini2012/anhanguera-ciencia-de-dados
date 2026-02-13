# Tópico: Explorando os Relacionamentos em Bancos de Dados (Simulação em Python)

# 1. Simulação das Tabelas (Entidades)

class Funcionario:
    """Simula a tabela Funcionarios (Chave Primária: id)"""
    def __init__(self, id, nome, funcao):
        self.id = id  # PK: funcionarioID
        self.nome = nome
        self.funcao = funcao
    
    def __repr__(self):
        return f"Funcionario(ID={self.id}, Nome='{self.nome}')"

class Tarefa:
    """Simula a tabela Tarefas (Chave Primária: id)"""
    def __init__(self, id, descricao, status="Pendente"):
        self.id = id  # PK: tarefaID
        self.descricao = descricao
        self.status = status
    
    def __repr__(self):
        return f"Tarefa(ID={self.id}, Descrição='{self.descricao[:20]}...', Status='{self.status}')"

# 2. Simulação da Tabela Associativa (Relacionamento N:M)

class AtribuicaoTarefas:
    """
    Simula a tabela AtribuicaoTarefas, resolvendo o relacionamento N:M
    entre Funcionarios e Tarefas.
    Contém as Chaves Estrangeiras (FKs).
    """
    def __init__(self):
        # Lista para armazenar as atribuições (simulando as linhas da tabela)
        self.atribuicoes = []

    def atribuir(self, funcionario_id, tarefa_id):
        """Adiciona uma tupla (Funcionario FK, Tarefa FK) ao relacionamento."""
        # ❗ Lógica da Chave Estrangeira (FK): Verifica se as IDs existem ANTES de atribuir
        if any(f.id == funcionario_id for f in BD_FUNCIONARIOS) and \
           any(t.id == tarefa_id for t in BD_TAREFAS):
            
            nova_atribuicao = {'funcionarioID': funcionario_id, 'tarefaID': tarefa_id}
            
            # Evitar duplicatas no relacionamento
            if nova_atribuicao not in self.atribuicoes:
                self.atribuicoes.append(nova_atribuicao)
                print(f"✅ Tarefa {tarefa_id} atribuída ao Funcionário {funcionario_id}.")
            else:
                print("⚠️ Atribuição já existente.")
        else:
            print("❌ Erro de Integridade Referencial: Funcionario ou Tarefa ID não encontrado.")

    def listar_tarefas_do_funcionario(self, funcionario_id):
        """Consulta: Retorna todas as tarefas de um funcionário específico."""
        tarefas_ids = [a['tarefaID'] for a in self.atribuicoes if a['funcionarioID'] == funcionario_id]
        
        tarefas_encontradas = [t for t in BD_TAREFAS if t.id in tarefas_ids]
        
        return tarefas_encontradas

# 3. Simulação da Tabela de Dependências (Auto-relacionamento)

class DependenciasTarefas:
    """Simula a tabela DependenciasTarefas para o auto-relacionamento."""
    def __init__(self):
        self.dependencias = []

    def adicionar_dependencia(self, tarefa_dependente_id, tarefa_precedente_id):
        """Registra que a primeira tarefa depende da segunda."""
        # A validação de FKs seria similar, garantindo que ambas as IDs de Tarefas existam.
        self.dependencias.append({
            'tarefaID_dependente': tarefa_dependente_id,
            'tarefaID_dependencia': tarefa_precedente_id
        })
        print(f"🔗 Dependência registrada: Tarefa {tarefa_dependente_id} depende da Tarefa {tarefa_precedente_id}.")

# --- Dados de Exemplo ---

# 'Tabelas' primárias
BD_FUNCIONARIOS = [
    Funcionario(1, "Alice", "Desenvolvedora"),
    Funcionario(2, "Bruno", "Gerente de Projetos")
]

BD_TAREFAS = [
    Tarefa(101, "Definir escopo do projeto", "Concluída"),
    Tarefa(102, "Modelar banco de dados"),
    Tarefa(103, "Implementar frontend da tela de login")
]

# Inicializando as tabelas de relacionamento
relacionamento_atribuicao = AtribuicaoTarefas()
relacionamento_dependencia = DependenciasTarefas()

# --- Execução e Teste da Lógica de Relacionamento ---

print("\n--- Teste de Atribuição (N:M) ---")

# Atribuições VÁLIDAS (Relacionamento Funcionario 1:M Atribuicao)
relacionamento_atribuicao.atribuir(1, 102) # Alice fará a modelagem
relacionamento_atribuicao.atribuir(2, 101) # Bruno fez a definição do escopo
relacionamento_atribuicao.atribuir(1, 103) # Alice também fará o frontend

# ❗ Tentativa de quebrar a Integridade Referencial (FK)
print("\n--- Teste de Integridade Referencial (FK) ---")
relacionamento_atribuicao.atribuir(99, 102) # Funcionario 99 não existe
relacionamento_atribuicao.atribuir(1, 999) # Tarefa 999 não existe

# Consulta para verificar o relacionamento
print("\n--- Resultado da Consulta ---")
tarefas_alice = relacionamento_atribuicao.listar_tarefas_do_funcionario(1)
print(f"Tarefas de Alice (ID 1): {tarefas_alice}")

# --- Teste de Dependências (Auto-relacionamento) ---
print("\n--- Teste de Dependências (Auto-relacionamento) ---")
# Tarefa 103 (Implementar frontend) depende de Tarefa 102 (Modelar BD)
relacionamento_dependencia.adicionar_dependencia(103, 102) 

# Tarefa 102 (Modelar BD) depende de Tarefa 101 (Definir escopo)
relacionamento_dependencia.adicionar_dependencia(102, 101)

print("\nDependências registradas:")
print(relacionamento_dependencia.dependencias)