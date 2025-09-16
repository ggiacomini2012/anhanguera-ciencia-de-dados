
# Exemplo Prático de Modelagem de Dados e Estratégias

Este documento exemplifica os conceitos de modelagem de dados apresentados na aula, aplicando as estratégias *Top-Down* e *Bottom-Up* a um cenário real.

## 1. Cenário do Problema

Vamos imaginar que precisamos criar um banco de dados para um sistema simples de **Blog**. O sistema precisa armazenar informações sobre os **autores** que escrevem, as **postagens** que eles publicam e os **comentários** que os leitores deixam nessas postagens.

---

## 2. Estratégia de Modelagem *Top-Down* (Do Geral para o Específico)

Nesta abordagem, começamos identificando as "coisas" ou "conceitos" principais do nosso sistema.

**Passo 1: Identificar as entidades principais (conjuntos de dados)**

Analisando o cenário, os principais conjuntos de dados são claramente:
- `Autor`: A pessoa que escreve as postagens.
- `Postagem`: O conteúdo que é publicado no blog.
- `Comentario`: A interação dos leitores com uma postagem.

**Passo 2: Detalhar os atributos (elementos) de cada entidade**

Agora, para cada entidade que identificamos, listamos as informações que precisamos guardar sobre ela:

- **Para `Autor`:**
  - Código de identificação
  - Nome completo
  - E-mail (para login)
  - Uma pequena biografia

- **Para `Postagem`:**
  - Código de identificação
  - Título da postagem
  - Conteúdo do texto
  - Data de publicação
  - A qual autor a postagem pertence? (Relacionamento)

- **Para `Comentario`:**
  - Código de identificação
  - Nome do leitor que comentou
  - Texto do comentário
  - Data do comentário
  - A qual postagem o comentário pertence? (Relacionamento)

---

## 3. Estratégia de Modelagem *Bottom-Up* (Do Específico para o Geral)

Nesta abordagem, o processo é inverso. Começamos listando todos os dados que precisamos armazenar, sem nos preocuparmos com a organização inicial.

**Passo 1: Listar todos os elementos de dados (atributos) necessários**

Vamos fazer um "brainstorm" de todas as informações que o sistema de Blog precisa gerenciar:
- Nome do autor
- Título da postagem
- Data em que o comentário foi feito
- Conteúdo principal da publicação
- E-mail do autor
- Biografia do autor
- Identificador único para cada postagem
- Texto do comentário do leitor
- Identificador único do autor
- Nome da pessoa que comentou
- Identificador único do comentário
- Data em que a postagem foi publicada

**Passo 2: Agrupar os elementos de dados em conjuntos lógicos (entidades)**

Agora, olhamos para a lista acima e agrupamos os atributos que se relacionam entre si, formando as entidades:

- **Grupo 1 (Dados sobre o Autor):**
  - Identificador único do autor
  - Nome do autor
  - E-mail do autor
  - Biografia do autor
  - *Conclusão: Este grupo forma a entidade `Autor`.*

- **Grupo 2 (Dados sobre a Postagem):**
  - Identificador único para cada postagem
  - Título da postagem
  - Conteúdo principal da publicação
  - Data em que a postagem foi publicada
  - *Conclusão: Este grupo forma a entidade `Postagem`.*

- **Grupo 3 (Dados sobre o Comentário):**
  - Identificador único do comentário
  - Nome da pessoa que comentou
  - Texto do comentário do leitor
  - Data em que o comentário foi feito
  - *Conclusão: Este grupo forma a entidade `Comentario`.*

Como visto, ambas as estratégias nos levam a um resultado similar, e na prática, os analistas costumam mesclar as duas abordagens (*middle-up-down*).

---

## 4. Resultado: Dicionário de Dados

Após a modelagem, o próximo passo é documentar a estrutura formalmente. O dicionário de dados é a ferramenta perfeita para isso, estabelecendo um padrão para toda a equipe de desenvolvimento.

**Tabela: autor**
| Campo | Descrição | Tipo | Tamanho | PK | FK |
| :--- | :--- | :--- | :--- |:---:|:---:|
| id_autor | Código identificador do autor | INTEGER | - | Sim | Não |
| nm_autor | Nome completo do autor | VARCHAR | 150 | Não | Não |
| ds_email | E-mail de login do autor | VARCHAR | 100 | Não | Não |
| ds_bio | Biografia resumida do autor | TEXT | - | Não | Não |

**Tabela: postagem**
| Campo | Descrição | Tipo | Tamanho | PK | FK |
| :--- | :--- | :--- | :--- |:---:|:---:|
| id_postagem | Código identificador da postagem | INTEGER | - | Sim | Não |
| ds_titulo | Título da postagem | VARCHAR | 200 | Não | Não |
| ds_conteudo | Corpo de texto da postagem | TEXT | - | Não | Não |
| dt_publicacao| Data e hora da publicação | DATETIME | - | Não | Não |
| id_autor | Chave do autor que publicou | INTEGER | - | Não | Sim |

**Tabela: comentario**
| Campo | Descrição | Tipo | Tamanho | PK | FK |
| :--- | :--- | :--- | :--- |:---:|:---:|
| id_comentario| Código identificador do comentário | INTEGER | - | Sim | Não |
| nm_leitor | Nome do leitor que comentou | VARCHAR | 150 | Não | Não |
| ds_texto | O texto do comentário | TEXT | - | Não | Não |
| dt_comentario| Data e hora do comentário | DATETIME | - | Não | Não |
| id_postagem | Chave da postagem comentada | INTEGER | - | Não | Sim |

Este dicionário serve como um guia essencial para a implementação do banco de dados (criação do esquema) e para a manutenção futura do sistema.
