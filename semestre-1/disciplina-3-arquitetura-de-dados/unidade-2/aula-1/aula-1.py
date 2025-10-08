# aula-1.py
# Autor: Exemplificando Aula
# Descrição: Este script demonstra os conceitos de Padrões de Sistemas,
#            Sistemas Distribuídos e Mobile aplicados ao desafio do app de supermercado.

import time
from abc import ABC, abstractmethod

# --- SEÇÃO 1: PADRÕES DE SISTEMAS (Design Patterns) ---
print("--- 🏗️  Seção 1: Aplicando Padrões de Projeto ---")

# Padrão de Projeto: Singleton
# Problema: Precisamos de uma única instância do carrinho de compras por sessão de usuário.
# Solução: O Singleton garante que apenas um objeto de carrinho seja criado.

class ShoppingCart:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("🛒 Criando o carrinho de compras ÚNICO para esta sessão.")
            cls._instance = super(ShoppingCart, cls).__new__(cls)
            cls._instance.items = []
        return cls._instance

    def add_item(self, item):
        print(f"   -> Item '{item}' adicionado ao carrinho.")
        self.items.append(item)

    def get_items(self):
        return self.items

# Padrão de Projeto: Factory
# Problema: Precisamos criar diferentes tipos de usuários (ex: Normal, Premium)
#           sem que o código principal precise saber os detalhes da criação de cada um.
# Solução: Uma "fábrica" decide qual objeto de usuário criar com base em um parâmetro.

class User(ABC):
    @abstractmethod
    def get_discount(self):
        pass

class NormalUser(User):
    def get_discount(self):
        return 0.0

class PremiumUser(User):
    def get_discount(self):
        return 0.15 # 15% de desconto

def user_factory(user_type):
    """A fábrica de usuários."""
    if user_type == 'premium':
        print("👤 Criando um usuário Premium. Bem-vindo de volta!")
        return PremiumUser()
    print("👤 Criando um usuário Normal.")
    return NormalUser()


# --- SEÇÃO 2: PADRÕES DE SISTEMAS DISTRIBUÍDOS (Simulação) ---
print("\n--- 🌐 Seção 2: Simulando um Sistema Distribuído ---")

# Padrão de Arquitetura: Broker (ou API Gateway)
# Problema: Em um sistema com múltiplos serviços (microservices), como o cliente
#           se comunica com eles de forma organizada e desacoplada?
# Solução: O Broker é um intermediário que recebe todas as requisições e as
#           redireciona para o serviço correto.

class Broker:
    def __init__(self):
        print("📮 Inicializando o Broker (Central de Comunicações).")
        self._services = {}

    def register_service(self, name, service):
        """Registra um serviço no broker."""
        self._services[name] = service
        print(f"   -> Serviço '{name}' registrado.")

    def route_request(self, service_name, payload):
        """Redireciona uma requisição para o serviço correto."""
        print(f"\nBroker recebeu requisição para '{service_name}'...")
        service = self._services.get(service_name)
        if service:
            return service.handle_request(payload)
        else:
            return "Erro: Serviço não encontrado."

# Simulação de Microservices
class ProductService:
    """Serviço que lida com informações de produtos."""
    def handle_request(self, product_id):
        print(f"   [ProductService] Buscando dados do produto '{product_id}'.")
        # Simula uma busca no banco de dados
        time.sleep(0.5)
        return {"id": product_id, "name": "Leite Integral", "price": 5.99}

class RecommendationService:
    """Serviço que gera recomendações personalizadas."""
    def handle_request(self, user):
        print(f"   [RecommendationService] Gerando recomendações para usuário...")
        # Lógica complexa de Machine Learning simulada aqui
        time.sleep(0.5)
        if isinstance(user, PremiumUser):
            return ["Vinho Importado", "Queijo Gorgonzola"]
        return ["Pão Francês", "Margarina"]


# --- SEÇÃO 3: PADRÕES DE SISTEMAS MOBILE (Simulação) ---
print("\n--- 📱 Seção 3: Simulando Padrões para App Mobile ---")

# Padrão de Projeto: Adapter
# Problema: O app precisa rodar em iOS e Android, que possuem componentes de UI
#           com interfaces (métodos) diferentes.
# Solução: O Adapter cria uma "capa" unificada. O app conversa com o Adapter,
#           e o Adapter "traduz" os comandos para a plataforma específica.

class IOS_UI:
    """API de UI específica do iOS."""
    def render_button_on_screen(self, x, y):
        print(f"🎨 [iOS] Desenhando um botão com cantos arredondados em ({x},{y}).")

class Android_UI:
    """API de UI específica do Android."""
    def draw_material_button(self, coord_x, coord_y):
        print(f"🎨 [Android] Desenhando um botão Material Design em ({coord_x},{coord_y}).")

class UIAdapter:
    """O Adapter que unifica as interfaces."""
    def __init__(self, os):
        self.os = os
        if os == 'ios':
            self._ui_kit = IOS_UI()
            print("   -> Adaptador configurado para iOS.")
        elif os == 'android':
            self._ui_kit = Android_UI()
            print("   -> Adaptador configurado para Android.")
        else:
            raise ValueError("Sistema Operacional não suportado")

    def draw_button(self, x, y):
        """Método unificado que o app usará."""
        print(f"App solicitou um botão em ({x},{y}). O Adaptador está traduzindo...")
        if self.os == 'ios':
            self._ui_kit.render_button_on_screen(x, y)
        elif self.os == 'android':
            self._ui_kit.draw_material_button(x, y)


# --- SEÇÃO 4: VAMOS EXERCITAR! (Orquestrando o Fluxo) ---
print("\n--- 👷‍♀️ Seção 4: Executando o Desafio do Supermercado ---")

# 1. Configuração do ambiente (simulando um dispositivo Android)
sistema_operacional_atual = 'android'
adapter_ui = UIAdapter(sistema_operacional_atual)

# 2. Configuração do Backend (Broker e Serviços)
broker = Broker()
broker.register_service("products", ProductService())
broker.register_service("recommendations", RecommendationService())

# 3. Simulação do fluxo do usuário
print("\n--- Início da Simulação da Jornada do Usuário ---")

# Usuário Premium faz login
current_user = user_factory('premium')

# O App renderiza a tela principal usando o Adapter
adapter_ui.draw_button(10, 20) # Botão de "Promoções"
adapter_ui.draw_button(10, 80) # Botão de "Meu Carrinho"

# Usuário pede para ver um produto, a requisição vai para o Broker
product_info = broker.route_request("products", "prod_12345")
print("   RESPOSTA DO BROKER:", product_info)

# Usuário recebe recomendações personalizadas
recommendations = broker.route_request("recommendations", current_user)
print("   RESPOSTA DO BROKER:", recommendations)

# Usuário usa o carrinho de compras (Singleton)
cart = ShoppingCart()
cart.add_item(product_info['name'])
cart.add_item(recommendations[0])

# Outra parte do código tenta criar um novo carrinho, mas recebe a mesma instância
another_cart_reference = ShoppingCart()
print(f"\nO carrinho tem os itens: {another_cart_reference.get_items()}")
print(f"Os dois carrinhos são o mesmo objeto? -> {cart is another_cart_reference}")

print("\n--- Fim da Simulação ---")