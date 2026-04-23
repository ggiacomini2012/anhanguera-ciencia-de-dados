from scipy.optimize import linprog

# Problema de Programação Linear - Aula 3 (Método Simplex)
# Maximizar Z = 3x1 + 2x2
# Sujeito a:
# x1 + x2 <= 6
# 5x1 + 2x2 <= 20
# x1, x2 >= 0

# Coeficientes da função objetivo (negativos para maximização no scipy)
c = [-3, -2]

# Coeficientes das restrições (lado esquerdo)
A = [
    [1, 1],  # x1 + x2 <= 6
    [5, 2]   # 5x1 + 2x2 <= 20
]

# Valores das restrições (lado direito)
b = [6, 20]

# Limites das variáveis (x1, x2 >= 0)
x_bounds = (0, None)

# Resolvendo usando o método Simplex (o 'highs' é o solver moderno que inclui Simplex)
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds], method='highs')

print("--- Resultado do Método Simplex ---")
print(f"Status: {res.message}")
print(f"Valor ótimo de x1: {res.x[0]:.2f}")
print(f"Valor ótimo de x2: {res.x[1]:.2f}")
print(f"Valor máximo de Z: {-res.fun:.2f}")

# Demonstração das variáveis de folga (slack)
slack_x3 = 6 - (res.x[0] + res.x[1])
slack_x4 = 20 - (5*res.x[0] + 2*res.x[1])

print(f"Variável de folga x3: {slack_x3:.2f}")
print(f"Variável de folga x4: {slack_x4:.2f}")
