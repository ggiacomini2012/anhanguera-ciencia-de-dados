# -*- coding: utf-8 -*-

"""
Este script Python demonstra como o esquema do banco de dados da editora pode ser
mapeado para classes Python usando um ORM (Mapeamento Objeto-Relacional).
Utilizamos a biblioteca SQLAlchemy para este exemplo.

Isso permite que os desenvolvedores interajam com o banco de dados usando objetos,
em vez de escreverem SQL diretamente.
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, DECIMAL, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define a base para as classes do modelo declarativo
Base = declarative_base()

# Tabela de associação para o relacionamento M:N entre Autor e Livro
autor_livro_association = Table('Autor_Livro', Base.metadata,
    Column('autor_id', Integer, ForeignKey('Autores.codigo_autor')),
    Column('livro_isbn', String(13), ForeignKey('Livros.isbn'))
)

# --- Definição das Classes (Entidades) ---

class Area(Base):
    __tablename__ = 'Areas'
    codigo_area = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    livros = relationship("Livro", back_populates="area")

class Formato(Base):
    __tablename__ = 'Formatos'
    codigo_formato = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    altura_cm = Column(DECIMAL(5, 2))
    largura_cm = Column(DECIMAL(5, 2))
    livros = relationship("Livro", back_populates="formato")

class Encadernacao(Base):
    __tablename__ = 'Encadernacoes'
    codigo_encadernacao = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    livros = relationship("Livro", back_populates="encadernacao")

class Autor(Base):
    __tablename__ = 'Autores'
    codigo_autor = Column(Integer, primary_key=True)
    nome_completo = Column(String(255), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    # ... outros atributos do autor ...
    
    # Relacionamento M:N com Livro
    livros = relationship("Livro", secondary=autor_livro_association, back_populates="autores")

class Livro(Base):
    __tablename__ = 'Livros'
    isbn = Column(String(13), primary_key=True)
    titulo = Column(String(255), nullable=False)
    # ... outros atributos do livro ...

    # Chaves Estrangeiras e Relacionamentos M:1
    area_id = Column(Integer, ForeignKey('Areas.codigo_area'))
    area = relationship("Area", back_populates="livros")
    
    formato_id = Column(Integer, ForeignKey('Formatos.codigo_formato'))
    formato = relationship("Formato", back_populates="livros")

    encadernacao_id = Column(Integer, ForeignKey('Encadernacoes.codigo_encadernacao'))
    encadernacao = relationship("Encadernacao", back_populates="livros")
    
    # Relacionamento M:N com Autor
    autores = relationship("Autor", secondary=autor_livro_association, back_populates="livros")

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Cria um banco de dados SQLite em memória para o exemplo
    engine = create_engine('sqlite:///:memory:')
    
    # Cria todas as tabelas no banco de dados
    Base.metadata.create_all(engine)
    
    # Cria uma sessão para interagir com o banco de dados
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # --- Inserindo dados de exemplo ---
    
    # Criando instâncias (objetos)
    autor1 = Autor(nome_completo="Carlos Machado", cpf="111.222.333-44")
    autor2 = Autor(nome_completo="Ana Alves", cpf="555.666.777-88")
    
    area_bd = Area(descricao="Banco de Dados")
    formato_padrao = Formato(descricao="Padrão", altura_cm=23.0, largura_cm=16.0)
    encad_brochura = Encadernacao(descricao="Brochura")
    
    livro_sql = Livro(
        isbn="9788575224373",
        titulo="Modelagem de Dados Avançada",
        area=area_bd,
        formato=formato_padrao,
        encadernacao=encad_brochura
    )
    
    # Associando autores ao livro (relacionamento M:N)
    livro_sql.autores.append(autor1)
    livro_sql.autores.append(autor2)
    
    # Adicionando os objetos à sessão
    session.add(autor1)
    session.add(autor2)
    session.add(area_bd)
    session.add(formato_padrao)
    session.add(encad_brochura)
    session.add(livro_sql)
    
    # Commit para salvar os dados no banco
    session.commit()
    
    # --- Consultando os dados ---
    print("--- Consulta ao Banco de Dados usando ORM ---")
    livro_consultado = session.query(Livro).filter_by(isbn="9788575224373").one()
    
    print(f"Título: {livro_consultado.titulo}")
    print(f"Área: {livro_consultado.area.descricao}")
    
    # Acessando o relacionamento M:N
    autores_do_livro = [autor.nome_completo for autor in livro_consultado.autores]
    print(f"Autores: {', '.join(autores_do_livro)}")
    
    session.close()
