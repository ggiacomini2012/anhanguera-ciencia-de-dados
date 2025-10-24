import time
import random
from concurrent.futures import ThreadPoolExecutor

# --- Configurações da Simulação ---
NUMERO_PEDIDOS = 20
NUMERO_SERVIDORES = 4

# --- Metáfora: Funções de Processamento ---

def processar_pedido_vertical(pedido):
    """
    Simula o processamento em um ambiente de Escalabilidade Vertical
    (Um único servidor fazendo tudo).
    """
    tempo_processamento = random.uniform(0.5, 1.5) # Tempo de processamento mais variável/lento
    print(f"⚙️ [Servidor Único] Processando Pedido #{pedido:03d}...")
    time.sleep(tempo_processamento)
    print(f"✅ [Servidor Único] Pedido #{pedido:03d} concluído em {tempo_processamento:.2f}s.")

def processar_pedido_horizontal(pedido, servidor_id):
    """
    Simula o processamento em um ambiente de Escalabilidade Horizontal
    (Vários servidores distribuindo a carga).
    """
    tempo_processamento = random.uniform(0.1, 0.4) # Tempo de processamento mais rápido
    print(f"💻 [Servidor {servidor_id}] Processando Pedido #{pedido:03d}...")
    time.sleep(tempo_processamento)
    print(f"✨ [Servidor {servidor_id}] Pedido #{pedido:03d} concluído em {tempo_processamento:.2f}s.")
    return f"Pedido {pedido:03d} processado pelo Servidor {servidor_id}"

# --- Simulação de Escalabilidade Vertical (Sem Paralelismo) ---
def simular_vertical():
    print("\n" + "="*50)
    print(f"🐌 SIMULAÇÃO DE ESCALABILIDADE VERTICAL ({NUMERO_PEDIDOS} Pedidos)")
    print(" (Apenas 1 'servidor', processamento sequencial)")
    print("="*50)

    start_time = time.time()
    for i in range(1, NUMERO_PEDIDOS + 1):
        processar_pedido_vertical(i)
    
    end_time = time.time()
    print("\n" + "*"*50)
    print(f"⏱️ Tempo Total (Vertical): {end_time - start_time:.2f} segundos")
    print("*"*50)

# --- Simulação de Escalabilidade Horizontal (Com Paralelismo/ThreadPoolExecutor) ---
def simular_horizontal():
    print("\n" + "="*60)
    print(f"🚀 SIMULAÇÃO DE ESCALABILIDADE HORIZONTAL ({NUMERO_PEDIDOS} Pedidos)")
    print(f" (Usando {NUMERO_SERVIDORES} 'servidores' em paralelo - Thread Pool)")
    print("="*60)

    start_time = time.time()
    
    # O ThreadPoolExecutor simula a distribuição de tarefas entre os N servidores (threads)
    with ThreadPoolExecutor(max_workers=NUMERO_SERVIDORES) as executor:
        # Mapeia cada pedido para um 'servidor' (thread) disponível
        futures = [
            executor.submit(
                processar_pedido_horizontal, 
                pedido_id, 
                (pedido_id % NUMERO_SERVIDORES) + 1 # Atribui o pedido a um dos servidores (1 a 4)
            ) 
            for pedido_id in range(1, NUMERO_PEDIDOS + 1)
        ]
        
        # Opcional: espera que todos os processos terminem
        for future in futures:
            future.result() 

    end_time = time.time()
    print("\n" + "*"*60)
    print(f"⏱️ Tempo Total (Horizontal): {end_time - start_time:.2f} segundos")
    print("*"*60)

# --- Execução da Simulação ---
if __name__ == "__main__":
    
    # 1. Simulação do Cenário de Crise (Vertical)
    simular_vertical() 

    # 2. Simulação da Solução (Horizontal)
    simular_horizontal()

    print("\n--- Conclusão da Simulação ---")
    print("A simulação demonstra que, ao distribuir a carga de trabalho")
    print("em vários 'servidores' (Escalabilidade Horizontal), o tempo")
    print("total de processamento é drasticamente reduzido, otimizando o desempenho.")