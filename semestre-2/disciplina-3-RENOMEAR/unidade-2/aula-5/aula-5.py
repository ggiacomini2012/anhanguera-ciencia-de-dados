# Simulação de Padrões de Arquitetura de Dados e Gerenciamento de Dados Mestres (MDM)
# Contexto: E-commerce expandindo para vendas móveis (Sistemas Distribuídos e Azure)

import uuid

# 1. Simulação do Repositório de Dados Principal (SQL/Legacy System)
# Armazena dados de clientes com alta consistência.
def get_customer_id():
    """Gera um ID único para o cliente mestre."""
    return str(uuid.uuid4())[:8].upper()

CLIENTES_PRINCIPAL = {
    # { customer_id: [Nome, Email, Endereco, Status_MDM] }
    "C4A1B2D3": ["Maria Oliveira", "maria.o@email.com", "Rua A, 123", "Mestre"]
}

# 2. Simulação do Repositório de Dados Móveis (Azure/Cloud Storage)
# Armazena dados de clientes provenientes do app móvel. Pode haver inconsistências.
CLIENTES_AZURE = {
    "maria_mobile_01": ["Maria O.", "maria.o@email.com", "Rua A", "Pendente"],
    "novo_cliente_2025": ["João S.", "joao.silva@teste.com", "Av. Central", "Pendente"]
}

# 3. Gerenciamento de Dados Mestres (MDM) - O "Guardião da Verdade"
def sincronizar_cliente_mdm(fonte_origem: str, dados_cliente: list):
    """
    Simula o processo de um Data Steward (ou sistema MDM) para harmonizar dados.
    Esta é a aplicação do 'Padrão MDM'.
    """
    nome_origem, email_origem, endereco_origem, status_origem = dados_cliente

    # Tenta encontrar correspondência pelo email (chave de ouro)
    for master_id, master_data in CLIENTES_PRINCIPAL.items():
        if master_data[1] == email_origem:
            print(f"🔗 MATCH ENCONTRADO: O cliente {nome_origem} (do {fonte_origem}) é o Master ID {master_id}.")
            
            # Aplica a Regra de Ouro (ex: prioriza o endereço do sistema principal)
            CLIENTES_PRINCIPAL[master_id][3] = "Mestre/Atualizado"
            print(f"✅ DADOS PRINCIPAIS ATUALIZADOS: Status alterado para '{CLIENTES_PRINCIPAL[master_id][3]}'")
            return master_id
    
    # Se não encontrou, cria um novo registro mestre
    novo_master_id = get_customer_id()
    CLIENTES_PRINCIPAL[novo_master_id] = [nome_origem, email_origem, endereco_origem, "Mestre"]
    print(f"✨ NOVO REGISTRO MESTRE CRIADO: Master ID {novo_master_id} para {nome_origem}.")
    return novo_master_id

# 4. Implementação do Fluxo (Aplicação da Arquitetura Distribuída)
def processar_dados_azure():
    """
    Simula a ingestão de dados de um sistema distribuído (Azure) para o núcleo (MDM).
    Isso é um exemplo do fluxo de um 'Modelo de Área de Interesse' (Vendas Móveis).
    """
    print("--- 📱 INICIANDO INGESTÃO DE DADOS MÓVEIS (AZURE) ---")
    
    for azure_id, dados in CLIENTES_AZURE.items():
        print(f"\n-> Processando registro do Azure ID: {azure_id}")
        master_id = sincronizar_cliente_mdm("Azure", dados)
        
        # Simula a comunicação entre os sistemas (Padrões de Sistemas Distribuídos)
        print(f"   [COMUNICAÇÃO OK] O sistema Azure agora referencia o Master ID: {master_id}")
        
        # Atualiza o status no Azure (opcionalmente, pode ser o Master ID)
        CLIENTES_AZURE[azure_id][3] = f"Mapeado para {master_id}"

# --- EXECUTANDO A SIMULAÇÃO ---

print("--- ESTADO INICIAL DOS DADOS ---")
print("Clientes Principais (SQL):", CLIENTES_PRINCIPAL)
print("Clientes Azure (Móvel):", CLIENTES_AZURE)
print("\n==================================")

# Executa o MDM para harmonizar os dados móveis com os dados mestres
processar_dados_azure()

print("\n==================================")
print("--- ESTADO FINAL APÓS O PROCESSO MDM ---")
print("Clientes Principais (A VERDADE MESTRE):")
# Note que a entrada "Maria Oliveira" foi atualizada (status 'Mestre/Atualizado')
# e "João S." foi adicionado como um novo registro mestre.
for cid, cdata in CLIENTES_PRINCIPAL.items():
    print(f"  {cid}: {cdata[0]} | Email: {cdata[1]} | Status: {cdata[3]}")
    
print("\nClientes Azure (Mapeados):")
# Note que os registros móveis agora sabem qual é o seu ID mestre correspondente.
for aid, adata in CLIENTES_AZURE.items():
    print(f"  {aid}: {adata[0]} | Status: {adata[3]}")

# Conclusão da Simulação:
# A arquitetura (neste caso, o código Python) permitiu a comunicação entre o sistema Azure
# e o sistema principal, garantindo que os Data Stewards (função MDM) pudessem manter 
# a "Única Versão da Verdade" sobre o cliente, resolvendo a duplicidade de "Maria".
# Este é um exemplo de como a aplicação de Padrões de Arquitetura e MDM (Gerenciamento de Dados Mestres)
# impulsiona o sucesso das organizações.