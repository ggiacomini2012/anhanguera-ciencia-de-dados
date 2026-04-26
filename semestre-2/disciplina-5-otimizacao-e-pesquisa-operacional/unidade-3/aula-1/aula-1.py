# -------------------------------------------------------------------------
# S2-D5-U3-A1: Softwares de Otimização e o Solver do Excel
# Disciplina: Otimização e Pesquisa Operacional
# Objetivo: Resolver o problema da empresa Venix (carrinhos e triciclos)
# -------------------------------------------------------------------------

from scipy.optimize import linprog

def resolver_venix():
    print("🚀 Iniciando Simulação da Produção Venix...")
    
    # Objetivo: Maximizar Lucro Z = 12*x1 + 60*x2
    # Como o linprog faz minimização, usamos valores negativos para maximizar
    c = [-12, -60]

    # Matriz de restrições (Lado esquerdo)
    # 0.25x1 + 0.50x2 <= 36 (Usinagem)
    # 0.10x1 + 0.75x2 <= 22 (Pintura)
    # 0.10x1 + 0.40x2 <= 15 (Montagem)
    A = [
        [0.25, 0.50],
        [0.10, 0.75],
        [0.10, 0.40]
    ]

    # Vetor de restrições (Lado direito - limites de horas)
    b = [36, 22, 15]

    # Limites das variáveis (x1 e x2 >= 0)
    x_bounds = (0, None)
    
    # Resolvendo o problema
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds], method='highs')

    if res.success:
        x1, x2 = res.x
        lucro_maximo = -res.fun
        
        print("\n✅ Solução Ótima Encontrada!")
        print(f"🚗 Quantidade de Carrinhos (x1): {x1:.2f}")
        print(f"🚲 Quantidade de Triciclos (x2): {x2:.2f}")
        print(f"💰 Lucro Total Máximo: R$ {lucro_maximo:.2f}")
        
        print("\n💡 Insight Prático:")
        print("Para atingir o lucro máximo de R$ 2.040,00, a Venix deve focar")
        print("na produção equilibrada de 70 carrinhos e 20 triciclos por semana.")
        print("As restrições de Pintura e Montagem são os gargalos (recursos escassos),")
        print("enquanto a Usinagem possui folga.")
    else:
        print("❌ Não foi possível encontrar uma solução viável.")

if __name__ == "__main__":
    resolver_venix()