import time
import random

# --- Simulação de uma Lista Encadeada (para fins didáticos) ---
class Node:
    """Um nó individual da lista encadeada."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Uma lista encadeada simples."""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Adiciona um novo nó ao final da lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def search(self, data):
        """Busca um elemento na lista encadeada."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# --- Configurações do teste ---
NUM_ELEMENTS = 10000
NUM_SEARCHES = 1000
data_to_add = list(range(NUM_ELEMENTS))
random.shuffle(data_to_add)

# --- Teste de Inserção ---
print("--- Teste de Inserção ---")

# Lista Encadeada
linked_list = LinkedList()
start_time_ll_insert = time.time()
for item in data_to_add:
    linked_list.append(item)
end_time_ll_insert = time.time()
print(f"Tempo de inserção na Lista Encadeada: {end_time_ll_insert - start_time_ll_insert:.4f} segundos")

# Tabela Hash (Dicionário)
hash_table = {}
start_time_ht_insert = time.time()
for item in data_to_add:
    hash_table[item] = True
end_time_ht_insert = time.time()
print(f"Tempo de inserção na Tabela Hash: {end_time_ht_insert - start_time_ht_insert:.4f} segundos")

# --- Teste de Busca ---
print("\n--- Teste de Busca ---")

# Elementos a serem buscados
elements_to_search = random.sample(data_to_add, NUM_SEARCHES)

# Lista Encadeada
start_time_ll_search = time.time()
for item in elements_to_search:
    linked_list.search(item)
end_time_ll_search = time.time()
print(f"Tempo de busca na Lista Encadeada: {end_time_ll_search - start_time_ll_search:.4f} segundos")

# Tabela Hash (Dicionário)
start_time_ht_search = time.time()
for item in elements_to_search:
    _ = hash_table.get(item)
end_time_ht_search = time.time()
print(f"Tempo de busca na Tabela Hash: {end_time_ht_search - start_time_ht_search:.4f} segundos")