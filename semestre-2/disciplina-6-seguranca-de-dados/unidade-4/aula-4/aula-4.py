"""
S2-D5-U4-A4 — Análise Estatística de Simulação
Assunto: Replicas, Horizontes e Estatísticas no Arena
Exemplo: Simulação de Banco (Horizonte Finito) 🏦⏱️
"""

import random

# Configurações do Experimento (Setup)
HORAS_OPERACAO = 8      # Horizonte Finito: 8 horas (480 min)
NUM_REPLICACOES = 5     # Várias replicações para média global
CHEGADA_MEDIA = 10      # Média de chegada a cada 10 min
SERVICO_MEDIO = 8       # Média de atendimento de 8 min

def rodar_replicacao(id_rep):
    """Simula um dia de operação (uma replicação)"""
    tempo = 0
    clientes_atendidos = 0
    tempos_espera = []
    
    # Simulação simplificada de um dia
    while tempo < HORAS_OPERACAO * 60:
        intervalo = random.expovariate(1.0 / CHEGADA_MEDIA)
        tempo += intervalo
        if tempo > HORAS_OPERACAO * 60: break
        
        espera = random.gammavariate(2, SERVICO_MEDIO/2) # Tempo de serviço variável
        tempos_espera.append(espera)
        clientes_atendidos += 1
        
    media_rep = sum(tempos_espera) / len(tempos_espera) if tempos_espera else 0
    return media_rep, clientes_atendidos

def analise_experimental():
    print(f"🔬 Iniciando Experimento: {NUM_REPLICACOES} Replicação(ões) 🔬")
    print("-" * 65)
    
    medias_das_replicas = []
    total_clientes_global = 0
    
    for i in range(1, NUM_REPLICACOES + 1):
        media_espera, qtd = rodar_replicacao(i)
        medias_das_replicas.append(media_espera)
        total_clientes_global += qtd
        print(f"🔄 Replicação {i}: Média de Espera = {media_espera:.2f} min | Clientes = {qtd}")

    # Estatísticas entre as replicações (Across Replications)
    media_global = sum(medias_das_replicas) / len(medias_das_replicas)
    min_media = min(medias_das_replicas)
    max_media = max(medias_das_replicas)

    print("-" * 65)
    print("📊 RELATÓRIO FINAL (ESTILO ARENA) 📊")
    print(f"📍 Horizonte: FINITO (Terminação em {HORAS_OPERACAO}h)")
    print(f"👥 Total de Clientes (Soma Global): {total_clientes_global}")
    print(f"⚖️ Média das Médias (Global): {media_global:.2f} min")
    print(f"📉 Valor Médio Mínimo: {min_media:.2f} min")
    print(f"📈 Valor Médio Máximo: {max_media:.2f} min")
    
    print("-" * 65)
    print("💡 Insight: Uma única replicação pode ser 'azarada' ou 'sortuda'.")
    print("   Ao rodar várias, chegamos a um valor estatisticamente confiável.")

if __name__ == "__main__":
    random.seed(10) # Para consistência nos resultados
    analise_experimental()
