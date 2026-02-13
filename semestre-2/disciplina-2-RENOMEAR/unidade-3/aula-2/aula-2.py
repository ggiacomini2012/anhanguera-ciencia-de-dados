# -*- coding: utf-8 -*-

"""
Este script é uma ferramenta simples de linha de comando para auxiliar na criação
e visualização de um Dicionário de Dados para um projeto de banco de dados.

Finalidade Pedagógica:
- Exemplificar a importância da documentação e padronização, como mencionado na aula.
- Demonstrar como os metadados (nome do campo, tipo, descrição) são organizados.
- Servir como um ponto de partida para a fase de 'Desenvolvimento' do ciclo de vida
  de um banco de dados, ajudando a evitar inconsistências.
"""

import json
import os

# Estrutura principal para armazenar nosso dicionário de dados em memória
dicionario_de_dados = {}

def limpar_tela():
    """Função para limpar o console (funciona em Windows, Linux e macOS)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_tabela():
    """Coleta informações e adiciona uma nova tabela ao dicionário."""
    limpar_tela()
    print("--- Adicionar Nova Tabela ---")
    nome_tabela = input("Digite o nome da tabela (ex: funcionario): ").lower()
    
    if nome_tabela in dicionario_de_dados:
        print(f"\nA tabela '{nome_tabela}' já existe.")
        input("Pressione Enter para continuar...")
        return
        
    descricao_tabela = input(f"Digite uma breve descrição para a tabela '{nome_tabela}': ")
    
    dicionario_de_dados[nome_tabela] = {
        "descricao": descricao_tabela,
        "campos": []
    }
    print(f"\nTabela '{nome_tabela}' criada com sucesso!")
    input("Pressione Enter para continuar...")

def adicionar_campo():
    """Adiciona um novo campo (atributo) a uma tabela existente."""
    limpar_tela()
    print("--- Adicionar Novo Campo a uma Tabela ---")
    
    if not dicionario_de_dados:
        print("Nenhuma tabela foi criada ainda. Crie uma tabela primeiro.")
        input("Pressione Enter para continuar...")
        return

    print("Tabelas existentes:", ", ".join(dicionario_de_dados.keys()))
    nome_tabela = input("Digite o nome da tabela à qual deseja adicionar um campo: ").lower()

    if nome_tabela not in dicionario_de_dados:
        print(f"\nA tabela '{nome_tabela}' não foi encontrada.")
        input("Pressione Enter para continuar...")
        return

    print(f"\n--- Adicionando campo à tabela '{nome_tabela}' ---")
    campo_info = {}
    campo_info['nome'] = input("Nome do campo (ex: cd_func): ")
    campo_info['descricao'] = input("Descrição do campo (ex: Código do funcionário): ")
    campo_info['tipo'] = input("Tipo do dado (ex: VARCHAR, INTEGER, DATE): ").upper()
    campo_info['tamanho'] = input("Tamanho (deixe em branco se não aplicável, ex: -): ") or "-"
    campo_info['pk'] = input("É Chave Primária (PK)? (s/n): ").lower() == 's'
    campo_info['fk'] = input("É Chave Estrangeira (FK)? (s/n): ").lower() == 's'
    
    # Validação simples para não ser PK e FK ao mesmo tempo
    if campo_info['pk'] and campo_info['fk']:
        print("\nUm campo não pode ser PK e FK ao mesmo tempo nesta ferramenta simplificada.")
        input("Pressione Enter para tentar novamente...")
        return

    dicionario_de_dados[nome_tabela]['campos'].append(campo_info)
    print("\nCampo adicionado com sucesso!")
    input("Pressione Enter para continuar...")

def visualizar_dicionario():
    """Exibe o dicionário de dados completo de forma organizada."""
    limpar_tela()
    print("--- Dicionário de Dados Completo ---")
    
    if not dicionario_de_dados:
        print("O dicionário de dados está vazio.")
        input("Pressione Enter para voltar ao menu...")
        return

    for nome_tabela, info_tabela in dicionario_de_dados.items():
        print("\n" + "="*50)
        print(f"Tabela: {nome_tabela}")
        print(f"Descrição: {info_tabela['descricao']}")
        print("-"*50)
        
        # Cabeçalho da tabela de campos
        print(f"{'Campo':<15} | {'Descrição':<30} | {'Tipo':<10} | {'Tamanho':<10} | {'PK':<5} | {'FK':<5}")
        print(f"{'-'*15} | {'-'*30} | {'-'*10} | {'-'*10} | {'-'*5} | {'-'*5}")

        if not info_tabela['campos']:
            print("Nenhum campo definido para esta tabela.")
        else:
            for campo in info_tabela['campos']:
                pk_str = "Sim" if campo.get('pk') else "Não"
                fk_str = "Sim" if campo.get('fk') else "Não"
                print(f"{campo.get('nome', ''):<15} | {campo.get('descricao', ''):<30} | {campo.get('tipo', ''):<10} | {campo.get('tamanho', ''):<10} | {pk_str:<5} | {fk_str:<5}")
    
    print("\n" + "="*50)
    input("\nPressione Enter para voltar ao menu...")

def salvar_dicionario():
    """Salva o dicionário de dados em um arquivo JSON."""
    limpar_tela()
    print("--- Salvar Dicionário de Dados ---")
    if not dicionario_de_dados:
        print("Não há nada para salvar. O dicionário está vazio.")
        input("Pressione Enter para continuar...")
        return

    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: meu_dicionario.json): ")
    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'
        
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dicionario_de_dados, f, indent=4, ensure_ascii=False)
        print(f"\nDicionário salvo com sucesso no arquivo '{nome_arquivo}'!")
    except IOError as e:
        print(f"\nOcorreu um erro ao salvar o arquivo: {e}")
    
    input("Pressione Enter para continuar...")

def menu_principal():
    """Exibe o menu principal e gerencia a entrada do usuário."""
    while True:
        limpar_tela()
        print("========================================")
        print("  Gerenciador de Dicionário de Dados  ")
        print("========================================")
        print("1. Adicionar Nova Tabela")
        print("2. Adicionar Campo a uma Tabela")
        print("3. Visualizar Dicionário de Dados")
        print("4. Salvar Dicionário em Arquivo JSON")
        print("5. Sair")
        print("----------------------------------------")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_tabela()
        elif escolha == '2':
            adicionar_campo()
        elif escolha == '3':
            visualizar_dicionario()
        elif escolha == '4':
            salvar_dicionario()
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
