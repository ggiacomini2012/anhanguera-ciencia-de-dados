# -*- coding: utf-8 -*-
"""
S2-D5-U2-A5: Programação Linear, Método Simplex e Dualidade
Objetivo: Resolver o problema de maximização de lucro da Fábrica de Produtos A e B.
"""

from scipy.optimize import linprog

def resolver_otimizacao():
    print("🏭 Iniciando otimização da produção da Fábrica...")

    # Função Objetivo: Max Z = 80x + 60y
    # Como o linprog sempre minimiza, invertemos os sinais para maximizar.
    # Min -Z = -80x - 60y
    c = [-80, -60]

    # Matriz de Restrições (Lado Esquerdo - LHS)
    # 1. 4x + 6y <= 24 (Horas na Máquina M1)
    # 2. 4x + 2y <= 16 (Horas na Máquina M2)
    # 3. 0x + 1y <= 3  (Demanda máxima do Produto B)
    A = [
        [4, 6],
        [4, 2],
        [0, 1]
    ]

    # Vetor de Restrições (Lado Direito - RHS)
    b = [24, 16, 3]

    # Limites das variáveis (Não-negatividade)
    # x >= 0 e y >= 0
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Execução do Método Simplex (através do solver 'highs')
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    if res.success:
        print("\n✅ Otimização concluída com sucesso!")
        print(f"📊 Produção de Produto A: {res.x[0]:.1f} unidades")
        print(f"📊 Produção de Produto B: {res.x[1]:.1f} unidades")
        print(f"💰 Lucro Total Máximo: R$ {-res.fun:.2f}")
        
        print("\n💡 Insight Prático:")
        print("Para atingir o pico de eficiência, a fábrica deve focar na produção")
        print(f"de {res.x[0]:.0f} unidades de A e {res.x[1]:.0f} de B. Isso consome")
        print("exatamente o limite das máquinas M1 e M2, gerando o lucro ótimo! 🚀")
    else:
        print("❌ Erro ao tentar encontrar a solução ótima.")

if __name__ == "__main__":
    resolver_otimizacao()
