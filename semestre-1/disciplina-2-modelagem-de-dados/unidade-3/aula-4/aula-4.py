# Este código simula a funcionalidade de uma ferramenta CASE.
# O objetivo é exemplificar a "engenharia direta" (forward engineering),
# gerando um script SQL a partir de um modelo de dados Python.

# 1. Definição do Modelo de Dados (equivalente ao DER em uma ferramenta CASE)
# Vamos modelar um sistema simples de "Biblioteca" com duas tabelas: 'Autores' e 'Livros'.

modelo_dados = {
    "Autores": {
        "campos": {
            "id_autor": "INTEGER PRIMARY KEY",
            "nome": "VARCHAR(100) NOT NULL",
            "nacionalidade": "VARCHAR(50)"
        }
    },
    "Livros": {
        "campos": {
            "id_livro": "INTEGER PRIMARY KEY",
            "titulo": "VARCHAR(255) NOT NULL",
            "ano_publicacao": "INTEGER",
            "id_autor": "INTEGER"
        },
        "relacionamentos": {
            "id_autor": {
                "referencia_tabela": "Autores",
                "referencia_campo": "id_autor"
            }
        }
    }
}

# 2. Funções de Geração (o coração da nossa "ferramenta CASE" simulada)

def gerar_script_sql(modelo_dados):
    """
    Gera um script SQL de criação de tabelas a partir de um modelo de dados.
    Esta função simula o "forward engineering".
    """
    script_sql = ""
    for nome_tabela, dados_tabela in modelo_dados.items():
        # Inicia a criação da tabela
        script_sql += f"CREATE TABLE {nome_tabela} (\n"
        
        # Adiciona os campos
        campos = []
        for campo, tipo in dados_tabela["campos"].items():
            campos.append(f"    {campo} {tipo}")
        
        # Adiciona relacionamentos (chaves estrangeiras)
        if "relacionamentos" in dados_tabela:
            for campo_fk, dados_fk in dados_tabela["relacionamentos"].items():
                ref_tabela = dados_fk["referencia_tabela"]
                ref_campo = dados_fk["referencia_campo"]
                campos.append(f"    FOREIGN KEY ({campo_fk}) REFERENCES {ref_tabela}({ref_campo})")
                
        script_sql += ",\n".join(campos)
        script_sql += "\n);\n\n"
        
    return script_sql

# 3. Execução do Programa e Exibição do Resultado
if __name__ == "__main__":
    print("Iniciando a simulação da ferramenta CASE...\n")
    print("Gerando o script SQL a partir do modelo de dados...\n")
    
    script_gerado = gerar_script_sql(modelo_dados)
    
    print("--- Script SQL Gerado (Forward Engineering) ---\n")
    print(script_gerado)
    print("-----------------------------------------------\n")
    print("Processo concluído. O script pode ser usado para criar o banco de dados físico.")