# BRIEFING ESTRATÉGICO PARA CLAUDE-CODE

## 1. CONTEXTO DO PROJETO
O Guilherme (Gui) é um Desenvolvedor Sênior que está automatizando sua própria faculdade de Ciência de Dados (Anhanguera). 

**O Desafio:** O portal da Anhanguera é instável, tem redirecionamentos complexos e exige 2FA (verificação via e-mail) esporádica. 
**A Missão:** Criar um Robô que entre no portal, encontre as disciplinas ativas, navegue pelas unidades de aula e extraia o conteúdo de texto dos IFrames (Aulas) para salvar em disco.

## 2. ARQUITETURA DEFINIDA (PILAR LOCAL)
Para evitar bloqueios de IPs internacionais e economizar custos de API Vision, decidimos que o **Claude-Code (ou Codex/Gemini local)** deve operar como o "Agente de Visão" através de um **Servidor MCP Local**.

### Ferramentas Instaladas:
- **Playwright/Puppeteer:** Gerenciando o navegador localmente.
- **Virtual Env (venv):** Criado na pasta `metas/faculdade/robo-scraper/` para isolar dependências.
- **MCP Puppeteer:** `@modelcontextprotocol/server-puppeteer` deve ser a ponte de comando.

## 3. ESTADO ATUAL
- Já mapeamos manualmente alguns seletores (veja `primeiro_codigo_playwrigth.py`).
- Já criamos um script de geração de sessão (`gerar_sessao.py`) que salva os cookies em `sessao_estado.json`.
- **Gargalo:** Scripts Python puros sofrem com a sincronicidade dos redirects da Anhanguera. Queremos que você (Claude) assuma o controle visual via MCP para navegar e identificar os nomes das disciplinas e aulas sem erro de seletor.

## 4. O QUE QUEREMOS DE VOCÊ AGORA
1. **Adicionar o MCP Puppeteer:** No terminal, rode `claude mcp add puppeteer npx -y @modelcontextprotocol/server-puppeteer`.
2. **Navegar e Mapear:** Use seus "olhos" de MCP para entrar em `https://www.anhanguera.com/aluno/meus-cursos` e listar para o Gui todas as disciplinas que você está enxergando na tela.
3. **Extração de Aula:** Vá até a Unidade 4 da disciplina de 'Probabilidade' (ou qualquer uma ativa) e extraia o texto de dentro do IFrame da aula usando `.inner_text()`.

**Regra de Ouro:** Não polua o sistema. Use o `.env` e o `.gitignore` que já criamos para senhas. Seja cirúrgico.
