# 📊 Anhanguera - Ciência de Dados

![GitHub repo size](https://img.shields.io/github/repo-size/ggiacomini2012/anhanguera-ciencia-de-dados)
![GitHub last commit](https://img.shields.io/github/last-commit/ggiacomini2012/anhanguera-ciencia-de-dados)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Repositório de estudos e projetos do curso de **Ciência de Dados da Anhanguera**.
Organizado por **semestres**, **disciplinas**, **unidades** e **aulas**, com exercícios, scripts em Python e materiais de apoio.

---

## 🚀 Como Começar (Setup do Ambiente)

Para executar os projetos e acompanhar os estudos deste repositório, siga os passos abaixo para configurar seu ambiente de desenvolvimento.

### 1. Instalações Essenciais

- **Python (3.10 ou superior):**
  - A linguagem principal do projeto. Se você ainda não tem, baixe em [python.org](https://www.python.org/downloads/).
  - **Importante:** Durante a instalação no Windows, marque a opção "Add Python to PATH".

- **Visual Studio Code (VS Code):**
  - O editor de código recomendado. Baixe em [code.visualstudio.com](https://code.visualstudio.com/).
  - Após instalar, abra o VS Code, vá para a aba de **Extensões** e instale a extensão oficial do **Python** da Microsoft.

- **Git:**
  - O sistema de controle de versão usado para gerenciar o código. Baixe em [git-scm.com](https://git-scm.com/downloads).

### 2. Configurando o Projeto

1.  **Clone o Repositório:**
    Abra seu terminal (ou o terminal do VS Code) e execute o comando:
    ```bash
    git clone https://github.com/ggiacomini2012/anhanguera-ciencia-de-dados.git
    ```

2.  **Abra a Pasta do Projeto:**
    ```bash
    cd anhanguera-ciencia-de-dados
    ```

3.  **Crie e Ative o Ambiente Virtual (`venv`):**
    Isso cria um ambiente Python isolado para o projeto, evitando conflitos de dependências.
    ```bash
    # Crie o ambiente (só precisa fazer uma vez)
    python -m venv venv

    # Ative o ambiente (faça isso toda vez que for trabalhar no projeto)
    # No Windows (PowerShell):
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

4.  **Instale as Dependências:**
    Com o ambiente virtual ativo, instale todas as bibliotecas necessárias com um único comando:
    ```bash
    pip install -r requirements.txt
    ```

Pronto! Seu ambiente está configurado e você já pode executar os scripts e notebooks do projeto.

---

## 📂 Estrutura do Repositório

- 📅 **semestre-X** → Pasta correspondente a cada semestre do curso.
- 💻 **disciplina-X** → Pasta correspondente a cada disciplina do curso.
- 📁 **trabalhos** → Pasta correspondente aos trabalhos da disciplina.
- 📁 **unidade-X** → Pasta correspondente a cada unidade do curso.

  - 👨‍🏫 **explicacao.md** → Arquivo contendo um explicação lúdica da aula.
  - 🐍 **aula-X.py** → Scripts, notebooks ou exercícios da aula.

---

## 🚀 Tecnologias e Ferramentas

- **Python 3** 🐍
- **Pandas, NumPy, Matplotlib, Seaborn** 📊
- **Scikit-learn** 🤖 (para Machine Learning)
- **Jupyter Notebook** 📓 (quando aplicável)

---

## 💡 Projetos e Conceitos em Destaque

Resumo de alguns dos principais estudos e mini-projetos do repositório.

- **App de Encomendas com Flask (`S1/D2/U1`)** 🍰
  - **O que é:** Uma aplicação web simples para gerenciar encomendas (CRUD) usando Flask e um banco de dados SQLite.
  - **Conceitos:** Desenvolvimento web com Python, persistência de dados, rotas e templates.

- **Análise de Algoritmos (`S1/D1/U4`)** 🚀
  - **O que é:** Comparativo de performance entre uma Lista Encadeada e uma Tabela Hash (dicionário Python) para inserção e busca.
  - **Conceitos:** Complexidade de Algoritmos (Big O), O(n) vs. O(1).

- **Detecção de Fraudes com Grafos (`S1/D1/U4`)** 🕵️‍♂️
  - **O que é:** Simulação de uma rede de transações financeiras para identificar atividades suspeitas usando a biblioteca `networkx`.
  - **Conceitos:** Teoria dos Grafos, visualização de dados, análise de redes.

- **Estruturas de Dados em Árvore (`S1/D1/U2`)** 🌳
  - **O que é:** Implementações de Árvores para resolver problemas práticos.
    - **Recomendação de Filmes:** Usa uma árvore simples para recomendar filmes por faixa etária.
    - **Árvore Binária de Busca (ABB):** Organiza dados para buscas eficientes.
    - **Árvore AVL:** Versão auto-balanceável da ABB para garantir performance.
  - **Conceitos:** Hierarquia de dados, busca, inserção, remoção e balanceamento.

---

## 🎯 Objetivo

Organizar os estudos de forma modular, acompanhando o progresso por **disciplina**, **unidade** e **aula**.
Facilitar revisões e práticas de **análise de dados, estatística e machine learning**.

---

## 📚 Estrutura de commit

`S1-D1-U1-A1` = **Semestre 1, Disciplina 1, Unidade 1, Aula 1**

---

## 💡 Dicas

- Siga o padrão de pastas `semestre-N/nome-disciplina-Z/unidade-X/aula-Y` para manter o repositório organizado.
- Atualize o README conforme novas unidades forem adicionadas.
- Use ambientes virtuais para gerenciar dependências do Python (`venv` ou `conda`).
- Utilize o conventional commits para manter o repositório legível.

---

✨ **Mantenha a prática constante!** Ciência de Dados é aprendizado contínuo. 🚀

Por: Guilherme Giacomini Teixeira
