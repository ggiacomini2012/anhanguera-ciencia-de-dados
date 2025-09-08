import copy
from datetime import datetime

# Simulação de um banco de dados (tabela de clientes)
banco_de_dados = {
    "clientes": [
        {"id": 1, "nome": "João Silva", "email": "joao.silva@email.com", "saldo": 5000.00},
        {"id": 2, "nome": "Maria Santos", "email": "maria.santos@email.com", "saldo": 12000.50}
    ]
}

# Simulação de privilégios de usuários
# Cada usuário tem uma lista de permissões (ex: SELECT, INSERT, DELETE)
usuarios = {
    "dba_admin": ["SELECT", "INSERT", "DELETE"],
    "analista_financeiro": ["SELECT"],
    "atendente_suporte": ["INSERT", "DELETE"]
}

# Simulação de uma trilha de auditoria para registrar ações
trilha_de_auditoria = []

def sincronizar_dados(db_original):
    """
    Simula a redundância de dados, criando uma cópia de backup.
    
    Args:
        db_original (dict): O banco de dados a ser copiado.
    
    Returns:
        dict: Uma cópia redundante do banco de dados.
    """
    print("Iniciando processo de sincronização de dados...")
    # Usamos copy.deepcopy() para garantir uma cópia independente
    db_redundante = copy.deepcopy(db_original)
    print("Sincronização concluída. Cópia redundante criada.")
    return db_redundante

def checar_privilegio(usuario, privilegio):
    """
    Verifica se um usuário tem o privilégio necessário para uma operação.
    
    Args:
        usuario (str): O nome do usuário.
        privilegio (str): O privilégio a ser checado (ex: 'SELECT').
    
    Returns:
        bool: True se o usuário tiver o privilégio, False caso contrário.
    """
    if usuario in usuarios and privilegio in usuarios[usuario]:
        return True
    return False

def registrar_auditoria(acao, usuario, tabela, detalhes):
    """
    Adiciona um registro à trilha de auditoria.
    
    Args:
        acao (str): A ação realizada (ex: 'CONSULTA', 'INSERCAO').
        usuario (str): O usuário que realizou a ação.
        tabela (str): A tabela afetada.
        detalhes (str): Detalhes da operação.
    """
    registro = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": usuario,
        "acao": acao,
        "tabela": tabela,
        "detalhes": detalhes
    }
    trilha_de_auditoria.append(registro)

def selecionar_dados(usuario):
    """
    Simula a operação SELECT, verificando privilégios e registrando a ação.
    """
    print(f"\n--- Tentativa de consulta de dados por '{usuario}' ---")
    if checar_privilegio(usuario, "SELECT"):
        print("Privilégio 'SELECT' concedido. Realizando consulta...")
        dados_clientes = banco_de_dados["clientes"]
        registrar_auditoria("CONSULTA", usuario, "clientes", "Consulta geral aos clientes")
        for cliente in dados_clientes:
            print(cliente)
    else:
        print("ACESSO NEGADO: O usuário não tem privilégio 'SELECT'.")

def inserir_dados(usuario, novo_cliente):
    """
    Simula a operação INSERT, verificando privilégios e registrando a ação.
    """
    print(f"\n--- Tentativa de inserção de dados por '{usuario}' ---")
    if checar_privilegio(usuario, "INSERT"):
        print("Privilégio 'INSERT' concedido. Inserindo novo cliente...")
        banco_de_dados["clientes"].append(novo_cliente)
        registrar_auditoria("INSERCAO", usuario, "clientes", f"Novo cliente inserido: {novo_cliente['id']}")
        print("Cliente inserido com sucesso!")
    else:
        print("ACESSO NEGADO: O usuário não tem privilégio 'INSERT'.")

def deletar_dados(usuario, cliente_id):
    """
    Simula a operação DELETE, verificando privilégios e registrando a ação.
    """
    print(f"\n--- Tentativa de exclusão de dados por '{usuario}' ---")
    if checar_privilegio(usuario, "DELETE"):
        print("Privilégio 'DELETE' concedido. Excluindo cliente...")
        cliente_encontrado = False
        for i, cliente in enumerate(banco_de_dados["clientes"]):
            if cliente["id"] == cliente_id:
                banco_de_dados["clientes"].pop(i)
                cliente_encontrado = True
                break
        
        if cliente_encontrado:
            registrar_auditoria("EXCLUSAO", usuario, "clientes", f"Cliente com ID {cliente_id} excluído")
            print(f"Cliente com ID {cliente_id} excluído com sucesso!")
        else:
            print(f"ERRO: Cliente com ID {cliente_id} não encontrado.")
    else:
        print("ACESSO NEGADO: O usuário não tem privilégio 'DELETE'.")

# --- Exemplo de uso e demonstração ---

if __name__ == "__main__":
    print("--- DEMONSTRAÇÃO DO SISTEMA DE SEGURANÇA E REDUNDÂNCIA ---")
    
    # Demonstração de redundância de dados
    backup_db = sincronizar_dados(banco_de_dados)
    
    # 1. Analista tenta consultar os dados (deve ter sucesso)
    selecionar_dados("analista_financeiro")
    
    # 2. Analista tenta inserir um novo cliente (deve falhar)
    novo_cliente_analista = {"id": 3, "nome": "Pedro Costa", "email": "pedro.costa@email.com", "saldo": 750.25}
    inserir_dados("analista_financeiro", novo_cliente_analista)
    
    # 3. Atendente de suporte tenta inserir um novo cliente (deve ter sucesso)
    novo_cliente_atendente = {"id": 3, "nome": "Pedro Costa", "email": "pedro.costa@email.com", "saldo": 750.25}
    inserir_dados("atendente_suporte", novo_cliente_atendente)
    
    # 4. Atendente de suporte tenta excluir o cliente 3 (deve ter sucesso)
    deletar_dados("atendente_suporte", 3)
    
    # 5. DBA, com todos os privilégios, insere e deleta um cliente (deve ter sucesso)
    print("\n--- Ações do DBA (administrador) ---")
    novo_cliente_dba = {"id": 4, "nome": "Ana Souza", "email": "ana.souza@email.com", "saldo": 2000.00}
    inserir_dados("dba_admin", novo_cliente_dba)
    selecionar_dados("dba_admin")
    deletar_dados("dba_admin", 4)
    
    print("\n--- Verificando a trilha de auditoria ---")
    if trilha_de_auditoria:
        for registro in trilha_de_auditoria:
            print(registro)
    else:
        print("Trilha de auditoria vazia.")

    print("\n--- Comparando o banco de dados principal com o de backup ---")
    print(f"Banco de dados principal: {banco_de_dados}")
    print(f"Banco de dados de backup: {backup_db}")
    print("\nNote que o banco de dados de backup permanece inalterado, demonstrando a redundância.")
