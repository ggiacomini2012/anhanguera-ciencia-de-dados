"""
S2-D5-U3-A3: Problema de Transporte com Transbordo
Exemplo: Empresa Petroquímica (Manaus/Recife -> SP/RJ -> BH/Joinville/POA)
"""

import pulp

def resolver_transbordo():
    print("🚀 Iniciando Otimização de Logística com Transbordo...")

    # 1. Definir o Problema (Minimização)
    prob = pulp.LpProblem("Minimizar_Custo_Transbordo", pulp.LpMinimize)

    # 2. Variáveis de Decisão
    # x_origem_intermediario
    x_MS = pulp.LpVariable("Manaus_SP", lowBound=0, cat='Integer')
    x_MR = pulp.LpVariable("Manaus_RJ", lowBound=0, cat='Integer')
    x_RS = pulp.LpVariable("Recife_SP", lowBound=0, cat='Integer')
    x_RR = pulp.LpVariable("Recife_RJ", lowBound=0, cat='Integer')

    # x_intermediario_destino
    x_SB = pulp.LpVariable("SP_BH", lowBound=0, cat='Integer')
    x_SJ = pulp.LpVariable("SP_Joinville", lowBound=0, cat='Integer')
    x_SP = pulp.LpVariable("SP_POA", lowBound=0, cat='Integer')
    x_RB = pulp.LpVariable("RJ_BH", lowBound=0, cat='Integer')
    x_RJ = pulp.LpVariable("RJ_Joinville", lowBound=0, cat='Integer')
    x_RP = pulp.LpVariable("RJ_POA", lowBound=0, cat='Integer')

    # 3. Função Objetivo (Custos Totais)
    # Custos Fábrica -> CD
    custo_origem = 8*x_MS + 10*x_MR + 7*x_RS + 6*x_RR
    # Custos CD -> Clientes
    custo_destino = 2*x_SB + 3*x_SJ + 4*x_SP + 1*x_RB + 4*x_RJ + 5*x_RP
    
    prob += custo_origem + custo_destino, "Custo_Total"

    # 4. Restrições
    # Capacidade das Fábricas (Origens)
    prob += x_MS + x_MR <= 500, "Capacidade_Manaus"
    prob += x_RS + x_RR <= 300, "Capacidade_Recife"

    # Demanda dos Clientes (Destinos)
    prob += x_SB + x_RB == 200, "Demanda_BH"
    prob += x_SJ + x_RJ == 250, "Demanda_Joinville"
    prob += x_SP + x_RP == 350, "Demanda_POA"

    # Equilíbrio nos Centros de Distribuição (Transbordo)
    # O que entra deve ser igual ao que sai
    prob += x_MS + x_RS == x_SB + x_SJ + x_SP, "Equilibrio_SP"
    prob += x_MR + x_RR == x_RB + x_RJ + x_RP, "Equilibrio_RJ"

    # 5. Resolver
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # 6. Exibir Resultados
    print(f"\n📊 Status da Solução: {pulp.LpStatus[prob.status]}")
    print(f"💰 Custo Mínimo Total: R$ {pulp.value(prob.objective):,.2f}")
    
    print("\n🚛 Fluxo de Transporte (Fábricas -> CDs):")
    print(f"📍 Manaus -> SP: {x_MS.varValue} un")
    print(f"📍 Manaus -> RJ: {x_MR.varValue} un")
    print(f"📍 Recife -> SP: {x_RS.varValue} un")
    print(f"📍 Recife -> RJ: {x_RR.varValue} un")

    print("\n📦 Fluxo de Transporte (CDs -> Clientes):")
    print(f"🏙️ SP -> BH: {x_SB.varValue} un")
    print(f"🏙️ SP -> Joinville: {x_SJ.varValue} un")
    print(f"🏙️ SP -> POA: {x_SP.varValue} un")
    print(f"🏙️ RJ -> BH: {x_RB.varValue} un")
    print(f"🏙️ RJ -> Joinville: {x_RJ.varValue} un")
    print(f"🏙️ RJ -> POA: {x_RP.varValue} un")

    print("\n💡 Insight: O transbordo permite consolidar cargas e reduzir custos usando rotas intermediárias mais baratas!")

if __name__ == "__main__":
    resolver_transbordo()
