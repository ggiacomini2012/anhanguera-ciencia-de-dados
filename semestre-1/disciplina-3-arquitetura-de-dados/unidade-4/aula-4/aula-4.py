import time
import threading
import random

# --- CONCEITOS BÁSICOS DE ESCALABILIDADE ---

def simular_processamento(tempo_base):
    """Simula uma carga de trabalho (ex: processar uma requisição web)."""
    # Adiciona uma pequena variação para simular a vida real
    delay = tempo_base + random.uniform(0.1, 0.5)
    time.sleep(delay)
    return delay

# --- 1. ESCALABILIDADE VERTICAL (Scale-Up) ---

class ServidorVertical:
    """
    Representa um único servidor potente.
    A capacidade é 'vertical' (tempo_base_processamento menor = mais potente).
    """
    def __init__(self, potencia_cpu_ms):
        # Potência do servidor: tempo de processamento em milissegundos
        self.potencia_cpu_ms = potencia_cpu_ms
        self.carga_atual = 0
        print(f"🎚️ Servidor Vertical iniciado com potência: {self.potencia_cpu_ms}ms por requisição.")

    def processar_requisicao(self):
        self.carga_atual += 1
        tempo_gasto = simular_processamento(self.potencia_cpu_ms / 1000)
        self.carga_atual -= 1
        return tempo_gasto

# --- 2. ESCALABILIDADE HORIZONTAL (Scale-Out) ---

class ServidorHorizontal:
    """
    Representa um servidor simples (nó).
    Todos os nós têm a mesma potência base.
    """
    def __init__(self, id, potencia_cpu_ms=1000):
        self.id = id
        self.potencia_cpu_ms = potencia_cpu_ms
        self.carga_atual = 0
        print(f"📦 Nó Horizontal-{id} iniciado com potência base: {self.potencia_cpu_ms}ms.")

    def processar_requisicao(self):
        self.carga_atual += 1
        tempo_gasto = simular_processamento(self.potencia_cpu_ms / 1000)
        self.carga_atual -= 1
        return tempo_gasto

class BalanceadorDeCarga:
    """
    Simula um Load Balancer que distribui a carga (requisições)
    para o servidor horizontal menos ocupado.
    """
    def __init__(self, nos):
        self.nos = nos
        print(f"⚖️ Balanceador de Carga ativo, gerenciando {len(nos)} nós.")

    def distribuir_e_processar(self):
        # Escolhe o nó com a menor carga de trabalho (simulando a distribuição eficiente)
        no_escolhido = min(self.nos, key=lambda no: no.carga_atual)
        
        # Simula o processamento em uma thread para paralelismo (concorrência)
        # Na vida real, a requisição seria enviada ao servidor e esperaria a resposta.
        tempo_gasto = no_escolhido.processar_requisicao()
        return tempo_gasto, no_escolhido.id

# --- CENÁRIO DE TESTE ---

def rodar_simulacao(sistema, total_requisicoes):
    """Função para medir o tempo de processamento total de várias requisições."""
    tempos_requisicoes = []
    
    # Criamos várias threads para simular a concorrência (vários usuários ao mesmo tempo)
    threads = []
    
    def worker():
        if isinstance(sistema, BalanceadorDeCarga):
            tempo, no_id = sistema.distribuir_e_processar()
            tempos_requisicoes.append(tempo)
            # print(f"  [Req] Processada no Nó-{no_id} em {tempo:.2f}s")
        else:
            tempo = sistema.processar_requisicao()
            tempos_requisicoes.append(tempo)
            # print(f"  [Req] Processada em {tempo:.2f}s")

    print(f"\n📢 Iniciando simulação com {total_requisicoes} requisições concorrentes...")
    start_time = time.time()

    # Criação das threads para as requisições
    for _ in range(total_requisicoes):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    # Espera todas as threads terminarem
    for t in threads:
        t.join()

    end_time = time.time()
    tempo_total = end_time - start_time
    
    print(f"✅ Simulação concluída.")
    print(f"Tempo total de execução para {total_requisicoes} requisições: {tempo_total:.2f} segundos.")
    print(f"Tempo médio de resposta por requisição: {sum(tempos_requisicoes) / total_requisicoes:.2f} segundos.")
    return tempo_total

# --- EXECUÇÃO DO EXEMPLO ---

TOTAL_REQUISICOES = 20

print("=======================================================================")
print("  SIMULAÇÃO DE ESCALABILIDADE (Vertical vs. Horizontal) - Aula 4")
print("=======================================================================")

# 1. CENÁRIO BASE: Servidor Vertical Simples (Potência baixa/tempo de resposta alto)
print("\n--- CENÁRIO 1: Servidor Vertical Simples (1500ms de base) ---")
servidor_v1 = ServidorVertical(potencia_cpu_ms=1500)
rodar_simulacao(servidor_v1, TOTAL_REQUISICOES)

# 2. CENÁRIO DE SCALE-UP (Aumento de Potência - Escalabilidade Vertical)
print("\n--- CENÁRIO 2: Servidor Vertical POTTENCIALIZADO (500ms de base) ---")
# Aumentamos os recursos do único servidor (Scale-Up)
servidor_v2 = ServidorVertical(potencia_cpu_ms=500)
rodar_simulacao(servidor_v2, TOTAL_REQUISICOES)


# 3. CENÁRIO DE SCALE-OUT (Adição de Nós - Escalabilidade Horizontal)
print("\n--- CENÁRIO 3: Sistema Horizontal (3 nós de 1500ms de base) ---")
# Usamos 3 servidores simples (Scale-Out)
nos_horizontais = [
    ServidorHorizontal(id=1, potencia_cpu_ms=1500),
    ServidorHorizontal(id=2, potencia_cpu_ms=1500),
    ServidorHorizontal(id=3, potencia_cpu_ms=1500)
]
balanceador = BalanceadorDeCarga(nos_horizontais)
rodar_simulacao(balanceador, TOTAL_REQUISICOES)

print("\n=======================================================================")
print("  ANÁLISE DO RESULTADO:")
print("  O Cenário 3 (Horizontal), apesar de ter servidores mais 'fracos' individualmente")
print("  (1500ms de base), deve demonstrar um tempo total de execução próximo ao")
print("  Cenário 2 (Vertical Potencializado - 500ms de base), devido à capacidade")
print("  de processar múltiplas requisições (Concorrência) em paralelo. Isso é o")
print("  poder da Escalabilidade Horizontal! 🚀")
print("=======================================================================")