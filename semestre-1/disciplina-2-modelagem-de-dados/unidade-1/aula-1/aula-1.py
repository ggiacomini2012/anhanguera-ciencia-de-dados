import sqlite3

def criar_e_preencher_banco():
    """
    Função para criar e preencher o banco de dados da faculdade.
    Simula o processo de matrícula de um estudante.
    """
    # Conecta ao banco de dados (se não existir, ele é criado)
    # O arquivo 'faculdade.db' será criado no mesmo diretório do script
    conn = sqlite3.connect('faculdade.db')
    cursor = conn.cursor()
    
    # --- Passo 1: Modelagem de Dados Relacional ---
    # Cria a tabela de departamentos (uma 'entidade' ou 'relação')
    print("Criando tabela 'departamentos'...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departamentos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)
    
    # Cria a tabela de estudantes (outra 'entidade' ou 'relação')
    # Observe a 'chave estrangeira' (FOREIGN KEY) que conecta as duas tabelas.
    # Isso demonstra o conceito de relacionamento em um banco de dados relacional.
    print("Criando tabela 'estudantes'...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes (
            matricula INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            departamento_id INTEGER,
            FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
        )
    """)
    
    # Insere dados nas tabelas
    print("Inserindo dados nas tabelas...")
    cursor.execute("INSERT OR IGNORE INTO departamentos (id, nome) VALUES (?, ?)", (1, 'Tecnologia da Informação'))
    cursor.execute("INSERT OR IGNORE INTO departamentos (id, nome) VALUES (?, ?)", (2, 'Ciências Contábeis'))
    
    # Inserção dos dados do estudante, como no exemplo da aula
    # Os dados do estudante estão "relacionados" ao departamento 1 (TI)
    cursor.execute("INSERT OR IGNORE INTO estudantes (matricula, nome, email, departamento_id) VALUES (?, ?, ?, ?)", 
                   (2025001, 'Maria Silva', 'maria.silva@email.com', 1))
    
    # Salva as alterações
    conn.commit()
    conn.close()
    print("Banco de dados 'faculdade.db' criado e preenchido com sucesso.\n")

def simular_aplicacoes():
    """
    Função que simula diferentes aplicações (secretaria e financeiro)
    acessando o mesmo banco de dados.
    """
    conn = sqlite3.connect('faculdade.db')
    cursor = conn.cursor()

    # --- Passo 2: Acesso e uso do Banco de Dados por diferentes Aplicações ---
    # Simulação da "Aplicação Secretaria"
    # A secretaria busca as informações completas do estudante, incluindo o nome do departamento.
    print("--- Simulação: Aplicação de Cadastro (Secretaria) ---")
    
    # A consulta JOIN é usada para "unir" os dados das duas tabelas.
    cursor.execute("""
        SELECT e.matricula, e.nome, e.email, d.nome 
        FROM estudantes e 
        JOIN departamentos d ON e.departamento_id = d.id 
        WHERE e.matricula = 2025001
    """)
    
    estudante_secretaria = cursor.fetchone()
    if estudante_secretaria:
        print("Dados do estudante para a secretaria:")
        print(f"  Matrícula: {estudante_secretaria[0]}")
        print(f"  Nome: {estudante_secretaria[1]}")
        print(f"  E-mail: {estudante_secretaria[2]}")
        print(f"  Departamento: {estudante_secretaria[3]}")
    else:
        print("Estudante não encontrado.")

    # Simulação da "Aplicação Financeiro"
    # O financeiro busca apenas o nome e o e-mail para emitir um boleto.
    print("\n--- Simulação: Aplicação Financeira (Emissão de Boletos) ---")
    cursor.execute("SELECT nome, email FROM estudantes WHERE matricula = 2025001")
    
    estudante_financeiro = cursor.fetchone()
    if estudante_financeiro:
        print("Dados do estudante para o financeiro:")
        print(f"  Nome: {estudante_financeiro[0]}")
        print(f"  E-mail para contato: {estudante_financeiro[1]}")
        print("  Boleto de pagamento gerado com sucesso!")
    else:
        print("Estudante não encontrado.")
    
    conn.close()

# Executa as funções
if __name__ == "__main__":
    criar_e_preencher_banco()
    simular_aplicacoes()