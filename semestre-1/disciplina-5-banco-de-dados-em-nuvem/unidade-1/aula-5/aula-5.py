import sqlite3
from contextlib import contextmanager

# ==============================================================================
# 🌟 Contexto: Simulação de um Banco de Dados em Nuvem
# Este script simula um ambiente de Multi-Tenancy em um DB em Nuvem.
# Cada 'Inquilino' (Tenant) tem sua própria tabela (esquema isolado)
# dentro do mesmo banco de dados compartilhado.
# ==============================================================================

DB_NOME = 'cloud_db_simulacao.db'

@contextmanager
def conectar_db(db_nome):
    """Gerenciador de contexto para conexão com o banco de dados."""
    conexao = sqlite3.connect(db_nome)
    try:
        yield conexao
    finally:
        conexao.close()

def criar_tabela_inquilino(tenant_id):
    """Cria uma tabela isolada para um 'inquilino' específico (Multi-Tenancy)."""
    nome_tabela = f'dados_tenant_{tenant_id}'
    try:
        with conectar_db(DB_NOME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {nome_tabela} (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    produto TEXT NOT NULL,
                    valor REAL
                )
            """)
            conn.commit()
        print(f"✅ Tabela para o Inquilino {tenant_id} criada com sucesso ({nome_tabela}).")
    except Exception as e:
        print(f"❌ Erro ao criar a tabela para o Inquilino {tenant_id}: {e}")

def inserir_dados(tenant_id, nome, produto, valor):
    """Insere dados em uma tabela de inquilino."""
    nome_tabela = f'dados_tenant_{tenant_id}'
    try:
        with conectar_db(DB_NOME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {nome_tabela} (nome, produto, valor)
                VALUES (?, ?, ?)
            """, (nome, produto, valor))
            conn.commit()
        print(f"➡️ Dados inseridos para o Inquilino {tenant_id}.")
    except Exception as e:
        print(f"❌ Erro ao inserir dados para o Inquilino {tenant_id}: {e}")

def buscar_dados(tenant_id):
    """Busca e retorna todos os dados de um inquilino."""
    nome_tabela = f'dados_tenant_{tenant_id}'
    print(f"\n--- Buscando Dados do Inquilino {tenant_id} (Tabela: {nome_tabela}) ---")
    try:
        with conectar_db(DB_NOME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {nome_tabela}")
            dados = cursor.fetchall()
            for linha in dados:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Produto: {linha[2]}, Valor: R${linha[3]:.2f}")
            if not dados:
                 print("Nenhum dado encontrado.")
    except Exception as e:
        print(f"❌ Erro ao buscar dados do Inquilino {tenant_id}: {e}")

# ==============================================================================
# 💡 Simulação de Elasticidade e Escalabilidade (Conceitual)
# ==============================================================================
def simular_escalabilidade(numero_novos_inquilinos):
    """
    Simula o crescimento do sistema (Escalabilidade Horizontal)
    ao adicionar novos 'inquilinos' ao mesmo banco de dados.
    Em um DBaaS real, isso envolveria adição de instâncias ou sharding.
    """
    print("\n=======================================================")
    print(f"📈 SIMULAÇÃO DE ESCALABILIDADE: Adicionando {numero_novos_inquilinos} novos inquilinos.")
    print("=======================================================")
    for i in range(1, numero_novos_inquilinos + 1):
        novo_tenant_id = 100 + i # ID a partir de 101
        criar_tabela_inquilino(novo_tenant_id)
        # Inserção de dados para testar o isolamento
        inserir_dados(novo_tenant_id, f"Cliente {novo_tenant_id}", "Licença PRO", 499.99)
    print("\n✅ Escalabilidade Horizontal (adição de inquilinos) concluída.")

# ==============================================================================
# 🚀 Execução do Exemplo
# ==============================================================================

# 1. Configuração inicial dos dois inquilinos originais
INQUILINO_A = 1
INQUILINO_B = 2

# Criação das estruturas isoladas (Multi-Tenancy)
criar_tabela_inquilino(INQUILINO_A)
criar_tabela_inquilino(INQUILINO_B)

# 2. Inserção de dados isolados para cada inquilino
inserir_dados(INQUILINO_A, "Maria", "Serviço Premium", 120.50)
inserir_dados(INQUILINO_A, "João", "Serviço Básico", 45.00)

inserir_dados(INQUILINO_B, "Pedro", "Recurso X", 89.90)
inserir_dados(INQUILINO_B, "Ana", "Recurso Y", 55.00)

# 3. Verificação (garantindo que os dados estão segregados)
buscar_dados(INQUILINO_A)
buscar_dados(INQUILINO_B)

# 4. Simulação de um crescimento súbito (Escalabilidade)
simular_escalabilidade(3)

# 5. Verificação de um novo inquilino (para confirmar o isolamento)
buscar_dados(102)

print("\nFIM DA SIMULAÇÃO.")