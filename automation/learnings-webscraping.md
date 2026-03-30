# Aprendizados de Web Scraping — Anhanguera AVA

Documentação dos aprendizados práticos obtidos durante o scraping do portal Anhanguera.
Serve como referência para projetos futuros, mesmo que o site alvo seja diferente.

---

## 1. Playwright em SPAs React

### Carregamento de página
- **Nunca usar `networkidle`** em portais com analytics (Google, Clarity, etc.) — as requisições nunca param e o timeout estoura.
- **Usar `domcontentloaded`** + `time.sleep()` em seguida.
- O React renderiza o conteúdo depois do `domcontentloaded`. O sleep é necessário para aguardar a hidratação dos componentes.
- Tempo mínimo testado no Anhanguera: **5 segundos** após `domcontentloaded`.

```python
page.wait_for_load_state("domcontentloaded", timeout=15000)
time.sleep(5)
```

### Encoding no Windows
- Emojis e acentos em `print()` causam `UnicodeEncodeError` no terminal Windows (cp1252).
- Solução obrigatória no início do script:

```python
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
```

---

## 2. Contexto de sessão em portais com múltiplos cursos

### O problema
Navegar diretamente para uma subpágina (ex: `/minhas-disciplinas`) sem ter "entrado" no curso antes resulta em página vazia ou sem conteúdo.

### A causa
O portal usa estado de sessão interno (React Context / cookies de curso) que só é definido quando o usuário clica no card do curso na home.

### A solução
Sempre navegar pelo caminho completo uma vez antes de acessar subpáginas:

```
login → /aluno/meus-cursos → click no card do curso → /aluno/tecnologo/KRT-xxx/
```

Depois disso, qualquer URL do curso funciona diretamente na mesma sessão.

---

## 3. Caminho de navegação — Portal Anhanguera

Mapeado via inspeção manual (MCP Playwright). Válido para o curso de Ciência de Dados.

```
1. GET  https://www.anhanguera.com/aluno/login
2. fill CPF → click Avançar
3. fill senha → click Avançar
4. wait_for_url **/aluno/meus-cursos
5. click [data-testid="card-enter-course-id-tecnologo-0"]
6. GET  https://www.anhanguera.com/aluno/tecnologo/KRT-c2e6f466-412d-4ed5-bcf6-e418880307cc/minhas-disciplinas
7. sleep(5) — aguarda React renderizar
8. click link com nome da disciplina → /enrollment/UUID
9. sleep(2) — aguarda página da disciplina
10. click button "UNIDADE N" → expande aulas
11. click [data-testid^="beta-learning-unit-card{N}-section{M}"] → abre aula
12. frame = page.locator('[data-testid="html-iframe"]').content_frame
    conteudo = frame.locator("body").inner_text()
```

---

## 4. Seletores confirmados

| Elemento | Seletor |
|---|---|
| Input CPF | `page.get_by_test_id("input-field-cpfLogin")` |
| Input senha | `page.get_by_test_id("passwordInput")` |
| Botão avançar | `page.get_by_test_id("btnForward")` |
| Card do curso | `page.get_by_test_id("card-enter-course-id-tecnologo-0")` |
| Link da disciplina | `page.get_by_role("link", name=NOME_EXATO_EM_MAIUSCULAS)` |
| Botões de unidade | `page.locator("button").filter(has_text=re.compile(r"UNIDADE\s+\d+", re.IGNORECASE))` |
| Cards de aula | `page.locator(f'[data-testid^="beta-learning-unit-card{N}-section"]')` |
| Iframe do conteúdo | `page.locator('[data-testid="html-iframe"]').content_frame` |

---

## 5. Nomes exatos das disciplinas no portal

Os nomes precisam ser idênticos ao que aparece no portal (maiúsculas, acentos incluídos).
Erros de grafia aqui fazem `get_by_role("link", name=...)` falhar silenciosamente.

**Semestre 1 (Aprovadas):**
- ESTRUTURA DE DADOS
- BANCOS DE DADOS EM NUVEM
- MODELAGEM DE DADOS
- ARQUITETURA DE DADOS
- GEOMETRIA ANALÍTICA E ÁLGEBRA VETORIAL
- PROJETO DE EXTENSÃO I - CIÊNCIA DE DADOS

