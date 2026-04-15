# aula-1.py
# Simulação de Estrutura de Banco de Dados MySQL em Python
# Tópico: Introdução ao MySQL: Conceitos, Tipos de Atributos e Cardinalidade

from datetime import date

# 1. Simulação dos Tipos de Atributos (DataType Validation)
# Funções simples para simular a verificação de tipos antes da inserção
def validar_int(valor, nome_campo):
    """Simula validação para tipos INT/BIGINT."""
    if not isinstance(valor, int):
        raise TypeError(f"Erro de Tipo: O campo '{nome_campo}' deve ser um número inteiro (INT).")
    return valor

def validar_varchar(valor, nome_campo, max_len):
    """Simula validação para tipo VARCHAR."""
    if not isinstance(valor, str):
        raise TypeError(f"Erro de Tipo: O campo '{nome_campo}' deve ser uma string (VARCHAR).")
    if len(valor) > max_len:
        raise ValueError(f"Erro de Tamanho: O campo '{nome_campo}' excedeu o limite de {max_len} caracteres.")
    return valor

def validar_date(valor, nome_campo):
    """Simula validação para tipo DATE."""
    if not isinstance(valor, date):
        raise TypeError(f"Erro de Tipo: O campo '{nome_campo}' deve ser um objeto date (DATE).")
    return valor

# 2. Simulação das Tabelas (Estrutura e Chaves)

# Armazenamento simples: listas de dicionários
TabelaFuncionario = []
TabelaProjeto = []
TabelaProjetoFuncionario = []

# Função para garantir a Chave Primária (PK)
def verificar_pk(tabela, pk_id, pk_nome):
    """Garante a unicidade da Chave Primária."""
    if any(registro[pk_nome] == pk_id for registro in tabela):
        raise ValueError(f"Erro de Chave Primária: O ID {pk_id} já existe na tabela.")

# --- Tabela Funcionario (Entidade Principal) ---
# Atributos: idFuncionario (INT, PK), nome (VARCHAR), cargo (VARCHAR), dataContratacao (DATE)
def inserir_funcionario(idF, nome, cargo, dataContratacao):
    try:
        verificar_pk(TabelaFuncionario, idF, 'idFuncionario')
        
        novo_funcionario = {
            'idFuncionario': validar_int(idF, 'idFuncionario'),
            'nome': validar_varchar(nome, 'nome', 255),
            'cargo': validar_varchar(cargo, 'cargo', 50),
            'dataContratacao': validar_date(dataContratacao, 'dataContratacao')
        }
        TabelaFuncionario.append(novo_funcionario)
        print(f"✅ Funcionário {nome} inserido.")
    except (TypeError, ValueError) as e:
        print(f"❌ Falha ao inserir funcionário: {e}")

# --- Tabela Projeto (Relação 1:N com Gerente) ---
# Atributos: idProjeto (INT, PK), nome (VARCHAR), dataInicio (DATE), idGerente (INT, FK)
def inserir_projeto(idP, nome, dataInicio, idGerente):
    try:
        verificar_pk(TabelaProjeto, idP, 'idProjeto')
        
        # Simulação da Chave Estrangeira (FK): idGerente -> TabelaFuncionario
        if not any(f['idFuncionario'] == idGerente for f in TabelaFuncionario):
             raise ValueError(f"Erro de Chave Estrangeira: Gerente ID {idGerente} não existe na tabela Funcionario.")
        
        novo_projeto = {
            'idProjeto': validar_int(idP, 'idProjeto'),
            'nome': validar_varchar(nome, 'nome', 255),
            'dataInicio': validar_date(dataInicio, 'dataInicio'),
            'idGerente': validar_int(idGerente, 'idGerente')
        }
        TabelaProjeto.append(novo_projeto)
        print(f"✅ Projeto '{nome}' inserido com Gerente {idGerente}.")
    except (TypeError, ValueError) as e:
        print(f"❌ Falha ao inserir projeto: {e}")

# --- Tabela ProjetoFuncionario (Tabela de Junção N:M) ---
# Atributos: idProjeto (INT, PK, FK), idFuncionario (INT, PK, FK), horasTrabalhadas (INT)
def atribuir_funcionario_projeto(idP, idF, horasTrabalhadas):
    try:
        # Simulação da Chave Primária Composta
        verificar_pk(TabelaProjetoFuncionario, (idP, idF), ('idProjeto', 'idFuncionario'))

        # Simulação das Chaves Estrangeiras (FKs)
        if not any(p['idProjeto'] == idP for p in TabelaProjeto):
             raise ValueError(f"Erro de FK: Projeto ID {idP} não existe.")
        if not any(f['idFuncionario'] == idF for f in TabelaFuncionario):
             raise ValueError(f"Erro de FK: Funcionário ID {idF} não existe.")
        
        nova_atribuicao = {
            'idProjeto': validar_int(idP, 'idProjeto'),
            'idFuncionario': validar_int(idF, 'idFuncionario'),
            'horasTrabalhadas': validar_int(horasTrabalhadas, 'horasTrabalhadas')
        }
        TabelaProjetoFuncionario.append(nova_atribuicao)
        print(f"✅ Atribuição: F({idF}) -> P({idP}) com {horasTrabalhadas} horas.")
    except (TypeError, ValueError) as e:
        print(f"❌ Falha ao atribuir funcionário ao projeto: {e}")


# 3. Execução e Teste dos Conceitos

# Inserção de Dados
inserir_funcionario(1, "Alice Gerente", "Gerente Senior", date(2018, 5, 15))
inserir_funcionario(2, "Bob Desenvolvedor", "Desenvolvedor JR", date(2021, 1, 20))
inserir_funcionario(3, "Charlie Designer", "Designer UX", date(2022, 9, 1))

print("\n--- Teste de Chave Primária ---")
inserir_funcionario(1, "Alice Duplicada", "Tentativa de PK duplicada", date(2023, 1, 1)) # DEVE FALHAR

print("\n--- Teste de Chave Estrangeira (1:N) ---")
inserir_projeto(100, "App Mobile Startup", date(2024, 3, 1), 1) # Gerente Alice (ID 1)
inserir_projeto(101, "Infraestrutura Cloud", date(2024, 4, 15), 99) # DEVE FALHAR (Gerente 99 não existe)

print("\n--- Teste de Cardinalidade N:M ---")
# Alice (1) e Bob (2) trabalhando no Projeto 100
atribuir_funcionario_projeto(100, 1, 160) # Atribuição 1
atribuir_funcionario_projeto(100, 2, 120) # Atribuição 2
# Bob (2) também trabalhando no Projeto 101 (Se o projeto for criado, mas falhou acima)
# Inserindo Projeto 102 (Gerente Bob)
inserir_projeto(102, "Web Site Institucional", date(2024, 7, 1), 2)
atribuir_funcionario_projeto(102, 3, 80) # Charlie (3) trabalhando no Projeto 102

print("\n--- Estruturas Finais (Simulação) ---")
print("Funcionários:", TabelaFuncionario)
print("Projetos:", TabelaProjeto)
print("Atribuições N:M:", TabelaProjetoFuncionario)

# Omissão da tabela supervisao por simplificação e ambiguidade no modelo original