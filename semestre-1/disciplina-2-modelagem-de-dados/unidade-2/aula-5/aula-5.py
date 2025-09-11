import sqlite3
from datetime import datetime

# Nome do arquivo: aula-5.py

def setup_database():
    """Cria as tabelas no banco de dados."""
    conn = sqlite3.connect('flores_brasil.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone TEXT
    );''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enderecos (
        endereco_id INTEGER PRIMARY KEY AUTOINCREMENT,
        rua TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL,
        cep TEXT NOT NULL,
        cliente_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
    );''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        tipo TEXT NOT NULL
    );''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        pedido_id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_pedido TEXT NOT NULL,
        status TEXT NOT NULL,
        cliente_id INTEGER,
        endereco_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
        FOREIGN KEY (endereco_id) REFERENCES enderecos(endereco_id)
    );''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedido_produtos (
        pedido_id INTEGER,
        produto_id INTEGER,
        quantidade INTEGER NOT NULL,
        PRIMARY KEY (pedido_id, produto_id),
        FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
        FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
    );''')

    conn.commit()
    conn.close()

def inserir_dados():
    """Insere dados de exemplo nas tabelas."""
    conn = sqlite3.connect('flores_brasil.db')
    cursor = conn.cursor()

    # Cliente
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
                   ("Maria Silva", "maria.silva@email.com", "1199887766"))
    cliente_id = cursor.lastrowid

    # Endereço
    cursor.execute("INSERT INTO enderecos (rua, cidade, estado, cep, cliente_id) VALUES (?, ?, ?, ?, ?)",
                   ("Rua das Flores, 123", "São Paulo", "SP", "01234-567", cliente_id))
    endereco_id = cursor.lastrowid

    # Produtos
    cursor.execute("INSERT INTO produtos (nome, descricao, preco, tipo) VALUES (?, ?, ?, ?)",
                   ("Buquê de Rosas Vermelhas", "Lindo buquê de 12 rosas vermelhas.", 85.50, "Flores"))
    produto1_id = cursor.lastrowid

    cursor.execute("INSERT INTO produtos (nome, descricao, preco, tipo) VALUES (?, ?, ?, ?)",
                   ("Caixa de Chocolates", "Caixa com 10 bombons sortidos.", 45.00, "Chocolates"))
    produto2_id = cursor.lastrowid

    # Pedido
    cursor.execute("INSERT INTO pedidos (data_pedido, status, cliente_id, endereco_id) VALUES (?, ?, ?, ?)",
                   (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Em Processamento", cliente_id, endereco_id))
    pedido_id = cursor.lastrowid

    # Relação Pedido-Produtos
    cursor.execute("INSERT INTO pedido_produtos (pedido_id, produto_id, quantidade) VALUES (?, ?, ?)",
                   (pedido_id, produto1_id, 1))
    cursor.execute("INSERT INTO pedido_produtos (pedido_id, produto_id, quantidade) VALUES (?, ?, ?)",
                   (pedido_id, produto2_id, 1))

    conn.commit()
    conn.close()

def consultar_pedido(cliente_email):
    """Consulta os detalhes de um pedido de um cliente."""
    conn = sqlite3.connect('flores_brasil.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT
        c.nome AS cliente_nome,
        p.data_pedido,
        e.rua,
        e.cidade,
        pr.nome AS produto_nome,
        pp.quantidade,
        pr.preco
    FROM
        clientes c
    JOIN
        pedidos p ON c.cliente_id = p.cliente_id
    JOIN
        enderecos e ON p.endereco_id = e.endereco_id
    JOIN
        pedido_produtos pp ON p.pedido_id = pp.pedido_id
    JOIN
        produtos pr ON pp.produto_id = pr.produto_id
    WHERE
        c.email = ?;
    ''', (cliente_email,))

    resultados = cursor.fetchall()
    conn.close()
    
    if resultados:
        print("--- Detalhes do Pedido ---")
        for row in resultados:
            print(f"Cliente: {row[0]}")
            print(f"Data do Pedido: {row[1]}")
            print(f"Local de Entrega: {row[2]}, {row[3]}")
            print(f"Produto: {row[4]} | Quantidade: {row[5]} | Preço Unitário: R${row[6]:.2f}")
    else:
        print("Nenhum pedido encontrado para este cliente.")

# Execução
if __name__ == "__main__":
    setup_database()
    inserir_dados()
    consultar_pedido("maria.silva@email.com")