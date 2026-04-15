
## 📚 Introdução ao MySQL: Conceitos, Tipos de Atributos e Cardinalidade (Aula 1)

Seja bem-vindo à sua primeira jornada no mundo dos **Bancos de Dados Relacionais** com o **MySQL**\! 🚀

Imagine um banco de dados como o **grande arquivo central de uma biblioteca digital** 🏛️. O MySQL é o **bibliotecário** (o SGBD) que não só organiza os livros (os dados), mas também garante que você encontre exatamente o que precisa, com rapidez e sem bagunça.

### 1\. Conceitos Fundamentais: A Estrutura da Biblioteca

Antes de tudo, precisamos entender os pilares que sustentam nosso sistema:

  * **Banco de Dados (Database):** É a **coleção organizada** de dados relacionados. No nosso exemplo, é a biblioteca inteira, com todos os seus estantes, livros e fichários.
  * **SGBD (Sistema de Gerenciamento de Banco de Dados):** É o **software** (como o MySQL, PostgreSQL, Oracle) que gerencia o banco de dados. Ele é o bibliotecário: o responsável por guardar, buscar, atualizar e manter a segurança de tudo.
  * **Tabelas (Tables):** São as **estruturas fundamentais** que organizam os dados em linhas e colunas. Pense nelas como **armários de fichas** dentro da biblioteca. Cada armário (tabela) armazena informações sobre uma **Entidade** específica (como "Livros", "Autores" ou "Leitores").
      * **Entidade:** É um objeto ou conceito do mundo real que podemos identificar (Ex: um **Funcionário**, um **Projeto**).
  * **Atributos (Attributes):** São as **características ou propriedades** que descrevem uma entidade. São as **colunas** da tabela. (Ex: Para a entidade `Livro`, os atributos seriam `Título`, `Autor`, `Ano de Publicação`).
  * **Chave Primária (**`PRIMARY KEY`**):** É um atributo (ou conjunto de atributos) que **identifica de forma única** cada registro (linha) em uma tabela. Ela é o **RG** ou **CPF** de cada ficha no armário, garantindo que não haja duplicatas. 🗝️
      * *Exemplo:* O `idFuncionario` na tabela `funcionario`.
  * **Chave Estrangeira (**`FOREIGN KEY`**):** É um campo em uma tabela que se **relaciona** com a Chave Primária de **outra** tabela. Ela é o **"fio"** que conecta informações em armários diferentes. 🔗
      * *Exemplo:* Na tabela `projeto`, o atributo `idGerente` é uma chave estrangeira que aponta para o `idFuncionario` na tabela `funcionario`.

-----

### 2\. Tipos de Atributos: O Material de Construção dos Dados

Quando criamos uma tabela, precisamos dizer ao MySQL **que tipo de dado** cada atributo irá armazenar. Isso é como escolher o tipo de recipiente para guardar diferentes itens (caixa para sólidos, garrafa para líquidos, etc.). Usar o tipo certo economiza espaço e garante que os dados façam sentido\! 🧠

| Tipo MySQL | O que Armazena | Metáfora Simplificada | Uso Comum |
| :--- | :--- | :--- | :--- |
| **INT / BIGINT** | Números inteiros. | Contadores, IDs de Livros (1, 2, 3...) | Identificadores, Quantidades |
| **VARCHAR** | Texto variável. | Uma etiqueta com espaço flexível. | Nomes, Títulos, Cargos |
| **CHAR** | Texto de tamanho fixo. | Uma etiqueta com tamanho exato. | Siglas (ex: 'SP', 'RJ') |
| **TEXT** | Textos longos. | Um pergaminho (sem limite de linhas). | Descrições longas, anotações |
| **DATE** | Data (Apenas dia/mês/ano). | Um calendário. | Datas de Início, Nascimento |
| **DATETIME** | Data e Hora. | Um calendário com relógio. | Data e hora de registro |
| **DECIMAL** | Números decimais precisos. | Balança de precisão para dinheiro. | Preços, Salários, Valores Monetários |
| **BOOLEAN** | Verdadeiro ou Falso (0 ou 1). | Um interruptor de luz (Ligado/Desligado). | Status: Ativo, Concluído |

*Lembre-se: Usar `VARCHAR(50)` significa que o campo pode ter até 50 caracteres. Tentar inserir 'Supercalifragilisticexpialidocious' (34 caracteres) em um `VARCHAR(20)` resultaria em um erro\!* 🛑

-----

### 3\. Cardinalidade: As Regras de Conexão (Relacionamentos)

A cardinalidade define as **regras de associação** entre as tabelas (entidades). É como definir as regras de relacionamento social: quantas pessoas podem se relacionar com quantas outras? 🤝

Existem três tipos principais:

#### 3.1. Um para Um (1:1) 💍

  * **Definição:** Uma instância da Entidade A se relaciona com **apenas uma** instância da Entidade B, e vice-versa.
  * **Metáfora:** O relacionamento entre um **Cidadão** e seu **Passaporte**. Cada cidadão tem *um* passaporte, e cada passaporte pertence a *um* cidadão.
  * **Implementação:** Em teoria, poderiam estar na mesma tabela, mas são separados por questões de organização e privacidade.

