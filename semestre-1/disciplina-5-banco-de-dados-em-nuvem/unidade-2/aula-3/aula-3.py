import sqlite3
import os

# 📂 Configuração do Banco de Dados
DB_NAME = 'techcorp_db.db'

def conectar_bd():
    """Conecta ou cria o banco de dados e retorna o objeto de conexão."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def configurar_tabela(conn):
    """Cria a tabela funcionarios se ela não existir."""
    cursor = conn.cursor()
    print("--- 1. Configurando a tabela 'funcionarios' ---")
    
    # Comandos DDL (Data Definition Language) para configuração
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT,
            departamento TEXT,
            salario REAL
        );
    """)
    conn.commit()
    print("Tabela 'funcionarios' verificada/criada com sucesso.")

def insert_dml(conn):
    """Realiza a operação INSERT (Task 2)."""
    cursor = conn.cursor()
    print("\n--- 2. INSERT: Inserindo Dados Iniciais (Task 2) ---")
    
    funcionarios_iniciais = [
        ('João Silva', 'Gerente', 'TI', 9500.00),
        ('Maria Santos', 'Analista', 'Marketing', 6800.00),
        ('Pedro Alvares', 'Desenvolvedor', 'TI', 8200.00),
        ('Ana Souza', 'Estagiária', 'Marketing', 2500.00)
    ]
    
    # Inserção de múltiplos registros de uma vez (melhor prática)
    cursor.executemany("""
        INSERT INTO funcionarios (nome, cargo, departamento, salario)
        VALUES (?, ?, ?, ?)
    """, funcionarios_iniciais)
    
    conn.commit()
    print(f"{cursor.rowcount} registros inseridos com sucesso.")

def select_dml(conn):
    """Realiza operações SELECT (Task 3)."""
    cursor = conn.cursor()
    
    print("\n--- 3. SELECT: Buscando Dados (Task 3) ---")

    # a) Todos os funcionários do departamento de TI
    print("\n[3a] Funcionários do departamento de TI:")
    cursor.execute("SELECT nome, cargo, salario FROM funcionarios WHERE departamento = 'TI'")
    for linha in cursor.fetchall():
        print(f"  Nome: {linha[0]}, Cargo: {linha[1]}, Salário: R$ {linha[2]:.2f}")

    # b) O funcionário com o salário mais alto (usando ORDER BY e LIMIT)
    print("\n[3b] Funcionário com o salário mais alto:")
    cursor.execute("SELECT nome, salario FROM funcionarios ORDER BY salario DESC LIMIT 1")
    mais_alto = cursor.fetchone()
    if mais_alto:
        print(f"  Nome: {mais_alto[0]}, Salário: R$ {mais_alto[1]:.2f}")

    # c) A contagem total de funcionários na empresa
    print("\n[3c] Contagem total de funcionários:")
    cursor.execute("SELECT COUNT(id_funcionario) FROM funcionarios")
    total = cursor.fetchone()[0]
    print(f"  Total de funcionários na TechCorp: {total}")

def update_dml(conn):
    """Realiza operações UPDATE (Task 4)."""
    cursor = conn.cursor()
    
    print("\n--- 4. UPDATE: Atualizando Dados (Task 4) ---")

    # a) Atualizar o salário de um funcionário específico (João Silva)
    print("\n[4a] Atualizando salário de João Silva...")
    cursor.execute("""
        UPDATE funcionarios
        SET salario = 10000.00
        WHERE nome = 'João Silva'
    """)
    conn.commit()
    print(f"  {cursor.rowcount} registro(s) atualizado(s). Novo salário verificado:")
    cursor.execute("SELECT salario FROM funcionarios WHERE nome = 'João Silva'")
    print(f"  Salário de João: R$ {cursor.fetchone()[0]:.2f}")

    # b) Mudar o departamento de um funcionário (Pedro Alvares)
    print("\n[4b] Mudando departamento de Pedro Alvares...")
    cursor.execute("""
        UPDATE funcionarios
        SET departamento = 'P&D', cargo = 'Especialista'
        WHERE nome = 'Pedro Alvares'
    """)
    conn.commit()
    print(f"  {cursor.rowcount} registro(s) atualizado(s). Novo departamento verificado:")
    cursor.execute("SELECT departamento, cargo FROM funcionarios WHERE nome = 'Pedro Alvares'")
    print(f"  Pedro agora é: {cursor.fetchone()}")


def delete_dml(conn):
    """Realiza a operação DELETE (Task 5)."""
    cursor = conn.cursor()

    print("\n--- 5. DELETE: Apagando Dados (Task 5) ---")

    # Remover um funcionário que não faz mais parte da empresa (Ana Souza)
    print("Removendo Ana Souza...")
    cursor.execute("DELETE FROM funcionarios WHERE nome = 'Ana Souza'")
    conn.commit()
    print(f"  {cursor.rowcount} registro(s) deletado(s).")
    
    # Verificação final
    cursor.execute("SELECT COUNT(id_funcionario) FROM funcionarios")
    print(f"  Total de funcionários após o DELETE: {cursor.fetchone()[0]}")


# Função principal para executar todo o fluxo
if __name__ == "__main__":
    # Limpa o BD anterior para um teste limpo (DDL implícito)
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Banco de dados anterior ({DB_NAME}) removido para novo teste.")

    conexao = None
    try:
        conexao = conectar_bd()
        
        # 1. Configuração (DDL)
        configurar_tabela(conexao)
        
        # 2. INSERT (DML)
        insert_dml(conexao)
        
        # 3. SELECT (DML)
        select_dml(conexao)
        
        # 4. UPDATE (DML)
        update_dml(conexao)
        
        # 5. DELETE (DML)
        delete_dml(conexao)

    except sqlite3.Error as e:
        print(f"Ocorreu um erro no SQLite: {e}")
        
    finally:
        if conexao:
            conexao.close()
            print("\nConexão com o banco de dados fechada.")