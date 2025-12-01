# aula-2.py
# Simulação dos Princípios da Computação em Nuvem (IaaS, PaaS, SaaS)
# Tópico: Tipos de Nuvens, Modelos de Serviço e Segurança.

import random

# --- 1. CONFIGURAÇÕES BÁSICAS ---
# Simula a capacidade inicial e os custos
CAPACIDADE_FISICA_MAXIMA = 50  # Infraestrutura Local (antiga)
CUSTO_IASS_POR_UNIDADE = 0.5   # Custo por Unidade de Recurso na Nuvem
CUSTO_PAAS_POR_UNIDADE = 0.8   # Custo por Unidade de Recurso com Plataforma
CUSTO_SAAS_POR_USUARIO = 1.0   # Custo por Usuário (RH/Colaboração)

# --- 2. FUNÇÕES DE SIMULAÇÃO DOS MODELOS DE SERVIÇO ---

def gerenciar_iaas(recursos_solicitados):
    """
    Simula a Infraestrutura como Serviço (IaaS).
    Usuário gerencia o SO e Aplicação, mas a escalabilidade é automática.
    """
    print("--- 🛠️ IaaS: Infraestrutura como Serviço (Amazon EC2 / AWS) ---")
    if recursos_solicitados > CAPACIDADE_FISICA_MAXIMA:
        print(f"✅ Sucesso! Escalabilidade Automática. {recursos_solicitados} VMs provisionadas.")
        print(f"   (Antigamente, seria necessário comprar um novo servidor!)")
    else:
        print(f"✅ {recursos_solicitados} VMs provisionadas sob demanda.")

    custo_total = recursos_solicitados * CUSTO_IASS_POR_UNIDADE
    return custo_total

def gerenciar_paas(linhas_de_codigo):
    """
    Simula a Plataforma como Serviço (PaaS).
    O foco está no código, a plataforma gerencia o resto (SO, servidores).
    """
    print("\n--- 🧑‍💻 PaaS: Plataforma como Serviço (Google App Engine) ---")
    velocidade_dev = linhas_de_codigo / 10 # Simula a velocidade aumentada

    if velocidade_dev > 50:
        print(f"✅ Desenvolvimento Ágil! Lançamento Rápido de 🚀 novos recursos.")
        print(f"   Desenvolvedores focaram em {linhas_de_codigo} linhas de código, PaaS gerenciou a infra.")
    else:
        print(f"⚠️ PaaS em Ação: Ambiente pronto. Foco no código.")

    # PaaS tem um custo marginalmente maior por recurso, mas otimiza o tempo
    custo_total = linhas_de_codigo * CUSTO_PAAS_POR_UNIDADE / 100
    return custo_total

def usar_saas(num_usuarios):
    """
    Simula o Software como Serviço (SaaS).
    Zero manutenção, apenas uso. Focado em aplicativos prontos (RH, Colaboração).
    """
    print("\n--- ☁️ SaaS: Software como Serviço (Microsoft 365 / Salesforce) ---")
    atualizacao_disponivel = random.choice([True, False])

    if atualizacao_disponivel:
        print(f"✅ Manutenção Zero! O provedor SaaS aplicou a atualização automaticamente.")
    
    print(f"   {num_usuarios} usuários acessando o sistema de RH/Colaboração imediatamente.")
    
    custo_total = num_usuarios * CUSTO_SAAS_POR_USUARIO
    return custo_total

# --- 3. SIMULAÇÃO DO CENÁRIO DA EMPRESA DE VAREJO ---

def executar_migracao():
    print("===================================================")
    print("  MIGRAÇÃO PARA NUVEM: EMPRESA DE VAREJO (Aula 2)  ")
    print("===================================================")

    # 1. Desafio de Infraestrutura (IaaS)
    print("\n[FASE 1: INFRAESTRUTURA DESATUALIZADA -> IaaS]")
    recursos_atuais_necessarios = 75
    custo_iaas = gerenciar_iaas(recursos_atuais_necessarios)
    
    # 2. Desafio de Desenvolvimento (PaaS)
    print("\n[FASE 2: DESENVOLVIMENTO LENTO -> PaaS]")
    codigos_desenvolvidos = 1500
    custo_paas = gerenciar_paas(codigos_desenvolvidos)

    # 3. Desafio Administrativo (SaaS)
    print("\n[FASE 3: SISTEMAS ADMINISTRATIVOS -> SaaS]")
    total_colaboradores = 200
    custo_saas = usar_saas(total_colaboradores)

    # 4. Resultados Finais
    print("\n--- 💰 Resultados e Custo-Efetividade ---")
    custo_total_nuvem = custo_iaas + custo_paas + custo_saas
    
    # Simulação de custo fixo antigo (apenas para comparação)
    # Assumindo que a infraestrutura local custava um valor fixo muito alto
    custo_fixo_antigo = 4000 
    
    print(f"Custo Simulado IaaS (Pay-as-you-go): $ {custo_iaas:.2f}")
    print(f"Custo Simulado PaaS (Tempo/Recursos): $ {custo_paas:.2f}")
    print(f"Custo Simulado SaaS (Por Usuário):   $ {custo_saas:.2f}")
    print(f"---------------------------------------------------")
    print(f"CUSTO TOTAL NA NUVEM:                $ {custo_total_nuvem:.2f}")
    print(f"CUSTO FIXO ANTERIOR (Estimativa):    $ {custo_fixo_antigo:.2f}")

    if custo_total_nuvem < custo_fixo_antigo:
        print("✅ EFICIÊNCIA OPERACIONAL: Economia significativa com o modelo Pay-as-you-go!")
    
    print("===================================================")

# Executa a simulação
if __name__ == "__main__":
    executar_migracao()