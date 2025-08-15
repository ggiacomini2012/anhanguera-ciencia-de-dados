# Passo 1: Definindo a classe para representar um Contato
class Contato:
    """
    Representa um contato com id, nome e telefone.
    """
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        """
        Retorna uma representação em string do contato.
        """
        return f"ID: {self.id}, Nome: {self.nome}, Telefone: {self.telefone}"

# Passo 2: Definindo a classe para o Nó da Árvore AVL
class NodoAVL:
    """
    Representa um nó em uma Árvore AVL.
    Cada nó armazena um contato, sua altura na árvore e referências
    para os filhos esquerdo e direito.
    """
    def __init__(self, contato):
        self.contato = contato
        self.esquerdo = None
        self.direito = None
        self.altura = 1  # A altura de um novo nó (folha) é sempre 1

# Passo 3: Definindo a classe principal da Agenda com a Árvore AVL
class AgendaAVL:
    """
    Implementa a agenda de contatos usando uma Árvore AVL.
    As operações de inserção e remoção garantem que a árvore
    permaneça balanceada.
    """

    def __init__(self):
        self.raiz = None

    # --- Funções Auxiliares para Balanceamento ---

    def _altura(self, nodo):
        """Retorna a altura de um nó. Se o nó for nulo, retorna 0."""
        if not nodo:
            return 0
        return nodo.altura

    def _fator_balanceamento(self, nodo):
        """Calcula o fator de balanceamento de um nó."""
        if not nodo:
            return 0
        return self._altura(nodo.esquerdo) - self._altura(nodo.direito)

    def _atualizar_altura(self, nodo):
        """Recalcula a altura de um nó com base na altura de seus filhos."""
        if not nodo:
            return 0
        return 1 + max(self._altura(nodo.esquerdo), self._altura(nodo.direito))

    # --- Rotações para Manter o Balanceamento ---

    def _rotacao_direita(self, z):
        """Executa uma rotação simples à direita."""
        y = z.esquerdo
        T3 = y.direito

        # Realiza a rotação
        y.direito = z
        z.esquerdo = T3

        # Atualiza as alturas
        z.altura = self._atualizar_altura(z)
        y.altura = self._atualizar_altura(y)

        return y

    def _rotacao_esquerda(self, z):
        """Executa uma rotação simples à esquerda."""
        y = z.direito
        T2 = y.esquerdo

        # Realiza a rotação
        y.esquerdo = z
        z.direito = T2

        # Atualiza as alturas
        z.altura = self._atualizar_altura(z)
        y.altura = self._atualizar_altura(y)

        return y

    # --- Operações Principais: Adicionar, Remover, Buscar ---

    def adicionar(self, contato):
        """Função pública para adicionar um novo contato na agenda."""
        if not isinstance(contato, Contato):
            raise ValueError("Apenas objetos do tipo Contato podem ser adicionados.")
        self.raiz = self._adicionar(self.raiz, contato)
        print(f"Contato '{contato.nome}' adicionado com sucesso.")

    def _adicionar(self, raiz_atual, contato):
        """Função recursiva para inserir um contato e balancear a árvore."""
        # 1. Inserção padrão de uma Árvore de Busca Binária
        if not raiz_atual:
            return NodoAVL(contato)
        elif contato.id < raiz_atual.contato.id:
            raiz_atual.esquerdo = self._adicionar(raiz_atual.esquerdo, contato)
        else:
            raiz_atual.direito = self._adicionar(raiz_atual.direito, contato)

        # 2. Atualizar a altura do nó ancestral
        raiz_atual.altura = self._atualizar_altura(raiz_atual)

        # 3. Obter o fator de balanceamento
        balance = self._fator_balanceamento(raiz_atual)

        # 4. Se o nó estiver desbalanceado, realizar as rotações
        # Caso Esquerda-Esquerda
        if balance > 1 and contato.id < raiz_atual.esquerdo.contato.id:
            return self._rotacao_direita(raiz_atual)

        # Caso Direita-Direita
        if balance < -1 and contato.id > raiz_atual.direito.contato.id:
            return self._rotacao_esquerda(raiz_atual)

        # Caso Esquerda-Direita
        if balance > 1 and contato.id > raiz_atual.esquerdo.contato.id:
            raiz_atual.esquerdo = self._rotacao_esquerda(raiz_atual.esquerdo)
            return self._rotacao_direita(raiz_atual)

        # Caso Direita-Esquerda
        if balance < -1 and contato.id < raiz_atual.direito.contato.id:
            raiz_atual.direito = self._rotacao_direita(raiz_atual.direito)
            return self._rotacao_esquerda(raiz_atual)

        return raiz_atual

    def remover(self, id):
        """Função pública para remover um contato pelo ID."""
        self.raiz = self._remover(self.raiz, id)
        print(f"Tentativa de remoção do contato com ID {id}.")


    def _remover(self, raiz_atual, id):
        """Função recursiva para remover um contato e balancear a árvore."""
        if not raiz_atual:
            return raiz_atual

        # 1. Remoção padrão de uma Árvore de Busca Binária
        if id < raiz_atual.contato.id:
            raiz_atual.esquerdo = self._remover(raiz_atual.esquerdo, id)
        elif id > raiz_atual.contato.id:
            raiz_atual.direito = self._remover(raiz_atual.direito, id)
        else:
            if raiz_atual.esquerdo is None:
                temp = raiz_atual.direito
                raiz_atual = None
                return temp
            elif raiz_atual.direito is None:
                temp = raiz_atual.esquerdo
                raiz_atual = None
                return temp
            
            temp = self._get_min_value_node(raiz_atual.direito)
            raiz_atual.contato = temp.contato
            raiz_atual.direito = self._remover(raiz_atual.direito, temp.contato.id)

        if raiz_atual is None:
            return raiz_atual

        # 2. Atualizar altura
        raiz_atual.altura = self._atualizar_altura(raiz_atual)

        # 3. Obter fator de balanceamento
        balance = self._fator_balanceamento(raiz_atual)

        # 4. Balancear a árvore
        # Caso Esquerda-Esquerda
        if balance > 1 and self._fator_balanceamento(raiz_atual.esquerdo) >= 0:
            return self._rotacao_direita(raiz_atual)
        
        # Caso Esquerda-Direita
        if balance > 1 and self._fator_balanceamento(raiz_atual.esquerdo) < 0:
            raiz_atual.esquerdo = self._rotacao_esquerda(raiz_atual.esquerdo)
            return self._rotacao_direita(raiz_atual)

        # Caso Direita-Direita
        if balance < -1 and self._fator_balanceamento(raiz_atual.direito) <= 0:
            return self._rotacao_esquerda(raiz_atual)

        # Caso Direita-Esquerda
        if balance < -1 and self._fator_balanceamento(raiz_atual.direito) > 0:
            raiz_atual.direito = self._rotacao_direita(raiz_atual.direito)
            return self._rotacao_esquerda(raiz_atual)

        return raiz_atual

    def _get_min_value_node(self, nodo):
        """Retorna o nó com o menor valor (ID) encontrado em uma subárvore."""
        if nodo is None or nodo.esquerdo is None:
            return nodo
        return self._get_min_value_node(nodo.esquerdo)


    def buscar_por_nome(self, nome):
        """Busca contatos pelo nome e retorna uma lista de correspondências."""
        resultados = []
        self._buscar_por_nome_recursivo(self.raiz, nome, resultados)
        return resultados

    def _buscar_por_nome_recursivo(self, nodo, nome, resultados):
        """Percorre a árvore em ordem para encontrar contatos por nome."""
        if not nodo:
            return

        # Busca na subárvore esquerda
        self._buscar_por_nome_recursivo(nodo.esquerdo, nome, resultados)

        # Verifica o nó atual
        if nome.lower() in nodo.contato.nome.lower():
            resultados.append(nodo.contato)

        # Busca na subárvore direita
        self._buscar_por_nome_recursivo(nodo.direito, nome, resultados)
        
    def imprimir_agenda(self):
        """Imprime todos os contatos da agenda em ordem de ID."""
        self._percorrer_em_ordem(self.raiz)

    def _percorrer_em_ordem(self, nodo):
        """Percorre a árvore em ordem (esquerda, raiz, direita) para impressão."""
        if nodo:
            self._percorrer_em_ordem(nodo.esquerdo)
            print(nodo.contato)
            self._percorrer_em_ordem(nodo.direito)


