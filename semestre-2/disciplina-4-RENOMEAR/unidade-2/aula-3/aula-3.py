import math

# --- Decomposição de Vetores (Problema de Carlos) ---

# Dados de entrada
D = 20  # Módulo do vetor deslocamento (em km)
alpha_graus = 30  # Ângulo em graus (em relação ao eixo Leste, positivo)

# Converter o ângulo para radianos
alpha_rad = math.radians(alpha_graus)

# 1. Cálculo das Componentes (Projeções do vetor nos eixos)
# Componente x (Leste) = D * cos(alpha)
Dx = D * math.cos(alpha_rad)

# Componente y (Norte) = D * sen(alpha)
Dy = D * math.sin(alpha_rad)

# 2. Exibição dos resultados
print("--- Resultados da Decomposição (aula-3.py) ---")
print(f"Módulo do Vetor (D): {D} km")
print(f"Ângulo (alpha): {alpha_graus}°")
print("-" * 40)
print(f"Componente Horizontal (Leste/Dx): {Dx:.2f} km")
print(f"Componente Vertical (Norte/Dy): {Dy:.2f} km")

# 3. Representação Analítica (Base Canônica)
print(f"\nRepresentação Analítica: D = ({Dx:.2f})i + ({Dy:.2f})j")

# 4. Verificação (Teorema de Pitágoras - D² = Dx² + Dy²)
D_verificado = math.sqrt(Dx**2 + Dy**2)
print(f"\nVerificação do Módulo (√Dx² + Dy²): {D_verificado:.2f} km")