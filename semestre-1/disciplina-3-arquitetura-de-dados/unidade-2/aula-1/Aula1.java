// aula-1.java
// Autor: Exemplificando Aula
// Descrição: Este arquivo demonstra os conceitos de Padrões de Sistemas,
//            Sistemas Distribuídos e Mobile em Java, aplicados ao
//            desafio do app de supermercado.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Classe principal que orquestra a simulação
public class Aula1 {

    public static void main(String[] args) throws InterruptedException {
        // --- SEÇÃO 4: VAMOS EXERCITAR! (Orquestrando o Fluxo) ---
        System.out.println("\n--- 👷‍♀️ Seção 4: Executando o Desafio do Supermercado ---");

        // 1. Configuração do ambiente (simulando um dispositivo Android)
        String sistemaOperacionalAtual = "android";
        UIAdapter adapterUI = new UIAdapter(sistemaOperacionalAtual);

        // 2. Configuração do Backend (Broker e Serviços)
        Broker broker = new Broker();
        broker.registerService("products", new ProductService());
        broker.registerService("recommendations", new RecommendationService());

        // 3. Simulação do fluxo do usuário
        System.out.println("\n--- Início da Simulação da Jornada do Usuário ---");

        // Usuário Premium faz login
        User currentUser = UserFactory.getUser("premium");

        // App renderiza a UI com o Adapter
        adapterUI.drawButton(10, 20); // Botão "Minha Conta"
        adapterUI.drawButton(10, 80); // Botão "Carrinho"

        // App busca dados de um produto via Broker
        String productInfo = (String) broker.routeRequest("products", "prod_abcde");
        System.out.println("   RESPOSTA DO BROKER: " + productInfo);

        // App busca recomendações via Broker
        @SuppressWarnings("unchecked")
        List<String> recommendations = (List<String>) broker.routeRequest("recommendations", currentUser);
        System.out.println("   RESPOSTA DO BROKER: " + recommendations);

        // Usuário usa o carrinho de compras (Singleton)
        ShoppingCart cart = ShoppingCart.getInstance();
        cart.addItem("Queijo Provolone");
        cart.addItem(recommendations.get(0));

        // Outra parte do código pega a mesma instância do carrinho
        ShoppingCart anotherCartReference = ShoppingCart.getInstance();
        System.out.println("\nO carrinho tem os itens: " + anotherCartReference.getItems());
        System.out.println("Os dois carrinhos são o mesmo objeto? -> " + (cart == anotherCartReference));

        System.out.println("\n--- Fim da Simulação ---");
    }
}


// --- SEÇÃO 1: PADRÕES DE SISTEMAS (Design Patterns) ---

// Padrão de Projeto: Singleton
class ShoppingCart {
    private static ShoppingCart instance;
    private List<String> items;

    private ShoppingCart() {
        System.out.println("🛒 Criando o carrinho de compras ÚNICO para esta sessão.");
        this.items = new ArrayList<>();
    }

    public static ShoppingCart getInstance() {
        if (instance == null) {
            instance = new ShoppingCart();
        }
        return instance;
    }

    public void addItem(String item) {
        System.out.println("   -> Item '" + item + "' adicionado ao carrinho.");
        this.items.add(item);
    }

    public List<String> getItems() {
        return this.items;
    }
}

// Padrão de Projeto: Factory
interface User {
    double getDiscount();
}

class NormalUser implements User {
    @Override
    public double getDiscount() { return 0.0; }
}

class PremiumUser implements User {
    @Override
    public double getDiscount() { return 0.20; } // 20% de desconto
}

class UserFactory {
    public static User getUser(String userType) {
        System.out.println("👤 Fábrica criando um usuário do tipo: " + userType);
        if ("premium".equalsIgnoreCase(userType)) {
            return new PremiumUser();
        }
        return new NormalUser();
    }
}


// --- SEÇÃO 2: PADRÕES DE SISTEMAS DISTRIBUÍDOS (Simulação) ---

// Interface para os microservices
interface Service {
    Object handleRequest(Object payload) throws InterruptedException;
}

// Padrão de Arquitetura: Broker
class Broker {
    private Map<String, Service> services = new HashMap<>();

    public Broker() {
        System.out.println("\n--- 🌐 Seção 2: Simulando um Sistema Distribuído ---");
        System.out.println("📮 Inicializando o Broker (Central de Comunicações).");
    }

    public void registerService(String name, Service service) {
        services.put(name, service);
        System.out.println("   -> Serviço '" + name + "' registrado.");
    }

    public Object routeRequest(String serviceName, Object payload) throws InterruptedException {
        System.out.println("\nBroker recebeu requisição para '" + serviceName + "'...");
        Service service = services.get(serviceName);
        if (service != null) {
            return service.handleRequest(payload);
        }
        return "Erro: Serviço não encontrado.";
    }
}

// Simulação de Microservices
class ProductService implements Service {
    @Override
    public Object handleRequest(Object payload) throws InterruptedException {
        System.out.println("   [ProductService] Buscando dados do produto '" + payload + "'.");
        Thread.sleep(500); // Simulando latência de rede
        return "{\"id\": \"" + payload + "\", \"name\": \"Vinho Tinto Seco\", \"price\": 75.90}";
    }
}

class RecommendationService implements Service {
    @Override
    public Object handleRequest(Object payload) throws InterruptedException {
        User user = (User) payload;
        System.out.println("   [RecommendationService] Gerando recomendações...");
        Thread.sleep(500); // Simulando processamento de IA
        if (user instanceof PremiumUser) {
            return List.of("Azeite Extra Virgem", "Salmão Fresco");
        }
        return List.of("Refrigerante", "Salsicha");
    }
}


// --- SEÇÃO 3: PADRÕES DE SISTEMAS MOBILE (Simulação) ---

// "Adaptees": As classes com interfaces incompatíveis
class IOS_UI {
    public void renderAppleButton(int x, int y) {
        System.out.println("🎨 [iOS] Desenhando um botão com visual da Apple em (" + x + "," + y + ").");
    }
}

class Android_UI {
    public void drawMaterialButton(int coordX, int coordY) {
        System.out.println("🎨 [Android] Desenhando um botão Material Design em (" + coordX + "," + coordY + ").");
    }
}

// Padrão de Projeto: Adapter
class UIAdapter {
    private String os;
    private IOS_UI iosKit;
    private Android_UI androidKit;

    public UIAdapter(String os) {
        System.out.println("\n--- 📱 Seção 3: Simulando Padrões para App Mobile ---");
        this.os = os;
        if ("ios".equals(os)) {
            this.iosKit = new IOS_UI();
            System.out.println("   -> Adaptador configurado para iOS.");
        } else if ("android".equals(os)) {
            this.androidKit = new Android_UI();
            System.out.println("   -> Adaptador configurado para Android.");
        }
    }

    public void drawButton(int x, int y) {
        System.out.println("App solicitou um botão em (" + x + "," + y + "). O Adaptador está traduzindo...");
        if ("ios".equals(this.os)) {
            iosKit.renderAppleButton(x, y);
        } else if ("android".equals(this.os)) {
            androidKit.drawMaterialButton(x, y);
        }
    }
}