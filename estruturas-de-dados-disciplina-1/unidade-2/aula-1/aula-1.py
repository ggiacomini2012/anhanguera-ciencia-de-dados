# -*- coding: utf-8 -*-

"""
================================================================================
ARQUIVO DE ESTUDO: ESTRUTURAS DE DADOS EM ÁRVORE E PYTHON
================================================================================
Objetivo:
Este arquivo serve como um exemplo prático da aula sobre estruturas de dados
em árvore, aplicando os conceitos na criação de um sistema de recomendação
de filmes (MVP) baseado em classificação etária.

Conteúdo:
1.  Implementação do MVP usando um dicionário (uma forma simples de árvore).
2.  (Opcional Avançado) Implementação usando Classes para uma estrutura de árvore mais formal.
3.  Exercícios práticos para fixar o conhecimento.
4.  Soluções dos exercícios.
================================================================================
"""

# ------------------------------------------------------------------------------
# PARTE 1: IMPLEMENTAÇÃO DO MVP COM DICIONÁRIO
# ------------------------------------------------------------------------------
# Para o nosso MVP, um dicionário é uma excelente escolha. É simples, legível e
# representa perfeitamente a relação hierárquica que precisamos: cada chave
# (classificação) possui uma lista de valores (filmes).

print("="*60)
print(" PARTE 1: MVP COM DICIONÁRIO ".center(60, "="))
print("="*60)


# A nossa "árvore" de dados. As chaves são a idade mínima da classificação.
filmes_por_classificacao = {
    0: [
        "O Rei Leão",
        "Meu Malvado Favorito",
        "Procurando Nemo"
    ],
    10: [
        "Harry Potter e a Pedra Filosofal",
        "Shrek",
        "Homem-Aranha no Aranhaverso"
    ],
    12: [
        "Os Vingadores (The Avengers)",
        "O Senhor dos Anéis: A Sociedade do Anel",
        "Piratas do Caribe: A Maldição do Pérola Negra"
    ],
    14: [
        "Batman: O Cavaleiro das Trevas",
        "Interestelar",
        "A Origem (Inception)"
    ],
    16: [
        "Coringa (Joker)",
        "Matrix",
        "Clube da Luta"
    ],
    18: [
        "O Poderoso Chefão",
        "Pulp Fiction: Tempo de Violência",
        "Cães de Aluguel"
    ]
}

def recomendar_filmes_mvp(idade_usuario):
    """
    Recomenda filmes de todas as classificações permitidas para a idade.
    """
    filmes_recomendados = []
    print(f"\n>>> Buscando recomendações para um usuário de {idade_usuario} anos...")

    # Percorre cada nó de categoria (classificação) na nossa árvore.
    for classificacao, filmes in filmes_por_classificacao.items():
        if idade_usuario >= classificacao:
            # Se o usuário tem idade para a categoria, adiciona os filmes.
            filmes_recomendados.extend(filmes)

    return filmes_recomendados

# --- Demonstração de uso ---
idade_exemplo = 13
recomendacoes = recomendar_filmes_mvp(idade_exemplo)
print(f"\nPara {idade_exemplo} anos, recomendamos os seguintes {len(recomendacoes)} filmes:")
for filme in recomendacoes:
    print(f"  - {filme}")


# ------------------------------------------------------------------------------
# PARTE 2: (AVANÇADO) ESTRUTURA COM CLASSES
# ------------------------------------------------------------------------------
# Conforme o sistema cresce, usar classes pode deixar o código mais organizado
# e extensível. Aqui, cada parte da árvore (nó) é um objeto.

print("\n\n" + "="*60)
print(" PARTE 2: ESTRUTURA COM CLASSES (AVANÇADO) ".center(60, "="))
print("="*60)

class No:
    """Representa um nó na nossa árvore, que pode ser uma categoria ou um filme."""
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, no_filho):
        self.filhos.append(no_filho)

# Construindo a árvore com objetos
raiz = No("Catálogo de Filmes")

# Criando nós de categoria e adicionando-os à raiz
for idade_min, lista_filmes in filmes_por_classificacao.items():
    # O valor do nó de categoria será a própria idade mínima
    no_categoria = No(idade_min)
    raiz.adicionar_filho(no_categoria)
    # Adicionando os filmes como filhos do nó de categoria
    for titulo_filme in lista_filmes:
        no_filme = No(titulo_filme)
        no_categoria.adicionar_filho(no_filme)


def recomendar_filmes_com_classes(idade_usuario, no_raiz):
    """
    Percorre a árvore de classes para encontrar filmes recomendados.
    """
    filmes_recomendados = []
    # Percorre os nós de categoria (filhos da raiz)
    for no_categoria in no_raiz.filhos:
        # O valor do nó de categoria é a idade (ex: 0, 10, 12)
        if idade_usuario >= no_categoria.valor:
            # Se tem idade, percorre os filhos deste nó (os filmes)
            for no_filme in no_categoria.filhos:
                filmes_recomendados.append(no_filme.valor)
    return filmes_recomendados

# --- Demonstração de uso ---
idade_exemplo_2 = 17
print(f"\n>>> Buscando recomendações para {idade_exemplo_2} anos usando a árvore de classes...")
recomendacoes_classes = recomendar_filmes_com_classes(idade_exemplo_2, raiz)
print(f"\nPara {idade_exemplo_2} anos, recomendamos os seguintes {len(recomendacoes_classes)} filmes:")
for filme in recomendacoes_classes:
    print(f"  - {filme}")


# ------------------------------------------------------------------------------
# PARTE 3: EXERCÍCIOS
# ------------------------------------------------------------------------------
# Agora é sua vez! Tente resolver os exercícios abaixo.
# As respostas estão na PARTE 4, mas tente primeiro sem olhar!

