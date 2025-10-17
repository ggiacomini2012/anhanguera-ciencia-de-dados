import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Arquivo: Aula5.java
 * Tema: Arquitetura de Dados Corporativos, Modelagem Dimensional e Análise OLAP em Java
 * * Este código simula a estrutura de um Data Warehouse (Tabelas Fato e Dimensão) 
 * e executa uma consulta analítica (OLAP) sobre as vendas.
 */

// ==============================================================================
// 1. MODELAGEM DIMENSIONAL: Classes representando as Dimensões e Fatos (Esquema Estrela)
// ==============================================================================

/**
 * Dimensão Produto: Descreve o produto.
 */
class DimensaoProduto {
    int idProduto;
    String nome;
    String categoria;

    public DimensaoProduto(int idProduto, String nome, String categoria) {
        this.idProduto = idProduto;
        this.nome = nome;
        this.categoria = categoria;
    }

    // Getters para uso na análise
    public int getIdProduto() { return idProduto; }
    public String getCategoria() { return categoria; }
}

/**
 * Tabela Fato Vendas: Contém as métricas e as chaves das dimensões.
 */
class FatoVendas {
    int idTransacao;
    int idProduto; // Chave Estrangeira para DimensaoProduto
    String uf;      // Chave Estrangeira (Simplificada) para DimensaoLocalizacao
    double valorLiquido; // O "Fato" (Métrica)
    
    // Metadado Operacional (Simulado)
    String dataCarga;

    public FatoVendas(int idTransacao, int idProduto, String uf, double valorLiquido, String dataCarga) {
        this.idTransacao = idTransacao;
        this.idProduto = idProduto;
        this.uf = uf;
        this.valorLiquido = valorLiquido;
        this.dataCarga = dataCarga;
    }
    
    // Getters para uso na análise
    public String getUf() { return uf; }
    public double getValorLiquido() { return valorLiquido; }
}

public class Aula5 {
    
    // ==============================================================================
    // 2. CARGA (L) - Inserção de Dados no DW
    // ==============================================================================
    private static List<FatoVendas> carregarFatos() {
        List<FatoVendas> fatos = new ArrayList<>();
        // Dados que já passaram pela Transformação (limpos e padronizados)
        fatos.add(new FatoVendas(101, 1001, "SP", 1350.45, "2024-10-17"));
        fatos.add(new FatoVendas(102, 1002, "RJ", 45.00, "2024-10-17"));
        fatos.add(new FatoVendas(103, 1003, "SP", 180.89, "2024-10-17"));
        fatos.add(new FatoVendas(104, 1004, "MG", 405.00, "2024-10-17"));
        fatos.add(new FatoVendas(105, 1002, "RJ", 45.00, "2024-10-17"));
        return fatos;
    }
    
    private static List<DimensaoProduto> carregarDimensaoProdutos() {
        List<DimensaoProduto> produtos = new ArrayList<>();
        produtos.add(new DimensaoProduto(1001, "Notebook X", "Eletrônicos"));
        produtos.add(new DimensaoProduto(1002, "MousePad", "Acessórios"));
        produtos.add(new DimensaoProduto(1003, "Fone Pro", "Áudio"));
        produtos.add(new DimensaoProduto(1004, "Teclado Mec", "Periféricos"));
        return produtos;
    }
    
    // ==============================================================================
    // 3. ANÁLISE OLAP (Processamento Analítico Online) - Usando Stream API
    // ==============================================================================
    
    /**
     * Simula uma consulta OLAP para calcular o total de vendas por UF.
     * Corresponde a uma agregação (SLICE) sobre a Dimensão Localização.
     * @param fatos Lista de Fatos de Vendas.
     * @return Um mapa com a UF (String) e o Total de Vendas (Double).
     */
    private static Map<String, Double> analisarVendasPorUF(List<FatoVendas> fatos) {
        System.out.println("--- 3.1. Análise OLAP: Agregando Vendas por UF (Slice) ---");
        
        // Uso da Stream API para simular a agregação de um sistema OLAP
        Map<String, Double> vendasPorUF = fatos.stream()
            .collect(Collectors.groupingBy(
                FatoVendas::getUf,
                Collectors.summingDouble(FatoVendas::getValorLiquido)
            ));
        
        return vendasPorUF;
    }

    /**
     * Simula uma consulta mais complexa, agregando por Categoria (DRIL-DOWN/ROLL-UP),
     * que exige a junção da Tabela Fato com a Tabela Dimensão Produto.
     * @param fatos Lista de Fatos de Vendas.
     * @param produtos Lista de Dimensão Produto.
     * @return Um mapa com a Categoria (String) e o Total de Vendas (Double).
     */
    private static Map<String, Double> analisarVendasPorCategoria(List<FatoVendas> fatos, List<DimensaoProduto> produtos) {
        System.out.println("\n--- 3.2. Análise OLAP: Agregando Vendas por Categoria (Drill-Down) ---");
        
        // Mapeia a Dimensão Produto para acesso rápido (como um índice)
        Map<Integer, DimensaoProduto> mapaProdutos = produtos.stream()
            .collect(Collectors.toMap(DimensaoProduto::getIdProduto, p -> p));

        // Agregação, unindo Fato e Dimensão
        Map<String, Double> vendasPorCategoria = fatos.stream()
            .collect(Collectors.groupingBy(
                fato -> mapaProdutos.getOrDefault(fato.idProduto, new DimensaoProduto(0, "Desconhecido", "Outros")).getCategoria(),
                Collectors.summingDouble(FatoVendas::getValorLiquido)
            ));
        
        return vendasPorCategoria;
    }

    public static void main(String[] args) {
        // 1. Carregamento dos dados no DW
        List<FatoVendas> fatosVendas = carregarFatos();
        List<DimensaoProduto> dimProdutos = carregarDimensaoProdutos();

        System.out.println("--- 0. Estrutura do Data Warehouse (DW) em Java ---");
        System.out.println("Modelagem: Esquema Estrela (FatoVendas e DimensaoProduto).");
        System.out.println("Fatos carregados: " + fatosVendas.size());

        // 2. Consulta Analítica 1: Vendas por UF
        Map<String, Double> vendasUF = analisarVendasPorUF(fatosVendas);
        vendasUF.forEach((uf, total) -> 
            System.out.printf("UF %s: R$ %.2f\n", uf, total));
        
        // 3. Consulta Analítica 2: Vendas por Categoria (Join Fato-Dimensão)
        Map<String, Double> vendasCategoria = analisarVendasPorCategoria(fatosVendas, dimProdutos);
        vendasCategoria.forEach((categoria, total) -> 
            System.out.printf("Categoria %s: R$ %.2f\n", categoria, total));

        // Metadados de Negócio (exemplo estático)
        System.out.println("\n--- 4. Uso de Metadados de Negócio ---");
        System.out.println("O 'valorLiquido' é a métrica principal. Definição: 'Valor de venda final já com 10% de imposto subtraído (limpo).'");
        System.out.println("✅ Simulação de Modelagem DW e Análise OLAP em Java concluída.");
    }
}