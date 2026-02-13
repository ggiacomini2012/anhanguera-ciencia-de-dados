# Nome do arquivo: aula-1.py
# Aula 1: Exemplificando Vetores e Segmentos Orientados em Python

import math

class Point:
    """
    Representa um Ponto no espaço 2D (Conceito Primitivo).
    Possui coordenadas x e y.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Retorna uma representação "oficial" do objeto
        return f"Point(x={self.x}, y={self.y})"

class Vector:
    """
    Representa um Vetor (livre) no espaço 2D.
    Um vetor é definido por suas componentes (dx, dy), que representam
    a "ideia" de magnitude, direção e sentido.
    """
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    @classmethod
    def from_points(cls, A, B):
        """
        Método de fábrica para criar um Vetor a partir de um
        SEGMENTO ORIENTADO (de A para B).
        Isso calcula as componentes do vetor.
        """
        # dx = B.x - A.x
        # dy = B.y - A.y
        return cls(B.x - A.x, B.y - A.y)

    def magnitude(self):
        """
        Calcula o MÓDULO (comprimento) do vetor.
        Usa o Teorema de Pitágoras: sqrt(dx^2 + dy^2)
        """
        return math.sqrt(self.dx**2 + self.dy**2)

    def is_null(self):
        """
        Verifica se é um VETOR NULO (módulo zero).
        """
        return self.dx == 0 and self.dy == 0

    def __eq__(self, other):
        """
        Verifica se dois vetores são EQUIPOLENTES.
        Dois vetores são iguais (equipolentes) se suas componentes
        (dx, dy) forem idênticas.
        """
        if not isinstance(other, Vector):
            return False
        return self.dx == other.dx and self.dy == other.dy

    def __repr__(self):
        # Representação do vetor por suas componentes
        return f"Vector(dx={self.dx}, dy={self.dy})"

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    print("--- 📐 Aula 1: Vetores em Python ---")

    # 1. Definindo Pontos
    A = Point(1, 2)
    B = Point(4, 6)
    
    C = Point(5, 1)
    D = Point(8, 5)

    # 2. Criando Vetores a partir de Segmentos Orientados
    # v1 representa o segmento orientado AB
    v1 = Vector.from_points(A, B)
    
    # v2 representa o segmento orientado CD
    v2 = Vector.from_points(C, D)

    print(f"\nSegmento AB: de {A} para {B}")
    print(f"  -> Gera o Vetor v1: {v1}")
    
    print(f"\nSegmento CD: de {C} para {D}")
    print(f"  -> Gera o Vetor v2: {v2}")

    # 3. Verificando Equipolência (Igualdade de Vetores)
    # v1 e v2 têm pontos de partida e chegada diferentes,
    # mas representam o MESMO vetor (dx=3, dy=4).
    print("\n--- Verificando Equipolência ---")
    print(f"v1 e v2 são equipolentes (iguais)? {v1 == v2}")

    # 4. Verificando Segmentos Opostos
    # O segmento BA é oposto ao segmento AB
    v3_oposto = Vector.from_points(B, A)
    print("\n--- Verificando Opostos ---")
    print(f"Segmento BA (oposto de AB): {v3_oposto}")
    print(f"v1 e v3 são opostos? {v1.dx == -v3_oposto.dx and v1.dy == -v3_oposto.dy}")

    # 5. Calculando o Módulo (Magnitude)
    print("\n--- Calculando Módulo ---")
    print(f"Módulo (comprimento) de v1: {v1.magnitude():.2f}") # Deve ser 5.0
    print(f"Módulo (comprimento) de v2: {v2.magnitude():.2f}") # Deve ser 5.0

    # 6. Verificando Vetor Nulo
    E = Point(10, 10)
    v_nulo = Vector.from_points(E, E)
    print("\n--- Verificando Vetor Nulo ---")
    print(f"Vetor do segmento EE: {v_nulo}")
    print(f"v_nulo é um vetor nulo? {v_nulo.is_null()}")