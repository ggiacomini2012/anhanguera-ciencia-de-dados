"""
Normalização de Dados em Python: Um Exemplo Prático

Este script demonstra o processo de normalização de dados (1FN, 2FN e 3FN)
usando listas de dicionários em Python para simular tabelas de banco de dados.

Imagine que temos uma única "tabela" desorganizada de funcionários, e nosso
objetivo é aplicar as regras de normalização para torná-la mais eficiente
e robusta.
"""

# --- Dados Iniciais (Tabela Não Normalizada) ---
print("--- 📝 Tabela Original (Não Normalizada) ---")
funcionarios_nao_normalizados = [
    {
        "matriculaFunc": "148-9",
        "nome": "Jane Anne",
        "idCargo": 191,
        "descCargo": "Analista Contábil I",
        "cidade_e_depto": "Curitiba, Contabilidade", # Exemplo de campo não atômico
        "data_de_admissao": "15/01/2018"
    },
    {
        "matriculaFunc": "721-4",
        "nome": "Klaus Lins",
        "idCargo": 323,
        "descCargo": "Assistente de Produção II",
        "cidade_e_depto": "São Paulo, Produção",
        "data_de_admissao": "21/11/2017"
    },
    {
        "matriculaFunc": "673-2",
        "nome": "Sandra Costa",
        "idCargo": 101,
        "descCargo": "Auxiliar de DP",
        "cidade_e_depto": "Santo André, RH",
        "data_de_admissao": "03/04/2018"
    }
]

# Função auxiliar para imprimir tabelas
def imprimir_tabela(tabela, nome):
    print(f"\n✅ Tabela '{nome}':")
    if not tabela:
        print("  (Vazia)")
        return
    
    # Pega as chaves do primeiro dicionário para os cabeçalhos
    cabecalhos = list(tabela[0].keys())
    print(" | ".join(cabecalhos))
    print("-" * (len(" | ".join(cabecalhos)) + 2))
    for linha in tabela:
        valores = [str(linha.get(h, '')) for h in cabecalhos]
        print(" | ".join(valores))

imprimir_tabela(funcionarios_nao_normalizados, "Funcionários Não Normalizados")

# --- Passo 1: Normalização para a Primeira Forma Normal (1FN) ---
print("\n--- 🚀 Aplicando a 1FN: Tornando os dados atômicos ---")
"""
Problema: O campo 'cidade_e_depto' contém múltiplos valores.
Solução: Dividir este campo em 'cidade' e 'departamento'.
Adicionamos 'idCidade' e 'idDepartamento' para simular a criação de chaves.
Isso também prepara o terreno para as próximas formas normais.
"""
funcionarios_1fn = []
cidades = {}
departamentos = {}
cidade_id_counter = 1
depto_id_counter = 1

for f in funcionarios_nao_normalizados:
    cidade_nome, depto_nome = f["cidade_e_depto"].split(', ')

    # Normalizando cidades
    if cidade_nome not in cidades:
        cidades[cidade_nome] = cidade_id_counter
        cidade_id_counter += 1
    
    # Normalizando departamentos
    if depto_nome not in departamentos:
        departamentos[depto_nome] = depto_id_counter
        depto_id_counter += 1

    # Criando a nova linha para a tabela de funcionários
    novo_funcionario = {
        "matriculaFunc": f["matriculaFunc"],
        "nome": f["nome"],
        "idCargo": f["idCargo"],
        "descCargo": f["descCargo"],
        "idCidade": cidades[cidade_nome],
        "idDepartamento": departamentos[depto_nome],
        "data_de_admissao": f["data_de_admissao"]
    }
    funcionarios_1fn.append(novo_funcionario)

# Criando as novas tabelas normalizadas
tabela_cidades_1fn = [{"idCidade": id, "cidade": nome} for nome, id in cidades.items()]

imprimir_tabela(funcionarios_1fn, "Funcionários (em 1FN)")
imprimir_tabela(tabela_cidades_1fn, "Cidades (em 1FN)")

# --- Passo 2: Normalização para a Segunda Forma Normal (2FN) ---
print("\n--- 📈 Aplicando a 2FN: Dependência Total da Chave Primária ---")
"""
Problema: A tabela 'Funcionários' ainda contém o campo 'descCargo', que
depende apenas do 'idCargo' e não da chave primária composta ('matriculaFunc' e 'idCargo').
Solução: Mover a descrição do cargo para sua própria tabela.
A mesma lógica se aplica ao departamento.
"""
# Removendo 'descCargo' da tabela de funcionários
funcionarios_2fn = [
    {k: v for k, v in f.items() if k != "descCargo"} 
    for f in funcionarios_1fn
]

# Criando a nova tabela de Cargos
cargos = {}
for f in funcionarios_nao_normalizados:
    cargos[f["idCargo"]] = f["descCargo"]

tabela_cargos_2fn = [{"idCargo": id, "descCargo": desc} for id, desc in cargos.items()]

# Removendo 'idDepartamento' da tabela de funcionários e criando a tabela de departamentos
departamentos = {}
for f in funcionarios_1fn:
    if f["idDepartamento"] not in departamentos:
        departamentos[f["idDepartamento"]] = f["idDepartamento"]

tabela_departamentos_2fn = [{"idDepartamento": id, "departamento": depto} for depto, id in departamentos.items()]

# A tabela de Funcionários em 2FN agora não possui 'descCargo'
funcionarios_2fn = [
    {k: v for k, v in f.items() if k not in ["descCargo", "idDepartamento"]}
    for f in funcionarios_1fn
]

imprimir_tabela(funcionarios_2fn, "Funcionários (em 2FN)")
imprimir_tabela(tabela_cargos_2fn, "Cargos (em 2FN)")
imprimir_tabela(tabela_departamentos_2fn, "Departamentos (em 2FN)")

# --- Passo 3: Normalização para a Terceira Forma Normal (3FN) ---
print("\n--- 🎯 Aplicando a 3FN: Eliminando Dependências Transitivas ---")
"""
A tabela 'Funcionários' na 2FN já está bem organizada, mas observe que
a 'cidade' e o 'departamento' que ainda estão ligadas por IDs na tabela
'Funcionários' e poderiam ter seus próprios campos. 
A tabela 'Funcionários' na 2FN já está bem organizada e não apresenta 
dependências transitivas evidentes neste exemplo. Se houvesse, como 
um campo 'nome_departamento' que depende de 'idDepartamento' (e não da chave primária),
ele seria removido. O que fizemos na 2FN já cobre o principal do 3FN aqui.
"""
print("\n✔️  Neste exemplo, a tabela de 'Funcionários' já está em 3FN após a aplicação da 2FN, pois não há dependências transitivas.")
print("    O campo 'descCargo' (que dependia de 'idCargo', não da chave primária 'matriculaFunc') foi movido para sua própria tabela.")

# As tabelas finais, após o processo de normalização completo, são:
print("\n--- ✨ Estado Final: Tabelas Normalizadas ---")
print("Este é o nosso modelo final, otimizado para eficiência e integridade.")
imprimir_tabela(funcionarios_2fn, "Funcionários Normalizado")
imprimir_tabela(tabela_cargos_2fn, "Cargos")
imprimir_tabela(tabela_cidades_1fn, "Cidades")
imprimir_tabela(tabela_departamentos_2fn, "Departamentos")

print("\n--- Fim do Processo de Normalização ---")