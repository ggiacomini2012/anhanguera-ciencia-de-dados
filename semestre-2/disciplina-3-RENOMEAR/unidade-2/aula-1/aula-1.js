// aula-1.js
// Autor: Exemplificando Aula
// Descrição: Este script demonstra os conceitos de Padrões de Sistemas,
//            Sistemas Distribuídos e Mobile em JavaScript, aplicados ao
//            desafio do app de supermercado.

// --- SEÇÃO 1: PADRÕES DE SISTEMAS (Design Patterns) ---
console.log("--- 🏗️  Seção 1: Aplicando Padrões de Projeto ---");

// Padrão de Projeto: Singleton
// Usando o padrão de módulo para garantir uma única instância.
const ShoppingCart = (function() {
    let instance;

    function createInstance() {
        let items = [];
        console.log("🛒 Criando o carrinho de compras ÚNICO para esta sessão.");
        return {
            addItem: function(item) {
                console.log(`   -> Item '${item}' adicionado ao carrinho.`);
                items.push(item);
            },
            getItems: function() {
                return items;
            }
        };
    }

    return {
        getInstance: function() {
            if (!instance) {
                instance = createInstance();
            }
            return instance;
        }
    };
})();

// Padrão de Projeto: Factory
// A fábrica decide qual objeto de usuário criar.
class User {
    // Em JS, podemos usar uma classe base ou simplesmente
    // garantir que as classes filhas implementem o método.
    getDiscount() {
        throw new Error("Método 'getDiscount' deve ser implementado.");
    }
}

class NormalUser extends User {
    getDiscount() {
        return 0.0;
    }
}

class PremiumUser extends User {
    getDiscount() {
        return 0.15; // 15% de desconto
    }
}

function userFactory(userType) {
    console.log(`👤 Fábrica criando um usuário do tipo: ${userType}.`);
    if (userType === 'premium') {
        return new PremiumUser();
    }
    return new NormalUser();
}


// --- SEÇÃO 2: PADRÕES DE SISTEMAS DISTRIBUÍDOS (Simulação) ---
console.log("\n--- 🌐 Seção 2: Simulando um Sistema Distribuído ---");

// Função helper para simular a latência da rede
const delay = ms => new Promise(res => setTimeout(res, ms));

// Padrão de Arquitetura: Broker (API Gateway)
// O Broker é um intermediário assíncrono para nossos microservices.
class Broker {
    constructor() {
        console.log("📮 Inicializando o Broker (Central de Comunicações).");
        this._services = new Map();
    }

    registerService(name, service) {
        this._services.set(name, service);
        console.log(`   -> Serviço '${name}' registrado.`);
    }

    async routeRequest(serviceName, payload) {
        console.log(`\nBroker recebeu requisição para '${serviceName}'...`);
        if (this._services.has(serviceName)) {
            const service = this._services.get(serviceName);
            return await service.handleRequest(payload);
        } else {
            return Promise.reject("Erro: Serviço não encontrado.");
        }
    }
}

// Simulação de Microservices
class ProductService {
    async handleRequest(productId) {
        console.log(`   [ProductService] Buscando dados do produto '${productId}'.`);
        await delay(500); // Simulando chamada de rede/banco de dados
        return { id: productId, name: "Café Especial", price: 25.50 };
    }
}

class RecommendationService {
    async handleRequest(user) {
        console.log(`   [RecommendationService] Gerando recomendações...`);
        await delay(500); // Simulando processamento de IA
        if (user instanceof PremiumUser) {
            return ["Croissant", "Geleia Artesanal"];
        }
        return ["Leite em pó", "Açúcar Refinado"];
    }
}

// --- SEÇÃO 3: PADRÕES DE SISTEMAS MOBILE (Simulação) ---
console.log("\n--- 📱 Seção 3: Simulando Padrões para App Mobile ---");

// Padrão de Projeto: Adapter
// O Adapter traduz chamadas unificadas para APIs específicas de cada plataforma.
class IOS_UI {
    renderButtonOnScreen(x, y) {
        console.log(`🎨 [iOS] Desenhando um botão com cantos arredondados em (${x},${y}).`);
    }
}

class Android_UI {
    drawMaterialButton(coordX, coordY) {
        console.log(`🎨 [Android] Desenhando um botão Material Design em (${coordX},${coordY}).`);
    }
}

class UIAdapter {
    constructor(os) {
        this.os = os;
        if (os === 'ios') {
            this._uiKit = new IOS_UI();
            console.log("   -> Adaptador configurado para iOS.");
        } else if (os === 'android') {
            this._uiKit = new Android_UI();
            console.log("   -> Adaptador configurado para Android.");
        } else {
            throw new Error("Sistema Operacional não suportado");
        }
    }

    drawButton(x, y) {
        console.log(`App solicitou um botão em (${x},${y}). O Adaptador está traduzindo...`);
        if (this.os === 'ios') {
            this._uiKit.renderButtonOnScreen(x, y);
        } else if (this.os === 'android') {
            this._uiKit.drawMaterialButton(x, y);
        }
    }
}

// --- SEÇÃO 4: VAMOS EXERCITAR! (Orquestrando o Fluxo) ---
// Usamos uma função `async` auto-executável para poder usar `await`.
(async function main() {
    console.log("\n--- 👷‍♀️ Seção 4: Executando o Desafio do Supermercado ---");

    // 1. Configuração do ambiente (simulando um dispositivo iOS)
    const sistemaOperacionalAtual = 'ios';
    const adapterUI = new UIAdapter(sistemaOperacionalAtual);

    // 2. Configuração do Backend
    const broker = new Broker();
    broker.registerService("products", new ProductService());
    broker.registerService("recommendations", new RecommendationService());

    // 3. Simulação do fluxo do usuário
    console.log("\n--- Início da Simulação da Jornada do Usuário ---");

    // Usuário Premium faz login
    const currentUser = userFactory('premium');

    // App renderiza a UI com o Adapter
    adapterUI.drawButton(15, 30); // Botão "Ver Ofertas"
    adapterUI.drawButton(15, 95); // Botão "Finalizar Compra"

    // App busca dados de um produto via Broker (chamada assíncrona)
    const productInfo = await broker.routeRequest("products", "prod_67890");
    console.log("   RESPOSTA DO BROKER:", productInfo);

    // App busca recomendações via Broker
    const recommendations = await broker.routeRequest("recommendations", currentUser);
    console.log("   RESPOSTA DO BROKER:", recommendations);

    // Usuário usa o carrinho de compras (Singleton)
    const cart = ShoppingCart.getInstance();
    cart.addItem(productInfo.name);
    cart.addItem(recommendations[0]);

    // Outra parte do código pega a instância do carrinho
    const anotherCartReference = ShoppingCart.getInstance();
    console.log(`\nO carrinho tem os itens: [${anotherCartReference.getItems().join(', ')}]`);
    console.log(`Os dois carrinhos são o mesmo objeto? -> ${cart === anotherCartReference}`);

    console.log("\n--- Fim da Simulação ---");
})();