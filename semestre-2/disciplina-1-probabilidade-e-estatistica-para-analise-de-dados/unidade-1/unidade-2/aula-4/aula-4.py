class VerticeAVL:
    """
    Representa um nó (ou vértice) em uma Árvore AVL.
    No contexto do nosso exercício, cada vértice armazena o ID de um livro.
    """

    def __init__(self, chave, pai=None):
        """
        Construtor: inicializa um vértice com uma chave (ID do livro),
        pai e subárvores esquerda e direita vazias.
        """
        self.chave = chave
        self.pai = pai
        self.esquerdo = None
        self.direito = None
        # A altura de um novo nó (folha) é 0.
        self._altura = 0

    def __str__(self):
        return str(self.chave)

    def __repr__(self):
        return str(self.chave)

    # --- Propriedades para Altura e Balanceamento ---

    @property
    def altura(self):
        """Retorna a altura do nó."""
        return self._altura

    def atualizar_altura(self):
        """
        Recalcula a altura de um nó.
        A altura é 1 + a maior altura entre as subárvores esquerda e direita.
        """
        alt_esq = self.esquerdo.altura if self.esquerdo else -1
        alt_dir = self.direito.altura if self.direito else -1
        self._altura = 1 + max(alt_esq, alt_dir)

    @property
    def fator_de_balanceamento(self):
        """
        Calcula o fator de balanceamento do nó.
        Fator = Altura(Subárvore Direita) - Altura(Subárvore Esquerda)
        """
        alt_esq = self.esquerdo.altura if self.esquerdo else -1
        alt_dir = self.direito.altura if self.direito else -1
        return alt_dir - alt_esq

    # --- Rotações e Balanceamento ---

    def balancear(self):
        """
        Verifica o fator de balanceamento e aplica as rotações necessárias
        para manter a propriedade da árvore AVL. Retorna a nova raiz da subárvore.
        """
        fb = self.fator_de_balanceamento

        # Árvore mais pesada à DIREITA (fb = 2)
        if fb == 2:
            # Caso RL (Direita-Esquerda): O filho direito está pesado à esquerda
            if self.direito and self.direito.fator_de_balanceamento < 0:
                print(f"-> Desbalanceamento detectado no nó {self.chave}. Caso RL.")
                print(f"   1. Rotação à DIREITA no filho ({self.direito.chave})")
                self.direito = self.direito._rotacao_para_direita()
            # Caso RR (Direita-Direita)
            print(f"-> Desbalanceamento detectado no nó {self.chave}. Caso RR.")
            print(f"   2. Rotação à ESQUERDA no nó ({self.chave})")
            return self._rotacao_para_esquerda()

        # Árvore mais pesada à ESQUERDA (fb = -2)
        if fb == -2:
            # Caso LR (Esquerda-Direita): O filho esquerdo está pesado à direita
            if self.esquerdo and self.esquerdo.fator_de_balanceamento > 0:
                print(f"-> Desbalanceamento detectado no nó {self.chave}. Caso LR.")
                print(f"   1. Rotação à ESQUERDA no filho ({self.esquerdo.chave})")
                self.esquerdo = self.esquerdo._rotacao_para_esquerda()
            # Caso LL (Esquerda-Esquerda)
            print(f"-> Desbalanceamento detectado no nó {self.chave}. Caso LL.")
            print(f"   2. Rotação à DIREITA no nó ({self.chave})")
            return self._rotacao_para_direita()

        # Se o nó já está balanceado, retorna ele mesmo.
        return self

    def _rotacao_para_esquerda(self):
        """Executa uma rotação simples à esquerda (usada nos casos RR e LR)."""
        nova_raiz = self.direito
        self.direito = nova_raiz.esquerdo

        if nova_raiz.esquerdo:
            nova_raiz.esquerdo.pai = self

        nova_raiz.pai = self.pai
        if not self.pai:
            # Se self era a raiz da árvore, agora nova_raiz é.
            pass
        elif self == self.pai.esquerdo:
            self.pai.esquerdo = nova_raiz
        else:
            self.pai.direito = nova_raiz
        
        nova_raiz.esquerdo = self
        self.pai = nova_raiz

        # Atualiza alturas (ordem é importante: primeiro o filho, depois a nova raiz)
        self.atualizar_altura()
        nova_raiz.atualizar_altura()

        return nova_raiz

    def _rotacao_para_direita(self):
        """Executa uma rotação simples à direita (usada nos casos LL e RL)."""
        nova_raiz = self.esquerdo
        self.esquerdo = nova_raiz.direito

        if nova_raiz.direito:
            nova_raiz.direito.pai = self

        nova_raiz.pai = self.pai
        if not self.pai:
            pass
        elif self == self.pai.direito:
            self.pai.direito = nova_raiz
        else:
            self.pai.esquerdo = nova_raiz

        nova_raiz.direito = self
        self.pai = nova_raiz

        # Atualiza alturas
        self.atualizar_altura()
        nova_raiz.atualizar_altura()

        return nova_raiz

