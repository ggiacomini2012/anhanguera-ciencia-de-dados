# É necessário instalar a biblioteca matplotlib para a visualização da Quadtree
# pip install matplotlib

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

#------------------------------------------------------------------------------
# PARTE 1: EXEMPLO DA ÁRVORE B PARA GERENCIADOR DE ANOTAÇÕES
#------------------------------------------------------------------------------

print("="*50)
print("PARTE 1: Árvore B para Gerenciador de Anotações")
print("="*50)

class Anotacao:
    """
    Representa uma anotação em um livro. A chave de ordenação é uma tupla
    (pagina, paragrafo), permitindo uma busca rápida e ordenada.
    """
    def __init__(self, pagina, paragrafo, texto):
        self.pagina = pagina
        self.paragrafo = paragrafo
        self.texto = texto
        # A chave é uma tupla para garantir a ordenação correta.
        self.chave = (pagina, paragrafo)

    def __repr__(self):
        return f"Anotacao(Pág: {self.pagina}, Parág: {self.paragrafo}, Texto: '{self.texto}')"

class NodoB:
    """
    Representa um nó (ou página) em uma Árvore B.
    Contém uma lista de chaves (anotações) e uma lista de filhos.
    """
    def __init__(self, folha=False):
        self.folha = folha
        self.chaves = []
        self.filhos = []

class ArvoreB:
    """
    Implementação simplificada de uma Árvore B.
    't' é o grau mínimo da árvore. O número de chaves em um nó fica
    entre t-1 e 2t-1.
    """
    def __init__(self, t):
        self.raiz = NodoB(folha=True)
        self.t = t # Grau mínimo

    def inserir(self, anotacao):
        """
        Função principal de inserção. Lida com o caso especial da raiz estar cheia.
        """
        raiz_antiga = self.raiz
        # Se a raiz estiver cheia, a árvore cresce em altura.
        if len(raiz_antiga.chaves) == (2 * self.t) - 1:
            nova_raiz = NodoB()
            self.raiz = nova_raiz
            nova_raiz.filhos.insert(0, raiz_antiga)
            self._dividir_filho(nova_raiz, 0)
            self._inserir_nao_cheio(nova_raiz, anotacao)
        else:
            self._inserir_nao_cheio(raiz_antiga, anotacao)

    def _inserir_nao_cheio(self, nodo, anotacao):
        """
        Insere uma anotação em um nó que não está cheio.
        """
        i = len(nodo.chaves) - 1
        if nodo.folha:
            # Se é um nó folha, encontra a posição e insere a anotação
            nodo.chaves.append(None)
            while i >= 0 and anotacao.chave < nodo.chaves[i].chave:
                nodo.chaves[i + 1] = nodo.chaves[i]
                i -= 1
            nodo.chaves[i + 1] = anotacao
        else:
            # Se não é folha, encontra o filho correto para descer
            while i >= 0 and anotacao.chave < nodo.chaves[i].chave:
                i -= 1
            i += 1
            # Se o filho estiver cheio, divide-o antes de descer
            if len(nodo.filhos[i].chaves) == (2 * self.t) - 1:
                self._dividir_filho(nodo, i)
                if anotacao.chave > nodo.chaves[i].chave:
                    i += 1
            self._inserir_nao_cheio(nodo.filhos[i], anotacao)

    def _dividir_filho(self, nodo_pai, i):
        """
        Divide um filho 'i' do 'nodo_pai' que está cheio.
        """
        t = self.t
        filho_cheio = nodo_pai.filhos[i]
        novo_filho = NodoB(folha=filho_cheio.folha)

        # Move a chave mediana do filho cheio para o pai
        nodo_pai.chaves.insert(i, filho_cheio.chaves[t - 1])
        nodo_pai.filhos.insert(i + 1, novo_filho)

        # Move as chaves maiores para o novo filho
        novo_filho.chaves = filho_cheio.chaves[t:(2 * t) - 1]
        # Remove as chaves movidas do filho original
        filho_cheio.chaves = filho_cheio.chaves[0:t - 1]

        # Se não for folha, move os filhos também
        if not filho_cheio.folha:
            novo_filho.filhos = filho_cheio.filhos[t:(2 * t)]
            filho_cheio.filhos = filho_cheio.filhos[0:t]

    def consultar(self, chave, nodo=None):
        """
        Busca por uma chave (pagina, paragrafo) na árvore.
        Retorna a anotação se encontrada, caso contrário None.
        """
        nodo = nodo if nodo is not None else self.raiz
        i = 0
        while i < len(nodo.chaves) and chave > nodo.chaves[i].chave:
            i += 1
        if i < len(nodo.chaves) and chave == nodo.chaves[i].chave:
            return nodo.chaves[i]
        elif nodo.folha:
            return None
        else:
            return self.consultar(chave, nodo.filhos[i])

    def listar_anotacoes(self):
        """
        Retorna uma lista de todas as anotações em ordem.
        """
        anotacoes = []
        self._percorrer_em_ordem(self.raiz, anotacoes)
        return anotacoes

    def _percorrer_em_ordem(self, nodo, anotacoes):
        """
        Função auxiliar para percorrer a árvore em ordem.
        """
        if nodo:
            for i in range(len(nodo.chaves)):
                if not nodo.folha:
                    self._percorrer_em_ordem(nodo.filhos[i], anotacoes)
                anotacoes.append(nodo.chaves[i])
            if not nodo.folha:
                self._percorrer_em_ordem(nodo.filhos[-1], anotacoes)

