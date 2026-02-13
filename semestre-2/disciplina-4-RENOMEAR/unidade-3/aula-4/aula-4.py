import numpy as np

# Função para realizar e exibir o Produto Vetorial (Cross Product)
def calcular_produto_vetorial(v1, v2):
    """
    Calcula o produto vetorial (v1 x v2) e seu módulo.
    O produto vetorial retorna um novo vetor perpendicular aos vetores de entrada.
    """
    # 1. Cálculo do Produto Vetorial (Numpy faz o determinante 3x3 para nós!)
    resultado_vetor = np.cross(v1, v2)

    # 2. Cálculo do Módulo (Tamanho) do vetor resultante
    modulo_resultado = np.linalg.norm(resultado_vetor)

    # 3. Módulo do resultado é a ÁREA do paralelogramo
    area_paralelogramo = modulo_resultado
    area_triangulo = 0.5 * area_paralelogramo

    print(f"--- 1. PRODUTO VETORIAL ({v1} x {v2}) ---")
    print(f"Vetor Resultante (Produto Vetorial): {resultado_vetor}")
    print(f"Módulo do Vetor Resultante (Área do Paralelogramo): {area_paralelogramo:.2f}")
    print(f"Área do Triângulo (Metade do Paralelogramo): {area_triangulo:.2f}")
    print("-" * 40)

    return resultado_vetor

# Função para realizar e exibir o Produto Misto (Triple Scalar Product)
def calcular_produto_misto(v1, v2, v3):
    """
    Calcula o produto misto (v1 . (v2 x v3)).
    O resultado é um escalar (número) que representa o volume.
    """
    print(f"--- 2. PRODUTO MISTO ({v1} . ({v2} x {v3})) ---")

    # 1. Organiza os três vetores em uma matriz 3x3
    matriz = np.array([v1, v2, v3])

    # 2. Calcula o determinante da matriz. O determinante é o Produto Misto.
    # O volume é o valor absoluto (módulo) do determinante.
    produto_misto = np.linalg.det(matriz)
    volume_paralelepipedo = abs(produto_misto)
    volume_tetraedro = volume_paralelepipedo / 6.0

    print(f"Matriz 3x3 (para cálculo do determinante):\n{matriz}")
    print(f"Produto Misto (Determinante): {produto_misto:.2f}")
    print(f"Volume do Paralelepípedo: {volume_paralelepipedo:.2f}")
    print(f"Volume do Tetraedro (1/6 do Paralelepípedo): {volume_tetraedro:.2f}")
    print("-" * 40)

    return volume_paralelepipedo

# --- RESOLUÇÃO DO PROBLEMA DA METALÚRGICA ---

# Vetores que definem as arestas da peça (Paralelepípedo)
VETOR_A = np.array([3, 0, 0])
VETOR_B = np.array([0, 4, 0])
VETOR_C = np.array([0, 0, 5])
QUANTIDADE_PEÇAS = 500

print("### 🛠️ Simulação da Produção da Metalúrgica (Aula 4) 🛠️ ###\n")

# A peça é um Paralelepípedo, então usamos o Módulo do Produto Misto.
# Calculamos o volume de UMA peça
volume_unitario = calcular_produto_misto(VETOR_A, VETOR_B, VETOR_C)

# Cálculo do volume total de aço
volume_total_necessario = volume_unitario * QUANTIDADE_PEÇAS

print(f"\n✅ RESULTADO FINAL (Problema Metalúrgica) ✅")
print(f"Volume de uma única peça (unidade de volume³): {volume_unitario:.2f}")
print(f"Total de peças a serem produzidas: {QUANTIDADE_PEÇAS}")
print(f"Volume total de aço necessário: {volume_total_necessario:.2f} unidades de volume³")

# Exemplo Adicional: Cálculo de um Produto Vetorial Simples (A x B)
print("\n### 🧪 Exemplo Básico de Produto Vetorial (Aplicações em Força/Torque) 🧪 ###")
v_forca = np.array([1, 2, 0]) # Força
v_posicao = np.array([0, 3, 0]) # Posição/Braço
calcular_produto_vetorial(v_forca, v_posicao)