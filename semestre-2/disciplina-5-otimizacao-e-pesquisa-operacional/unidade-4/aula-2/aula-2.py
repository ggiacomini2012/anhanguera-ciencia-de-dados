"""
S2-D5-U4-A2 — Simulação de Processos (Arena vs Python)
Assunto: Modelagem de Filas e Fluxogramas no Arena
Exemplo: Sistema de Lava-Jato 🚗🚿
"""

import random
import time

# Configurações da Simulação (Parâmetros do Bloco CREATE e PROCESS)
TEMPO_ENTRE_CHEGADAS_MEDIO = 5  # Média de 5 minutos (Exponencial)
TEMPO_LAVAGEM = 7               # Tempo fixo de lavagem (Constante)
TOTAL_VEICULOS = 10             # Quantidade de veículos para a simulação

def simulador_lava_jato():
    print("🚀 Iniciando Simulação de Lava-Jato (Estilo Arena) 🚀")
    print("-" * 50)
    
    tempo_atual = 0
    veiculos_atendidos = 0
    fila = 0
    recurso_ocupado = False
    proxima_chegada = random.expovariate(1.0 / TEMPO_ENTRE_CHEGADAS_MEDIO)
    tempo_fim_lavagem = float('inf')

    while veiculos_atendidos < TOTAL_VEICULOS:
        # Evento: Chegada de Veículo (Bloco CREATE)
        if proxima_chegada <= tempo_fim_lavagem:
            tempo_atual = proxima_chegada
            fila += 1
            print(f"⏰ Tempo: {tempo_atual:.2f} min | 🚗 Veículo chegou! (Fila: {fila})")
            
            # Agenda a próxima chegada (Random Expo)
            proxima_chegada = tempo_atual + random.expovariate(1.0 / TEMPO_ENTRE_CHEGADAS_MEDIO)
            
            # Se o recurso estiver livre, inicia atendimento (Bloco SEIZE no Process)
            if not recurso_ocupado:
                fila -= 1
                recurso_ocupado = True
                tempo_fim_lavagem = tempo_atual + TEMPO_LAVAGEM
                print(f"✨ Tempo: {tempo_atual:.2f} min | 🧽 Iniciando lavagem... (Recurso Ocupado)")

        # Evento: Fim de Atendimento (Bloco RELEASE no Process + DISPOSE)
        else:
            tempo_atual = tempo_fim_lavagem
            veiculos_atendidos += 1
            recurso_ocupado = False
            print(f"✅ Tempo: {tempo_atual:.2f} min | 🧼 Lavagem concluída! Veículo saiu. (Atendidos: {veiculos_atendidos})")
            
            # Verifica se há alguém na fila para entrar (Próximo na fila)
            if fila > 0:
                fila -= 1
                recurso_ocupado = True
                tempo_fim_lavagem = tempo_atual + TEMPO_LAVAGEM
                print(f"✨ Tempo: {tempo_atual:.2f} min | 🧽 Próximo da fila entrando... (Recurso Ocupado)")
            else:
                tempo_fim_lavagem = float('inf')

    print("-" * 50)
    print(f"🏁 Simulação Finalizada!")
    print(f"📊 Total de Veículos Processados: {veiculos_atendidos}")
    print(f"💡 Insight: Se o tempo de lavagem ({TEMPO_LAVAGEM}) for maior que a média de chegada ({TEMPO_ENTRE_CHEGADAS_MEDIO}), a fila tenderá ao infinito!")

if __name__ == "__main__":
    # Seed para resultados reproduzíveis
    random.seed(42)
    simulador_lava_jato()
