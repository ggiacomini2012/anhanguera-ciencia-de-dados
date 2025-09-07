# -*- coding: utf-8 -*-
# Exemplo de Sistema de Gerenciamento de Banco de Dados (SGBD)
# Este script Python simula as principais funcionalidades de um SGBD,
# como manipulação de dados, controle de concorrência e garantias ACID.

import threading
import time
import random
import json

# ==============================================================================
# Representação do Banco de Dados
# Usamos um dicionário simples para simular uma tabela de dados.
# A chave é o 'id_produto' e o valor é um dicionário com os detalhes.
# ==============================================================================
db_data = {
    "101": {"nome": "Refrigerador A", "estoque": 5, "preco": 2500.00},
    "102": {"nome": "Televisão B", "estoque": 10, "preco": 1800.00},
    "103": {"nome": "Micro-ondas C", "estoque": 8, "preco": 550.00},
}

# ==============================================================================
# Simulação de Transações (conceito central de um SGBD)
# Uma transação é uma unidade de trabalho que acessa e modifica dados.
# ==============================================================================

class Transacao:
    """
    Simula uma transação de banco de dados com comandos DML.
    """
    def __init__(self, id_transacao):
        self.id = id_transacao
        self.log_transacao = {}
        self.estado = "ativa"

    def pesquisar_estoque(self, id_produto):
        """Simula um comando SELECT (DML)."""
        print(f"Transação {self.id}: Pesquisando estoque do produto {id_produto}...")
        time.sleep(random.uniform(0.1, 0.5)) # Simula latência
        try:
            estoque_atual = db_data[id_produto]["estoque"]
            print(f"Transação {self.id}: Estoque atual de {id_produto} é {estoque_atual}.")
            return estoque_atual
        except KeyError:
            print(f"Transação {self.id}: Produto {id_produto} não encontrado.")
            return None

    def vender_produto(self, id_produto, quantidade):
        """Simula um comando UPDATE (DML) com controle de atomicidade."""
        print(f"Transação {self.id}: Tentando vender {quantidade} unidade(s) de {id_produto}...")
        if self.estado != "ativa":
            print(f"Transação {self.id} não está ativa. Operação cancelada.")
            return False

        # Verifica o estado inicial para atomicidade
        if id_produto not in self.log_transacao:
            self.log_transacao[id_produto] = db_data[id_produto]["estoque"]

        estoque_atual = db_data[id_produto]["estoque"]
        if estoque_atual >= quantidade:
            db_data[id_produto]["estoque"] -= quantidade
            print(f"Transação {self.id}: Venda de {quantidade} unidade(s) de {id_produto} bem-sucedida.")
            return True
        else:
            print(f"Transação {self.id}: Falha na venda! Estoque de {id_produto} insuficiente.")
            self.reverter() # Aciona a atomicidade
            return False

    def reverter(self):
        """
        Simula a propriedade de Atomicidade (reverter mudanças em caso de falha).
        """
        print(f"Transação {self.id}: Revertendo mudanças...")
        for id_produto, estoque_original in self.log_transacao.items():
            db_data[id_produto]["estoque"] = estoque_original
        self.estado = "revertida"
        print(f"Transação {self.id}: Mudanças revertidas. Estado: {self.estado}")

    def commit(self):
        """
        Simula a propriedade de Durabilidade (gravar as mudanças).
        """
        self.estado = "commitada"
        print(f"Transação {self.id}: Transação finalizada e commitada. Estado: {self.estado}")

# ==============================================================================
# Simulação do SGBD e Concorrência
# Este é o "software" que gerencia as transações.
# ==============================================================================

class SGBD:
    """
    Simula um SGBD com controle de concorrência e logs.
    """
    def __init__(self):
        # Simula a "memória" do SGBD
        self.lock = threading.Lock() # Trava para garantir o isolamento
        self.logs = []

    def log_transacao(self, mensagem):
        """Grava eventos para auditoria e recuperação."""
        self.logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {mensagem}")

    def processar_transacao_isolada(self, transacao):
        """
        Simula o Isolamento, garantindo que apenas uma transação
        modifique os dados por vez.
        """
        self.lock.acquire() # Adquire a trava para garantir acesso exclusivo
        try:
            self.log_transacao(f"Iniciando transação isolada {transacao.id}")
            transacao.vender_produto("101", 1) # Tenta vender um Refrigerador
            transacao.commit()
        finally:
            self.lock.release() # Libera a trava
            self.log_transacao(f"Finalizando transação isolada {transacao.id}")

    def processar_transacao_concorrente(self, transacao):
        """
        Simula um problema de concorrência sem isolamento.
        Duas transações acessando o mesmo recurso.
        """
        self.log_transacao(f"Iniciando transação concorrente {transacao.id}")
        transacao.vender_produto("101", 1) # Tenta vender o Refrigerador
        time.sleep(1) # Simula um atraso para permitir a outra transação interagir
        transacao.commit()
        self.log_transacao(f"Finalizando transação concorrente {transacao.id}")


# ==============================================================================
# Exemplo de Uso
# ==============================================================================

def main():
    """
    Função principal para demonstrar o SGBD em ação.
    """
    sgbd = SGBD()

    print("--- Exemplo 1: Concorrência SEM controle de Isolamento ---")
    print("Dois vendedores (transações) tentam vender o mesmo produto ao mesmo tempo.")
    print("Estoque inicial do Refrigerador A: 5 unidades.")
    print("Isto pode causar um problema de consistência.")

    # Resetando os dados para o exemplo
    db_data["101"]["estoque"] = 5

    # Cria duas transações concorrentes (simulando dois vendedores)
    t1_concorrente = threading.Thread(target=sgbd.processar_transacao_concorrente, args=(Transacao("Vendedor 1"),))
    t2_concorrente = threading.Thread(target=sgbd.processar_transacao_concorrente, args=(Transacao("Vendedor 2"),))

    t1_concorrente.start()
    t2_concorrente.start()

    t1_concorrente.join()
    t2_concorrente.join()

    print("\n--- Resultado após o Exemplo 1 ---")
    print(f"Estoque final do Refrigerador A: {db_data['101']['estoque']}")
    print("Observe que o estoque pode ter ficado incorreto, devido à falta de isolamento.")

    print("\n--- Exemplo 2: Concorrência COM controle de Isolamento (garantindo ACID) ---")
    print("O SGBD utiliza travas para evitar que as transações se interfiram.")
    print("Isto garante o requisito de Isolamento, um dos pilares do ACID.")

    # Resetando os dados novamente
    db_data["101"]["estoque"] = 5

    # Cria duas transações que serão processadas pelo SGBD com controle de isolamento
    t1_isolada = threading.Thread(target=sgbd.processar_transacao_isolada, args=(Transacao("Vendedor 3"),))
    t2_isolada = threading.Thread(target=sgbd.processar_transacao_isolada, args=(Transacao("Vendedor 4"),))

    t1_isolada.start()
    t2_isolada.start()

    t1_isolada.join()
    t2_isolada.join()

    print("\n--- Resultado após o Exemplo 2 ---")
    print(f"Estoque final do Refrigerador A: {db_data['101']['estoque']}")
    print("Neste caso, o estoque está correto, pois o SGBD garantiu o isolamento.")

    print("\n--- Resumo dos logs do SGBD ---")
    for log in sgbd.logs:
        print(log)

if __name__ == "__main__":
    main()
