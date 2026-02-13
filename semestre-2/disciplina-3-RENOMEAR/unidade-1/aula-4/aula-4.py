# Nome do arquivo: aula-4.py
# Exemplo de Modelagem Lógica e Estrutura de Dados em Python para o Banco de Dados Livraria
# Usamos classes para simular as Tabelas (Entidades) e seus Atributos (Colunas)

class Cliente:
    """
    Simula a Tabela CLIENTE do Modelo Lógico.
    Armazena os dados dos clientes.
    """
    def __init__(self, cod_cliente, nome, endereco):
        # cod_cliente é a Chave Primária (PK)
        self.cod_cliente = cod_cliente
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f"Cliente(PK={self.cod_cliente}, Nome='{self.nome}')"

class Editora:
    """
    Simula a Tabela EDITORA do Modelo Lógico.
    Armazena os dados das editoras.
    """
    def __init__(self, cod_editora, nome):
        # cod_editora é a Chave Primária (PK)
        self.cod_editora = cod_editora
        self.nome = nome

    def __repr__(self):
        return f"Editora(PK={self.cod_editora}, Nome='{self.nome}')"

class Livro:
    """
    Simula a Tabela LIVRO do Modelo Lógico.
    Relaciona-se com EDITORA (1:N) e ESTOQUE (1:1).
    """
    def __init__(self, cod_livro, titulo, ano_publicacao, cod_editora_fk):
        # cod_livro é a Chave Primária (PK)
        self.cod_livro = cod_livro
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        # cod_editora_fk é a Chave Estrangeira (FK) que referencia a Editora
        self.cod_editora_fk = cod_editora_fk

    def __repr__(self):
        return f"Livro(PK={self.cod_livro}, Título='{self.titulo}', FK_Editora={self.cod_editora_fk})"

class Pedido:
    """
    Simula a Tabela PEDIDO do Modelo Lógico.
    Relaciona-se com CLIENTE (N:1) e ITENS_PEDIDO (1:N).
    """
    def __init__(self, num_pedido, data_pedido, valor_total, cod_cliente_fk):
        # num_pedido é a Chave Primária (PK)
        self.num_pedido = num_pedido
        self.data_pedido = data_pedido
        self.valor_total = valor_total
        # cod_cliente_fk é a Chave Estrangeira (FK) que referencia o Cliente
        self.cod_cliente_fk = cod_cliente_fk

    def __repr__(self):
        return f"Pedido(PK={self.num_pedido}, Data='{self.data_pedido}', FK_Cliente={self.cod_cliente_fk})"

class ItensPedido:
    """
    Simula a Tabela ITENS_PEDIDO (tabela associativa) do Modelo Lógico.
    Esta tabela resolve o relacionamento Muitos-para-Muitos (N:N) entre Pedido e Livro.
    Possui uma Chave Composta (Composite Key) de (num_pedido, cod_livro).
    """
    def __init__(self, num_pedido_fk, cod_livro_fk, quantidade, preco_unitario):
        # A Chave Primária Composta é formada pela junção destas duas FKs
        self.num_pedido_fk = num_pedido_fk
        self.cod_livro_fk = cod_livro_fk
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def __repr__(self):
        return f"ItemPedido(PK_Composta=({self.num_pedido_fk}, {self.cod_livro_fk}), Qtd={self.quantidade})"

class Estoque:
    """
    Simula a Tabela ESTOQUE do Modelo Lógico.
    Relaciona-se com LIVRO (1:1), garantindo que cada livro tenha apenas um registro de estoque.
    """
    def __init__(self, cod_livro_fk, quantidade_disponivel):
        # cod_livro_fk é a Chave Primária (PK) E a Chave Estrangeira (FK)
        self.cod_livro_fk = cod_livro_fk
        self.quantidade_disponivel = quantidade_disponivel

    def __repr__(self):
        return f"Estoque(PK/FK_Livro={self.cod_livro_fk}, Qtd_Disp={self.quantidade_disponivel})"

# --- EXEMPLIFICANDO O USO DAS CLASSES (Inserção de Dados) ---

# 1. Criação de Editoras
print("--- Editoras (Base N:1 para Livro) ---")
editora_a = Editora(cod_editora=101, nome="Atlas Publishing")
editora_b = Editora(cod_editora=102, nome="Tech Books Inc.")
print(editora_a)
print(editora_b)

# 2. Criação de Livros (Referenciando Editoras com FK)
print("\n--- Livros (Mapeando FK para Editora) ---")
livro_1 = Livro(cod_livro=1, titulo="Aventura em Python", ano_publicacao=2023, cod_editora_fk=102)
livro_2 = Livro(cod_livro=2, titulo="SQL Avançado", ano_publicacao=2022, cod_editora_fk=102)
livro_3 = Livro(cod_livro=3, titulo="Modelagem de Dados", ano_publicacao=2021, cod_editora_fk=101)
print(livro_1)
print(livro_2)
print(livro_3)

# 3. Criação de Estoque (Referenciando Livros com PK/FK)
print("\n--- Estoque (Relacionamento 1:1 com Livro) ---")
estoque_1 = Estoque(cod_livro_fk=1, quantidade_disponivel=50)
estoque_2 = Estoque(cod_livro_fk=2, quantidade_disponivel=30)
print(estoque_1)
print(estoque_2)

# 4. Criação de Clientes
print("\n--- Clientes ---")
cliente_a = Cliente(cod_cliente=500, nome="Mariana Silva", endereco="Rua A")
print(cliente_a)

# 5. Criação de Pedido (Referenciando Cliente com FK)
print("\n--- Pedidos (Mapeando FK para Cliente) ---")
pedido_1 = Pedido(num_pedido=1000, data_pedido="2024-10-01", valor_total=150.00, cod_cliente_fk=500)
print(pedido_1)

# 6. Criação de Itens do Pedido (Chave Composta e FKs para Pedido e Livro)
print("\n--- Itens do Pedido (Resolvendo o N:N) ---")
item_1 = ItensPedido(num_pedido_fk=1000, cod_livro_fk=1, quantidade=1, preco_unitario=80.00)
item_2 = ItensPedido(num_pedido_fk=1000, cod_livro_fk=3, quantidade=1, preco_unitario=70.00)
print(item_1)
print(item_2)

print("\n\n*A estrutura de classes acima espelha a arquitetura do Modelo Lógico, onde as FKs definem os relacionamentos entre as 'tabelas'.*")