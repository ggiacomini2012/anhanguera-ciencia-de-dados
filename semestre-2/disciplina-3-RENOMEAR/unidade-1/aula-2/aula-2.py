# aula-2.py
# Simulação da Arquitetura de Três Camadas (ANSI/SPARC) e uso de Linguagens SQL (DDL/DML) em Python

class CamadaInterna_SGBD:
    """
    Representa a Camada Interna (Física) e o SGBD.
    Armazena os dados brutos e executa comandos DDL e DML.
    """
    def __init__(self):
        # Simula o armazenamento físico em um dicionário de 'tabelas'
        self.dados_fisicos = {
            'Funcionarios': [],
            'Vendas': []
        }
        print("✅ Camada Interna: SGBD (SQL) inicializado e pronto para armazenar dados.")

    # ----------------------------------------------------
    # Simulação de DDL (Data Definition Language) - Criação de Estrutura
    # ----------------------------------------------------
    def executar_ddl(self, comando_sql):
        """Simula a execução de comandos DDL como CREATE TABLE."""
        if 'CREATE TABLE' in comando_sql.upper():
            tabela = comando_sql.split()[2].replace('(', '')
            if tabela not in self.dados_fisicos:
                # Simula a criação de uma nova 'tabela'
                self.dados_fisicos[tabela] = []
                print(f"   ⚙️ DDL Executado: Tabela '{tabela}' criada com sucesso.")
            return True
        return False

    # ----------------------------------------------------
    # Simulação de DML (Data Manipulation Language) - Manipulação de Dados
    # ----------------------------------------------------
    def executar_dml(self, comando_sql, dados=None):
        """Simula a execução de comandos DML como INSERT e SELECT."""
        comando = comando_sql.upper().split()[0]
        tabela = comando_sql.split()[2] if len(comando_sql.split()) > 2 else None

        if comando == 'INSERT' and tabela:
            if tabela in self.dados_fisicos and dados:
                self.dados_fisicos[tabela].append(dados)
                print(f"   ➕ DML Executado: Registro inserido em '{tabela}'.")
                return True
        elif comando == 'SELECT' and tabela:
            print(f"   🔍 DML Executado: Buscando dados brutos em '{tabela}'.")
            return self.dados_fisicos.get(tabela, [])
        
        return False

class CamadaConceitual_Regras:
    """
    Representa a Camada Conceitual (Lógica).
    Define a estrutura (Modelo ER) e as regras de negócio.
    Usa a Camada Interna (SGBD) para armazenamento.
    """
    def __init__(self, sgbd: CamadaInterna_SGBD):
        self.sgbd = sgbd
        # Estrutura lógica (simula o Modelo Entidade-Relacionamento)
        self.esquema_logico = {
            'Funcionarios': ['id', 'nome', 'departamento', 'salario'],
            'Vendas': ['produto', 'valor', 'departamento_id']
        }
        print("🧠 Camada Conceitual: Regras de negócio definidas.")
        
        # Garante que as estruturas (tabelas) existam na camada interna (DDL)
        self.sgbd.executar_ddl("CREATE TABLE Funcionarios (...)")
        self.sgbd.executar_ddl("CREATE TABLE Vendas (...)")

    def adicionar_funcionario(self, id, nome, depto, salario):
        """Regra de negócio: Adiciona um novo funcionário."""
        dados = {'id': id, 'nome': nome, 'departamento': depto, 'salario': salario}
        # A Camada Conceitual usa DML para interagir com a Camada Interna
        self.sgbd.executar_dml("INSERT INTO Funcionarios (id, nome, departamento, salario)", dados)

    def adicionar_venda(self, produto, valor, depto_id):
        """Regra de negócio: Registra uma nova venda."""
        dados = {'produto': produto, 'valor': valor, 'departamento_id': depto_id}
        self.sgbd.executar_dml("INSERT INTO Vendas (produto, valor, departamento_id)", dados)

    def obter_todos_os_dados_funcionarios(self):
        """Consulta central para a Camada Externa."""
        return self.sgbd.executar_dml("SELECT * FROM Funcionarios")

