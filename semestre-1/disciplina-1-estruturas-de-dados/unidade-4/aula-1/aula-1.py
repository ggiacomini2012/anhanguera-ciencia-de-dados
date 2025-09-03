# Definimos o número total de classes, que será o tamanho da nossa tabela hash.
NUMERO_CLASSES = 15

# O dicionário 'inventario' atuará como nossa tabela hash.
# As chaves serão os números das classes (0 a 14) e os valores a contagem de produtos.
inventario = {i: 0 for i in range(NUMERO_CLASSES)}

# Esta é a nossa função hash.
# Ela usa o método da divisão para determinar a classe do produto.
# O identificador único do produto é a "chave" de entrada.
# Usamos os dois últimos dígitos do ID para determinar a classe.
# No problema, a classe 0 corresponde à 15, então fazemos o ajuste.
def funcao_hash_por_classe(identificador):
  # Garante que o identificador é um número inteiro.
  identificador = int(identificador)
  # O resto da divisão por 100 nos dá os dois últimos dígitos.
  classe = identificador % 100
  # Ajusta a classe 15 para 0, se necessário.
  if classe == 15:
    return 0
  else:
    # A classe do produto é o resto da divisão por NUMERO_CLASSES (15).
    # Isso mapeia as classes 0-14 para os índices da nossa tabela.
    return classe % NUMERO_CLASSES

# Esta função adiciona um produto ao inventário.
def adicionar_produto(identificador):
  # Calcula a classe do produto usando a função hash.
  classe = funcao_hash_por_classe(identificador)

  # Verifica se a classe existe no nosso inventário.
  if classe in inventario:
    # Se a classe existir, incrementa a contagem de produtos dessa classe.
    inventario[classe] += 1
    print(f"Produto com ID {identificador} adicionado à classe {classe}.")
  else:
    # Trata uma colisão ou um caso onde a classe não é válida.
    print(f"Erro: Classe {classe} não encontrada. Impossível adicionar o produto.")

# Esta função consulta a quantidade de produtos em uma classe específica.
def consultar_produtos_por_classe(identificador):
  # Calcula a classe do produto usando a função hash.
  classe = funcao_hash_por_classe(identificador)
  
  # Verifica se a classe existe no nosso inventário.
  if classe in inventario:
    # Retorna a contagem de produtos dessa classe.
    contagem = inventario[classe]
    print(f"A classe {classe} tem {contagem} produto(s) em estoque.")
    return contagem
  else:
    # Trata um caso onde a classe não é válida.
    print(f"Erro: Classe {classe} não encontrada.")
    return None

# --- Simulação de uso do sistema ---

print("Estado inicial do inventário:")
print(inventario)
print("-" * 30)

# Adicionando alguns produtos para simular o uso.
adicionar_produto(1234567805) # Classe 5
adicionar_produto(9876543205) # Classe 5
adicionar_produto(1122334401) # Classe 1
adicionar_produto(5566778812) # Classe 12
adicionar_produto(9900112201) # Classe 1

print("\nEstado do inventário após as adições:")
print(inventario)
print("-" * 30)

# Consultando a quantidade de produtos de uma classe específica.
consultar_produtos_por_classe(1122334401) # Consulta a classe 1
consultar_produtos_por_classe(1234567805) # Consulta a classe 5

print("-" * 30)
print("Fim da demonstração.")
