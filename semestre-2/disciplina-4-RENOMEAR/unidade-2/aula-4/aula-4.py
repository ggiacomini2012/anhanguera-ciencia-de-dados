
def checar_dimensao(vetor_a, vetor_b):
    """
    Verifica se dois vetores têm a mesma dimensão (tamanho).
    Essencial para Adição e Subtração.
    """
    if len(vetor_a) != len(vetor_b):
        raise ValueError("Operação inválida: Os vetores devem ter a mesma dimensão.")
    return len(vetor_a)

def adicionar_vetores(vetor_a, vetor_b):
    """
    Soma dois vetores componente por componente (Adição Algébrica).
    Metáfora: Força Resultante ou Deslocamento Final.
    """
    dimensao = checar_dimensao(vetor_a, vetor_b)
    vetor_resultante = []

    # Iteramos sobre cada par de componentes (x, y, z...)
    for i in range(dimensao):
        componente_soma = vetor_a[i] + vetor_b[i]
        vetor_resultante.append(componente_soma)

    return vetor_resultante

def subtrair_vetores(vetor_a, vetor_b):
    """
    Subtrai o vetor_b do vetor_a (v_a - v_b).
    É o mesmo que v_a + (-v_b).
    """
    dimensao = checar_dimensao(vetor_a, vetor_b)
    vetor_resultante = []

    # Iteramos sobre cada par de componentes (x, y, z...)
    for i in range(dimensao):
        componente_subtracao = vetor_a[i] - vetor_b[i]
        vetor_resultante.append(componente_subtracao)

    return vetor_resultante

def multiplicar_por_escalar(escalar, vetor):
    """
    Multiplica cada componente do vetor por um número real (escalar).
    Metáfora: 'Esticar' ou 'Encolher' o vetor.
    """
    vetor_resultante = []

    for componente in vetor:
        # k * u = (k*u_x, k*u_y, k*u_z, ...)
        componente_multiplicada = escalar * componente
        vetor_resultante.append(componente_multiplicada)

    return vetor_resultante

# ------------------------------------------------------------------
# 📌 EXEMPLOS PRÁTICOS
# ------------------------------------------------------------------

# Vetores de Exemplo (3D - R3)
u = [3, 5, 2] # Ex: Deslocamento (3m leste, 5m norte, 2m para cima)
v = [7, 6, -1] # Ex: Outro deslocamento ou Força

print("Vetor u: ", u)
print("Vetor v: ", v)
print("-" * 30)

# 1. Adição de Vetores (u + v)
r_soma = adicionar_vetores(u, v)
print(f"Soma (u + v): {r_soma}")
# Resultado Esperado: [3+7, 5+6, 2+(-1)] = [10, 11, 1]

# 2. Subtração de Vetores (u - v)
r_subtracao = subtrair_vetores(u, v)
print(f"Subtração (u - v): {r_subtracao}")
# Resultado Esperado: [3-7, 5-6, 2-(-1)] = [-4, -1, 3]

# 3. Multiplicação por Escalar (k * u)
k = 2.5 # O Escalar (número real)
r_multiplicacao = multiplicar_por_escalar(k, u)
print(f"Multiplicação (2.5 * u): {r_multiplicacao}")
# Resultado Esperado: [2.5*3, 2.5*5, 2.5*2] = [7.5, 12.5, 5.0]

# 4. Multiplicação por Escalar Negativo (-2 * v)
k_neg = -2
r_oposto_escalonado = multiplicar_por_escalar(k_neg, v)
print(f"Multiplicação (-2 * v - Inverte o Sentido): {r_oposto_escalonado}")
# Resultado Esperado: [-2*7, -2*6, -2*-1] = [-14, -12, 2]

# Exemplo de erro (dimensões diferentes)
# w = [1, 2]
# try:
#     adicionar_vetores(u, w)
# except ValueError as e:
#     print("\nErro de Dimensão (Esperado):", e)