
import json

# --- 1. DADOS ESTRUTURADOS (A Tabela Perfeita) ---
# Em Python, representamos dados estruturados, como os de um banco de dados relacional (SQL), 
# usando uma Lista de Dicionários, onde cada Dicionário tem chaves fixas (colunas).

print("--- 1. DADOS ESTRUTURADOS (Lista de Dicionários) ---")

# A 'tabela' de clientes (como a Tabela 1 da explicação)
clientes_estruturados = [
    {
        "id_cliente": 1, 
        "nome": "Mario de Souza", 
        "cpf": "111.111.111-11", 
        "satisfacao_estrelas": 5
    },
    {
        "id_cliente": 2, 
        "nome": "Anderson Inácio", 
        "cpf": "222.222.222-22", 
        "satisfacao_estrelas": 3
    },
    # Nota: A estrutura (chaves) é a mesma para todos os registros.
]

# Exemplo de consulta (Análise estruturada fácil)
media_satisfacao = sum(c['satisfacao_estrelas'] for c in clientes_estruturados) / len(clientes_estruturados)
print(f"Média de Satisfação do Cliente (fácil de calcular): {media_satisfacao:.2f} estrelas")
print(f"Registro do Cliente ID 1: {clientes_estruturados[0]}")
print("-" * 50)


# --- 2. DADOS NÃO ESTRUTURADOS (A Selva de Textos e Mídia) ---
# Representados por strings longas (textos livres) ou referências a arquivos de mídia (imagens, vídeos). 
# Difíceis de processar sem ferramentas de IA/NLP.

print("--- 2. DADOS NÃO ESTRUTURADOS (Texto Livre e Mídia) ---")

# Feedback de cliente em texto livre (avaliação de produto)
feedback_texto_livre = (
    "O produto é bom, mas a embalagem veio amassada. "
    "A cor não era exatamente o que eu esperava, mas o material é de alta qualidade. "
    "Vou anexar uma foto do defeito."
)

# Referência a um arquivo de mídia (que precisaria de Visão Computacional)
caminho_arquivo_foto = "caminho/para/foto_unboxing_cliente_2.jpg"

print(f"Trecho do Feedback: '{feedback_texto_livre[:60]}...'")
print(f"Caminho do Arquivo de Mídia: {caminho_arquivo_foto}")

# Para analisar isso, precisaríamos de uma biblioteca de NLP (ex: NLTK, SpaCy)
# Exemplo de análise superficial de sentimento (simulada)
if 'alta qualidade' in feedback_texto_livre.lower():
    print("Análise Simples: Detectado termo 'alta qualidade' (positivo).")
print("-" * 50)


# --- 3. DADOS PARCIALMENTE ESTRUTURADOS (JSON Flexível) ---
# Usamos o formato JSON (representado por Dicionários em Python)
# Ele combina chaves fixas com a flexibilidade de incluir ou omitir informações e usar listas/textos livres.

print("--- 3. DADOS PARCIALMENTE ESTRUTURADOS (JSON) ---")

# Avaliação do cliente A - Inclui informações detalhadas
avaliacao_a = {
    "id_avaliacao": "rev_001",
    "id_produto": "PROD-42",
    "data": "2025-10-12",
    "estrelas": 4, # Estruturado
    "comentario_livre": "Adorei a velocidade de entrega, mas senti falta de um manual em português.", # Não Estruturado
    "tags": ["entrega_rapida", "falta_manual"] # Lista flexível
}

# Avaliação do cliente B - Estrutura um pouco diferente (sem 'tags' ou 'data')
avaliacao_b = {
    "id_avaliacao": "rev_002",
    "id_produto": "PROD-18",
    "estrelas": 5,
    "comentario_livre": "Simplesmente perfeito! O melhor produto que comprei este ano.",
    # 'data' e 'tags' foram omitidos, o que é comum em NoSQL/JSON
}

# Convertendo para a string JSON (formato de transporte de dados)
json_a = json.dumps(avaliacao_a, indent=4, ensure_ascii=False)
print("\nJSON da Avaliação A:")
print(json_a)

# Demonstração da flexibilidade (acessando campos existentes e tratando ausentes)
print(f"\nEstrelas da Avaliação B: {avaliacao_b['estrelas']}")
# Usamos .get() para acessar 'data' de forma segura, retornando 'N/A' se não existir.
print(f"Data da Avaliação B (campo flexível): {avaliacao_b.get('data', 'N/A')}")
print("-" * 50)