// Aula_2.java
// Exemplo em Java: Simulação de Modelos Lógicos de Dados para a empresa de Varejo.
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// --- 1. MODELO LÓGICO CORPORATIVO (MLC): As Entidades ---

/**
 * Representa a entidade Cliente do MLC.
 * Esta é a definição lógica e estrutural do dado.
 */
class Cliente {
    int idCliente;
    String nome;
    String regiao;

    public Cliente(int idCliente, String nome, String regiao) {
        this.idCliente = idCliente;
        this.nome = nome;
        this.regiao = regiao;
    }

    @Override
    public String toString() {
        return "Cliente{ID=" + idCliente + ", Nome='" + nome + "', Regiao='" + regiao + "'}";
    }
}

/**
 * Representa a entidade Produto do MLC.
 */
class Produto {
    int idProduto;
    String nome;
    double preco;

    public Produto(int idProduto, String nome, double preco) {
        this.idProduto = idProduto;
        this.nome = nome;
        this.preco = preco;
    }
    
    public double getPreco() {
        return preco;
    }

    @Override
    public String toString() {
        return "Produto{ID=" + idProduto + ", Nome='" + nome + "', Preco=" + preco + "}";
    }
}

/**
 * Representa a entidade Venda (o FATO), definindo o RELACIONAMENTO (MER).
 */
class Venda {
    int idVenda;
    int idCliente; // Chave Estrangeira
    int idProduto; // Chave Estrangeira
    int quantidade;
    String data;

    public Venda(int idVenda, int idCliente, int idProduto, int quantidade, String data) {
        this.idVenda = idVenda;
        this.idCliente = idCliente;
        this.idProduto = idProduto;
        this.quantidade = quantidade;
        this.data = data;
    }

    public int getIdProduto() {
        return idProduto;
    }

    public int getQuantidade() {
        return quantidade;
    }
}

// --- 2. MODELO LÓGICO DE REPOSITÓRIO (MLR) - Simulação do Data Warehouse ---

/**
 * Simula um Data Warehouse de Vendas.
 * Utiliza estruturas de dados para representar as tabelas (Fatos e Dimensões).
 */
class DataWarehouseVendas {
    // Tabelas de Dimensão (para lookup rápido)
    private Map<Integer, Cliente> dimClientes = new HashMap<>();
    private Map<Integer, Produto> dimProdutos = new HashMap<>();
    
    // Tabela de Fato
    private List<Venda> fatoVendas = new ArrayList<>();

    public DataWarehouseVendas(List<Cliente> clientes, List<Produto> produtos, List<Venda> vendas) {
        // Carrega as Dimensões
        for (Cliente c : clientes) {
            dimClientes.put(c.idCliente, c);
        }
        for (Produto p : produtos) {
            dimProdutos.put(p.idProduto, p);
        }
        // Carrega o Fato
        fatoVendas.addAll(vendas);
        System.out.println("[DW Vendas] Carregados " + fatoVendas.size() + " registros de vendas.");
    }

    /**
     * Calcula o faturamento total, demonstrando o uso do modelo lógico relacional (Fato + Dimensão).
     */
    public double calcularFaturamentoTotal() {
        double faturamento = 0.0;
        for (Venda venda : fatoVendas) {
            Produto produto = dimProdutos.get(venda.getIdProduto());
            if (produto != null) {
                faturamento += venda.getQuantidade() * produto.getPreco();
            }
        }
        return faturamento;
    }
    
    /**
     * Simulação de uma análise para a Área de Interesse de Marketing (Filtrando Dimensões).
     */
    public List<Cliente> buscarClientesPorRegiao(String regiaoFoco) {
        List<Cliente> clientesSegmentados = new ArrayList<>();
        for (Cliente cliente : dimClientes.values()) {
            if (cliente.regiao.equalsIgnoreCase(regiaoFoco)) {
                clientesSegmentados.add(cliente);
            }
        }
        return clientesSegmentados;
    }
}

// --- 3. EXECUÇÃO PRINCIPAL ---

public class Aula_2 {
    public static void main(String[] args) {
        System.out.println("--- DEMONSTRAÇÃO DA ARQUITETURA DE DADOS EM JAVA ---");

        // DADOS DE EXEMPLO (População das Entidades MLC)
        List<Cliente> clientesDados = List.of(
            new Cliente(101, "Ana Silva", "Sul"),
            new Cliente(102, "Bruno Costa", "Norte"),
            new Cliente(103, "Carla Meirelles", "Sul"),
            new Cliente(104, "David Lopes", "Norte")
        );

        List<Produto> produtosDados = List.of(
            new Produto(501, "Celular X", 1500.00),
            new Produto(502, "Notebook Y", 4500.00),
            new Produto(503, "Fone Z", 250.00)
        );

        List<Venda> vendasDados = List.of(
            new Venda(1, 101, 501, 1, "2024-09-01"),
            new Venda(2, 102, 503, 2, "2024-09-02"),
            new Venda(3, 101, 502, 1, "2024-09-03"),
            new Venda(4, 104, 501, 3, "2024-09-04"),
            new Venda(5, 103, 503, 1, "2024-09-05"),
            new Venda(6, 102, 502, 1, "2024-09-06")
        );
        
        // 1. Implementação do Data Warehouse (MLR Corporativo)
        System.out.println("\n[MLR] Inicializando Data Warehouse...");
        DataWarehouseVendas dwVarejo = new DataWarehouseVendas(clientesDados, produtosDados, vendasDados);

        // Uso do DW para uma métrica corporativa
        double faturamento = dwVarejo.calcularFaturamentoTotal();
        System.out.printf("✅ Análise Corporativa (DW): Faturamento Total = R$%.2f\n", faturamento);

        // 2. Uso da Área de Interesse (MAI) - Marketing
        String regiaoFoco = "Sul";
        List<Cliente> clientesSul = dwVarejo.buscarClientesPorRegiao(regiaoFoco);
        
        System.out.println("\n🎯 Análise de Marketing (MAI): Clientes da Região '" + regiaoFoco + "':");
        for (Cliente c : clientesSul) {
            System.out.println("- " + c.nome);
        }
    }
}