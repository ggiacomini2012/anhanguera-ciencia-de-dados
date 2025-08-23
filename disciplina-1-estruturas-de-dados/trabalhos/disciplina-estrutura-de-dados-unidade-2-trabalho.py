"""
Aqui está a atividade/trabalho da Unidade 2 da disciplina de Estrutura de Dados.
Deixarei comentários no código para deixar mais claro tanto o raciocínio da 
implementação quanto a lógica por trás das Árvores AVL.
"""

# ---------------------------------
# ATIVIDADE PROPOSTA
# ---------------------------------
# Você foi contratado como um desenvolvedor de software para um novo jogo de 
# Pokémon e recebeu a tarefa de implementar um sistema eficiente de gerenciamento 
# de Pokémon utilizando uma Árvore AVL. Cada Pokémon no jogo é caracterizado 
# por um nome e um valor de força, que é um número inteiro.

# ---------------------------------
# Objetivos do Exercício
# ---------------------------------

# 1. Implementação da Árvore AVL:
#    - Implemente uma Árvore AVL que armazene informações sobre cada Pokémon. 
#      Os nós da árvore devem conter o nome do Pokémon e seu valor de força. 
#      A árvore será ordenada pelo nome.

# 2. Funcionalidade de Busca:
#    - Desenvolva uma função para buscar Pokémon na árvore pelo nome. Esta função 
#      deve retornar as informações do Pokémon se ele for encontrado.

# 3. Funcionalidade de Listagem:
#    - Crie uma função para listar todos os Pokémon da árvore em ordem 
#      decrescente de força. Isso permitirá que os jogadores vejam os 
#      Pokémon mais fortes primeiro.

# 4. Funcionalidade de Remoção:
#    - Implemente uma função para remover Pokémon da árvore por nome, garantindo 
#      que a árvore se mantenha balanceada após a remoção.

# ---------------------------------
# CÓDIGO PARA A ATIVIDADE
# ---------------------------------

# - PokemonNode: A classe que define a estrutura de cada nó da árvore.

# - AVLTree: A classe principal que contém toda a lógica da árvore, incluindo:
#     - Funções auxiliares para altura e balanceamento.
#     - As rotações (_rotacao_direita e _rotacao_esquerda) que são o coração 
#       do balanceamento.
#     - As funções principais (inserir, remover, buscar, 
#       listar_em_ordem_decrescente_forca).

# - Programa Principal (if __name__ == "__main__":): 
#     Uma seção para testar todas as funcionalidades implementadas, mostrando 
#     que a árvore funciona como esperado.


class PokemonNode:
    """
    Classe que representa um nó na Árvore AVL.
    Cada nó armazena os dados de um Pokémon e a altura da sub-árvore.
    A chave para a ordenação da árvore será o nome do Pokémon.
    """
    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca
        self.altura = 1
        self.esquerda = None
        self.direita = None

