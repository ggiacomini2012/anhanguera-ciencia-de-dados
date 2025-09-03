# Importamos o módulo heapq, que contém as ferramentas para trabalhar com uma fila de prioridade.
import heapq
import itertools # Usaremos para criar um contador sequencial único.

# --- Estrutura e Funções Auxiliares ---

# Nossa "fila" será uma lista simples. O módulo heapq irá gerenciá-la como um heap.
fila_de_atendimento = []

# Criamos um contador para garantir a ordem de chegada (FIFO) para prioridades iguais.
contador = itertools.count()

# Função auxiliar para adicionar solicitações à fila de forma organizada.
def adicionar_solicitacao(descricao, prioridade):
  """Adiciona uma solicitação à fila com sua prioridade e ordem de chegada."""
  
  # O contador garante que, se duas solicitações tiverem a mesma prioridade,
  # a que foi adicionada primeiro terá um número de sequência menor e sairá antes.
  sequencia = next(contador)
  
  # Criamos a entrada como uma tupla. heapq irá ordenar por prioridade, depois por sequência.
  entrada = (prioridade, sequencia, descricao)
  
  # Usamos heappush para adicionar o item à fila mantendo a propriedade do heap.
  # Isso é uma operação eficiente: O(log n).
  heapq.heappush(fila_de_atendimento, entrada)
  print(f"-> Solicitação adicionada: '{descricao}' com prioridade {prioridade}.")


# --- Simulação do Atendimento ---

print("Iniciando o dia no centro de atendimento...\n")

# Adicionando algumas solicitações padrão no início do dia.
adicionar_solicitacao("Resetar senha do cliente A", prioridade=2)
adicionar_solicitacao("Verificar status do pedido do cliente B", prioridade=2)

# De repente, chega uma solicitação urgente!
adicionar_solicitacao("Sistema de pagamento OFFLINE!", prioridade=1)

# Mais uma solicitação padrão é adicionada.
adicionar_solicitacao("Atualizar endereço do cliente C", prioridade=2)

# Outra solicitação urgente, mas que chegou depois da primeira.
adicionar_solicitacao("Servidor principal com uso de 100% de CPU", prioridade=1)


print("\n--- Fila de atendimento atual (visão interna do heap) ---")
# A ordem interna da lista não parece ordenada, mas a estrutura de heap garante
# que o primeiro elemento (índice 0) é sempre o de menor valor (maior prioridade).
print(fila_de_atendimento)


print("\n--- Processando as solicitações na ordem correta ---")

# Enquanto a fila não estiver vazia...
while fila_de_atendimento:
  # Usamos heappop para remover e retornar o item de MAIOR prioridade (o menor número).
  # Esta também é uma operação eficiente: O(log n).
  prioridade, _, descricao = heapq.heappop(fila_de_atendimento)
  
  tipo = "URGENTE" if prioridade == 1 else "PADRÃO"
  print(f"Atendendo [Tipo: {tipo}]: {descricao}")

print("\nTodas as solicitações foram atendidas!")