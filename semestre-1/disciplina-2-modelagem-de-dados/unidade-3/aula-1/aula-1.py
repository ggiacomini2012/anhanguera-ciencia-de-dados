# -*- coding: utf-8 -*-
#
# Arquivo: aula-1.py
# Descrição: Exemplo de modelagem de dados usando classes Python.
#             Simula as entidades e relacionamentos descritos na aula sobre DER.
#

print("📚✨ Iniciando a modelagem do sistema da editora... ✨📖\n")

# --- Entidades (nossas 'tabelas' conceituais) ---
# Cada classe representa uma entidade do nosso Diagrama de Entidade-Relacionamento (DER).

class Area:
    """Representa a entidade Áreas."""
    def __init__(self, codigo_area, descricao):
        self.codigo_area = codigo_area
        self.descricao = descricao

    def __str__(self):
        return f"Área: {self.descricao} (Cód: {self.codigo_area})"

class Formato:
    """Representa a entidade Formatos."""
    def __init__(self, codigo_formato, descricao, altura, largura):
        self.codigo_formato = codigo_formato
        self.descricao = descricao
        self.altura = altura
        self.largura = largura

    def __str__(self):
        return f"Formato: {self.descricao} ({self.altura}x{self.largura} cm)"

class Encadernacao:
    """Representa a entidade Encadernações."""
    def __init__(self, codigo_encadernacao, descricao):
        self.codigo_encadernacao = codigo_encadernacao
        self.descricao = descricao

    def __str__(self):
        return f"Encadernação: {self.descricao}"

class Autor:
    """Representa a entidade Autores."""
    def __init__(self, codigo_autor, nome, cpf, rg, telefone, data_nascimento, genero, estado_civil, local_trabalho, endereco):
        self.codigo_autor = codigo_autor
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.estado_civil = estado_civil
        self.local_trabalho = local_trabalho
        self.endereco = endereco # Endereço é um atributo composto (Dicionário)

    def __str__(self):
        return f"Autor: {self.nome} (Cód: {self.codigo_autor})"

class Livro:
    """
    Representa a entidade Livros.
    Inclui referências para as entidades relacionadas (foreign keys conceituais).
    """
    def __init__(self, isbn, titulo, num_paginas, peso, custo, preco_venda, num_edicao, ano_edicao, num_reimpressao, num_contrato, area, formato, encadernacao):
        self.isbn = isbn
        self.titulo = titulo
        self.num_paginas = num_paginas
        self.peso = peso
        self.custo = custo
        self.preco_venda = preco_venda
        self.num_edicao = num_edicao
        self.ano_edicao = ano_edicao
        self.num_reimpressao = num_reimpressao
        self.num_contrato = num_contrato
        
        # Atributos que representam os relacionamentos (chaves estrangeiras conceituais)
        self.area = area
        self.formato = formato
        self.encadernacao = encadernacao
        self.autores = [] # Relacionamento M:N (Autor escreve Livro)

    def adicionar_autor(self, autor):
        """Método para adicionar um autor a este livro."""
        self.autores.append(autor)
        print(f"  > O autor '{autor.nome}' foi adicionado ao livro '{self.titulo}'.")

    def __str__(self):
        return f"Livro: {self.titulo} (ISBN: {self.isbn})"


# --- Instanciando as Entidades e Definindo os Relacionamentos ---

# 1. Criando instâncias de Áreas
area_ti = Area(codigo_area=1, descricao="Tecnologia da Informação")
area_design = Area(codigo_area=2, descricao="Design Gráfico")

# 2. Criando instâncias de Formatos
formato_brochura = Formato(codigo_formato=101, descricao="Brochura", altura=23, largura=16)
formato_capa_dura = Formato(codigo_formato=102, descricao="Capa Dura", altura=25, largura=18)

# 3. Criando instâncias de Encadernações
encadernacao_comum = Encadernacao(codigo_encadernacao=201, descricao="Costura")
encadernacao_espiral = Encadernacao(codigo_encadernacao=202, descricao="Espiral")

# 4. Criando instâncias de Autores
endereco_autor1 = {"logradouro": "Rua das Alamedas, 123", "bairro": "Centro", "cidade": "São Paulo", "estado": "SP"}
autor1 = Autor(codigo_autor=301, nome="Ana Silva", cpf="111.222.333-44", rg="12.345.678-9", telefone="(11) 98765-4321", data_nascimento="01/01/1980", genero="Feminino", estado_civil="Casada", local_trabalho="Universo Dev", endereco=endereco_autor1)

endereco_autor2 = {"logradouro": "Avenida Brasil, 456", "bairro": "Jardins", "cidade": "Rio de Janeiro", "estado": "RJ"}
autor2 = Autor(codigo_autor=302, nome="Pedro Santos", cpf="444.555.666-77", rg="98.765.432-1", telefone="(21) 91234-5678", data_nascimento="15/05/1975", genero="Masculino", estado_civil="Solteiro", local_trabalho="Tecno Soluções", endereco=endereco_autor2)


# 5. Criando instâncias de Livros e estabelecendo os relacionamentos M:1
# Livro 1: "Banco de Dados para Iniciantes"
livro1 = Livro(
    isbn="978-85-7522-383-7",
    titulo="Banco de Dados para Iniciantes",
    num_paginas=450,
    peso=0.8,
    custo=25.00,
    preco_venda=65.00,
    num_edicao=3,
    ano_edicao=2024,
    num_reimpressao=1,
    num_contrato="C-1001",
    area=area_ti, # Relacionamento M:1 com 'Áreas'
    formato=formato_capa_dura, # Relacionamento M:1 com 'Formatos'
    encadernacao=encadernacao_comum # Relacionamento M:1 com 'Encadernações'
)

# Livro 2: "Design de Interfaces Modernas"
livro2 = Livro(
    isbn="978-85-7522-123-4",
    titulo="Design de Interfaces Modernas",
    num_paginas=320,
    peso=0.6,
    custo=18.00,
    preco_venda=55.00,
    num_edicao=2,
    ano_edicao=2023,
    num_reimpressao=2,
    num_contrato="C-1002",
    area=area_design,
    formato=formato_brochura,
    encadernacao=encadernacao_espiral
)

# 6. Estabelecendo o relacionamento M:N (Autor escreve Livro)
print("\n🔗 Criando os relacionamentos 'Autor escreve Livro' (M:N):")
livro1.adicionar_autor(autor1)
livro1.adicionar_autor(autor2) # Exemplo de livro com múltiplos autores
livro2.adicionar_autor(autor1) # Exemplo de autor com múltiplos livros

# --- Imprimindo os Dados para Visualização ---
print("\n--- Relatório de Livros e seus Detalhes ---")
print(f"{livro1}")
print(f"  > Pertence à: {livro1.area.descricao}")
print(f"  > Formato: {livro1.formato.descricao}")
print(f"  > Encadernação: {livro1.encadernacao.descricao}")
print(f"  > Autores: {[autor.nome for autor in livro1.autores]}")

print("-" * 30)

print(f"{livro2}")
print(f"  > Pertence à: {livro2.area.descricao}")
print(f"  > Formato: {livro2.formato.descricao}")
print(f"  > Encadernação: {livro2.encadernacao.descricao}")
print(f"  > Autores: {[autor.nome for autor in livro2.autores]}")

print("\n🎉 Modelagem concluída com sucesso! 🎉")