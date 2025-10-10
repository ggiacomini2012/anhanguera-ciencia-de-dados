# aula-3.py
# Exemplo de Armazenamento de Dados: SQL em Ação com Python
# Demonstra as categorias DDL (CREATE), DML (INSERT, SELECT) e DTL (COMMIT)
# e serve como base para a conexão a um serviço como o SQL Azure na Nuvem.

import sqlite3
import os

# --------------------------------------------------------------------------------------
# 1. Conexão ao "Castelo" (Banco de Dados SQL)
# --------------------------------------------------------------------------------------
# Usamos o SQLite, um banco de dados local embutido, para simular um SGBD Relacional
# A conexão com um SQL Azure ou PostgreSQL seria muito similar, apenas mudando a string de conexão.

DB_NAME = 'tesouro_dados_aula3.db'

# Remove o arquivo do banco de dados se ele já existir para garantir um teste limpo
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

try:
    # Cria uma conexão e um cursor (o "operário" que envia comandos)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print(f"✅ Conexão estabelecida com sucesso ao banco de dados: {DB_NAME}")

    # ----------------------------------------------------------------------------------
    # 2. DDL (Data Definition Language) - O Arquiteto constrói a tabela
    # ----------------------------------------------------------------------------------
    # Criamos a tabela 'Projetos_Nuvem' com colunas definidas (estrutura)
    print("\n-- Executando DDL: Criando a tabela 'Projetos_Nuvem' (CREATE TABLE)")
    cursor.execute("""
    CREATE TABLE Projetos_Nuvem (
        id INTEGER PRIMARY KEY,
        nome_projeto TEXT NOT NULL,
        plataforma_nuvem TEXT NOT NULL,
        modelo_servico TEXT, -- IaaS, PaaS, SaaS
        custo_mensal REAL
    );
    """)
    print("📋 Tabela 'Projetos_Nuvem' criada. Estrutura definida!")

    # ----------------------------------------------------------------------------------
    # 3. DML (Data Manipulation Language) - Os Pedreiros inserem os dados
    # ----------------------------------------------------------------------------------
    projetos = [
        ('Data Lake', 'Azure', 'PaaS', 150.00),
        ('Website Institucional', 'AWS', 'IaaS', 45.50),
        ('Email Corporativo', 'GCP', 'SaaS', 25.00),
        ('Análise de Logs', 'Azure', 'PaaS', 89.90)
    ]

    print("\n-- Executando DML: Inserindo novos registros (INSERT)")
    cursor.executemany("INSERT INTO Projetos_Nuvem (nome_projeto, plataforma_nuvem, modelo_servico, custo_mensal) VALUES (?, ?, ?, ?)", projetos)
    print(f"➕ {cursor.rowcount} registros inseridos com sucesso.")

    # ----------------------------------------------------------------------------------
    # 4. DTL (Data Transaction Language) - O Notário garante a persistência
    # ----------------------------------------------------------------------------------
    # O COMMIT garante que as inserções sejam salvas permanentemente no disco.
    print("-- Executando DTL: Confirmando a transação (COMMIT)")
    conn.commit()
    print("✅ Transação confirmada. Dados salvos.")

    # ----------------------------------------------------------------------------------
    # 5. DML (Data Manipulation Language) - O Pedreiro consulta os dados
    # ----------------------------------------------------------------------------------
    print("\n-- Executando DML: Consultando dados do Azure (SELECT com Predicado)")
    cursor.execute("SELECT nome_projeto, modelo_servico FROM Projetos_Nuvem WHERE plataforma_nuvem = 'Azure'")

    print("\nProjetos na Azure:")
    for row in cursor.fetchall():
        print(f"  - Projeto: {row[0]}, Modelo: {row[1]}")

    # Consultando Funções Agregadas (Resumindo os dados)
    print("\n-- Consultando Funções Agregadas (AVG, SUM, COUNT)")
    cursor.execute("SELECT AVG(custo_mensal), SUM(custo_mensal), COUNT(id) FROM Projetos_Nuvem")
    media, soma, total = cursor.fetchone()

    print(f"📊 Análise de Custos:")
    print(f"  - Custo Mensal Médio dos Projetos: R$ {media:.2f}")
    print(f"  - Custo Mensal Total (SUM): R$ {soma:.2f}")
    print(f"  - Número Total de Projetos (COUNT): {total}")


except sqlite3.Error as e:
    print(f"❌ Ocorreu um erro no SQL: {e}")
    # O ROLLBACK seria chamado aqui em um cenário real de erro (DTL)
    if 'conn' in locals() and conn:
        conn.rollback()
        print("↩️ Transação desfeita (ROLLBACK) devido ao erro.")

finally:
    # 6. Finalização - Fechando a porta do castelo
    if 'conn' in locals() and conn:
        conn.close()
        print("\n✅ Conexão SQL encerrada.")

# NOTA SOBRE NUVEM:
# Para conectar ao SQL Azure, seria necessário instalar o driver 'pyodbc'
# e mudar a linha de conexão para algo como:
# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=...;DATABASE=...;UID=...;PWD=...')
# O resto do código (DDL, DML, DTL) permaneceria o mesmo!