
# 🚀 Aula 3: Dominando o SQL DML – A Linguagem que Dá Vida aos Dados

## 🌟 O que é DML? (Data Manipulation Language)

Imagine que seu banco de dados é um **guarda-roupa digital** 🧥👖. O DDL (Data Definition Language) é o que usamos para construir o guarda-roupa (criar as mesas, as gavetas, as prateleiras). Já o **DML** é a chave que usamos para **interagir com o conteúdo** dentro dele: colocar roupas novas, tirar as velhas, mover de lugar, e ver o que temos disponível!

O DML engloba os comandos essenciais para a manipulação dos dados armazenados:

* **SELECT:** Ver ou "Buscar" o que está no guarda-roupa. (Consulta)
* **INSERT:** Colocar uma peça nova de roupa. (Inserção)
* **UPDATE:** Mudar uma roupa de lugar ou reformá-la. (Modificação)
* **DELETE:** Jogar uma peça fora. (Remoção)

Dominar esses quatro verbos é crucial para qualquer desenvolvedor ou analista de dados.

---

## 🎯 Cenário Prático: Gerenciando a TechCorp

Vamos aplicar os comandos DML no cenário que você propôs: a empresa **TechCorp**, que precisa de um sistema de gerenciamento de funcionários.

### 🛠️ Configuração Inicial (DDL - Apenas Contexto)

Antes de manipular, precisamos criar o banco de dados e a tabela.

```sql
-- Criar o banco de dados (Task 1)
CREATE DATABASE IF NOT EXISTS techcorp_db;

-- Usar o banco de dados
USE techcorp_db;

-- Criar a tabela 'funcionarios'
CREATE TABLE funcionarios (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    departamento VARCHAR(50),
    salario DECIMAL(10, 2)
);
````

-----

## 1\. ➕ INSERT: Inserindo Novos Dados (A Peça Nova de Roupa)

O comando `INSERT` é como abrir o armário e **colocar um novo item** lá dentro. Ele adiciona uma ou mais linhas à sua tabela.

### Sintaxe Mágica ✨

```sql
INSERT INTO nome_da_tabela (coluna1, coluna2, ...)
VALUES (valor1, valor2, ...);
```

### 🧑‍💻 Task 2: Inserir Dados Iniciais

Vamos inserir os três registros iniciais de funcionários na nossa tabela `funcionarios`.

```sql
-- Inserção 1: João, o Gerente de TI
INSERT INTO funcionarios (nome, cargo, departamento, salario)
VALUES ('João Silva', 'Gerente', 'TI', 9500.00);

-- Inserção 2: Maria, a Analista de Marketing
INSERT INTO funcionarios (nome, cargo, departamento, salario)
VALUES ('Maria Santos', 'Analista', 'Marketing', 6800.00);

-- Inserção 3: Pedro, o Desenvolvedor
INSERT INTO funcionarios (nome, cargo, departamento, salario)
VALUES ('Pedro Alvares', 'Desenvolvedor', 'TI', 8200.00);

-- Inserção 4 (Bônus): Para ter mais dados para testes
INSERT INTO funcionarios (nome, cargo, departamento, salario)
VALUES ('Ana Souza', 'Estagiária', 'Marketing', 2500.00);
```

> **Dica de Ouro:** Se você for inserir valores em **todas** as colunas, pode omitir a lista de colunas, mas isso é arriscado se a estrutura da tabela mudar\!

-----

## 2\. 🔍 SELECT: Consultando e Buscando Dados (A Visão Geral)

O comando `SELECT` é, sem dúvida, o mais utilizado do SQL\! Ele é seu **par de binóculos** 🔭 para ver o que está no banco de dados.

### Sintaxe Básica ⚙️

```sql
SELECT coluna1, coluna2, ... (ou *)
FROM nome_da_tabela
WHERE condicao; -- A cláusula WHERE é o filtro!
```

### 🔎 Task 3: Buscando Dados Específicos

#### a) Todos os funcionários do departamento de TI

Queremos filtrar a tabela para ver apenas quem trabalha em "TI".

```sql
SELECT nome, cargo, salario
FROM funcionarios
WHERE departamento = 'TI';
```

#### b) O funcionário com o salário mais alto

Aqui usamos funções de agregação, como `MAX()`, para encontrar o maior valor.

```sql
-- Opção A: Usando ORDER BY e LIMIT (Mais comum)
SELECT nome, cargo, salario
FROM funcionarios
ORDER BY salario DESC  -- Ordena do maior para o menor
LIMIT 1;               -- Pega apenas o primeiro

