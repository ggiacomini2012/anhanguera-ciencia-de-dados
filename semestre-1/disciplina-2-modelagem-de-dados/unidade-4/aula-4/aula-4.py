import sqlite3

# --- Simulação de um banco de dados "legado" ---
# Vamos criar um arquivo de banco de dados SQLite que simula a estrutura
# de um sistema antigo, sem documentação clara.

def criar_banco_legado():
    """
    Cria um banco de dados 'biblioteca_legado.db' com tabelas e dados.
    """
    try:
        conn = sqlite3.connect('biblioteca_legado.db')
        cursor = conn.cursor()

        # Tabela 'livros_info' (simulando falta de padronização nos nomes)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros_info (
                id_livro INTEGER PRIMARY KEY,
                nome_livro TEXT NOT NULL,
                nome_do_autor TEXT NOT NULL,
                ano_de_publ INTEGER
            );
        ''')

        # Tabela 'membros_dados' (sem chave primária explícita, campo 'identif' com erro de digitação)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS membros_dados (
                identif TEXT NOT NULL,
                nome_membro TEXT NOT NULL
            );
        ''')

        # Tabela 'emprestimos_registros' (relacionamentos não explícitos, nomes de colunas ambíguos)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos_registros (
                id_transacao INTEGER PRIMARY KEY,
                livro_id INTEGER,
                membro_identificacao TEXT,
                data_emprestimo TEXT
            );
        ''')

        # Inserir dados de exemplo
        cursor.execute("INSERT INTO livros_info VALUES (1, 'Aventuras em Python', 'Ana Maria', 2020);")
        cursor.execute("INSERT INTO livros_info VALUES (2, 'SQL para Dummies', 'John Smith', 2018);")
        cursor.execute("INSERT INTO membros_dados VALUES ('MEMB123', 'Carlos Souza');")
        cursor.execute("INSERT INTO membros_dados VALUES ('MEMB456', 'Maria Oliveira');")
        cursor.execute("INSERT INTO emprestimos_registros VALUES (101, 1, 'MEMB123', '2023-10-25');")
        cursor.execute("INSERT INTO emprestimos_registros VALUES (102, 2, 'MEMB456', '2023-10-26');")

        conn.commit()
        print("Banco de dados legado 'biblioteca_legado.db' criado com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# --- Etapa de Engenharia Reversa ---

def engenharia_reversa_biblioteca():
    """
    Simula o processo de engenharia reversa para entender a estrutura
    do banco de dados 'biblioteca_legado.db'.
    """
    print("\n--- Iniciando o processo de Engenharia Reversa ---")
    try:
        conn = sqlite3.connect('biblioteca_legado.db')
        cursor = conn.cursor()

        # Passo 1: Coleta de informações - Listar as tabelas existentes
        print("\nPasso 1: Descobrindo as tabelas existentes...")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()
        print("Tabelas encontradas:", [t[0] for t in tabelas])

        # Passo 2: Análise do banco de dados - Inspecionar a estrutura de cada tabela
        print("\nPasso 2: Analisando a estrutura das tabelas...")
        for tabela in [t[0] for t in tabelas]:
            print(f"\nDetalhes da tabela '{tabela}':")
            cursor.execute(f"PRAGMA table_info('{tabela}');")
            colunas = cursor.fetchall()
            for col in colunas:
                print(f"  Coluna: {col[1]}, Tipo: {col[2]}, Chave Primária: {'Sim' if col[5] else 'Não'}")

        # Passo 3: Identificação de Relacionamentos (Lógica de Negócio)
        # O analista precisa inferir que 'livro_id' se refere a 'id_livro' e 'membro_identificacao' a 'identif'
        print("\nPasso 3: Inferindo relacionamentos e regras de negócio...")
        print("-> A coluna 'livro_id' na tabela 'emprestimos_registros' parece ser uma Chave Estrangeira para 'id_livro' em 'livros_info'.")
        print("-> A coluna 'membro_identificacao' na tabela 'emprestimos_registros' parece ser uma Chave Estrangeira para 'identif' em 'membros_dados'.")

        # Passo 4: Geração de um "modelo lógico" simplificado
        print("\nPasso 4: Criando o novo modelo lógico (conceitual)...")
        print("Entidades:")
        print("  - Livro (id, titulo, autor, ano)")
        print("  - Membro (id, nome)")
        print("  - Empréstimo (id, livro_id, membro_id, data)")
        print("\nRelacionamentos:")
        print("  - Um Livro pode ter muitos Empréstimos (1:N)")
        print("  - Um Membro pode ter muitos Empréstimos (1:N)")

    except sqlite3.Error as e:
        print(f"Erro durante a engenharia reversa: {e}")
    finally:
        if conn:
            conn.close()
        print("\n--- Engenharia Reversa concluída. Novo modelo de dados definido. ---")

# --- Execução do processo ---
if __name__ == "__main__":
    criar_banco_legado()
    engenharia_reversa_biblioteca()