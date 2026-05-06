"""
S2-D5-U3-A4: Problema de Designação (Atribuição)
Exemplo: Alocação de 3 Equipes para 3 Projetos de Eletrônicos
Objetivo: Minimizar o tempo total de desenvolvimento (em semanas)
"""

import pulp

def resolver_designacao():
    print("🎯 Iniciando Problema de Designação (Atribuição)...")

    # 1. Matriz de Custos (Semanas)
    # Equipes (Linhas) x Projetos (Colunas)
    custos = [
        [16, 20, 24], # Equipe 1
        [30, 26, 24], # Equipe 2
        [16, 24, 20]  # Equipe 3
    ]
    
    n = len(custos) # Número de equipes/projetos (3x3)

    # 2. Definir o Problema
    prob = pulp.LpProblem("Minimizar_Tempo_Designacao", pulp.LpMinimize)

    # 3. Variáveis de Decisão (Binárias: 0 ou 1)
    # x[i][j] = 1 se a equipe i for alocada ao projeto j
    x = pulp.LpVariable.dicts("alocacao", (range(n), range(n)), cat='Binary')

    # 4. Função Objetivo
    prob += pulp.lpSum([custos[i][j] * x[i][j] for i in range(n) for j in range(n)]), "Tempo_Total"

    # 5. Restrições
    # Cada equipe deve ser designada a exatamente um projeto
    for i in range(n):
        prob += pulp.lpSum([x[i][j] for j in range(n)]) == 1, f"Equipe_{i+1}_Um_Projeto"

    # Cada projeto deve ser realizado por exatamente uma equipe
    for j in range(n):
        prob += pulp.lpSum([x[i][j] for i in range(n)]) == 1, f"Projeto_{j+1}_Uma_Equipe"

    # 6. Resolver
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # 7. Exibir Resultados
    print(f"\n📊 Status da Solução: {pulp.LpStatus[prob.status]}")
    print(f"⏳ Tempo Total Mínimo: {pulp.value(prob.objective)} semanas")
    
    print("\n🤝 Alocações Realizadas:")
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j]) == 1:
                print(f"✅ Equipe {i+1} -> Projeto {j+1} (Duração: {custos[i][j]} semanas)")

    print("\n💡 Insight: O Problema de Designação é um caso especial de transporte onde demanda e oferta são sempre 1!")

if __name__ == "__main__":
    resolver_designacao()
