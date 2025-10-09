// aula-2.js
// Exemplo em JavaScript: Simulação de Modelos Lógicos de Dados para Varejo.
// Usamos classes ES6 para definir as entidades (MLC) e objetos para os repositórios lógicos.

// --- 1. MODELO LÓGICO CORPORATIVO (MLC): As Entidades ---

/**
 * Representa a entidade Cliente (MLC).
 * Define a estrutura lógica dos dados do cliente.
 */
class Cliente {
    constructor(idCliente, nome, regiao) {
        this.idCliente = idCliente; // Atributo: Chave Primária
        this.nome = nome;           // Atributo: Detalhe
        this.regiao = regiao;       // Atributo: Detalhe
    }
}

/**
 * Representa a entidade Produto (MLC).
 */
class Produto {
    constructor(idProduto, nome, preco) {
        this.idProduto = idProduto;
        this.nome = nome;
        this.preco = preco;
    }
}

/**
 * Representa a entidade Venda (MLC), essencialmente o relacionamento entre Cliente e Produto.
 */
class Venda {
    constructor(idVenda, idCliente, idProduto, quantidade, data) {
        this.idVenda = idVenda;
        this.idCliente = idCliente; // Chave Estrangeira (Relacionamento com Cliente)
        this.idProduto = idProduto; // Chave Estrangeira (Relacionamento com Produto)
        this.quantidade = quantidade;
        this.data = data;
    }
}

// --- 2. MODELO DE ÁREA DE INTERESSE (MAI) & MODELO LÓGICO DE REPOSITÓRIO (MLR) ---

/**
 * Simula um Data Mart para a Área de Interesse de Marketing (MLR especializado).
 * Focado em segmentação de clientes.
 */
class DataMartMarketing {
    constructor() {
        // O repositório armazena os dados filtrados e relevantes
        this.clientes = [];
        console.log("\n[MAI/MLR] Data Mart de Marketing inicializado.");
    }

    carregarClientes(dadosClientes) {
        // Simula o processo ETL (Extração, Transformação, Carga) para o Data Mart.
        this.clientes = dadosClientes;
        console.log(`[Marketing] Carregados ${this.clientes.length} clientes para o Data Mart.`);
    }

    analisarClientesPorRegiao(regiaoFoco) {
        /** Exemplo de análise feita pelo departamento de Marketing. */
        return this.clientes.filter(cliente => cliente.regiao === regiaoFoco);
    }
}

/**
 * Simula um Data Warehouse centralizado (MLR abrangente) para análises corporativas.
 * Armazena Fatos (Vendas) e Dimensões (Clientes, Produtos).
 */
class DataWarehouseVendas {
    constructor() {
        this.dimClientes = {};
        this.dimProdutos = {};
        this.fatoVendas = [];
        console.log("\n[MAI/MLR] Data Warehouse de Vendas inicializado.");
    }

    carregarDadosCompletos(clientes, produtos, vendas) {
        // Mapeia Clientes e Produtos por ID para fácil acesso (simulando tabelas de dimensão)
        clientes.forEach(c => this.dimClientes[c.idCliente] = c);
        produtos.forEach(p => this.dimProdutos[p.idProduto] = p);
        
        // Carrega o Fato (Vendas)
        this.fatoVendas = vendas;
        console.log(`[DW Vendas] Carregados ${this.fatoVendas.length} registros de vendas para análise.`);
    }

    calcularFaturamentoTotal() {
        /** Exemplo de métrica de negócio que usa os relacionamentos do modelo lógico. */
        let faturamento = 0;
        
        this.fatoVendas.forEach(venda => {
            const produto = this.dimProdutos[venda.idProduto];
            if (produto) {
                faturamento += venda.quantidade * produto.preco;
            }
        });
        return faturamento;
    }
}

// --- DADOS DE EXEMPLO (População das Entidades MLC) ---

const clientesDados = [
    new Cliente(101, "Ana Silva", "Sul"),
    new Cliente(102, "Bruno Costa", "Norte"),
    new Cliente(103, "Carla Meirelles", "Sul"),
    new Cliente(104, "David Lopes", "Norte"),
];

const produtosDados = [
    new Produto(501, "Celular X", 1500.00),
    new Produto(502, "Notebook Y", 4500.00),
    new Produto(503, "Fone Z", 250.00),
];

const vendasDados = [
    new Venda(1, 101, 501, 1, "2024-09-01"),
    new Venda(2, 102, 503, 2, "2024-09-02"),
    new Venda(3, 101, 502, 1, "2024-09-03"),
    new Venda(4, 104, 501, 3, "2024-09-04"),
    new Venda(5, 103, 503, 1, "2024-09-05"),
    new Venda(6, 102, 502, 1, "2024-09-06"),
];

// --- EXECUÇÃO E DEMONSTRAÇÃO ---

console.log("--- DEMONSTRAÇÃO DA ARQUITETURA DE DADOS EM JAVASCRIPT ---");

// 1. Uso do Data Warehouse (MLR Corporativo)
const dwVarejo = new DataWarehouseVendas();
dwVarejo.carregarDadosCompletos(clientesDados, produtosDados, vendasDados);

const faturamentoTotal = dwVarejo.calcularFaturamentoTotal();
console.log(`\n✅ Análise Corporativa (DW): Faturamento Total = R$${faturamentoTotal.toFixed(2)}`);

// 2. Uso do Data Mart (MLR/MAI Especializado)
const dmMkt = new DataMartMarketing();
// O Data Mart carrega apenas a informação que lhe é relevante
dmMkt.carregarClientes(clientesDados);

const regiaoFoco = "Sul";
const clientesSul = dmMkt.analisarClientesPorRegiao(regiaoFoco);
console.log(`\n🎯 Análise de Marketing (DM): Clientes da Região '${regiaoFoco}':`);
clientesSul.forEach(c => console.log(`- ${c.nome}`));

console.log("\n🔍 Exemplo de Entidade do MLC:");
console.log(new Produto(1000, "Cadeira Ergonômica", 899.99));
// Note que as classes (MLC) fornecem a base estrutural para todos os repositórios.