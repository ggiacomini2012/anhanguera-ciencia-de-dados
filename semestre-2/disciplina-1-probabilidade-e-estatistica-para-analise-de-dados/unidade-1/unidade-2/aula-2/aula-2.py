class No:
    """Representa um nó da Árvore Binária de Busca."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class ArvoreBB:
    """Implementa a Árvore Binária de Busca (ABB) com operações de inserção, busca e remoção."""
    def __init__(self):
        self.root = None

    def inserir(self, key):
        """Método público para inserir uma chave na árvore."""
        if self.root is None:
            self.root = No(key)
        else:
            self._inserir_recursivo(self.root, key)

    def _inserir_recursivo(self, current_no, key):
        """Função auxiliar recursiva para a inserção."""
        if key < current_no.key:
            if current_no.left is None:
                current_no.left = No(key)
            else:
                self._inserir_recursivo(current_no.left, key)
        else: # key >= current_no.key (considerando que não há chaves duplicadas)
            if current_no.right is None:
                current_no.right = No(key)
            else:
                self._inserir_recursivo(current_no.right, key)

    def buscar(self, key):
        """Método público para buscar uma chave na árvore."""
        return self._buscar_recursivo(self.root, key)

    def _buscar_recursivo(self, current_no, key):
        """Função auxiliar recursiva para a busca."""
        if current_no is None or current_no.key == key:
            return current_no
        if key < current_no.key:
            return self._buscar_recursivo(current_no.left, key)
        return self._buscar_recursivo(current_no.right, key)

    def remover(self, key):
        """Método público para remover uma chave da árvore."""
        self.root = self._remover_recursivo(self.root, key)

    def _remover_recursivo(self, current_no, key):
        """Função auxiliar recursiva para a remoção, cobrindo os 3 casos descritos."""
        if current_no is None:
            return current_no

        if key < current_no.key:
            current_no.left = self._remover_recursivo(current_no.left, key)
        elif key > current_no.key:
            current_no.right = self._remover_recursivo(current_no.right, key)
        else:
            # Caso 1: Nó com 0 ou 1 filho
            if current_no.left is None:
                return current_no.right
            elif current_no.right is None:
                return current_no.left
            
            # Caso 2: Nó com 2 filhos
            # Encontrar o sucessor (menor nó da subárvore direita)
            temp_no = self._encontrar_minimo(current_no.right)
            current_no.key = temp_no.key
            current_no.right = self._remover_recursivo(current_no.right, temp_no.key)
        
        return current_no

    def _encontrar_minimo(self, no):
        """Encontra o nó com a menor chave em uma subárvore."""
        while no.left is not None:
            no = no.left
        return no

    def imprimir_ordenado(self):
        """Imprime os nós da árvore em ordem crescente (in-order traversal)."""
        self._imprimir_ordenado_recursivo(self.root)
        print()

    def _imprimir_ordenado_recursivo(self, no):
        """Função auxiliar para a impressão ordenada."""
        if no:
            self._imprimir_ordenado_recursivo(no.left)
            print(no.key, end=' ')
            self._imprimir_ordenado_recursivo(no.right)

# --- Exemplo de uso ---
print("--- Criando e populando a árvore ---")
arvore = ArvoreBB()
sequencia = [14, 4, 18, 0, 21, 17, 1, 8, 13]
print(f"Inserindo a sequência: {sequencia}")
for chave in sequencia:
    arvore.inserir(chave)

print("\n--- Impressão da árvore em ordem crescente ---")
arvore.imprimir_ordenado() # Saída: 0 1 4 8 13 14 17 18 21

print("\n--- Buscando elementos ---")
busca1 = arvore.buscar(8)
if busca1:
    print("Elemento 8 encontrado!")
else:
    print("Elemento 8 não encontrado.")

busca2 = arvore.buscar(100)
if busca2:
    print("Elemento 100 encontrado!")
else:
    print("Elemento 100 não encontrado.")

print("\n--- Removendo elementos ---")
print("Árvore antes da remoção (ordenada): ", end='')
arvore.imprimir_ordenado()

print("\nRemovendo o nó folha 1...")
arvore.remover(1)
print("Árvore após a remoção (ordenada): ", end='')
arvore.imprimir_ordenado()

print("\nRemovendo o nó com 1 filho (4)...")
arvore.remover(4)
print("Árvore após a remoção (ordenada): ", end='')
arvore.imprimir_ordenado()

print("\nRemovendo o nó com 2 filhos (18)...")
arvore.remover(18)
print("Árvore após a remoção (ordenada): ", end='')
arvore.imprimir_ordenado()