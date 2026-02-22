import random

# 1. DEFINIÇÃO DA POPULAÇÃO 🏫
# Vamos criar uma lista de 1000 'ID's de alunos, como se fosse o banco de dados de uma escola.
populacao = list(range(1, 1001))

def realizar_amostragem(tamanho_amostra):
    print(f"--- Iniciando Amostragem Aleatória Simples (n={tamanho_amostra}) ---")
    
    # 2. REPRODUTIBILIDADE (SEED) 🔁
    # Definir uma semente garante que o 'aleatório' seja o mesmo toda vez que rodarmos.
    # Útil para estudos científicos onde outros precisam conferir seus dados!
    random.seed(42)
    
    # 3. SELEÇÃO ALEATÓRIA 🎲
    # O método random.sample garante que:
    # - Cada elemento tenha a mesma chance de ser escolhido.
    # - A amostragem seja SEM reposição (um aluno não sai duas vezes).
    amostra = random.sample(populacao, k=tamanho_amostra)
    
    return amostra

# Executando o exemplo
tamanho_n = 10
minha_amostra = realizar_amostragem(tamanho_n)

print(f"Alunos selecionados para a pesquisa: \n{minha_amostra}")
print("-" * 50)

# 4. ILUSTRANDO O CONCEITO DE VIÉS (SEM SEED) 🚨
# Se não usarmos a semente, a cada 'colherada' na sopa, teremos um resultado diferente.
print("Sorteio rápido sem semente (mudará a cada execução):")
print(random.sample(populacao, k=5))