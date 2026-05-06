# ==============================================================================
# S2-D5-U2-A4: O Problema Primal e Dual (Dualidade)
# ==============================================================================

import numpy as np
from scipy.optimize import linprog

# 🏭 O Problema Primal:
# Queremos decidir a produção de P1 e P2 para MAXIMIZAR o Lucro.
# Max Z = 50*x1 + 90*x2
# Sujeito a:
# 2*x1 + 3*x2 <= 300    (Limitação do Recurso 1)
# 10*x1 + 5*x2 <= 1000  (Limitação do Recurso 2)
# x1, x2 >= 0

print("🏭 Problema Primal: Maximização de Lucro na Produção")

# linprog resolve MINIMIZAÇÃO, então invertemos o sinal do lucro
c = [-50, -90] 
A = [[2, 3],
     [10, 5]]
b = [300, 1000]

# Resolvendo com o método 'highs'
res_primal = linprog(c, A_ub=A, b_ub=b, method='highs')

print(f"✅ Produção Ótima:")
print(f"   📦 Produto 1 (P1): {res_primal.x[0]:.2f} unidades")
print(f"   📦 Produto 2 (P2): {res_primal.x[1]:.2f} unidades")
print(f"💰 Lucro Máximo (Z): {-res_primal.fun:.2f}")


# 🔄 Analisando a Solução do Dual:
# A solução do Dual nos dá o valor de oportunidade dos recursos (Preços Sombra / Shadow Prices)
print("\n🔍 Analisando os Preços Sombra (Solução do Dual):")
marginals = res_primal.ineqlin.marginals

print(f"   Recurso 1 (y1): {abs(marginals[0]):.2f} (Valor de Oportunidade por unidade de R1)")
print(f"   Recurso 2 (y2): {abs(marginals[1]):.2f} (Valor de Oportunidade por unidade de R2)")

print("\n💡 Insight Prático:")
print("A solução do problema dual nos informa o valor marginal de cada recurso.")
print("Neste caso, a empresa lucraria R$ 30,00 a mais se tivesse 1 unidade adicional do Recurso 1.")
print("Como o Recurso 2 não foi totalmente utilizado (sobrou na produção), seu valor de oportunidade (preço sombra) é 0.")