#### 3.2. Um para Muitos (1:N) 👨‍👩‍👧‍👦

  * **Definição:** Uma instância da Entidade A pode se relacionar com **várias** instâncias da Entidade B, mas uma instância da Entidade B se relaciona com **apenas uma** da Entidade A.
  * **Metáfora:** O relacionamento entre um **Departamento** e seus **Funcionários**. Um departamento pode ter *muitos* funcionários, mas cada funcionário pertence a *um* só departamento.
  * **Implementação:** O lado "muitos" (N) recebe a Chave Estrangeira que aponta para o lado "um" (1). (O funcionário tem o ID do Departamento).

#### 3.3. Muitos para Muitos (N:M) 🌐

  * **Definição:** Várias instâncias da Entidade A podem se relacionar com **várias** instâncias da Entidade B, e vice-versa.
  * **Metáfora:** O relacionamento entre **Estudantes** e **Disciplinas**. Um estudante pode cursar *várias* disciplinas, e uma disciplina tem *vários* estudantes.
  * **Implementação:** **Requer uma Tabela Intermediária (ou Tabela de Junção)**. Esta tabela contém as Chaves Estrangeiras de ambas as tabelas originais, e sua Chave Primária é a combinação de ambas (Chave Composta).
      * *Exemplo:* Tabela `EstudanteDisciplina` conecta `Estudante` e `Disciplina`.

-----

### 4\. Exemplo Prático: Sistema de Gerenciamento de Projetos (DCL)

Vamos aplicar esses conceitos ao nosso desafio inicial: projetar um sistema de gerenciamento de projetos.

**Entidades:** `funcionario`, `projeto`, e uma tabela intermediária para a relação N:M.

**Relacionamentos e Cardinalidade:**

1.  **Gerente e Projeto:** 1 Gerente (Funcionario) para N Projetos (1:N). O `projeto` tem a FK `idGerente`.
2.  **Funcionário e Projeto:** N Funcionários para M Projetos (N:M). Requer a tabela de junção `projetoFuncionario`.
3.  **Gerente e Funcionário (Supervisão):** 1 Gerente para N Funcionários (1:N). Requer a tabela de junção `supervisao` (ou uma FK `idGerente` na tabela `funcionario`).

O código SQL abaixo define a estrutura (Data Definition Language - DDL) que atende a esses requisitos:

```sql
-- Tabela funcionario
CREATE TABLE funcionario (
  idFuncionario INT PRIMARY KEY, -- Chave Primária (PK) - Identificador Único
  nome VARCHAR(255) NOT NULL,
  cargo VARCHAR(50),
  dataContratacao DATE
);

-- Tabela projeto
CREATE TABLE projeto (
  idProjeto INT PRIMARY KEY, -- Chave Primária (PK)
  nome VARCHAR(255) NOT NULL,
  dataInicio DATE,
  -- idGerente é Chave Estrangeira (FK) apontando para funcionario
  idGerente INT, 
  FOREIGN KEY (idGerente) REFERENCES funcionario(idFuncionario)
);

-- Tabela projetoFuncionario (relação N:M entre Projeto e Funcionario)
CREATE TABLE projetoFuncionario (
  idProjeto INT,
  idFuncionario INT,
  horasTrabalhadas INT,
  -- Chave Primária Composta
  PRIMARY KEY (idProjeto, idFuncionario), 
  -- Chaves Estrangeiras para as tabelas originais
  FOREIGN KEY (idProjeto) REFERENCES projeto(idProjeto),
  FOREIGN KEY (idFuncionario) REFERENCES funcionario(idFuncionario)
);

-- Tabela supervisao (relação 1:N para gerente-funcionário)
-- Esta tabela modela que "Um gerente pode supervisionar vários funcionários"
-- enquanto "Um funcionário só pode ter um gerente" (que poderia ser modelado
-- com uma FK idGerente na tabela funcionario, mas faremos com a tabela de junção
-- conforme a estrutura fornecida no material).

-- NOTA: A estrutura original fornecida (supervisao com PK Composta)
-- implica em uma relação N:M. Para forçar a regra de 1:N ('Um funcionário SÓ pode ter um gerente'),
-- a chave primária deveria ser apenas idFuncionario, e idGerente seria uma FK.
-- Mantendo a estrutura original do material para fins de exercício:
CREATE TABLE supervisao (
  idGerente INT,
  idFuncionario INT,
  PRIMARY KEY (idGerente, idFuncionario), -- Assumindo que a relação N:M na supervisão está ok para fins didáticos
  FOREIGN KEY (idGerente) REFERENCES funcionario(idFuncionario),
  FOREIGN KEY (idFuncionario) REFERENCES funcionario(idFuncionario) -- A referência original estava incorreta (FuncionarioID), corrigida para idFuncionario
);
```

