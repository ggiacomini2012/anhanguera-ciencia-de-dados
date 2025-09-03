# Você foi apresentado à seguinte problemática:

# Você é um programador trabalhando em um sistema de gestão de bibliotecas e precisa desenvolver uma funcionalidade que armazene e gerencie informações sobre os livros e os empréstimos. Como você poderia construir uma solução em Python para tal?

# Para armazenar informações sobre os livros, você pode utilizar um dicionário built-in em Python, pois ele permite armazenar pares de chave-valor, facilitando a associação dos dados do livro com valores específicos.

# Usando um dicionário built-in para armazenar informações do livro

livros = {

'ISBN1': {'título': 'A Arte da Guerra', 'autor': 'Sun Tzu', 'ano': 500},

'ISBN2': {'título': '1984', 'autor': 'George Orwell', 'ano': 1949}

}

# Para gerenciar os empréstimos, você poderia definir uma classe personalizada, pois os empréstimos podem envolver operações mais complexas que beneficiariam de métodos específicos, como a atualização das datas de empréstimo e devolução ou o cálculo de multas por atraso.

# Definindo uma classe personalizada para empréstimos

# Uma classe é um "molde" ou "planta" para criar objetos. 
# Aqui, a classe `Emprestimo` servirá para criar objetos que representam cada empréstimo realizado na biblioteca.
class Emprestimo:
    # O método `__init__` é um método especial chamado "construtor". 
    # Ele é executado automaticamente sempre que um novo objeto da classe é criado (instanciado).
    # `self` é uma referência ao próprio objeto que está sendo criado. É através do `self` que definimos os atributos (características) do objeto.
    # `livro`, `data_emprestimo` e `data_devolucao` são os parâmetros que precisamos fornecer ao criar um novo empréstimo.
    def __init__(self, livro, data_emprestimo, data_devolucao):
        # Abaixo, estamos definindo os atributos do objeto.
        # `self.livro` cria um atributo chamado `livro` no objeto e atribui a ele o valor do parâmetro `livro`.
        self.livro = livro
        # `self.data_emprestimo` cria o atributo `data_emprestimo`.
        self.data_emprestimo = data_emprestimo
        # `self.data_devolucao` cria o atributo `data_devolucao`.
        self.data_devolucao = data_devolucao

# --- Como a classe Emprestimo funciona na prática ---

# "Instanciar" uma classe significa criar um objeto a partir do "molde" (a classe).
# Cada objeto é uma instância independente com seus próprios dados.

# Aqui, estamos criando o primeiro objeto de empréstimo, chamado `emprestimo1`.
# - `livros['ISBN1']` é o primeiro argumento, que passa o dicionário do livro "A Arte da Guerra".
# - `'2023-01-01'` é o segundo argumento, a data de empréstimo.
# - `'2023-01-15'` é o terceiro argumento, a data de devolução.
# O Python chama o método `__init__` da classe `Emprestimo` com esses valores.
emprestimo1 = Emprestimo(livros['ISBN1'], '2023-01-01', '2023-01-15') 

# Criando o segundo objeto de empréstimo, `emprestimo2`, para o livro "1984".
emprestimo2 = Emprestimo(livros['ISBN2'], '2023-02-01', '2023-02-15')

# --- Acessando os dados dos objetos ---

# Depois de criar os objetos, podemos acessar seus atributos (os dados que guardamos neles) usando a notação de ponto.

# Exemplo 1: Acessando os dados do primeiro empréstimo
print("--- Detalhes do Empréstimo 1 ---")
# O atributo `livro` do `emprestimo1` é um dicionário. Podemos acessar suas chaves.
print(f"Livro emprestado: {emprestimo1.livro['título']}")
print(f"Autor: {emprestimo1.livro['autor']}")
print(f"Data do empréstimo: {emprestimo1.data_emprestimo}")
print(f"Data de devolução: {emprestimo1.data_devolucao}")
print("\n") # Adiciona uma linha em branco para separar

# Exemplo 2: Acessando os dados do segundo empréstimo
print("--- Detalhes do Empréstimo 2 ---")
print(f"Livro emprestado: {emprestimo2.livro['título']}")
print(f"Data do empréstimo: {emprestimo2.data_emprestimo}")
print(f"Data de devolução: {emprestimo2.data_devolucao}")
print("\n")

# A grande vantagem da classe é que ela organiza a lógica. 
# Poderíamos, por exemplo, adicionar um método para verificar se um empréstimo está atrasado.
# (Isso é um passo mais avançado, mas mostra o poder das classes).

# A escolha entre estruturas de dados built-in e personalizadas depende das necessidades específicas do sistema. No exemplo da biblioteca:

# Os dicionários built-in são adequados para armazenar informações dos livros, pois oferecem uma maneira simples e eficiente de acessar e manipular dados associativos sem a necessidade de funcionalidades adicionais.
# As estruturas de dados definidas pelo usuário, como a classe Emprestimo, fornecem maior flexibilidade para incorporar lógicas de negócios complexas, como métodos para manipular as datas dos empréstimos e calcular atrasos, o que seria mais complicado de implementar com estruturas de dados built-in.
# Portanto, a decisão foi baseada na complexidade dos dados e operações necessárias: o uso pragmático de dicionários built-in para informações simples de livros e a criação de uma classe personalizada para gerenciar a lógica específica de empréstimos.
