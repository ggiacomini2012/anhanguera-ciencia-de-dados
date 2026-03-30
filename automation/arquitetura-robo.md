# Arquitetura do Robô da Faculdade (Web Scraper)

Este documento define o blueprint do projeto de automação do curso de Ciência de Dados do Gui.

## 1. A Pilha Tecnológica (Tech Stack)
- **Linguagem:** `Python` (Alinhado com o curso de Ciência de Dados).
- **Biblioteca de Automação:** `Playwright` (Mais moderno, rápido e imune a travamentos de renderização dinâmica em comparação com o antigo Selenium).
- **Segurança de Login:** O robô vai ler as credenciais protegidas localmente no arquivo `credenciais-acessos-gerais.md` e preencher os campos do AVA.

## 2. A Separação de Responsabilidades (Decisão de Ouro)
O Gui tomou a decisão arquitetural corretíssima de separar a "Captura" da "Geração". O robô de Python **não** vai chamar nenhuma API paga de IA. Ele vai agir exclusivamente como uma esteira mecânica. 

### Fase 1: O Extrator (Script Python)
1. Faz login no portal.
2. Navega até a aula exata.
3. Extrai o conteúdo em texto puro/bruto.
4. Cria iterativamente a árvore de pastas correta: `[Semestre X] > [Disciplina] > [Unidade Y] > [Aula Z] > \web-scraping\`.
5. Salva o material lá dentro num arquivo `.txt` feio e cru (ex: `conteudo_bruto.txt`).

### Fase 2: O Gerador (Inteligência Artificial Local)
1. O robô em Python para aqui e avisa que terminou.
2. O Gui usa o assistente de IA integrado (Antigravity ou Claude-Code) diretamente do VS Code.
3. O Gui dá o comando: *"Leia o conteúdo bruto da Aula Z e dissequem ele. Crie a Aula em Python e a Explicação.md"*.
## 3. Blindagem Técnica (Descobertas Críticas)

A implementação prática revelou que o portal Anhanguera possui barreiras dinâmicas. O robô foi blindado com:

- **Exterminador de Pop-ups (Joyride):** Injeção de JavaScript (`page.evaluate`) para remover overlays de tutorias que bloqueiam cliques.
- **Método de Posição (O Sniper):** Navegação baseada no índice do card (`.nth(X)`) para ignorar nomes de texto truncados ou modificados por porcentagens (`0%`, `100%`).
- **Resiliência de Login:** Timeouts estendidos (60s) para o campo de senha, compensando a lentidão de backend da validação de CPF.

---
**Status da Arquitetura:** 100% Validada e Operacional.

Essa divisão garante que o script não seja cobrado via API (economia) e fatiar o problema torna o robô muito mais fácil de codar sem interrupções.
