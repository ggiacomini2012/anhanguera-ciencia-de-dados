"""
Exemplo prático de um Diagrama Entidade-Relacionamento (DER) simples
traduzido para classes em Python.

Neste modelo, temos duas entidades: Cliente e Pedido.
Elas se relacionam de forma que um Cliente pode ter vários Pedidos,
mas um Pedido pertence a apenas um Cliente.

"""

# --- Entidade: Cliente ---
# Representa a tabela "Cliente" no banco de dados.
class Cliente:
    def __init__(self, id_cliente, nome, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        # Uma lista para armazenar os pedidos associados a este cliente.
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        """Associa um pedido a este cliente."""
        self.pedidos.append(pedido)

    def __repr__(self):
        """Retorna uma representação legível do objeto."""
        return f"<Cliente(ID: {self.id_cliente}, Nome: {self.nome})>"


# --- Entidade: Pedido ---
# Representa a tabela "Pedido" no banco de dados.
class Pedido:
    def __init__(self, id_pedido, data, valor_total, cliente):
        self.id_pedido = id_pedido
        self.data = data
        self.valor_total = valor_total
        # O "cliente" é a chave estrangeira, a conexão com a entidade Cliente.
        self.cliente = cliente

    def __repr__(self):
        """Retorna uma representação legível do objeto."""
        return f"<Pedido(ID: {self.id_pedido}, Cliente: {self.cliente.nome}, Valor: R${self.valor_total})>"


# --- Exemplo de uso ---

# 1. Criando instâncias das entidades
print("1. Criando um cliente e alguns pedidos...")
cliente1 = Cliente(1, "Ana Silva", "ana.silva@email.com")
pedido1 = Pedido(101, "2023-10-25", 150.75, cliente1)
pedido2 = Pedido(102, "2023-10-26", 300.50, cliente1)

# 2. Estabelecendo o relacionamento
# Adicionamos os pedidos à lista do cliente.
cliente1.adicionar_pedido(pedido1)
cliente1.adicionar_pedido(pedido2)

# 3. Verificando o resultado
print("\n2. Verificando os dados:")
print(f"Detalhes do cliente: {cliente1}")
print(f"Pedidos do cliente {cliente1.nome}:")
for pedido in cliente1.pedidos:
    print(f"  - {pedido}")

# Podemos também acessar o cliente a partir do pedido.
print(f"\nDetalhes do pedido 101:")
print(f"  - Pedido {pedido1.id_pedido} feito por: {pedido1.cliente.nome}")

print("\n---")
print("Este código simula a estrutura de um DER de forma programática, onde as classes representam as 'entidades' e as referências entre elas (como o 'self.cliente' em Pedido) representam os 'relacionamentos'.")