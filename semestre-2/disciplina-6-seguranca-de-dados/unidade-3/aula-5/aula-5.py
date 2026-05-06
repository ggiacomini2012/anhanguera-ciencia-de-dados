# -------------------------------------------------------------------------
# FACULDADE ANHANGUERA - CIÊNCIA DE DADOS
# Disciplina: Otimização e Pesquisa Operacional
# Aula 5: Ponto de Chegada - Problemas de Designação e Solver
# Identificador: S2-D5-U3-A5
# -------------------------------------------------------------------------

import numpy as np
from scipy.optimize import linear_sum_assignment

def resolver_designacao():
    print("🚀 Iniciando Simulação de Otimização de Processos (Indústria de Autopeças)")
    print("-" * 60)

    # Matriz de Custos (Tempos em horas)
    # Linhas: Atividades (Acabamento, Montagem, Pintura)
    # Colunas: Máquinas (M1, M2, M3)
    custos = np.array([
        [8, 10, 12],  # Acabamento
        [15, 13, 12], # Montagem
        [8, 12, 10]   # Pintura
    ])

    print("📊 Tabela de Tempos (Horas):")
    print("           M1  M2  M3")
    print(f"Acabamento: {custos[0]}")
    print(f"Montagem:   {custos[1]}")
    print(f"Pintura:    {custos[2]}")
    print("-" * 60)

    # Resolvendo o problema de designação (Problema do Húngaro / Linear Sum Assignment)
    # O objetivo é minimizar a soma dos custos
    row_ind, col_ind = linear_sum_assignment(custos)

    print("🎯 Solução Ótima Encontrada:")
    atividades = ["Acabamento", "Montagem", "Pintura"]
    maquinas = ["Máquina 1", "Máquina 2", "Máquina 3"]
    
    tempo_total = 0
    for i, j in zip(row_ind, col_ind):
        tempo = custos[i, j]
        tempo_total += tempo
        print(f"✅ {atividades[i]} -> {maquinas[j]} ({tempo} horas)")

    print("-" * 60)
    print(f"⏱️ Tempo Total de Processamento: {tempo_total} horas")
    
    # Insight Prático
    print("\n💡 Insight Data Science:")
    print("O Problema de Designação é a base para algoritmos de matchmaking e alocação de recursos.")
    print("Em Data Science, usamos isso para otimizar frotas, escalas de funcionários e até")
    print("pareamento em sistemas de recomendação complexos.")

if __name__ == "__main__":
    resolver_designacao()
