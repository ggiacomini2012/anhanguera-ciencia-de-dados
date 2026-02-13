import time
import random

class CloudDatabaseProvider:
    """
    Classe base que define o contrato para qualquer provedor de nuvem.
    Imagine isso como um 'Adaptador Universal'.
    """
    def __init__(self, nome, tipo_banco):
        self.nome = nome
        self.tipo_banco = tipo_banco
        self.conectado = False

    def conectar(self):
        print(f"🔌 [{self.nome}] Tentando conectar ao {self.tipo_banco}...")
        time.sleep(1) # Simula latência de rede
        self.conectado = True
        print(f"✅ [{self.nome}] Conexão estabelecida com sucesso!")

    def executar_query(self, query):
        if not self.conectado:
            print(f"❌ [{self.nome}] Erro: Você precisa conectar primeiro.")
            return
        
        print(f"🔍 [{self.nome}] Executando: '{query}'")
        time.sleep(0.5) # Simula processamento
        
        # Simula resultados diferentes baseados no provedor
        if "AWS" in self.nome:
            print(f"⚡ [{self.nome}] Resultado retornado via Amazon RDS/Aurora (Alta Disponibilidade).")
        elif "Azure" in self.nome:
            print(f"🏢 [{self.nome}] Resultado retornado via Azure SQL (Integrado ao AD Corporativo).")
        elif "GCP" in self.nome:
            print(f"🚀 [{self.nome}] Resultado retornado via Google Cloud SQL (Alta Performance).")
        
        print(f"   └── Dados: {{ id: {random.randint(1, 100)}, status: 'ok' }}")

    def desconectar(self):
        self.conectado = False
        print(f"zzz [{self.nome}] Conexão encerrada.\n")

# --- Simulação do Cenário da Aula (E-commerce Multi-Cloud) ---

def main():
    print("=== ☁️  Simulador de Infraestrutura Multi-Cloud  ☁️ ===\n")

    # 1. Instanciando os conectores (como se tivéssemos contratado os serviços)
    aws_db = CloudDatabaseProvider("AWS", "Amazon Aurora (PostgreSQL)")
    azure_db = CloudDatabaseProvider("Azure", "Azure SQL Database")
    gcp_db = CloudDatabaseProvider("GCP", "Google Cloud SQL (MySQL)")

    # Cenário 1: O E-commerce processando uma venda crítica (AWS Aurora)
    print("--- Cenário 1: Venda Crítica (Alta Disponibilidade) ---")
    aws_db.conectar()
    aws_db.executar_query("INSERT INTO vendas (valor) VALUES (150.00)")
    aws_db.desconectar()

    # Cenário 2: O RH consultando dados corporativos (Azure)
    print("--- Cenário 2: Consulta Interna Corporativa (Ecossistema Microsoft) ---")
    azure_db.conectar()
    azure_db.executar_query("SELECT * FROM funcionarios WHERE id = 42")
    azure_db.desconectar()

    # Cenário 3: Analytics e Big Data (GCP)
    print("--- Cenário 3: Análise de Dados Massiva (Performance) ---")
    gcp_db.conectar()
    gcp_db.executar_query("SELECT AVG(ticket_medio) FROM historico_vendas")
    gcp_db.desconectar()

if __name__ == "__main__":
    main()