# -*- coding: utf-8 -*-
"""
FACULDADE ANHANGUERA - CIÊNCIA DE DADOS
Semestre: 2 | Disciplina: Otimização e Pesquisa Operacional (D5)
Unidade: 2 | Aula: 2 - Método Gráfico
---------------------------------------------------------
Objetivo: Resolver um problema de Programação Linear (PL) 
utilizando o Método Gráfico (focado em duas variáveis).

Enunciado do Exercício:
Maximizar Z = 3x1 + 2x2
Sujeito a:
    1x1 + 2x2 <= 12
    2x1 + 3x2 <= 12
    2x1 + 1x2 <= 8
    x1, x2 >= 0
"""

import numpy as np
from scipy.optimize import linprog

def resolver_pl_grafico():
    print("🚀 Iniciando Resolução de Problema de Programação Linear")
    print("📋 Problema: Maximizar Lucro (Z = 3x1 + 2x2)")
    print("-" * 50)

    # Coeficientes da função objetivo (linprog minimiza, então usamos negativo para maximizar)
    c = [-3, -2]

    # Coeficientes das restrições (Lado esquerdo: A_ub * x <= b_ub)
    A = [
        [1, 2],  # x1 + 2x2 <= 12
        [2, 3],  # 2x1 + 3x2 <= 12
        [2, 1]   # 2x1 + x2 <= 8
    ]
    
    # Lado direito das restrições
    b = [12, 12, 8]

    # Limites das variáveis (x1 >= 0, x2 >= 0)
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    # Executando o Simplex (que é o motor por trás, mas validamos os vértices do gráfico)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

    if res.success:
        x1_opt, x2_opt = res.x
        z_opt = -res.fun  # Invertendo o sinal de volta para Maximização
        
        print(f"✅ Solução Ótima Encontrada!")
        print(f"📍 Coordenadas (Vértice Ótimo): x1 = {x1_opt:.2f}, x2 = {x2_opt:.2f}")
        print(f"💰 Lucro Máximo (Z): R$ {z_opt:.2f}")
        
        print("\n🔍 Analisando os Vértices da Região Factível (Método Gráfico):")
        vertices = [
            (0, 0),
            (0, 4),  # Interseção com eixo x2 da restrição 2
            (3, 2),  # Interseção das restrições 2 e 3
            (4, 0)   # Interseção com eixo x1 da restrição 3
        ]
        
        for v in vertices:
            v_z = 3 * v[0] + 2 * v[1]
            status = "⭐ ÓTIMO" if v_z == z_opt else "🔹 Factível"
            print(f"   - Ponto {v}: Z = {v_z} {status}")
            
    else:
        print("❌ Não foi possível encontrar uma solução viável.")

    print("-" * 50)
    print("💡 Insight Data Science: No mundo real, x1 e x2 podem ser recursos limitados ")
    print("   (máquinas, horas, matéria-prima). O método gráfico nos ajuda a visualizar ")
    print("   que a solução ótima SEMPRE estará em um dos vértices da região factível! 📈")

if __name__ == "__main__":
    resolver_pl_grafico()