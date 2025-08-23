
"""
Aqui está a atividade/trabalho da unidade 1 da disciplina Estrutura de Dados.
Deixarei comentarios para deixar mais claro o raciocinio quanto da implementação quanto da logica.
"""

# ATIVIDADE 

# 1. Crie uma classe Node que represente um nó em uma lista encadeada.
# 2. Crie uma classe LinkedList que represente a lista encadeada.
# 3. Implemente um método append para adicionar um novo nó ao final da lista.
# 4. Implemente um método print_list para exibir os dados de todos os nós da lista.
# 5. Implemente uma função count_nodes para contar o número de nós em uma lista encadeada.

# CÓDIGO PARA A ATIVIDADE

# class Node:
#  def __init__(self, data):
#  # Insira aqui seu codigo…….
# Class LinkedList:
#  def __init__(self):
#  # Insira aqui seu codigo….
#  def append(self, data):
#  # Insira aqui seu codigo….
#  def print_list(self):
#  # Insira aqui seu codigo…..
# # Implementar uma função para contar o número de nós em uma lista encadeada.
# def count_nodes(linked_list):
#  # Insira aqui seu codigo



# Definição da classe Node, que representa cada elemento (nó) da lista.
class Node:
  """
  Classe que representa um nó em uma lista encadeada.
  Cada nó armazena um dado (data) e uma referência (next) para o próximo nó.
  """
  def __init__(self, data):
    self.data = data  # O dado armazenado no nó.
    self.next = None  # A referência para o próximo nó, inicializada como None.

# Definição da classe LinkedList, que gerencia a estrutura da lista encadeada.
class LinkedList:
  """
  Classe que representa a lista encadeada.
  Contém uma referência para o primeiro nó da lista (head).
  """
  def __init__(self):
    self.head = None  # A cabeça da lista, inicializada como None para uma lista vazia.

  def append(self, data):
    """
    Adiciona um novo nó com o dado fornecido ao final da lista encadeada.
    """
    new_node = Node(data)
    # Se a lista estiver vazia, o novo nó se torna a cabeça da lista.
    if self.head is None:
      self.head = new_node
      return
    
    # Se a lista não estiver vazia, percorre até o último nó.
    last_node = self.head 
    while last_node.next:
      last_node = last_node.next
    
    # Define o novo nó como o próximo do último nó atual.
    last_node.next = new_node

  def print_list(self):
    """
    Exibe no console os dados de todos os nós da lista encadeada.
    """
    current_node = self.head
    while current_node:
      print(current_node.data, end=" -> ") # Exibe o dado do nó atual, seguido de uma seta.
      current_node = current_node.next # Atualiza o nó atual para o próximo nó.
    print("None") # Exibe "None" para indicar o final da lista.

# Implementação da função para contar o número de nós em uma lista encadeada.
def count_nodes(linked_list):
  """
  Recebe uma lista encadeada como parâmetro e retorna o número de nós presentes nela.
  A função percorre a lista, incrementando um contador a cada nó visitado.
  """
  count = 0
  current_node = linked_list.head # A cabeça da lista, inicializada como None para uma lista vazia.
  while current_node: # Enquanto o nó atual não for None.
    count += 1 # Incrementa o contador a cada nó visitado.
    current_node = current_node.next # Atualiza o nó atual para o próximo nó.
  return count # Retorna o número de nós presentes na lista.

# --- Programa Principal ---

# 1. Cria uma nova lista encadeada.
my_list = LinkedList()

# 2. Adiciona elementos à lista usando o método append.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Imprime a lista encadeada para visualização.
print("Lista Encadeada:")
my_list.print_list()

# 4. Chama a função count_nodes para obter o número de nós.
total_nodes = count_nodes(my_list)

# 5. Exibe o resultado.
print(f"\nO número de nós na lista é: {total_nodes}")