class AVLTree:
    """
    Classe que implementa a Árvore AVL com as funcionalidades
    de inserção, remoção, busca e listagem de Pokémon.
    """

    # --- Funções Auxiliares da Árvore ---

    def get_altura(self, no):
        """Retorna a altura de um nó (0 se o nó for nulo)."""
        if not no:
            return 0
        return no.altura

    def get_balanco(self, no):
        """Calcula o fator de balanceamento de um nó."""
        if not no:
            return 0
        return self.get_altura(no.esquerda) - self.get_altura(no.direita)

    def get_min_valor_no(self, no):
        """Encontra o nó com o menor valor (nome) em uma sub-árvore."""
        if no is None or no.esquerda is None:
            return no
        return self.get_min_valor_no(no.esquerda)

    # --- Rotações da Árvore AVL ---

    def _rotacao_direita(self, z):
        """Executa uma rotação simples à direita."""
        print(f"Executando rotação à direita no nó: {z.nome}")
        y = z.esquerda
        T3 = y.direita

        # Realiza a rotação
        y.direita = z
        z.esquerda = T3

        # Atualiza as alturas
        z.altura = 1 + max(self.get_altura(z.esquerda), self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda), self.get_altura(y.direita))

        return y

    def _rotacao_esquerda(self, z):
        """Executa uma rotação simples à esquerda."""
        print(f"Executando rotação à esquerda no nó: {z.nome}")
        y = z.direita
        T2 = y.esquerda

        # Realiza a rotação
        y.esquerda = z
        z.direita = T2

        # Atualiza as alturas
        z.altura = 1 + max(self.get_altura(z.esquerda), self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda), self.get_altura(y.direita))

        return y

    # --- Funcionalidades Principais ---

    def inserir(self, raiz, nome, forca):
        """Insere um novo Pokémon na árvore e a balanceia."""
        # 1. Inserção padrão de uma Árvore de Busca Binária
        if not raiz:
            return PokemonNode(nome, forca)
        elif nome < raiz.nome:
            raiz.esquerda = self.inserir(raiz.esquerda, nome, forca)
        else:
            raiz.direita = self.inserir(raiz.direita, nome, forca)

        # 2. Atualiza a altura do nó ancestral
        raiz.altura = 1 + max(self.get_altura(raiz.esquerda), self.get_altura(raiz.direita))

        # 3. Calcula o fator de balanceamento e aplica as rotações se necessário
        balanco = self.get_balanco(raiz)

        # Caso Esquerda-Esquerda
        if balanco > 1 and nome < raiz.esquerda.nome:
            return self._rotacao_direita(raiz)

        # Caso Direita-Direita
        if balanco < -1 and nome > raiz.direita.nome:
            return self._rotacao_esquerda(raiz)

        # Caso Esquerda-Direita
        if balanco > 1 and nome > raiz.esquerda.nome:
            raiz.esquerda = self._rotacao_esquerda(raiz.esquerda)
            return self._rotacao_direita(raiz)

        # Caso Direita-Esquerda
        if balanco < -1 and nome < raiz.direita.nome:
            raiz.direita = self._rotacao_direita(raiz.direita)
            return self._rotacao_esquerda(raiz)

        return raiz

    def remover(self, raiz, nome):
        """Remove um Pokémon da árvore pelo nome e a balanceia."""
        # 1. Remoção padrão de uma Árvore de Busca Binária
        if not raiz:
            return raiz

        if nome < raiz.nome:
            raiz.esquerda = self.remover(raiz.esquerda, nome)
        elif nome > raiz.nome:
            raiz.direita = self.remover(raiz.direita, nome)
        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp
            
            temp = self.get_min_valor_no(raiz.direita)
            raiz.nome = temp.nome
            raiz.forca = temp.forca
            raiz.direita = self.remover(raiz.direita, temp.nome)

        if raiz is None:
            return raiz

        # 2. Atualiza a altura e rebalanceia a árvore
        raiz.altura = 1 + max(self.get_altura(raiz.esquerda), self.get_altura(raiz.direita))
        balanco = self.get_balanco(raiz)

        # Casos de rebalanceamento (semelhantes à inserção)
        # Caso Esquerda-Esquerda
        if balanco > 1 and self.get_balanco(raiz.esquerda) >= 0:
            return self._rotacao_direita(raiz)
        # Caso Esquerda-Direita
        if balanco > 1 and self.get_balanco(raiz.esquerda) < 0:
            raiz.esquerda = self._rotacao_esquerda(raiz.esquerda)
            return self._rotacao_direita(raiz)
        # Caso Direita-Direita
        if balanco < -1 and self.get_balanco(raiz.direita) <= 0:
            return self._rotacao_esquerda(raiz)
        # Caso Direita-Esquerda
        if balanco < -1 and self.get_balanco(raiz.direita) > 0:
            raiz.direita = self._rotacao_direita(raiz.direita)
            return self._rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, nome):
        """Busca um Pokémon pelo nome e retorna o nó se encontrado."""
        if raiz is None or raiz.nome == nome:
            return raiz
        
        if nome < raiz.nome:
            return self.buscar(raiz.esquerda, nome)
        else:
            return self.buscar(raiz.direita, nome)

    def listar_em_ordem_decrescente_forca(self, raiz):
        """
        Retorna uma lista de todos os Pokémon ordenados pela força, do maior para o menor.
        A árvore é ordenada por nome, então precisamos coletar todos e depois ordenar.
        """
        pokemons = []
        self._coletar_todos_pokemons(raiz, pokemons)
        
        # Ordena a lista de pokémons pela força em ordem decrescente
        pokemons.sort(key=lambda p: p.forca, reverse=True)
        
        return pokemons

    def _coletar_todos_pokemons(self, no, lista):
        """Função auxiliar recursiva para percorrer a árvore e coletar todos os nós."""
        if no:
            self._coletar_todos_pokemons(no.esquerda, lista)
            lista.append(no)
            self._coletar_todos_pokemons(no.direita, lista)
            
    def imprimir_arvore(self, no, nivel=0, prefixo="Raiz:"):
        """Imprime a estrutura da árvore no console."""
        if no is not None:
            print(" " * (nivel * 4) + prefixo + no.nome + f" (Força: {no.forca}, Altura: {no.altura})")
            if no.esquerda is not None or no.direita is not None:
                self.imprimir_arvore(no.esquerda, nivel + 1, "E---")
                self.imprimir_arvore(no.direita, nivel + 1, "D---")


