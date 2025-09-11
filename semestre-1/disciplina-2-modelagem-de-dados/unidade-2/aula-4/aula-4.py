"""
Arquivo: aula-4.py

Descrição:
Este script Python demonstra conceitos de modelagem de dados, como
entidades, cardinalidade e chaves, utilizando uma abordagem orientada
a objetos para simular um sistema de gerenciamento de biblioteca.
Ele representa entidades como `Livro` e `Area`, e mostra como elas
se relacionam. A classe `Livro` tem uma chave estrangeira (`id_area`)
que se conecta à chave primária da classe `Area`.

O script também simula a inserção de dados e a recuperação de
informações, ilustrando como as chaves estrangeiras ajudam a
relacionar dados entre diferentes "tabelas" (classes).
"""

class Area:
    """
    Representa a entidade forte 'Area' (ex: "Ficção", "História").
    Cada área possui um ID único que serve como chave primária.
    """
    def __init__(self, id_area, nome_area):
        self.id_area = id_area  # Chave primária
        self.nome_area = nome_area

    def __str__(self):
        return f"Área: {self.nome_area} (ID: {self.id_area})"

class Livro:
    """
    Representa a entidade fraca 'Livro', que depende da entidade 'Area'.
    Um livro não pode existir sem estar associado a uma área.
    """
    def __init__(self, id_livro, titulo, autor, id_area):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.id_area = id_area  # Chave estrangeira, referencia Area.id_area

    def __str__(self):
        return f"Livro: '{self.titulo}' por {self.autor}"


# --- Simulação de uso ---
# Criação de "tabelas" (listas de objetos)
tabela_areas = []
tabela_livros = []

# Popula a "tabela" de áreas (entidades fortes)
ficcao = Area(id_area=1, nome_area="Ficção Científica")
fantasia = Area(id_area=2, nome_area="Fantasia")
tabela_areas.extend([ficcao, fantasia])

# Popula a "tabela" de livros (entidades fracas)
# A chave estrangeira `id_area` conecta o livro à sua área correspondente.
livro1 = Livro(id_livro=101, titulo="Duna", autor="Frank Herbert", id_area=1)
livro2 = Livro(id_livro=102, titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", id_area=2)
livro3 = Livro(id_livro=103, titulo="Neuromancer", autor="William Gibson", id_area=1)
tabela_livros.extend([livro1, livro2, livro3])

# Demonstração de um relacionamento 1:M (Um para Muitos)
# Uma Área (`id_area`) pode ter muitos Livros.
# Um Livro tem apenas uma Área.
print("--- Relacionamento 1:M (Uma Área tem Muitos Livros) ---")

for area in tabela_areas:
    print(f"\nLivros na área: {area.nome_area}")
    for livro in tabela_livros:
        # A chave estrangeira é usada para encontrar os livros da área
        if livro.id_area == area.id_area:
            print(f"  - {livro.titulo}")

# Demonstração de como as chaves funcionam
print("\n--- Demonstração de Chaves ---")

# Acessando o livro diretamente por sua "chave primária"
livro_desejado = next((livro for livro in tabela_livros if livro.id_livro == 102), None)
if livro_desejado:
    print(f"Livro com ID 102: '{livro_desejado.titulo}'")

# Acessando a área de um livro usando a "chave estrangeira"
area_do_livro = next((area for area in tabela_areas if area.id_area == livro_desejado.id_area), None)
if area_do_livro:
    print(f"Este livro pertence à área: {area_do_livro.nome_area}")