**Semestre 2 (confirmados):**
- PROBABILIDADE E ESTATÍSTICA PARA ANÁLISE DE DADOS
- PROCESSAMENTO DE LINGUAGEM NATURAL-NLP
- PROJETO INTEGRADO INOVAÇÃO - CIÊNCIA DE DADOS
- CÁLCULO DIFERENCIAL E INTEGRAL I

---

## 6. Decisão: automatizar ou fazer na mão

| Tarefa | Recomendação | Motivo |
|---|---|---|
| Mapeamento de unidades/aulas (JSON) | Mão | É feito uma vez por disciplina. 5 min manual vs horas de debug |
| Extração de conteúdo de aulas | Automatizar | Volume alto (~120 aulas). Manual seria 3-4h de trabalho repetitivo |
| Dashboard dinâmico de scraping | Não fazer | Overkill para uso pessoal de estudo |

---

## 8. O Exterminador de Tutorais (Joyride Overlays) 🛡️

### O Problema
O portal usa o `react-joyride` para tutoriais. Esses pop-ups criam um "Spotlight" (holofote) e um "Overlay" (camada por cima) que bloqueia cliques, mesmo que o elemento esteja visível.

### A Solução (JS Injection)
Injetar um script na página que remove as classes do Joyride do DOM antes de qualquer clique crítico:

```python
def dismiss_popups(page):
    try:
        # Remove a máscara escura e o foco do tutorial
        page.evaluate("() => document.querySelectorAll('.react-joyride__overlay').forEach(el => el.remove())")
        page.evaluate("() => document.querySelectorAll('.react-joyride__spotlight').forEach(el => el.remove())")
    except: pass
    # Fecha botões comuns que aparecem em cima
    for btn in ["Entendi", "✕"]:
        try: page.get_by_role("button", name=btn).click(timeout=1000)
        except: pass
```

---

## 9. Lidando com Títulos Truncados e Dinâmicos 🎯

### O Problema
O portal trunca títulos longos no menu de unidades (ex: `Análise e Interpretação...`). Buscar pelo nome exato falha se o nome estiver cortado ou modificado por porcentagens (ex: `100%`).

### A Solução (Método de Posição ou Regex Parcial)
1. **Regex Parcial:** Usar `re.compile(f"Texto Parcial", re.I)` para ignorar maiúsculas/minúsculas e truncamentos.
2. **Índice de Posição (Sênior):** Contar os cards dentro da unidade e clicar no **N-ésimo** filho (`.nth(X)`). Isso ignora o nome do arquivo e foca na ordem lógica da disciplina.

```python
# Clica no 4º item (Aula 4) da lista de cards visíveis
cards = page.locator('[data-testid^="beta-learning-unit-card4-section"]')
cards.nth(3).click(force=True) # 0-indexed
```

---

## 10. Robustez do Login (Lags de Backend) 🐢

### O Problema
Após clicar em "Avançar" no CPF, o backend do portal leva tempo para validar o usuário e carregar o campo de senha. Timeouts de 20s costumam falhar em horários de pico.

### A Solução (Paciência de 60s)
1. Usar `time.sleep(15)` após o CPF para o portal "se encontrar".
2. Setar `wait_for(state="visible", timeout=60000)` para o `passwordInput`.
3. Adicionar um print de progresso em cada etapa (`[LOGIN] Digitando CPF...`) para saber exatamente onde o servidor está travando.

```python
page.get_by_test_id("btnForward").click(force=True)
page.keyboard.press("Enter") # Garante o envio do form
page.get_by_test_id("passwordInput").wait_for(state="visible", timeout=60000)
```

---

## 11. Arquitetura de Resumos (O Cérebro) 🧠

### O Fluxo de Estudo Mastigado
Conforme o `RESUMIDOR_WORKFLOW.md`, não basta extrair o dado bruto. Para gerar valor de estudo, precisamos:
1. **Processar o `conteudo_bruto.txt`** via IA.
2. **Gerar `aula-Z.py`** com simulações práticas.
3. **Gerar `explicacao.md`** com tom lúdico e emojis.
4. **Sinalizar como `concluido`** para controle de progresso.

---
**Última atualização:** Março/2026 — *Vencendo as barreiras da Anhanguera.*
