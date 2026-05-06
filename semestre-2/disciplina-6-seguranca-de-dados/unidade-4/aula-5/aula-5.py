import random
import time

class Cliente:
    """Representa uma Entidade no software Arena."""
    def __init__(self, id_cliente):
        self.id = id_cliente
        # Atributos da Entidade
        self.idade = random.randint(18, 85)
        self.itens = random.randint(1, 50)

    def __str__(self):
        return f"Cliente {self.id} [Idade: {self.idade}, Itens: {self.itens}]"

def simular_fluxo_mercado(num_clientes=10):
    print("=== Simulação de Fluxograma (Módulo Arena) ===\n")
    
    contadores = {"Prioritário": 0, "Até 15 Itens": 0, "Normal": 0}
    
    for i in range(1, num_clientes + 1):
        # Módulo CREATE
        cliente = Cliente(i)
        print(f"CREATE: Chegada do {cliente}")
        
        # Módulo DECIDE (Lógica de Cascata)
        if cliente.idade > 60:
            # Módulo PROCESS (Simulado)
            print(" -> [DECIDE: É Idoso? SIM] -> Encaminhado para CAIXA PRIORITÁRIO")
            contadores["Prioritário"] += 1
        elif cliente.itens <= 15:
            # Módulo PROCESS (Simulado)
            print(" -> [DECIDE: É Idoso? NÃO] -> [DECIDE: Até 15 Itens? SIM] -> Encaminhado para CAIXA RÁPIDO")
            contadores["Até 15 Itens"] += 1
        else:
            # Módulo PROCESS (Simulado)
            print(" -> [DECIDE: É Idoso? NÃO] -> [DECIDE: Até 15 Itens? NÃO] -> Encaminhado para CAIXA NORMAL")
            contadores["Normal"] += 1
            
        # Módulo DISPOSE
        print(" -> DISPOSE: Atendimento finalizado. Entidade saiu do sistema.\n")
        time.sleep(0.1)

    print("=== RELATÓRIO FINAL (Módulo de Dados) ===")
    for fila, qtd in contadores.items():
        print(f"Total na Fila {fila}: {qtd}")

if __name__ == "__main__":
    simular_fluxo_mercado(15)
