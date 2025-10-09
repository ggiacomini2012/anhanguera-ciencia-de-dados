# aula-2.py
# Exemplo em Python: Simulação de Modelos Lógicos e Áreas de Interesse em Varejo.
# Usamos classes (POO) para representar as entidades (MLC) e um sistema de agregação
# para simular as Áreas de Interesse e os Repositórios Lógicos.

# --- 1. MODELO LÓGICO CORPORATIVO (MLC): As Entidades e seus Atributos ---

class Cliente:
    """Representa a entidade Cliente do MLC."""
    def __init__(self, id_cliente, nome, regiao):
        self.id_cliente = id_cliente  # Atributo: Identificação
        self.nome = nome              # Atributo: Nome do cliente
        self.regiao = regiao          # Atributo: Região de moradia

    def __repr__(self):
        return f"Cliente(ID: {self.id_cliente}, Nome: {self.nome}, Região: {self.regiao})"

class Produto:
    """Representa a entidade Produto do MLC."""
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto # Atributo: Identificação
        self.nome = nome             # Atributo: Nome do produto
        self.preco = preco           # Atributo: Preço unitário

    def __repr__(self):
        return f"Produto(ID: {self.id_produto}, Nome: {self.nome}, Preço: R${self.preco:.2f})"

class Venda:
    """Representa a entidade Transação de Venda (o relacionamento entre Cliente e Produto)."""
    def __init__(self, id_venda, id_cliente, id_produto, quantidade, data):
        self.id_venda = id_venda
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.data = data

    def __repr__(self):
        return f"Venda(ID: {self.id_venda}, Cliente: {self.id_cliente}, Produto: {self.id_produto}, Qtd: {self.quantidade}, Data: {self.data})"

# --- 2. MODELO DE ÁREA DE INTERESSE (MAI) & MODELO LÓGICO DE REPOSITÓRIO (MLR) ---

class DataMartMarketing:
    """
    Simula um Data Mart de Marketing, uma Área de Interesse.
    Foca apenas em dados de Cliente e Vendas para segmentação e campanhas.
    """
    def __init__(self):
        # O repositório armazena listas (simulando tabelas filtradas)
        self.dados_clientes = {}
        self.dados_vendas = []
        print("\n[MAI/MLR] Data Mart de Marketing inicializado.")

    def carregar_dados_brutos(self, clientes, vendas):
        """Carrega e filtra dados relevantes para Marketing."""
        # Marketing está interessado em Clientes (para segmentação) e Vendas (para comportamento)
        for cliente in clientes:
            self.dados_clientes[cliente.id_cliente] = cliente
        
        # Simula a agregação/carregamento no repositório
        for venda in vendas:
            self.dados_vendas.append(venda)
        print(f"[Marketing] Carregados {len(self.dados_clientes)} clientes e {len(self.dados_vendas)} vendas.")

    def analisar_clientes_por_regiao(self, regiao):
        """Exemplo de análise que o time de Marketing faria."""
        clientes_segmentados = [
            c for c in self.dados_clientes.values() if c.regiao == regiao
        ]
        return clientes_segmentados

class DataWarehouseVendas:
    """
    Simula um Data Warehouse (DW), uma Área de Interesse/Repositório central.
    Armazena todos os fatos (Vendas) e dimensões (Cliente, Produto) para análise histórica.
    """
    def __init__(self):
        self.fato_vendas = []
        self.dim_clientes = {}
        self.dim_produtos = {}
        print("\n[MAI/MLR] Data Warehouse de Vendas inicializado.")

    def carregar_dados_completos(self, clientes, produtos, vendas):
        """Carrega todos os dados (entidades) no repositório DW."""
        for c in clientes:
            self.dim_clientes[c.id_cliente] = c
        for p in produtos:
            self.dim_produtos[p.id_produto] = p
        
        # Fato Vendas
        self.fato_vendas.extend(vendas)
        print(f"[DW Vendas] Carregados {len(self.fato_vendas)} registros de vendas para análise.")

    def calcular_faturamento_total(self):
        """Exemplo de métrica de negócio obtida a partir do modelo lógico (fatos e dimensões)."""
        faturamento = 0
        for venda in self.fato_vendas:
            produto = self.dim_produtos.get(venda.id_produto)
            if produto:
                faturamento += venda.quantidade * produto.preco
        return faturamento

# --- DADOS DE EXEMPLO (Simulação da Coleta) ---

clientes_dados = [
    Cliente(101, "Ana Silva", "Sul"),
    Cliente(102, "Bruno Costa", "Norte"),
    Cliente(103, "Carla Meirelles", "Sul"),
    Cliente(104, "David Lopes", "Norte"),
]

produtos_dados = [
    Produto(501, "Celular X", 1500.00),
    Produto(502, "Notebook Y", 4500.00),
    Produto(503, "Fone Z", 250.00),
]

vendas_dados = [
    Venda(1, 101, 501, 1, "2024-09-01"),
    Venda(2, 102, 503, 2, "2024-09-02"),
    Venda(3, 101, 502, 1, "2024-09-03"),
    Venda(4, 104, 501, 3, "2024-09-04"),
    Venda(5, 103, 503, 1, "2024-09-05"),
    Venda(6, 102, 502, 1, "2024-09-06"),
]

# --- EXECUÇÃO E DEMONSTRAÇÃO DOS MODELOS LÓGICOS ---

print("--- DEMONSTRAÇÃO DA ARQUITETURA DE DADOS ---")

# 1. Implementação do Data Warehouse (Repositório Geral)
dw_varejo = DataWarehouseVendas()
dw_varejo.carregar_dados_completos(clientes_dados, produtos_dados, vendas_dados)

# Uso do DW para uma métrica corporativa (Modelos Lógicos de Repositórios em ação)
faturamento = dw_varejo.calcular_faturamento_total()
print(f"\n✅ Análise Corporativa (DW): Faturamento Total = R${faturamento:.2f}")

# 2. Implementação do Data Mart (Repositório Especializado para Área de Interesse)
dm_marketing = DataMartMarketing()
dm_marketing.carregar_dados_brutos(clientes_dados, vendas_dados)

# Uso do DM para uma ação de marketing (Área de Interesse em ação)
regiao_foco = "Sul"
clientes_sul = dm_marketing.analisar_clientes_por_regiao(regiao_foco)
print(f"\n🎯 Análise de Marketing (DM): Clientes da Região '{regiao_foco}':")
for c in clientes_sul:
    print(f"- {c.nome}")

# 3. Demonstração de uma Entidade do MLC
print("\n🔍 Entidade Cliente (MLC) Isolada:")
cliente_teste = Cliente(999, "Teste Estrutura", "Teste")
print(cliente_teste)

# A CLASSE Venda representa o RELACIONAMENTO entre Cliente e Produto,
# um pilar do Modelo Lógico Corporativo (MER).