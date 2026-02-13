# --- 1. Definição da Estrutura do Produto ---
# A classe Produto representa as informações de um item no e-commerce.
# Ela possui atributos para ID, nome, descrição e preço.
class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        """Método para retornar uma representação em string do objeto."""
        return f"ID: {self.id}, Nome: {self.nome}, Descrição: {self.descricao}, Preço: R${self.preco:.2f}"

# --- 2. Implementação do Cache ---
# O cache é implementado usando um dicionário em Python.
# As chaves são os IDs dos produtos e os valores são instâncias da classe Produto.
# Este dicionário age como um 'map' que utiliza hashes internamente para otimizar o acesso.
cache = {}

# --- 3. Funcionalidades do Cache ---

# 3.1. Inserção: Permite adicionar produtos ao cache.
def adicionar_produto_ao_cache(produto):
    """Adiciona um objeto Produto ao cache."""
    cache[produto.id] = produto
    print(f"Produto '{produto.nome}' (ID: {produto.id}) adicionado ao cache.")

# 3.2. Consulta: Desenvolve uma função para consultar produtos pelo ID.
def consultar_produto(id):
    """
    Consulta um produto no cache pelo ID.
    Se o produto estiver no cache, retorna seus detalhes.
    Caso contrário, simula uma busca no 'banco de dados', armazena o resultado no cache
    e então retorna os detalhes do produto.
    """
    if id in cache:
        print(f"Produto (ID: {id}) encontrado no cache.")
        return cache[id]
    else:
        print(f"Produto (ID: {id}) NÃO encontrado no cache. Simunando busca no 'banco de dados'...")
        # Simulação de busca no "banco de dados".
        if id == "PROD001":
            produto_encontrado = Produto(id, "Teclado Mecânico", "Teclado de alta performance para jogos", 350.00)
        elif id == "PROD002":
            produto_encontrado = Produto(id, "Mouse Óptico Gamer", "Mouse com alta precisão e RGB", 150.00)
        elif id == "PROD003":
            produto_encontrado = Produto(id, "Monitor Ultrawide", "Monitor para produtividade e imersão", 1200.00)
        else:
            # Produto genérico caso o ID não seja um dos pré-definidos para simulação.
            produto_encontrado = Produto(id, f"Produto Genérico {id}", "Descrição padrão para produto genérico", 100.00)

        # Armazena o produto recém-encontrado no cache para futuras consultas.
        adicionar_produto_ao_cache(produto_encontrado)
        return produto_encontrado

# 3.3. Remoção (opcional): Implementa uma funcionalidade para remover produtos do cache.
def remover_produto_do_cache(id):
    """Remove um produto do cache pelo ID, se ele existir."""
    if id in cache:
        del cache[id]
        print(f"Produto (ID: {id}) removido do cache.")
    else:
        print(f"Produto (ID: {id}) não está no cache para remoção.")

# --- Demonstração de Uso ---
if __name__ == "__main__":
    print("--- Inicializando o sistema de cache ---")

    # Criando alguns produtos
    produto1 = Produto("PROD001", "Teclado Mecânico", "Teclado de alta performance para jogos", 350.00)
    produto2 = Produto("PROD002", "Mouse Óptico Gamer", "Mouse com alta precisão e RGB", 150.00)

    # 1. Inserindo produtos diretamente no cache
    print("\n--- Teste de Inserção ---")
    adicionar_produto_ao_cache(produto1)
    adicionar_produto_ao_cache(produto2)
    print(f"Estado atual do cache: {len(cache)} produtos.")

    # 2. Consultando produtos
    print("\n--- Teste de Consulta ---")
    # Consulta de um produto que já está no cache (Cache Hit)
    print("\nConsultando PROD001:")
    p_consultado1 = consultar_produto("PROD001")
    if p_consultado1:
        print(f"Detalhes do produto consultado: {p_consultado1}")

    # Consulta de um produto que NÃO está no cache (Cache Miss)
    # Isso simulará uma busca no "banco de dados" e adicionará o produto ao cache.
    print("\nConsultando PROD003:")
    p_consultado3 = consultar_produto("PROD003")
    if p_consultado3:
        print(f"Detalhes do produto consultado: {p_consultado3}")
    print(f"Estado atual do cache: {len(cache)} produtos.")

    # Tentando consultar PROD003 novamente para ver o Cache Hit
    print("\nConsultando PROD003 (novamente):")
    p_consultado3_again = consultar_produto("PROD003")
    if p_consultado3_again:
        print(f"Detalhes do produto consultado: {p_consultado3_again}")

    # 3. Removendo produtos
    print("\n--- Teste de Remoção ---")
    remover_produto_do_cache("PROD001")
    print(f"Estado atual do cache: {len(cache)} produtos.")

    # Tentando consultar o produto removido
    print("\nConsultando PROD001 após remoção:")
    p_consultado1_after_removal = consultar_produto("PROD001")
    if p_consultado1_after_removal:
        print(f"Detalhes do produto consultado: {p_consultado1_after_removal}")
    print(f"Estado atual do cache: {len(cache)} produtos.")

    print("\n--- Fim da demonstração ---")