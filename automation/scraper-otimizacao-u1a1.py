import os
import sys
import time
import pathlib
import re
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

SCRIPT_DIR = pathlib.Path(__file__).parent
BASE_DIR = (
    SCRIPT_DIR.parent
    / "semestre-2"
    / "disciplina-5-RENOMEAR"  # pasta de Otimizacao e Pesquisa Operacional
    / "unidade-1"
)

DASHBOARD_URL = "https://www.anhanguera.com/aluno/meus-cursos"

# Qual aula scraping (posição 1-based dentro da unidade)
AULAS_ALVO = [1]  # ajuste para [1,2,3,4] se quiser todas

def dismiss_popups(page):
    try:
        page.evaluate("() => document.querySelectorAll('.react-joyride__overlay').forEach(el => el.remove())")
        page.evaluate("() => document.querySelectorAll('.react-joyride__spotlight').forEach(el => el.remove())")
    except: pass
    for btn in ["Entendi", "✕"]:
        try: page.get_by_role("button", name=btn).click(timeout=1000)
        except: pass

def ir_para_otimizacao_u1(page):
    print("[*] Navegando para o Dashboard...")
    page.goto(DASHBOARD_URL)
    time.sleep(10)
    dismiss_popups(page)

    print("[*] Clicando no curso: Ciência de Dados...")
    page.get_by_test_id("card-enter-course-id-tecnologo-0").click(force=True)

    print("[*] Abrindo todas as disciplinas...")
    page.get_by_test_id("see-all-subjects").wait_for(state="visible", timeout=20000)
    page.get_by_test_id("see-all-subjects").click(force=True)
    time.sleep(3)

    # Otimização fica na aba padrão "Em Andamento" (não precisa mudar aba)
    print("[*] Procurando disciplina Otimização e Pesquisa Operacional...")
    page.get_by_role("link", name=re.compile("OTIMIZA", re.I)).click(force=True)
    time.sleep(10)
    dismiss_popups(page)

    print("[*] Expandindo UNIDADE 1...")
    page.get_by_role("button", name=re.compile("UNIDADE 1", re.I)).first.click(force=True)
    time.sleep(5)

def extrair_aula_por_posicao(page, unit_index: int, pos_index: int):
    """Clica no N-ésimo card da unidade aberta e extrai o texto secção a secção."""
    print(f"\n🎯 ALVO: Unidade {unit_index}, Aula {pos_index}...")

    # data-testid cards seguem o padrão beta-learning-unit-card{unit}-section
    cards = page.locator(f'[data-testid^="beta-learning-unit-card{unit_index}-section"]')
    cards.first.wait_for(state="visible", timeout=20000)

    card = cards.nth(pos_index - 1)
    aula_nome = card.inner_text().split("\n")[0]
    print(f"[*] Capturando: {aula_nome}")

    card.click(force=True)
    time.sleep(8)
    dismiss_popups(page)

    save_dir = BASE_DIR / f"aula-{pos_index}" / "web-scraping"
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / "conteudo_bruto.txt"

    sections = page.locator('[data-testid^="beta-section-menu-list-item"]')
    count = sections.count()
    print(f"[*] {count} seções encontradas.")

    blocos = []
    for i in range(count):
        secao = sections.nth(i)
        nome_secao = secao.inner_text().strip().replace("\n", " ")
        print(f"    [{i+1}/{count}] Lendo: {nome_secao[:60]}...")
        secao.click(force=True)
        time.sleep(6)

        try:
            iframe = page.locator('[data-testid="html-iframe"]')
            iframe.wait_for(state="visible", timeout=15000)
            texto = iframe.content_frame.locator("body").inner_text(timeout=20000)
            blocos.append(f"=== SECAO {i+1}: {nome_secao} ===\n\n{texto.strip()}\n")
            print(f"       OK - {len(texto)} chars")
        except:
            print(f"       AVISO: Sem texto (midia).")
            blocos.append(f"=== SECAO {i+1}: {nome_secao} ===\n\n[MIDIA/SEM TEXTO]\n")

    save_path.write_text("\n\n".join(blocos), encoding="utf-8")
    print(f"\nSALVO: {save_path}")
    return str(save_path)

def main():
    cpf = os.getenv("ANHANGUERA_CPF")
    senha = os.getenv("ANHANGUERA_SENHA")
    print("\n[INICIO] Robo Scraper - Otimizacao e Pesquisa Operacional - U1")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # LOGIN
        print("[LOGIN] Acessando portal...")
        page.goto("https://www.anhanguera.com/aluno/login")
        time.sleep(30)  # portal é lento (~60s delay documentado)
        dismiss_popups(page)

        print("[LOGIN] Aguardando campo CPF aparecer...")
        page.get_by_test_id("input-field-cpfLogin").wait_for(state="visible", timeout=60000)
        print("[LOGIN] CPF...")
        page.get_by_test_id("input-field-cpfLogin").fill(cpf)
        page.get_by_test_id("btnForward").click(force=True)
        page.keyboard.press("Enter")

        print("[LOGIN] Aguardando campo de senha (ate 60s)...")
        page.get_by_test_id("passwordInput").wait_for(state="visible", timeout=60000)

        print("[LOGIN] Senha...")
        page.get_by_test_id("passwordInput").fill(senha)
        page.get_by_test_id("btnForward").click(force=True)

        print("[LOGIN] Aguardando redirecionamento para Meus Cursos...")
        page.wait_for_url("**/aluno/meus-cursos", timeout=120000)
        print("Login OK!")

        # EXTRACAO
        for aula_idx in AULAS_ALVO:
            try:
                ir_para_otimizacao_u1(page)
                path = extrair_aula_por_posicao(page, unit_index=1, pos_index=aula_idx)
                print(f"\nAula {aula_idx} concluida -> {path}")
            except Exception as e:
                print(f"\nERRO na Aula {aula_idx}: {e}")
                import traceback; traceback.print_exc()

        print("\nMISSAO CUMPRIDA!")
        input("Pressione Enter para fechar o browser...")
        browser.close()

if __name__ == "__main__":
    main()
