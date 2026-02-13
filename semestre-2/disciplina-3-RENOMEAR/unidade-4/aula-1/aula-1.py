
"""
Este script simula um Sistema de Gerenciamento de Banco de Dados (SGBD)
de forma extremamente simplificada, usando apenas classes e dicionários em Python.
O objetivo é ilustrar os conceitos de:
- Armazenamento de dados (tabelas)
- Manipulação de dados (DML: Inserir, Selecionar, Atualizar)
- Controle de transações (Princípio da Atomicidade - ACID)
- Visões externas para diferentes usuários.

Vamos usar o cenário da loja de e-commerce da nossa aula.
"""

# 🏛️ Pense nesta classe como o próprio SGBD, o "bibliotecário" dos nossos dados.
class SimpleSGBD:
    """
    Uma classe que simula as operações básicas de um SGBD em memória.
    """
    def __init__(self):
        #  NIVEL INTERNO: Aqui, estamos simulando o armazenamento de dados.
        # Em um SGBD real, isso seria gerenciado em disco de forma complexa.
        # Nossas "tabelas" são dicionários que guardam listas de registros.
        self._dados = {
            "clientes": [],
            "produtos": [],
            "pedidos": []
        }
        # Para simular chaves primárias únicas
        self._proximo_id = {
            "clientes": 1,
            "produtos": 1,
            "pedidos": 1
        }
        print("🚀 SGBD Simples iniciado. Banco de dados em memória criado.")

    # 👨‍✈️ Esta seção simula o PROCESSADOR DML (Data Manipulation Language)
    def inserir(self, tabela, registro):
        """ Simula o comando INSERT. """
        if tabela not in self._dados:
            print(f"❌ Erro: Tabela '{tabela}' não existe.")
            return None
        
        # Simula uma chave primária auto-incrementável
        id_chave = f"id_{tabela[:-1]}" # ex: id_cliente
        registro[id_chave] = self._proximo_id[tabela]
        self._proximo_id[tabela] += 1
        
        self._dados[tabela].append(registro)
        print(f"✅ Registro inserido na tabela '{tabela}': {registro}")
        return registro

    def selecionar(self, tabela, condicao=None):
        """ 
        Simula o comando SELECT. 
        A 'condicao' é uma função lambda, simulando a cláusula WHERE.
        Isto também representa o OTIMIZADOR DE CONSULTAS de forma muito básica.
        """
        if tabela not in self._dados:
            print(f"❌ Erro: Tabela '{tabela}' não existe.")
            return []
        
        if condicao is None:
            # SELECT * FROM tabela
            return self._dados[tabela]
        
        # SELECT * FROM tabela WHERE <condicao>
        return [registro for registro in self._dados[tabela] if condicao(registro)]

    def atualizar_estoque(self, id_produto, quantidade):
        """ Simula um UPDATE específico para o estoque. """
        for produto in self._dados["produtos"]:
            if produto["id_produto"] == id_produto:
                produto["estoque"] -= quantidade
                return True
        return False

    # 🤵 Esta função simula o GERENCIADOR DE TRANSAÇÕES
    def processar_pedido(self, id_cliente, id_produto, quantidade):
        """
        Simula uma transação de venda, aplicando o princípio de ATOMICIDADE (o 'A' do ACID).
        A operação só é concluída se todas as etapas forem bem-sucedidas.
        """
        print(f"\n⚡ Iniciando transação: Cliente {id_cliente} quer comprar {quantidade} unidade(s) do Produto {id_produto}.")

        # 1. Verificar se o cliente existe
        cliente = self.selecionar("clientes", lambda c: c["id_cliente"] == id_cliente)
        if not cliente:
            print("❌ TRANSAÇÃO FALHOU: Cliente não encontrado. Rollback.")
            return False

        # 2. Verificar se o produto existe e tem estoque
        produto = self.selecionar("produtos", lambda p: p["id_produto"] == id_produto)
        if not produto:
            print("❌ TRANSAÇÃO FALHOU: Produto não encontrado. Rollback.")
            return False
        
        produto_em_estoque = produto[0]
        if produto_em_estoque["estoque"] < quantidade:
            print(f"❌ TRANSAÇÃO FALHOU: Estoque insuficiente para o produto '{produto_em_estoque['nome']}'. Rollback.")
            return False

        # --- PONTO DE NÃO RETORNO: Se todas as verificações passaram, executa as operações ---
        print("... Verificações concluídas. Efetuando alterações...")
        
        # 3. Atualizar o estoque do produto (operação de UPDATE)
        self.atualizar_estoque(id_produto, quantidade)
        
        # 4. Criar um novo pedido (operação de INSERT)
        novo_pedido = {
            "id_cliente": id_cliente,
            "id_produto": id_produto,
            "quantidade": quantidade,
            "status": "Concluído"
        }
        self.inserir("pedidos", novo_pedido)

        print("✅ TRANSAÇÃO CONCLUÍDA COM SUCESSO! Pedido processado.")
        return True

# --- Código principal que utiliza o nosso SGBD ---
if __name__ == "__main__":
    
    # Criamos uma instância do nosso sistema de gerenciamento
    sgbd = SimpleSGBD()

    # Populando o banco de dados
    print("\n--- Populando o banco de dados ---")
    sgbd.inserir("clientes", {"nome": "Alice", "email": "alice@email.com"})
    sgbd.inserir("clientes", {"nome": "Beto", "email": "beto@email.com"})
    
    sgbd.inserir("produtos", {"nome": "Notebook Gamer", "preco": 5000.00, "estoque": 10})
    sgbd.inserir("produtos", {"nome": "Mouse sem Fio", "preco": 150.00, "estoque": 30})
    sgbd.inserir("produtos", {"nome": "Teclado Mecânico", "preco": 350.00, "estoque": 5})

    # 🌇 Simulando a VISÃO EXTERNA: Diferentes "usuários" consultando os dados
    print("\n--- Consultas (Visão Externa) ---")
    
    # Visão do Vendedor: "Quais produtos custam menos de R$ 500?"
    produtos_baratos = sgbd.selecionar("produtos", lambda p: p["preco"] < 500)
    print(f"👀 Visão do Vendedor (produtos baratos): {produtos_baratos}")

    # Visão do Gerente de Estoque: "Quais produtos têm estoque baixo (<= 5)?"
    estoque_baixo = sgbd.selecionar("produtos", lambda p: p["estoque"] <= 5)
    print(f"📦 Visão do Gerente de Estoque (estoque baixo): {estoque_baixo}")

    # --- Simulando Transações de Venda ---
    print("\n--- Processamento de Pedidos (Transações) ---")
    
    # Caso 1: Transação com sucesso
    sgbd.processar_pedido(id_cliente=1, id_produto=3, quantidade=2)

    # Caso 2: Tentativa de transação com falha (estoque insuficiente)
    sgbd.processar_pedido(id_cliente=2, id_produto=3, quantidade=10) # Teclado só tem 3 em estoque agora

    # Caso 3: Tentativa de transação com falha (produto inexistente)
    sgbd.processar_pedido(id_cliente=1, id_produto=99, quantidade=1)

    # --- Verificando o estado final do banco de dados ---
    print("\n--- Estado final do Banco de Dados ---")
    print("Produtos:")
    for p in sgbd.selecionar("produtos"):
        print(f"  - {p}")

    print("\nPedidos:")
    for o in sgbd.selecionar("pedidos"):
        print(f"  - {o}")