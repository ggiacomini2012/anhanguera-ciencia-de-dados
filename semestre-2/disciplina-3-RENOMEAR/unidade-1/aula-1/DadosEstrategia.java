// Arquivo: aula-1.java
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Classe que exemplifica a Arquitetura de Dados e a Pirâmide DIKW (Data, Information, Knowledge, Wisdom)
 * no contexto de um E-commerce.
 */
public class DadosEstrategia {

    // Representação do DADO Bruto (O Esquema Físico da transação)
    static class Transacao {
        int transacaoId;
        String clienteId;
        String produtoCor;
        double valor;
        String data;

        public Transacao(int transacaoId, String clienteId, String produtoCor, double valor, String data) {
            this.transacaoId = transacaoId;
            this.clienteId = clienteId;
            this.produtoCor = produtoCor;
            this.valor = valor;
            this.data = data;
        }

        @Override
        public String toString() {
            return String.format("{ID: %d, Cliente: %s, Cor: %s, Valor: %.2f}", 
                                  transacaoId, clienteId, produtoCor, valor);
        }
    }

    // Representação da INFORMAÇÃO (Dados refinados e contextualizados)
    static class ClienteInfo {
        String clienteId;
        double totalGasto;
        int numCompras;
        double ticketMedio;

        public ClienteInfo(String clienteId, double totalGasto, int numCompras) {
            this.clienteId = clienteId;
            this.totalGasto = totalGasto;
            this.numCompras = numCompras;
            this.ticketMedio = totalGasto / numCompras;
        }

        @Override
        public String toString() {
            return String.format("Cliente %s | Total Gasto: %.2f | Compras: %d | Ticket Médio: %.2f",
                                  clienteId, totalGasto, numCompras, ticketMedio);
        }
    }

    public static void main(String[] args) {
        
        // --- 1. DADOS (Data) Brutos ---
        List<Transacao> dadosBrutos = new ArrayList<>();
        dadosBrutos.add(new Transacao(1001, "C001", "azul", 150.00, "2023-09-01"));
        dadosBrutos.add(new Transacao(1002, "C002", "verde", 50.00, "2023-09-01"));
        dadosBrutos.add(new Transacao(1003, "C001", "verde", 200.00, "2023-09-02"));
        dadosBrutos.add(new Transacao(1004, "C003", "azul", 80.00, "2023-09-02"));
        dadosBrutos.add(new Transacao(1005, "C002", "vermelho", 120.00, "2023-09-03"));

        System.out.println("--- 1. DADOS (Data) Brutos ---");
        dadosBrutos.forEach(System.out::println);
        System.out.println("=".repeat(50) + "\n");
        
        // --- 2. INFORMAÇÃO (Information): Refinando os Dados ---
        List<ClienteInfo> informacaoContextualizada = refinarParaInformacao(dadosBrutos);

        System.out.println("--- 2. INFORMAÇÃO (Information) Contextualizada ---");
        informacaoContextualizada.forEach(System.out::println);
        System.out.println("=".repeat(50) + "\n");

        // --- 3. CONHECIMENTO (Knowledge): Padrões de Compra ---
        String conhecimentoGerado = gerarConhecimento(dadosBrutos);

        System.out.println("--- 3. CONHECIMENTO (Knowledge) - Padrão Descoberto ---");
        System.out.println(conhecimentoGerado);
        System.out.println("=".repeat(50) + "\n");

        // --- 4. SABEDORIA (Wisdom): Ação Estratégica ---
        System.out.println("--- 4. SABEDORIA (Wisdom) - Direcional Estratégico ---");
        aplicarSabedoria(conhecimentoGerado, informacaoContextualizada);
        System.out.println("=".repeat(50) + "\n");
    }
    
    /**
     * Simula a camada de Arquitetura de Dados (ETL) para transformar DADOS em INFORMAÇÃO.
     */
    private static List<ClienteInfo> refinarParaInformacao(List<Transacao> dados) {
        Map<String, List<Transacao>> transacoesPorCliente = 
            dados.stream().collect(Collectors.groupingBy(t -> t.clienteId));

        List<ClienteInfo> infoList = new ArrayList<>();
        
        for (Map.Entry<String, List<Transacao>> entry : transacoesPorCliente.entrySet()) {
            String clienteId = entry.getKey();
            List<Transacao> listaTransacoes = entry.getValue();
            
            double totalGasto = listaTransacoes.stream().mapToDouble(t -> t.valor).sum();
            int numCompras = listaTransacoes.size();
            
            infoList.add(new ClienteInfo(clienteId, totalGasto, numCompras));
        }
        return infoList;
    }

    /**
     * Simula a análise de dados para gerar CONHECIMENTO (o como/padrão).
     */
    private static String gerarConhecimento(List<Transacao> dados) {
        Set<String> clientesAzul = dados.stream()
            .filter(t -> t.produtoCor.equals("azul"))
            .map(t -> t.clienteId)
            .collect(Collectors.toSet());

        Set<String> clientesVerde = dados.stream()
            .filter(t -> t.produtoCor.equals("verde"))
            .map(t -> t.clienteId)
            .collect(Collectors.toSet());

        // Interseção: clientes que compraram AZUL E VERDE
        clientesAzul.retainAll(clientesVerde);
        
        if (!clientesAzul.isEmpty()) {
            return "PADRÃO ENCONTRADO: Os clientes " + clientesAzul + " compram AZUL e VERDE. Forte indicador de 'Cross-selling'.";
        } else {
            return "Nenhum padrão de compra AZUL/VERDE significativo encontrado.";
        }
    }

    /**
     * Simula a aplicação do CONHECIMENTO e INFORMAÇÃO para a SABEDORIA (o porquê/ação).
     */
    private static void aplicarSabedoria(String conhecimento, List<ClienteInfo> informacao) {
        
        // Sabedoria 1: Baseada no Padrão de Cross-selling
        if (conhecimento.contains("AZUL e VERDE")) {
            System.out.println("✅ AÇÃO ESTRATÉGICA (Sabedoria): Criar uma regra de negócio para oferecer promoções em produtos VERDES para clientes que acabaram de comprar AZUL.");
        }
        
        // Sabedoria 2: Baseada em Alta Informação (Ticket Médio)
        double ticketMedioMeta = 150.00;
        List<String> clientesElite = informacao.stream()
            .filter(c -> c.ticketMedio >= ticketMedioMeta)
            .map(c -> c.clienteId)
            .collect(Collectors.toList());
            
        if (!clientesElite.isEmpty()) {
            System.out.println("✅ AÇÃO ESTRATÉGICA (Sabedoria): Clientes com Ticket Médio maior que R$" + String.format("%.2f", ticketMedioMeta) + " (" + clientesElite + ") serão alocados no 'Programa VIP' para retenção de alto valor.");
        }
    }
}