class ArvoreAVL:
    """
    Classe que gerencia a Árvore AVL como um todo,
    mantendo uma referência para a raiz.
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        """Insere uma chave na árvore e atualiza a raiz se necessário."""
        print(f"\n--- Inserindo livro com ID: {chave} ---")
        if not self.raiz:
            self.raiz = VerticeAVL(chave)
        else:
            self.raiz = self._inserir_recursivo(self.raiz, chave)
        
        print("Árvore resultante:")
        self.imprimir()

    def _inserir_recursivo(self, no_atual, chave):
        """Método auxiliar para inserção recursiva."""
        if not no_atual:
            return VerticeAVL(chave)
        
        if chave < no_atual.chave:
            no_atual.esquerdo = self._inserir_recursivo(no_atual.esquerdo, chave)
            no_atual.esquerdo.pai = no_atual
        elif chave > no_atual.chave:
            no_atual.direito = self._inserir_recursivo(no_atual.direito, chave)
            no_atual.direito.pai = no_atual
        else:
            # Chave já existe, não faz nada.
            return no_atual

        # Atualiza a altura do nó ancestral
        no_atual.atualizar_altura()

        # Balanceia a árvore a partir deste nó e retorna a nova raiz da subárvore
        return no_atual.balancear()

    def buscar(self, chave):
        """Busca por uma chave na árvore."""
        print(f"\n--- Buscando livro com ID: {chave} ---")
        no_encontrado = self._buscar_recursivo(self.raiz, chave)
        if no_encontrado:
            print(f"Livro com ID {chave} ENCONTRADO!")
            return no_encontrado
        else:
            print(f"Livro com ID {chave} NÃO encontrado.")
            return None

    def _buscar_recursivo(self, no_atual, chave):
        if not no_atual or no_atual.chave == chave:
            return no_atual
        if chave < no_atual.chave:
            return self._buscar_recursivo(no_atual.esquerdo, chave)
        return self._buscar_recursivo(no_atual.direito, chave)
    
    def remover(self, chave):
        """Remove um nó da árvore."""
        print(f"\n--- Removendo livro com ID: {chave} ---")
        if not self.raiz:
            print("Árvore vazia, nada para remover.")
            return
        self.raiz = self._remover_recursivo(self.raiz, chave)
        print("Árvore resultante:")
        self.imprimir()

    def _remover_recursivo(self, no_atual, chave):
        if not no_atual:
            return no_atual

        # 1. Encontrar o nó a ser removido
        if chave < no_atual.chave:
            no_atual.esquerdo = self._remover_recursivo(no_atual.esquerdo, chave)
        elif chave > no_atual.chave:
            no_atual.direito = self._remover_recursivo(no_atual.direito, chave)
        else:
            # Nó encontrado! Agora, tratar os 3 casos de remoção.
            # Caso 1: Nó com um filho ou nenhum filho
            if not no_atual.esquerdo:
                temp = no_atual.direito
                no_atual = None
                return temp
            elif not no_atual.direito:
                temp = no_atual.esquerdo
                no_atual = None
                return temp
            
            # Caso 2: Nó com dois filhos
            # Encontrar o sucessor (menor nó da subárvore direita)
            temp = self._get_menor_no(no_atual.direito)
            no_atual.chave = temp.chave # Copia a chave do sucessor para este nó
            # Remove o sucessor da subárvore direita
            no_atual.direito = self._remover_recursivo(no_atual.direito, temp.chave)

        # Se a árvore ficou vazia (tinha só um nó)
        if not no_atual:
            return no_atual

        # 2. Atualizar a altura e balancear
        no_atual.atualizar_altura()
        return no_atual.balancear()

    def _get_menor_no(self, no_atual):
        """Encontra o nó com a menor chave em uma subárvore (o mais à esquerda)."""
        if no_atual is None or no_atual.esquerdo is None:
            return no_atual
        return self._get_menor_no(no_atual.esquerdo)

    def imprimir(self):
        """Imprime a árvore de forma visual."""
        if not self.raiz:
            print("A árvore está vazia.")
            return
        
        def _imprimir_recursivo(vertice, recuo=0, prefixo="Raiz:"):
            if vertice is not None:
                if vertice.direito:
                    _imprimir_recursivo(vertice.direito, recuo + 10, "D:")
                
                print(" " * recuo + f"{prefixo} [{vertice.chave}] (h={vertice.altura}, fb={vertice.fator_de_balanceamento})")

                if vertice.esquerdo:
                    _imprimir_recursivo(vertice.esquerdo, recuo + 10, "E:")

        _imprimir_recursivo(self.raiz)

# --- EXECUÇÃO DA DEMONSTRAÇÃO ---
if __name__ == "__main__":
    print("=====================================================")
    print("  DEMONSTRAÇÃO DA ÁRVORE AVL - GESTÃO DE BIBLIOTECA")
    print("=====================================================")

    catalogo = ArvoreAVL()

    # --- Demonstração de Inserção e Rotações ---
    
    print("\n### CASO 1: ROTAÇÃO SIMPLES À ESQUERDA (RR) ###")
    catalogo.inserir(10)
    catalogo.inserir(20)
    catalogo.inserir(30) # Causa desbalanceamento RR no nó 10

    print("\n### CASO 2: ROTAÇÃO SIMPLES À DIREITA (LL) ###")
    catalogo.inserir(5)
    catalogo.inserir(3)  # Causa desbalanceamento LL no nó 10

    print("\n### CASO 3: ROTAÇÃO DUPLA ESQUERDA-DIREITA (LR) ###")
    catalogo.inserir(1)
    catalogo.inserir(4) # Causa desbalanceamento LR no nó 5

    print("\n### CASO 4: ROTAÇÃO DUPLA DIREITA-ESQUERDA (RL) ###")
    catalogo.inserir(40)
    catalogo.inserir(25) # Causa desbalanceamento RL no nó 20
    
    print("\n=====================================================")
    print("           ESTADO FINAL DA ÁRVORE APÓS INSERÇÕES")
    print("=====================================================")
    catalogo.imprimir()

    # --- Demonstração de Busca ---
    print("\n=====================================================")
    print("           DEMONSTRAÇÃO DE BUSCA")
    print("=====================================================")
    catalogo.buscar(25) # Chave que existe
    catalogo.buscar(99) # Chave que não existe

    # --- Demonstração de Remoção ---
    print("\n=====================================================")
    print("           DEMONSTRAÇÃO DE REMOÇÃO")
    print("=====================================================")
    # Removendo um nó folha (não causa desbalanceamento)
    catalogo.remover(1)
    # Removendo um nó com dois filhos (pode causar desbalanceamento)
    catalogo.remover(20)