class CamadaExterna_Views:
    """
    Representa a Camada Externa (Visão do Usuário).
    Cria 'Views' personalizadas para diferentes usuários/departamentos.
    Usa a Camada Conceitual para obter os dados brutos.
    """
    def __init__(self, conceitual: CamadaConceitual_Regras):
        self.conceitual = conceitual
        print("🖥️ Camada Externa: Interfaces de usuário prontas para gerar 'Views'.")

    # ----------------------------------------------------
    # Simulação de 'Views' (Visões personalizadas)
    # ----------------------------------------------------
    def view_rh(self):
        """Visão do RH: Nome e Salário (dados sensíveis)."""
        print("\n=> VIEW RH (Dados Sensíveis)")
        dados_brutos = self.conceitual.obter_todos_os_dados_funcionarios()
        # Filtra os dados brutos para criar a VIEW personalizada
        view_data = [{'Nome': f['nome'], 'Salário': f['salario']} for f in dados_brutos]
        return view_data

    def view_vendas_simples(self):
        """Visão de Vendas: Nome e Departamento (sem salários)."""
        print("\n=> VIEW VENDAS (Dados Operacionais)")
        dados_brutos = self.conceitual.obter_todos_os_dados_funcionarios()
        # Filtra os dados brutos para criar a VIEW personalizada
        view_data = [{'Nome': f['nome'], 'Departamento': f['departamento']} for f in dados_brutos if f['departamento'] == 'Vendas']
        return view_data

# =========================================================================
# Execução e Demonstração do Fluxo
# =========================================================================
print("=================================================================")
print("  Início da Simulação: Arquitetura de Três Camadas ANSI/SPARC")
print("=================================================================")

# 1. Inicialização das Camadas (Bottom-up)
sgbd = CamadaInterna_SGBD()  # Camada Interna
regras = CamadaConceitual_Regras(sgbd) # Camada Conceitual
views = CamadaExterna_Views(regras) # Camada Externa

print("\n--- Processamento de Dados (Camada Conceitual) ---")
# 2. Inserção de Dados (DML) via Camada Conceitual
regras.adicionar_funcionario(101, "Alice", "RH", 5500.00)
regras.adicionar_funcionario(102, "Bob", "Vendas", 4800.00)
regras.adicionar_funcionario(103, "Carlos", "Vendas", 4700.00)
regras.adicionar_venda("Laptop", 3500.00, 102)
regras.adicionar_venda("Mouse", 50.00, 103)


# 3. Consulta de Dados (Camada Externa) - Personalização
print("\n--- Acesso Personalizado aos Dados (Camada Externa) ---")

# Visão do RH (necessita de dados de salário)
rh_data = views.view_rh()
for registro in rh_data:
    print(f"  RH Vê: Nome: {registro['Nome']}, Salário: {registro['Salário']}")

# Visão de Vendas (não deve ver salários, apenas dados operacionais)
vendas_data = views.view_vendas_simples()
for registro in vendas_data:
    print(f"  Vendas Vê: Nome: {registro['Nome']}, Depto: {registro['Departamento']}")


print("\n--- Desacoplamento ---")
# Demonstração do Desacoplamento:
# Se a Camada Interna mudasse (ex: de MySQL para PostgreSQL), 
# a Camada Conceitual e Externa (que usa as funções 'sgbd.executar_dml') não precisariam mudar.
# O Python abstrai o "como" o dado é guardado, focando no "o que" é guardado.
print("Exemplo de Desacoplamento: A Camada Externa solicitou dados e o SGBD (Camada Interna)")
print(f"respondeu. Se mudarmos o SGBD, o método 'view_rh()' (Camada Externa) não muda,")
print("apenas a implementação da 'CamadaInterna_SGBD' precisaria ser ajustada.")