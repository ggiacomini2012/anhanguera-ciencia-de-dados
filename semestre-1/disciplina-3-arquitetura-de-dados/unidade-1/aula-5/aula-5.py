# aula-5.py
# Exemplo em Python da implementação do Modelo Físico (usando SQLite)
# O Modelo Físico é o resultado da tradução do Modelo Lógico e da Normalização.

import sqlite3
import os

# 1. Definir o nome do banco de dados (o ambiente físico)
DB_NAME = 'biblioteca_universitaria.db'

def configurar_banco_dados():
    """
    Cria a conexão e as tabelas com base no Modelo Lógico/Físico projetado.
    """
    # Excluir o arquivo se ele existir para garantir um ambiente limpo para o teste
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    
    # Conexão com o banco de dados (será criado se não existir)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print(f"✔️ Conectado ao banco de dados: {DB_NAME}")
    print("-" * 30)

    # DDL (Data Definition Language) - Criação das Tabelas
    
    # Tabela 1: Aluno (Entidade principal - Chave Primária ID_Aluno)
    # Modelagem Lógica: ID_Aluno (PK), Nome, Data_Matricula
    try:
        cursor.execute("""
        CREATE TABLE Aluno (
            ID_Aluno INTEGER PRIMARY KEY,   -- PK (Chave Primária)
            Nome TEXT NOT NULL,             -- TEXT (Tipo de dado para string)
            Data_Matricula DATE NOT NULL    -- DATE (Tipo de dado para data)
        );
        """)
        print("✅ Tabela 'Aluno' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"❌ Erro ao criar Tabela Aluno: {e}")
        
    # Tabela 2: Autor (Entidade principal - Chave Primária ID_Autor)
    # Modelagem Lógica: ID_Autor (PK), Nome, Data_Nascimento
    try:
        cursor.execute("""
        CREATE TABLE Autor (
            ID_Autor INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Data_Nascimento DATE,
            Biografia TEXT
        );
        """)
        print("✅ Tabela 'Autor' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"❌ Erro ao criar Tabela Autor: {e}")

    # Tabela 3: Livro (Entidade principal - Chave Primária ISBN)
    # Modelagem Lógica: ISBN (PK), Titulo, Ano_Publicacao, ID_Autor (FK)
    # Nota: Simplificamos o relacionamento para um livro ter apenas um autor.
    try:
        cursor.execute("""
        CREATE TABLE Livro (
            ISBN TEXT PRIMARY KEY,               -- ISBN como PK (Chave Primária)
            Titulo TEXT NOT NULL,
            Ano_Publicacao INTEGER,
            ID_Autor INTEGER,                    -- FK (Chave Estrangeira)
            FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor) 
        );
        """)
        print("✅ Tabela 'Livro' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"❌ Erro ao criar Tabela Livro: {e}")
        
    # Tabela 4: Empréstimo (Entidade de relacionamento - Chaves Estrangeiras)
    # Modelagem Lógica: ID_Emprestimo (PK), ID_Aluno (FK), ISBN (FK), Data_Emprestimo, Data_Devolucao_Prevista
    try:
        cursor.execute("""
        CREATE TABLE Emprestimo (
            ID_Emprestimo INTEGER PRIMARY KEY,
            ID_Aluno INTEGER NOT NULL,
            ISBN TEXT NOT NULL,
            Data_Emprestimo DATE NOT NULL,
            Data_Devolucao_Prevista DATE NOT NULL,
            FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID_Aluno), -- FK referenciando Aluno
            FOREIGN KEY (ISBN) REFERENCES Livro(ISBN)          -- FK referenciando Livro
        );
        """)
        print("✅ Tabela 'Emprestimo' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"❌ Erro ao criar Tabela Emprestimo: {e}")

    # 2. Inserir alguns dados para demonstração (DML - Data Manipulation Language)
    cursor.execute("INSERT INTO Aluno VALUES (101, 'Maria da Silva', '2023-08-15')")
    cursor.execute("INSERT INTO Autor VALUES (1, 'Fernando Machado', '1975-01-20', 'Especialista em BD')")
    cursor.execute("INSERT INTO Livro VALUES ('978-8575225409', 'Banco de Dados Avançado', 2020, 1)")
    cursor.execute("INSERT INTO Emprestimo VALUES (1, 101, '978-8575225409', '2025-10-01', '2025-10-15')")
    
    # 3. Consultar dados para verificar a integridade
    print("-" * 30)
    print("📋 Consulta de Exemplo (JOIN para verificar Empréstimo):")
    cursor.execute("""
    SELECT 
        A.Nome AS Aluno, 
        L.Titulo AS Livro, 
        E.Data_Emprestimo
    FROM Emprestimo E
    JOIN Aluno A ON E.ID_Aluno = A.ID_Aluno
    JOIN Livro L ON E.ISBN = L.ISBN;
    """)
    
    for row in cursor.fetchall():
        print(f"Aluno: {row[0]}, Livro: {row[1]}, Data: {row[2]}")
    
    # 4. Commit e Fechamento
    conn.commit()
    conn.close()
    print("-" * 30)
    print("✔️ Banco de dados criado, populado e conexão fechada.")


if __name__ == "__main__":
    configurar_banco_dados()
    
# Para rodar o arquivo, salve-o como aula-5.py e execute no terminal: python aula-5.py