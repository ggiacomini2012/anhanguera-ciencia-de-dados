import time
import random
from datetime import datetime

# --- Simulação de Arquitetura de Dados em Nuvem e Distribuída (Inventário em Varejo) ---

# O "Servidor Central" na Nuvem (simulado por um dicionário Python)
CLOUD_INVENTORY_DB = {
    "SKU-100": {"nome": "Camiseta Básica", "estoque": 500, "localizacoes": ["SP", "RJ", "Online"]},
    "SKU-201": {"nome": "Calça Jeans Premium", "estoque": 250, "localizacoes": ["SP", "RJ", "Online"]},
    "SKU-302": {"nome": "Tênis Esportivo", "estoque": 800, "localizacoes": ["SP", "RJ", "Online"]},
}

# --- Funções do Servidor (Nuvem) ---

def provisionar_recursos_nuvem(capacidade_atual, demanda_esperada):
    """
    Simula a escalabilidade sob demanda, uma característica chave da Nuvem.
    Se a demanda esperada for maior que 80% da capacidade, 'escala-se' a infraestrutura.
    """
    print("☁️ Verificando capacidade da Nuvem...")
    if demanda_esperada > (capacidade_atual * 0.8):
        nova_capacidade = capacidade_atual * 2  # Escala o dobro
        print(f"✅ ESCALABILIDADE ATIVADA: Capacidade dobrou de {capacidade_atual} para {nova_capacidade}.")
        return nova_capacidade
    else:
        print(f"🔄 Capacidade OK ({capacidade_atual}). Nível de uso atual: {demanda_esperada / capacidade_atual * 100:.2f}%.")
        return capacidade_atual

def buscar_estoque_global(sku):
    """Simula a consulta global ao banco de dados em nuvem, acessível por todos os clientes."""
    if sku in CLOUD_INVENTORY_DB:
        item = CLOUD_INVENTORY_DB[sku]
        print(f"\n🔍 Consulta Global ({datetime.now().strftime('%H:%M:%S')}):")
        print(f"   Produto: {item['nome']} (SKU: {sku})")
        print(f"   Estoque Total: {item['estoque']}")
        print(f"   Disponível em: {', '.join(item['localizacoes'])}")
        return item['estoque']
    else:
        print(f"\n❌ Produto {sku} não encontrado no sistema.")
        return 0

# --- Funções dos Clientes (Lojas / E-commerce) ---

def realizar_venda(sku, quantidade, local):
    """
    Simula a transação de venda e a atualização ACID (Atomicidade) no sistema distribuído.
    Se o estoque for suficiente, a transação é commitada.
    """
    global CLOUD_INVENTORY_DB
    
    if sku not in CLOUD_INVENTORY_DB:
        print(f"⚠️ Venda Falha em {local}: Produto {sku} inexistente.")
        return False
        
    estoque_atual = CLOUD_INVENTORY_DB[sku]["estoque"]
    
    # 1. Isolamento (Garantindo que a leitura do estoque seja a mais recente)
    time.sleep(0.01) 
    
    if estoque_atual >= quantidade:
        try:
            # 2. Atomicidade (A operação deve ser total ou nada)
            novo_estoque = estoque_atual - quantidade
            
            # Simula o COMMIT/escrita no DB em Nuvem (Sincronização em Tempo Real)
            CLOUD_INVENTORY_DB[sku]["estoque"] = novo_estoque
            
            # 3. Durabilidade (A mudança persistiu)
            print(f"✅ Venda SUCESSO em {local} ({datetime.now().strftime('%H:%M:%S')}):")
            print(f"   -> {quantidade} un. de {CLOUD_INVENTORY_DB[sku]['nome']} vendidas.")
            print(f"   -> Novo Estoque Global (Consistência): {novo_estoque}.")
            
            # Simulação do processamento distribuído (diminuição da demanda local após a venda)
            return True
            
        except Exception as e:
            # Simula o ROLLBACK
            print(f"🔥 ERRO DE TRANSAÇÃO: {e}. Estoque não foi alterado (Rollback).")
            return False
    else:
        print(f"⛔ Venda Falha em {local}: Estoque Insuficiente! Apenas {estoque_atual} restantes.")
        return False

# ----------------- Fluxo de Simulação -----------------

print("===================================================================")
print("     SIMULAÇÃO DE ARQUITETURA DISTRIBUÍDA EM NUVEM (Varejo)       ")
print("===================================================================")

# 1. Cliente E-commerce verifica estoque para pedido grande (Consulta Global)
print("\n--- PASSO 1: Cliente E-commerce (Nó) Consulta Estoque Global ---")
buscar_estoque_global("SKU-100")


# 2. Lojas fazem vendas simultâneas (Sincronização em Tempo Real)
print("\n--- PASSO 2: Transações Simultâneas (SP, RJ, Online) ---")

# Venda na loja de São Paulo
realizar_venda("SKU-100", 50, "Loja-SP")

# Cliente Online faz um pedido grande (exigindo alta disponibilidade da nuvem)
realizar_venda("SKU-100", 400, "E-commerce-Online")

# Venda na loja do Rio de Janeiro
realizar_venda("SKU-100", 10, "Loja-RJ")

# 3. Tentativa de venda de item com estoque insuficiente (Teste de Atomicidade/Consistência)
print("\n--- PASSO 3: Tentativa de Venda Insuficiente (Garantia ACID) ---")
realizar_venda("SKU-100", 100, "Loja-SP") # Deve falhar, pois o estoque deve estar em 40 (500-50-400-10)

# 4. Demonstração de Escalabilidade da Nuvem
print("\n--- PASSO 4: Gerenciamento de Infraestrutura (Nuvem) ---")
capacidade_atual_servidor = 1000  # Ex: 1000 transações/segundo
demanda_pico = 950                # Ex: 950 transações/segundo esperadas na Black Friday

capacidade_atual_servidor = provisionar_recursos_nuvem(capacidade_atual_servidor, demanda_pico)

demanda_normal = 300
capacidade_atual_servidor = provisionar_recursos_nuvem(capacidade_atual_servidor, demanda_normal)

print("\n===================================================================")
print("  Conclusão: O sistema distribuído em nuvem garante coerência (ACID)")
print("  e flexibilidade (escalabilidade) para o varejo multicanal.")
print("===================================================================")