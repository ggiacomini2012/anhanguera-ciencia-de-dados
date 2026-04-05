# Próximos Passos: O Robô Escaneador (20/03/2026)

Este arquivo serve como "gancho" mental para o início da próxima sessão.

## 🎯 Objetivo Imediato
Implementar a navegação automatizada no AVA da Anhanguera para extrair o conteúdo da **Aula 5 da Unidade 4 (Disciplina 1)**.

## 📋 Checklist de Início
- [ ] Validar se as credenciais do `credenciais-acessos-gerais.md` funcionam no login manual (conferir se o redirecionamento mudou).
- [ ] Rodar o script `automation/extrair-aulas.py` em modo **Headless: false** para observar o Playwright interagindo com os campos de CPF e Senha.
- [ ] Mapear o seletor (ID ou CSS) do botão de download de materiais de aula.

## 💡 Dica para a IA de amanhã
O robô deve ser resiliente a redirecionamentos. Use `wait_for_navigation` ou `wait_for_url` conforme documentado no `learnings-webscraping.md`.

*Bom trabalho, Gui de amanhã. O Gui de hoje já fez a parte chata (limpeza e organização).*
