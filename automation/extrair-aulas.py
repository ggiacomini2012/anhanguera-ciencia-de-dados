import os
import sys
import time
import pathlib
import re
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

# MISSÃO FINAL: AULAS 4 E 5 POR POSIÇÃO
SCRIPT_DIR = pathlib.Path(__file__).parent
BASE_DIR = (
    SCRIPT_DIR.parent
    / "semestre-2"
    / "disciplina-1-probabilidade-e-estatistica-para-analise-de-dados"
    / "unidade-4"
)

DASHBOARD_URL = "https://www.anhanguera.com/aluno/meus-cursos"

def dismiss_popups(page):
    try:
        page.evaluate("() => document.querySelectorAll('.react-joyride__overlay').forEach(el => el.remove())")
        page.evaluate("() => document.querySelectorAll('.react-joyride__spotlight').forEach(el => el.remove())")
    except: pass
    for btn in ["Entendi", "✕"]:
        try: page.get_by_role("button", name=btn).click(timeout=1000)
        except: pass

def ir_para_unidade4(page):
    print("[*] Dashboard...")
    page.goto(DASHBOARD_URL)
    time.sleep(10)
    dismiss_popups(page)
    
    print("[*] Clicando no curso: Ciência de Dados...")
    page.get_by_test_id("card-enter-course-id-tecnologo-0").click(force=True)
    
    print("[*] Disciplinas...")
    page.get_by_test_id("see-all-subjects").wait_for(state="visible", timeout=20000)
    page.get_by_test_id("see-all-subjects").click(force=True)
    
    # Aba Aprovadas para Probabilidade
    print("[*] Aba Aprovadas...")
    try: page.get_by_role("tab", name="Aprovadas").click(timeout=5000)
    except: pass
    time.sleep(3)

    print("[*] Selecionando Probabilidade...")
    page.get_by_role("link", name=re.compile("PROBABILIDADE", re.I)).click(force=True)
    time.sleep(10)
    dismiss_popups(page)
    
    print("[*] Expandindo UNIDADE 4...")
    page.get_by_role("button", name=re.compile("UNIDADE 4", re.I)).last.click(force=True)
    time.sleep(5)

def extrair_aula_por_posicao(page, pos_index: int):
    """Clica no N-ésimo card da unidade aberta e extrai texto."""
    print(f"\n🎯 ALVO: EXTRAINDO ITEM {pos_index} da Unidade 4...")
    
    # Localiza todos os cards de aula dentro da Unidade 4
    # Usamos o data-testid beta-learning-unit-card4 porque sabemos que i=4
    cards = page.locator('[data-testid^="beta-learning-unit-card4-section"]')
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
    print(f"[*] {count} seções encontradas na {aula_nome}.")

    blocos = []
    for i in range(count):
        secao = sections.nth(i)
        nome_secao = secao.inner_text().strip().replace("\n", " ")
        print(f"    [{i+1}/{count}] Lendo: {nome_secao[:50]}...")
        secao.click(force=True)
        time.sleep(6)

        try:
            iframe = page.locator('[data-testid="html-iframe"]')
            iframe.wait_for(state="visible", timeout=15000)
            texto = iframe.content_frame.locator("body").inner_text(timeout=20000)
            blocos.append(f"=== SEÇÃO {i+1}: {nome_secao} ===\n\n{texto.strip()}\n")
            print(f"       ✅ SUCESSO.")
        except:
            print(f"       ⚠️  Sem texto.")
            blocos.append(f"=== SEÇÃO {i+1}: {nome_secao} ===\n\n[MÍDIA]\n")

    save_path.write_text("\n\n".join(blocos), encoding="utf-8")
    print(f"🏆 SALVO: {save_path}")

def main():
    cpf = os.getenv("ANHANGUERA_CPF")
    senha = os.getenv("ANHANGUERA_SENHA")
    print("\n[INÍCIO] Robô Ativo - Método de Posição (4 e 5) 🤖")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # LOGIN (REFORÇADO contra lentidão extrema)
        print("[LOGIN] Acessando site...")
        page.goto("https://www.anhanguera.com/aluno/login")
        time.sleep(15) 
        dismiss_popups(page)
        
        print(f"[LOGIN] Digitando CPF...")
        page.get_by_test_id("input-field-cpfLogin").fill(cpf)
        page.get_by_test_id("btnForward").click(force=True)
        page.keyboard.press("Enter")
        
        print("[LOGIN] Aguardando campo de senha (Paciência de 60s)...")
        page.get_by_test_id("passwordInput").wait_for(state="visible", timeout=60000)
        
        print("[LOGIN] Digitando Senha...")
        page.get_by_test_id("passwordInput").fill(senha)
        page.get_by_test_id("btnForward").click(force=True)
        
        print("[LOGIN] Aguardando Meus Cursos...")
        page.wait_for_url("**/aluno/meus-cursos", timeout=120000)
        print("✅ Login Realizado!")


        
        # EXTRAÇÃO POR POSIÇÃO (Aula 4 e Aula 5)
        for p_idx in [4, 5]:
            try:
                ir_para_unidade4(page) # Garante que a unidade esteja aberta
                extrair_aula_por_posicao(page, p_idx)
                print(f"✅ Aula {p_idx} Finalizada!")
            except Exception as e:
                print(f"❌ Erro na posição {p_idx}: {e}")

        
        print("\n🎉 MISSÃO CUMPRIDA!")
        browser.close()

if __name__ == "__main__":
    main()
