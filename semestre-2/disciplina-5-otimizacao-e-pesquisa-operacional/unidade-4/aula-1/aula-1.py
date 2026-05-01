# -------------------------------------------------------------------------
# FACULDADE ANHANGUERA - CIÊNCIA DE DADOS
# Disciplina: Otimização e Pesquisa Operacional
# Aula 1: Introdução à Simulação de Sistemas
# Identificador: S2-D5-U4-A1
# -------------------------------------------------------------------------

import random
import time

def simular_producao():
    print("🏭 Iniciando Simulação de Linha de Produção Estocástica (Aleatória)")
    print("-" * 60)

    # Definição das etapas (Entidades Estáticas/Processos)
    etapas = [
        "Corte ✂️", 
        "Torneamento 🌀", 
        "Fresamento ⚙️", 
        "Retífica ✨", 
        "Embalagem 📦"
    ]

    # Atributos do Lote (Entidade Dinâmica)
    lote_id = 101
    tempo_total = 0

    print(f"📦 Processando Lote #{lote_id}...")
    
    for etapa in etapas:
        # Simulando tempo de processamento aleatório (Modelo Estocástico)
        # Em segundos para a simulação ser rápida
        tempo_processamento = random.uniform(0.5, 2.0) 
        tempo_total += tempo_processamento
        
        print(f"⏳ Executando: {etapa}...", end="\r")
        time.sleep(tempo_processamento) # Imitando a passagem do tempo
        print(f"✅ Concluído: {etapa} ({tempo_processamento:.2f} horas simuladas)")

    print("-" * 60)
    print(f"⏱️ Tempo Total de Fabricação: {tempo_total:.2f} horas")
    
    # Verificação (Simples lógica de validação)
    if tempo_total > 8:
        print("⚠️ Alerta: Gargalo detectado! O tempo excedeu o limite do turno.")
    else:
        print("🟢 Fluxo eficiente: Produção dentro dos parâmetros esperados.")

    # Insight Data Science
    print("\n💡 Insight Data Science:")
    print("Diferente da Otimização Linear (onde buscamos o ponto exato), na Simulação")
    print("nós 'jogamos os dados' várias vezes para entender a variabilidade.")
    print("Em ciência de dados, isso se assemelha às Simulações de Monte Carlo,")
    print("usadas para prever riscos financeiros e comportamentos de usuários.")

if __name__ == "__main__":
    simular_producao()
