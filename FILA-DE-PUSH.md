# Fila de Push Pendente

Regra: **um push por dia**, sempre do commit mais antigo para o mais novo.
Após fazer o push do dia, risque o item desta lista.

## Como fazer o push de um commit específico

```bash
# Dentro da pasta ciencia-de-dados:
git push origin <HASH>:refs/heads/main
```

**Por que `hash:refs/heads/main` e não só `git push origin main`?**
- `git push origin main` sempre pega o HEAD (commit mais novo) e leva tudo junto.
- `hash:refs/heads/main` empurra apenas até aquele commit específico, sem subir os mais novos.
- `refs/heads/main` é o caminho completo da branch no remote — evita confusão com tags.

---

## Fila (do mais antigo para o mais novo)

- [x] `4436ab9` — `feat: S2-D1-U4-A3: Correção e Ajuste de Conteúdo Teórico`
- [x] `42193e5` — `feat: S2-D1-U4-A4: Consolidação de Exercícios e Explicação`
- [x] `c420565` — `feat: S2-D1-U4-A5: Conclusão da Unidade de Inferência`
- [x] `e98d6da` — `feat: infraestrutura de automação para raspagem de aulas`
- [x] `35c5dfd` — `feat: organização das disciplinas do Semestre 2`
- [x] `8f664fb` — `feat: S2-D1-U4: Conteúdos Adicionais via Web Scraping`
- [ ] `a44d754` — `fix: S2-D1-U2-A2: Correção de typo no nome do arquivo`
- [ ] `ae2ec37` — `fix: S2-D1-U3-A2: Correção de typo no nome do arquivo`
- [ ] `911a83b` — `feat(infra): S2-D1: Roteiro de automação do Robô Escaneador (AVA)`