-- Opção B: Usando Subquery (Mais complexo, mas poderoso)
SELECT nome, cargo, salario
FROM funcionarios
WHERE salario = (SELECT MAX(salario) FROM funcionarios);
```

#### c) A contagem total de funcionários na empresa

Usamos a função de agregação `COUNT()` para saber o "tamanho" da equipe.

```sql
SELECT COUNT(id_funcionario) AS total_funcionarios
FROM funcionarios;
```

> **Agregação:** Funções como `COUNT()`, `SUM()`, `AVG()`, `MIN()` e `MAX()` são os **super-poderes** do SQL para resumir dados.

-----

## 3\. ✏️ UPDATE: Modificando Dados Existentes (A Reforma da Roupa)

O `UPDATE` permite que você **modifique** os valores das colunas em linhas já existentes. É crucial SEMPRE usar a cláusula `WHERE`, ou você mudará a tabela **inteira**\!

### Sintaxe Crucial ⚠️

```sql
UPDATE nome_da_tabela
SET coluna1 = novo_valor1, coluna2 = novo_valor2, ...
WHERE condicao; -- SEMPRE use o WHERE!
```

### 💼 Task 4: Atualizar Dados

#### a) Atualizar o salário de um funcionário específico (João Silva)

O João se destacou e merece um aumento\!

```sql
UPDATE funcionarios
SET salario = 10000.00 -- Novo salário
WHERE nome = 'João Silva';
```

#### b) Mudar o departamento de um funcionário (Pedro Alvares)

O Pedro migrou de TI para P\&D (Pesquisa e Desenvolvimento).

```sql
UPDATE funcionarios
SET departamento = 'P&D', cargo = 'Especialista' -- Podemos mudar múltiplos campos
WHERE nome = 'Pedro Alvares';
```

> **Lembrete:** Se você rodasse `UPDATE funcionarios SET salario = 0;` sem o `WHERE`, todos os funcionários estariam de repente sem salário\! **Perigo\!** 🚨

-----

## 4\. ❌ DELETE: Apagando Dados (Jogando a Roupa Fora)

O comando `DELETE` remove linhas inteiras da sua tabela. Assim como o `UPDATE`, o `WHERE` é seu **melhor amigo** (e seu salva-vidas\!).

### Sintaxe Simples, Efeito Dramático 💀

```sql
DELETE FROM nome_da_tabela
WHERE condicao; -- SEMPRE use o WHERE!
```

### 🗑️ Task 5: Apagar Dados

#### Remover um funcionário que não faz mais parte da empresa (Ana Souza)

A Ana concluiu o estágio e não continuará.

```sql
DELETE FROM funcionarios
WHERE nome = 'Ana Souza';
```

> **Diferença Vital:**
>
>   * `DELETE FROM tabela;` (Sem WHERE) remove **todas as linhas**, mas a estrutura da tabela permanece.
>   * `TRUNCATE TABLE tabela;` (DDL) é muito mais rápido, remove todas as linhas e **reseta** o contador (se houver `AUTO_INCREMENT`).
>   * `DROP TABLE tabela;` (DDL) remove a tabela e **tudo** que a envolve (índices, estrutura, dados).

-----

## 💡 Conclusão: O Poder na Sua Mão

Com `SELECT`, `INSERT`, `UPDATE` e `DELETE`, você tem o controle total sobre a informação.

  * **SELECT** informa você.
  * **INSERT** alimenta o sistema.
  * **UPDATE** mantém a precisão.
  * **DELETE** garante a limpeza.

Parabéns\! Você dominou os pilares do SQL DML, e a **TechCorp** agora pode gerenciar sua equipe eficientemente.

