# Importa as bibliotecas necessárias
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# --- Configuração do Banco de Dados ---
# Conecta ou cria um arquivo de banco de dados chamado 'encomendas.db'
def get_db_connection():
    conn = sqlite3.connect('encomendas.db')
    # Permite acessar colunas por nome
    conn.row_factory = sqlite3.Row
    return conn

# Cria a tabela de encomendas se ela ainda não existir
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS encomendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            bolo TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            data_entrega TEXT NOT NULL,
            valor REAL NOT NULL
        );
    ''')
    conn.close()

# Executa a função para criar a tabela ao iniciar o aplicativo
create_table()

# --- Rotas da Aplicação (Páginas Web) ---

# Rota para a página inicial (mostra a lista de encomendas)
@app.route('/')
def index():
    conn = get_db_connection()
    # Pega todas as encomendas do banco de dados, ordenadas por data de entrega
    encomendas = conn.execute('SELECT * FROM encomendas ORDER BY data_entrega').fetchall()
    conn.close()
    return render_template('index.html', encomendas=encomendas)

# Rota para adicionar uma nova encomenda
@app.route('/adicionar', methods=('GET', 'POST'))
def adicionar_encomenda():
    if request.method == 'POST':
        # Pega os dados do formulário enviado pelo usuário
        cliente = request.form['cliente']
        bolo = request.form['bolo']
        quantidade = request.form['quantidade']
        data_entrega = request.form['data_entrega']
        valor = request.form['valor']

        # Insere os dados na tabela de encomendas
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO encomendas (cliente, bolo, quantidade, data_entrega, valor) VALUES (?, ?, ?, ?, ?)',
            (cliente, bolo, quantidade, data_entrega, valor)
        )
        conn.commit()
        conn.close()
        # Redireciona o usuário para a página inicial
        return redirect(url_for('index'))
    
    # Se a requisição for GET, apenas mostra o formulário
    return render_template('adicionar.html')

# --- Executa o Aplicativo ---
if __name__ == '__main__':
    # Inicia o servidor web do Flask no modo de debug
    app.run(debug=True)