# --- Exemplo de Uso ---
if __name__ == "__main__":
    # 1. Criando a agenda
    minha_agenda = AgendaAVL()

    # 2. Adicionando contatos
    print("--- Adicionando Contatos ---")
    minha_agenda.adicionar(Contato(10, "Ana", "1111-1111"))
    minha_agenda.adicionar(Contato(20, "Beto", "2222-2222"))
    minha_agenda.adicionar(Contato(30, "Carla", "3333-3333"))
    minha_agenda.adicionar(Contato(5, "Daniel", "4444-4444"))
    minha_agenda.adicionar(Contato(15, "Eva", "5555-5555"))
    minha_agenda.adicionar(Contato(25, "Ana Julia", "6666-6666"))

    # 3. Exibindo todos os contatos (em ordem de ID)
    print("\n--- Agenda Completa (em ordem de ID) ---")
    minha_agenda.imprimir_agenda()

    # 4. Buscando contatos por nome
    print("\n--- Buscando contatos com nome 'Ana' ---")
    resultados_busca = minha_agenda.buscar_por_nome("Ana")
    if resultados_busca:
        for contato in resultados_busca:
            print(contato)
    else:
        print("Nenhum contato encontrado com o nome 'Ana'.")
        
    # 5. Removendo um contato
    print("\n--- Removendo o contato com ID 10 (Ana) ---")
    minha_agenda.remover(10)
    
    # 6. Exibindo a agenda novamente após a remoção
    print("\n--- Agenda Após Remoção ---")
    minha_agenda.imprimir_agenda()