# Importa a biblioteca sqlite3 para trabalhar com o banco de dados
import sqlite3

# --- 1. CONEXÃO COM O BANCO DE DADOS ---
# O arquivo 'biblioteca.db' será criado se não existir.
try:
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()
    print("Conexão com o banco de dados estabelecida com sucesso!")
except sqlite3.Error as e:
    print(f"Erro ao conectar com o banco de dados: {e}")
    exit()

# --- 2. IMPLEMENTAÇÃO DO MODELO FÍSICO ---
# Aqui, usamos comandos SQL dentro do Python para criar as tabelas.

# A instrução 'IF NOT EXISTS' evita erros caso a tabela já tenha sido criada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Autores (
        id_autor INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        nacionalidade TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Livros (
        id_livro INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        ano_publicacao INTEGER,
        id_autor INTEGER,
        FOREIGN KEY (id_autor) REFERENCES Autores(id_autor)
    );
""")

# --- 3. INSERÇÃO DE DADOS ---
# Demonstração de como inserir dados nas tabelas.
# Usamos a função executemany() para inserir múltiplos registros de uma vez.

autores_para_inserir = [
    (1, 'Machado de Assis', 'Brasileiro'),
    (2, 'Clarice Lispector', 'Brasileira'),
    (3, 'J.R.R. Tolkien', 'Britânico')
]
cursor.executemany("INSERT OR IGNORE INTO Autores VALUES (?, ?, ?)", autores_para_inserir)

livros_para_inserir = [
    (101, 'Dom Casmurro', 1899, 1),
    (102, 'Memórias Póstumas de Brás Cubas', 1881, 1),
    (103, 'A Hora da Estrela', 1977, 2),
    (104, 'O Senhor dos Anéis', 1954, 3)
]
cursor.executemany("INSERT OR IGNORE INTO Livros VALUES (?, ?, ?, ?)", livros_para_inserir)

# Garante que as mudanças sejam salvas no arquivo do banco de dados
conexao.commit()
print("Dados inseridos e salvos com sucesso!")

# --- 4. CONSULTA E EXIBIÇÃO DE DADOS ---
# Demonstração de como consultar os dados usando JOIN.

print("\n--- Listando Livros e Seus Autores ---")
cursor.execute("""
    SELECT 
        L.titulo,
        A.nome AS autor
    FROM Livros AS L
    JOIN Autores AS A ON L.id_autor = A.id_autor;
""")

# Pega todos os resultados da consulta
resultados = cursor.fetchall()

# Exibe os resultados
for livro in resultados:
    print(f"Livro: {livro[0]}, Autor: {livro[1]}")

# --- 5. FECHAMENTO DA CONEXÃO ---
# É uma boa prática sempre fechar a conexão ao terminar.
conexao.close()
print("\nConexão com o banco de dados fechada.")