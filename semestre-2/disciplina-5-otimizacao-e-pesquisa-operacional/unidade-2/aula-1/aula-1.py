# 📈 Aula: Fundamentos da Programação Linear (PL)
# S2-D5-U2-A1

import numpy as np
from scipy.optimize import linprog

"""
💡 INSIGHT DA AULA:
A Programação Linear é como um 'GPS Financeiro'. Você diz onde quer chegar (Lucro Máximo) 
e quais são os obstáculos (Recursos Limitados), e o algoritmo encontra o caminho matemático exato.
"""

def resolver_exemplo_producao():
    print("🚀 Iniciando Otimização de Produção...")
    
    # Exemplo 1 do material:
    # Maximizar L = 1000*x1 + 1800*x2
    # Como o solver 'linprog' apenas MINIMIZA, multiplicamos os coeficientes por -1
    c = [-1000, -1800]
    
    # Restrições de Desigualdade (A_ub * x <= b_ub)
    # 20*x1 + 30*x2 <= 1200 (Horas de produção)
    A = [[20, 30]]
    b = [1200]
    
    # Limites das variáveis (Bounds)
    # x1 <= 40 (Demanda P1)
    # x2 <= 30 (Demanda P2)
    # x1, x2 >= 0
    x1_bounds = (0, 40)
    x2_bounds = (0, 30)
    
    # Resolvendo o problema usando o método Simplex (mencionado na aula)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='highs')
    
    if res.success:
        print("\n✅ SOLUÇÃO ÓTIMA ENCONTRADA!")
        print(f"📦 Produção de P1: {res.x[0]:.2f} unidades")
        print(f"📦 Produção de P2: {res.x[1]:.2f} unidades")
        print(f"💰 Lucro Total Máximo: R$ {-res.fun:.2f}")
        print("\n💡 INTERPRETAÇÃO:")
        print("Para ganhar o máximo de dinheiro respeitando as 1.200 horas,")
        print("devemos focar nessas quantidades específicas.")
    else:
        print("❌ Não foi possível encontrar uma solução viável.")

def termos_tecnicos():
    print("\n--- 📖 DICIONÁRIO RÁPIDO DO DATA SCIENTIST ---")
    termos = {
        "Variáveis de Decisão": "O que nós controlamos (ex: quanto fabricar) 🕹️",
        "Função-Objetivo": "Nossa meta (ex: lucro máximo) 🎯",
        "Restrições": "Nossos limites (ex: tempo, matéria-prima) 🛑",
        "Simplex": "O algoritmo 'mágico' que resolve tudo 🪄"
    }
    for termo, desc in termos.items():
        print(f"🔹 {termo}: {desc}")

if __name__ == "__main__":
    resolver_exemplo_producao()
    termos_tecnicos()