# --- Programa Principal e Testes ---
if __name__ == "__main__":
    pokedex_avl = AVLTree()
    raiz = None

    # Inserindo Pokémon
    pokemons_para_inserir = [
        ("Pikachu", 90), ("Charizard", 120), ("Bulbasaur", 80),
        ("Squirtle", 85), ("Mewtwo", 150), ("Gengar", 110),
        ("Alakazam", 130)
    ]
    
    print("--- INSERINDO POKÉMON ---")
    for nome, forca in pokemons_para_inserir:
        print(f"\nInserindo {nome}...")
        raiz = pokedex_avl.inserir(raiz, nome, forca)
        pokedex_avl.imprimir_arvore(raiz)
        print("-" * 20)

    print("\n\n--- ESTRUTURA FINAL DA ÁRVORE ---")
    pokedex_avl.imprimir_arvore(raiz)

    # Teste de Busca
    print("\n\n--- TESTANDO BUSCA POR NOME ---")
    nome_busca = "Mewtwo"
    pokemon_encontrado = pokedex_avl.buscar(raiz, nome_busca)
    if pokemon_encontrado:
        print(f"Pokémon '{nome_busca}' encontrado! Força: {pokemon_encontrado.forca}")
    else:
        print(f"Pokémon '{nome_busca}' não encontrado.")
        
    nome_busca = "Ditto"
    pokemon_encontrado = pokedex_avl.buscar(raiz, nome_busca)
    if pokemon_encontrado:
        print(f"Pokémon '{nome_busca}' encontrado! Força: {pokemon_encontrado.forca}")
    else:
        print(f"Pokémon '{nome_busca}' não encontrado.")

    # Teste de Listagem por Força
    print("\n\n--- LISTANDO POKÉMON POR ORDEM DECRESCENTE DE FORÇA ---")
    lista_fortes = pokedex_avl.listar_em_ordem_decrescente_forca(raiz)
    for pokemon in lista_fortes:
        print(f"- {pokemon.nome} (Força: {pokemon.forca})")

    # Teste de Remoção
    print("\n\n--- TESTANDO REMOÇÃO ---")
    nome_remover = "Bulbasaur"
    print(f"\nRemovendo '{nome_remover}'...")
    raiz = pokedex_avl.remover(raiz, nome_remover)
    pokedex_avl.imprimir_arvore(raiz)
    
    nome_remover = "Charizard"
    print(f"\nRemovendo '{nome_remover}'...")
    raiz = pokedex_avl.remover(raiz, nome_remover)
    pokedex_avl.imprimir_arvore(raiz)
