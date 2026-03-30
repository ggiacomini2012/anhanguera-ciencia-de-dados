# 🧠 WORKFLOW: RESUMIDOR DE AULAS SÊNIOR

Este guia define como transformar os dados brutos extraídos pelo robô em materiais de estudo de alta qualidade (Arquitetura Sênior).

## 📂 Estrutura de Entrada e Saída
Para cada aula localizada em:
`metas/faculdade/ciencia-de-dados/semestre-2/disciplina-X/unidade-Y/aula-Z/`

1. **ENTRADA:** `web-scraping/conteudo_bruto.txt`
2. **SAÍDA 1:** `aula-Z.py` (Exemplos práticos. O 'Z' deve ser o número da aula).
3. **SAÍDA 2:** `explicacao.md` (Resumo lúdico e mastigado).
4. **SINALIZADOR:** `web-scraping/concluido` (Arquivo vazio para marcar como processado).

## 📜 Regras de Criação

### 1. O Arquivo Script (`aula-Z.py`)
- **REGRA DE OURO:** NUNCA criar um arquivo novo chamado `aula.py`. Sempre preencher o arquivo já existente `aula-Z.py`.
- Deve conter códigos Python que exemplifiquem os conceitos da aula.

- Se a aula for teórica (ex: Probabilidade), criar simulações ou funções que demonstrem os cálculos.
- Incluir comentários explicativos no código.

### 2. O Arquivo `explicacao.md`
- **Tom:** Lúdico, amigável e incentivador.
- **Formatação:** Usar emojis 🚀, 💡, 📊, ⚡.
- **Estrutura:** 
  - # 📝 Título da Aula
  - ## 💡 O que de fato importa? (Resumo em 3 pontos).
  - ## 🚀 Na prática (Exemplos simplificados).
  - ## 🧠 Dica de Ouro.

### 3. O Sinal `concluido`
- Após gerar os dois arquivos, criar o arquivo `concluido` na pasta de web-scraping para evitar reprocessamento.

---
**Objetivo:** Facilitar o estudo futuro com explicações rápidas e códigos prontos para rodar.
