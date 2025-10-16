import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.text.DecimalFormat;

// --- 1. CLASSE MODELO DE DADOS BRUTOS (Simulando o ODS) ---
class VendaODS {
    int idTransacao;
    String dataVenda;
    String regiaoVenda; // Pode estar inconsistente (Ex: "sudeste", "Sudeste")
    String nomeProduto;
    double valorBruto;
    int quantidade;

    public VendaODS(int id, String data, String regiao, String produto, double valor, int qtd) {
        this.idTransacao = id;
        this.dataVenda = data;
        this.regiaoVenda = regiao;
        this.nomeProduto = produto;
        this.valorBruto = valor;
        this.quantidade = qtd;
    }
}

// --- 2. CLASSE MODELO DE DADOS LIMPOS (Simulando o DW) ---
class VendaDW {
    String data;
    String regiao; // Já padronizada
    String produto;
    int quantidade;
    double receitaTotal; // Métrica calculada (FATO)

    public VendaDW(String data, String regiao, String produto, int quantidade, double receita) {
        this.data = data;
        this.regiao = regiao;
        this.produto = produto;
        this.quantidade = quantidade;
        this.receitaTotal = receita;
    }
}


public class Aula4 {

    // Simula a etapa de Transformação (T) do ETL
    public static List<VendaDW> transformarDados(List<VendaODS> dadosODS) {
        List<VendaDW> dadosDW = new ArrayList<>();

        System.out.println("2. TRANSFORMAÇÃO: Limpeza e Enriquecimento de Dados...");

        for (VendaODS item : dadosODS) {
            // T1: Padronização da Região (Limpeza de Dados)
            String regiaoPadronizada = item.regiaoVenda.substring(0, 1).toUpperCase() + 
                                       item.regiaoVenda.substring(1).toLowerCase();

            // T2: Cálculo da Receita Total (Enriquecimento)
            double receita = item.valorBruto * item.quantidade;

            // Cria o objeto DW (Modelo limpo)
            VendaDW vendaDW = new VendaDW(
                item.dataVenda,
                regiaoPadronizada,
                item.nomeProduto,
                item.quantidade,
                receita
            );
            dadosDW.add(vendaDW);
        }
        return dadosDW;
    }

    // Simula uma consulta SQL de Agregação (GROUP BY e SUM)
    public static Map<String, Double> consultarReceitaPorRegiao(List<VendaDW> dadosDW) {
        // O HashMap simula a agregação, onde a chave é a Região e o valor é a soma da Receita
        Map<String, Double> receitaPorRegiao = new HashMap<>();

        System.out.println("\n4. CONSULTA ANALÍTICA: Agrupando Receita por Região (Simulando SQL)...");

        for (VendaDW item : dadosDW) {
            String regiao = item.regiao;
            double receita = item.receitaTotal;

            // Se a região já existe, adiciona a receita; senão, inicializa.
            receitaPorRegiao.put(regiao, receitaPorRegiao.getOrDefault(regiao, 0.0) + receita);
        }
        return receitaPorRegiao;
    }

    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("#,##0.00");

        // --- 1. EXTRAÇÃO (E) - Dados Brutos do ODS ---
        System.out.println("1. EXTRAÇÃO: Capturando dados brutos do ODS.");
        List<VendaODS> dadosODS = new ArrayList<>();
        dadosODS.add(new VendaODS(101, "2025-09-01", "sudeste", "TV 50", 2500.50, 1));
        dadosODS.add(new VendaODS(102, "2025-09-01", "Sudeste", "FONE Bluetooth", 150.00, 2));
        dadosODS.add(new VendaODS(103, "2025-09-02", "NORTE", "TV 50", 2500.50, 1));
        dadosODS.add(new VendaODS(104, "2025-09-02", "Norte", "FONE Bluetooth", 150.00, 3));
        dadosODS.add(new VendaODS(105, "2025-09-03", "SUL", "TV 50", 2500.50, 1));
        dadosODS.add(new VendaODS(106, "2025-09-03", "sul", "FONE Bluetooth", 150.00, 4));

        // --- 2. TRANSFORMAÇÃO E CARGA (T e L) para o DW ---
        List<VendaDW> dadosDW = transformarDados(dadosODS);
        System.out.println("3. CARGA: Dados limpos carregados no DW. Total de " + dadosDW.size() + " registros.");


        // --- 4. CONSULTA E GERAÇÃO DE RELATÓRIO ---
        Map<String, Double> relatorioReceita = consultarReceitaPorRegiao(dadosDW);

        System.out.println("\n--- RELATÓRIO FINAL: Receita por Região ---");
        String regiaoMaisRentavel = "";
        double maiorReceita = 0.0;

        for (Map.Entry<String, Double> entrada : relatorioReceita.entrySet()) {
            String regiao = entrada.getKey();
            double receita = entrada.getValue();

            System.out.println("Região " + regiao + ": R$ " + df.format(receita));

            if (receita > maiorReceita) {
                maiorReceita = receita;
                regiaoMaisRentavel = regiao;
            }
        }

        // --- 5. TOMADA DE DECISÃO ---
        System.out.println("\n--- TOMADA DE DECISÃO ---");
        System.out.println("KPI de Receita por Região indica que:");
        System.out.println("A **Região " + regiaoMaisRentavel + "** é a mais rentável (R$ " + df.format(maiorReceita) + ").");
        System.out.println("Ação: Direcionar a verba de marketing para impulsionar a região de menor receita ou focar no campeão de vendas.");
    }
}