# --- Demonstração da Árvore B ---
# Criando uma árvore com grau mínimo 3 (nós podem ter de 2 a 5 chaves)
arvore_anotacoes = ArvoreB(t=3)

# Criando e inserindo anotações
anotacoes_para_inserir = [
    Anotacao(10, 2, "Revisar este conceito."),
    Anotacao(5, 1, "Citação importante."),
    Anotacao(25, 3, "Ideia para o projeto final."),
    Anotacao(8, 4, "Lembrar da referência bibliográfica."),
    Anotacao(15, 1, "Definição chave."),
    Anotacao(3, 5, "Início do capítulo."),
    Anotacao(30, 1, "Conclusão do autor."),
]

print("Inserindo anotações na Árvore B...")
for an in anotacoes_para_inserir:
    print(f"Inserindo: {an}")
    arvore_anotacoes.inserir(an)

print("\n--- Listando todas as anotações em ordem ---")
lista_ordenada = arvore_anotacoes.listar_anotacoes()
for an in lista_ordenada:
    print(an)

print("\n--- Consultando anotações específicas ---")
chave_busca = (15, 1)
resultado = arvore_anotacoes.consultar(chave_busca)
print(f"Buscando pela chave {chave_busca}: {resultado}")

chave_busca = (100, 1)
resultado = arvore_anotacoes.consultar(chave_busca)
print(f"Buscando por uma chave inexistente {chave_busca}: {resultado}")

print("\nObservação: A remoção em Árvores B é um processo complexo que envolve a fusão")
print("ou redistribuição de chaves entre nós para manter o balanço, e foi omitida")
print("neste exemplo para focar nos conceitos principais de inserção e busca.\n")


#------------------------------------------------------------------------------
# PARTE 2: EXEMPLO DA QUADTREE PARA DADOS ESPACIAIS
#------------------------------------------------------------------------------

print("="*50)
print("PARTE 2: Quadtree para Visualização de Dados 2D")
print("="*50)

class Ponto:
    """Representa um ponto no espaço 2D."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class NoQuadtree:
    """Representa um nó (quadrante) na Quadtree."""
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.pontos = []
        self.dividido = False
        self.ne = None # Nordeste
        self.nw = None # Noroeste
        self.se = None # Sudeste
        self.sw = None # Sudoeste

    def contem(self, ponto):
        """Verifica se um ponto está dentro dos limites deste nó."""
        return (self.x <= ponto.x < self.x + self.largura and
                self.y <= ponto.y < self.y + self.altura)

class QuadTree:
    """A estrutura da Quadtree."""
    def __init__(self, x, y, largura, altura, capacidade):
        self.limite = NoQuadtree(x, y, largura, altura)
        self.capacidade = capacidade # Quantos pontos um nó pode conter antes de se dividir

    def subdividir(self, no):
        """Divide um nó em quatro sub-nós."""
        x, y, w, h = no.x, no.y, no.largura, no.altura
        hw, hh = w / 2, h / 2

        no.ne = NoQuadtree(x + hw, y + hh, hw, hh)
        no.nw = NoQuadtree(x, y + hh, hw, hh)
        no.se = NoQuadtree(x + hw, y, hw, hh)
        no.sw = NoQuadtree(x, y, hw, hh)
        no.dividido = True

    def inserir(self, ponto, no=None):
        """Insere um ponto na Quadtree."""
        if no is None:
            no = self.limite

        if not no.contem(ponto):
            return False

        if len(no.pontos) < self.capacidade:
            no.pontos.append(ponto)
            return True
        else:
            if not no.dividido:
                self.subdividir(no)

            if self.inserir(ponto, no.ne): return True
            if self.inserir(ponto, no.nw): return True
            if self.inserir(ponto, no.se): return True
            if self.inserir(ponto, no.sw): return True

    def desenhar(self, ax, no=None):
        """Função recursiva para desenhar os limites dos nós da Quadtree."""
        if no is None:
            no = self.limite

        rect = patches.Rectangle((no.x, no.y), no.largura, no.altura, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        if no.dividido:
            self.desenhar(ax, no.ne)
            self.desenhar(ax, no.nw)
            self.desenhar(ax, no.se)
            self.desenhar(ax, no.sw)

# --- Demonstração da Quadtree ---
print("Gerando visualização da Quadtree...")

# Configuração da figura
fig, ax = plt.subplots(1)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal', adjustable='box')
ax.set_title("Exemplo de Quadtree")

# Criando a Quadtree com capacidade 4 por nó
qtree = QuadTree(0, 0, 100, 100, capacidade=4)

# Inserindo 100 pontos aleatórios
pontos_x = []
pontos_y = []
for _ in range(100):
    p = Ponto(random.uniform(0, 100), random.uniform(0, 100))
    pontos_x.append(p.x)
    pontos_y.append(p.y)
    qtree.inserir(p)

# Desenhando a árvore e os pontos
qtree.desenhar(ax)
ax.scatter(pontos_x, pontos_y, s=10, c='b')

print("A imagem gerada mostra como o espaço foi dividido recursivamente.")
print("Quadrantes com mais pontos foram divididos mais vezes.")
plt.show()