print("\n\n" + "="*60)
print(" PARTE 3: EXERCÍCIOS ".center(60, "="))
print("="*60)

# -------------------------------------------------
# EXERCÍCIO 1: Adicionar um novo filme
# -------------------------------------------------
# Adicione o filme "Divertidamente" à categoria "Livre" (chave 0) no
# dicionário 'filmes_por_classificacao'.
# Depois, imprima apenas a lista de filmes da categoria 0 para confirmar.

print("\n--- Exercício 1: Adicionar um filme ---")
# ESCREVA SEU CÓDIGO AQUI


# -------------------------------------------------
# EXERCÍCIO 2: Contar os resultados
# -------------------------------------------------
# Crie uma nova função chamada `recomendar_e_contar` que seja uma cópia
# da `recomendar_filmes_mvp`, mas que, ao final, retorne uma TUPLA
# contendo a lista de filmes E o número total de filmes.
# Exemplo de retorno: (['filme1', 'filme2'], 2)

print("\n--- Exercício 2: Contar os resultados ---")
# ESCREVA SUA FUNÇÃO E O CÓDIGO DE TESTE AQUI


# -------------------------------------------------
# EXERCÍCIO 3: Adicionar uma nova categoria
# -------------------------------------------------
# O sistema de classificação mudou! Adicione uma nova categoria para filmes
# com classificação "a partir de 8 anos". Adicione pelo menos dois filmes
# a esta nova categoria no dicionário `filmes_por_classificacao`.
# Em seguida, teste a função `recomendar_filmes_mvp` com a idade 9.

print("\n--- Exercício 3: Adicionar uma categoria ---")
# ESCREVA SEU CÓDIGO AQUI


# -------------------------------------------------
# EXERCÍCIO 4: Sugerir a próxima categoria
# -------------------------------------------------
# Crie uma função `sugerir_proxima_categoria(idade_usuario)` que mostra ao
# usuário qual a próxima classificação etária que ele poderá assistir e
# quais filmes estarão disponíveis.
# Exemplo: para um usuário de 13 anos, a função deve indicar que a próxima
# categoria é "14 anos" e listar os filmes dela.
# Dica: Você precisará ordenar as chaves do dicionário.

print("\n--- Exercício 4: Sugerir a próxima categoria ---")
# ESCREVA SUA FUNÇÃO E O CÓDIGO DE TESTE AQUI


# ------------------------------------------------------------------------------
# PARTE 4: RESPOSTAS DOS EXERCÍCIOS
# ------------------------------------------------------------------------------
# Verifique aqui se você acertou!

print("\n\n" + "="*60)
print(" PARTE 4: RESPOSTAS DOS EXERCÍCIOS ".center(60, "="))
print("="*60)

# -------------------------------------------------
# SOLUÇÃO DO EXERCÍCIO 1
# -------------------------------------------------
print("\n--- Solução do Exercício 1 ---")
filmes_por_classificacao[0].append("Divertidamente")
print("Lista de filmes 'Livre' atualizada:")
print(filmes_por_classificacao[0])


# -------------------------------------------------
# SOLUÇÃO DO EXERCÍCIO 2
# -------------------------------------------------
print("\n--- Solução do Exercício 2 ---")
def recomendar_e_contar(idade_usuario):
    filmes_recomendados = []
    for classificacao, filmes in filmes_por_classificacao.items():
        if idade_usuario >= classificacao:
            filmes_recomendados.extend(filmes)
    # Retorna a lista e também o seu tamanho (len)
    return (filmes_recomendados, len(filmes_recomendados))

# Teste da função
lista, contagem = recomendar_e_contar(12)
print(f"Para 12 anos, foram encontrados {contagem} filmes.")


# -------------------------------------------------
# SOLUÇÃO DO EXERCÍCIO 3
# -------------------------------------------------
print("\n--- Solução do Exercício 3 ---")
# Adicionando a nova chave e a lista de filmes
filmes_por_classificacao[8] = ["As Crônicas de Nárnia", "E.T. - O Extraterrestre"]
print("Dicionário atualizado com a categoria 8 anos.")

# Testando a recomendação para 9 anos
recomendacoes_9_anos = recomendar_filmes_mvp(9)
print(f"\nRecomendações para 9 anos ({len(recomendacoes_9_anos)} filmes):")
print(recomendacoes_9_anos)


# -------------------------------------------------
# SOLUÇÃO DO EXERCÍCIO 4
# -------------------------------------------------
print("\n--- Solução do Exercício 4 ---")
def sugerir_proxima_categoria(idade_usuario):
    # Pega todas as classificações e as ordena de forma crescente
    classificacoes_ordenadas = sorted(filmes_por_classificacao.keys())

    for classificacao in classificacoes_ordenadas:
        if idade_usuario < classificacao:
            proxima_classificacao = classificacao
            filmes_da_proxima = filmes_por_classificacao[proxima_classificacao]

            print(f"\nQuando você tiver {proxima_classificacao} anos, poderá assistir a:")
            for filme in filmes_da_proxima:
                print(f"  - {filme}")
            return # Para a função após encontrar a primeira categoria superior

    print("\nVocê já tem idade para assistir a todas as categorias de filmes!")

# Teste da função
print("Sugestão para alguém com 13 anos:")
sugerir_proxima_categoria(13)

print("\nSugestão para alguém com 16 anos:")
sugerir_proxima_categoria(16)

print("\nSugestão para alguém com 25 anos:")
sugerir_proxima_categoria(25)

print("\n\n" + "="*60)
print(" FIM DO ESTUDO ".center(60, "="))
print("="*60)