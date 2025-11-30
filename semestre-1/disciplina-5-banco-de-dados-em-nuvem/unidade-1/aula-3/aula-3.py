# Arquivo: aula-3.py
import random
import time

# --- 1. SIMULAÇÃO DE MULTI-TENANCY (Isolamento Lógico) ---

class BancoDeDadosMultiTenant:
    """
    Representa um único Banco de Dados que hospeda múltiplos inquilinos (tenants).
    Os dados são isolados logicamente usando o 'tenant_id'.
    """
    def __init__(self):
        # Dicionário onde a chave é o tenant_id e o valor é uma lista de dados.
        self.dados = {}
        print("🛠️ Banco de Dados Multi-Tenant inicializado.")

    def adicionar_dados(self, tenant_id, dado):
        """Adiciona um novo dado, garantindo que vá para o espaço do tenant correto."""
        if tenant_id not in self.dados:
            self.dados[tenant_id] = []
            print(f"   [Tenant {tenant_id}] Novo inquilino provisionado (novo 'quarto' no hotel).")

        self.dados[tenant_id].append(dado)
        print(f"   [Tenant {tenant_id}] Dado '{dado}' armazenado com sucesso.")

    def buscar_dados(self, tenant_id):
        """Busca dados, garantindo que apenas os dados do tenant sejam retornados."""
        return self.dados.get(tenant_id, [])

# --- 2. SIMULAÇÃO DE ELASTICIDADE (Ajuste Automático de Recursos) ---

class ProvedorDeNuvemElastico:
    """
    Simula a capacidade de escalar recursos (Elasticidade Horizontal)
    com base na demanda.
    """
    def __init__(self, capacidade_inicial=1):
        self.capacidade_servidores = capacidade_inicial  # Número de instâncias/servidores ativos
        self.limite_uso_para_escalar = 0.7  # 70% de uso
        self.uso_atual = 0.0
        print(f"☁️ Provedor de Nuvem iniciado com {self.capacidade_servidores} servidor(es).")

    def monitorar_e_ajustar(self, demanda_total):
        """Monitora a demanda e executa a elasticidade (Scale Up/Down)."""
        
        # Uso (Demanda / Capacidade Máxima do Servidor * Número de Servidores)
        self.uso_atual = demanda_total / (10 * self.capacidade_servidores)
        
        print(f"\n📈 Monitoramento: Uso atual é de {self.uso_atual:.2f} (Limite para Scale Up: {self.limite_uso_para_escalar}).")

        # --- ELASTICIDADE: SCALE UP (Escalar para Cima) ---
        if self.uso_atual > self.limite_uso_para_escalar:
            self.capacidade_servidores += 1
            print(f"🔥 ALERTA DE PICO! Executando Scale-Out (Elasticidade).")
            print(f"   Capacidade ajustada para {self.capacidade_servidores} servidor(es).")
            # Recalcula o uso após o Scale-Up
            self.uso_atual = demanda_total / (10 * self.capacidade_servidores)
            print(f"   Novo uso após Scale-Out: {self.uso_atual:.2f}")
            return True
        
        # --- ELASTICIDADE: SCALE DOWN (Escalar para Baixo) ---
        elif self.uso_atual < 0.3 and self.capacidade_servidores > 1:
            self.capacidade_servidores -= 1
            print(f"🌬️ DEMANDA BAIXA. Executando Scale-Down (Otimização de Custos).")
            print(f"   Capacidade ajustada para {self.capacidade_servidores} servidor(es).")
            return True
        
        else:
            print("🟢 Uso normal. Mantendo capacidade estável.")
            return False

# --- FLUXO PRINCIPAL DE SIMULAÇÃO ---

# 1. Configurar o ambiente Multi-Tenancy e Elástico
db = BancoDeDadosMultiTenant()
nuvem = ProvedorDeNuvemElastico()

print("\n" + "="*50)
print("1ª RODADA: Demanda Baixa e Multi-Tenancy")
print("="*50)

# Multi-Tenancy em Ação
db.adicionar_dados(tenant_id=101, dado="Fatura_Jan_2025") # Cliente A
db.adicionar_dados(tenant_id=202, dado="Config_Especial_X") # Cliente B
db.adicionar_dados(tenant_id=101, dado="Relatorio_Vendas") # Cliente A

# Teste de Isolamento: Apenas o Cliente A vê seus dados
dados_cliente_a = db.buscar_dados(tenant_id=101)
print(f"\n🔑 Verificando Isolamento (Tenant 101): {dados_cliente_a}")


# Simulação de Elasticidade com Demanda Baixa
demanda_baixa = 5 
nuvem.monitorar_e_ajustar(demanda_baixa)


print("\n" + "="*50)
print("2ª RODADA: Pico de Demanda (Black Friday) - Elasticidade em Ação")
print("="*50)

# Simulação de Elasticidade com Demanda Alta
demanda_alta = 25 # Carga que excede 70% de 1 servidor (10 * 1)
nuvem.monitorar_e_ajustar(demanda_alta)

# O sistema faz um reajuste (Scale-Out) e processa a carga com mais capacidade
print(f"\n🔄 Carga de trabalho processada usando {nuvem.capacidade_servidores} servidor(es).")


print("\n" + "="*50)
print("3ª RODADA: Retorno à Normalidade - Otimização de Custos")
print("="*50)

# Simulação de Elasticidade com Demanda Mínima
demanda_minima = 2 # Carga que fica abaixo de 30% de 2 servidores
nuvem.monitorar_e_ajustar(demanda_minima)

# O sistema faz um reajuste (Scale-Down) para economizar
print(f"\n✅ Sistema estabilizado, otimizando custos com {nuvem.capacidade_servidores} servidor(es).")