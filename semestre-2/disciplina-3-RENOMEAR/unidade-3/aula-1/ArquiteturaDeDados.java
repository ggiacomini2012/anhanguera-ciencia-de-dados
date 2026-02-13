import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ArquiteturaDeDados {

    // 1. CLASSE ESTRUTURADA: Simula um registro de tabela com campos fixos (como um DADO ESTRUTURADO)
    static class ClienteEstruturado {
        public final int id_cliente;
        public final String nome;
        public final String cpf;
        public final int satisfacaoEstrelas;

        public ClienteEstruturado(int id, String n, String c, int e) {
            this.id_cliente = id;
            this.nome = n;
            this.cpf = c;
            this.satisfacaoEstrelas = e;
        }

        @Override
        public String toString() {
            return "{ID: " + id_cliente + ", Nome: " + nome + ", Estrelas: " + satisfacaoEstrelas + "}";
        }
    }

    public static void main(String[] args) {
        
        System.out.println("--- Tipos de Dados em Java para Arquitetura ---");

        // --- 1. DADOS ESTRUTURADOS (Lista de Objetos de Classe Fixa) ---
        // A lista de clientes força todos os objetos a terem exatamente os mesmos campos.
        System.out.println("\n--- 1. DADOS ESTRUTURADOS (List<ClienteEstruturado>) ---");
        
        List<ClienteEstruturado> clientesEstruturados = new ArrayList<>();
        clientesEstruturados.add(new ClienteEstruturado(1, "Mario de Souza", "111.111.111-11", 5));
        clientesEstruturados.add(new ClienteEstruturado(2, "Anderson Inácio", "222.222.222-22", 3));
        
        // Cálculo em dados estruturados (muito eficiente)
        double totalEstrelas = 0;
        for (ClienteEstruturado cliente : clientesEstruturados) {
            totalEstrelas += cliente.satisfacaoEstrelas;
        }
        double mediaSatisfacao = totalEstrelas / clientesEstruturados.size();
        
        System.out.printf("Média de Satisfação: %.2f estrelas\n", mediaSatisfacao);
        System.out.println("Registro do Cliente 1: " + clientesEstruturados.get(0));
        System.out.println("-".repeat(50));


        // --- 2. DADOS NÃO ESTRUTURADOS (Strings Longas e Referências a Arquivos) ---
        // Em Java, longas Strings representam textos livres, e Strings curtas representam caminhos de arquivos.
        System.out.println("--- 2. DADOS NÃO ESTRUTURADOS (Strings) ---");
        
        String feedbackTextoLivre = "O produto é maravilhoso, mas o atendimento demorou para responder. Espero que melhorem o suporte.";
        String caminhoArquivoAudio = "/dados/nao_estruturados/audio_chamada_cliente_4.mp3"; 

        System.out.println("Trecho do Feedback: \"" + feedbackTextoLivre.substring(0, 50) + "...\"");
        System.out.println("Caminho do Arquivo: " + caminhoArquivoAudio);
        
        // Análise de NLP (simulada)
        if (feedbackTextoLivre.toLowerCase().contains("maravilhoso")) {
            System.out.println("Análise Simples: Termo 'maravilhoso' detectado (positivo).");
        }
        System.out.println("-".repeat(50));


        // --- 3. DADOS PARCIALMENTE ESTRUTURADOS (Map/JSON Flexível) ---
        // Usamos um Map<String, Object> para simular a flexibilidade do JSON ou de um Banco NoSQL. 
        // Os valores podem ser de tipos diferentes (String, Integer, Boolean, etc.).
        System.out.println("--- 3. DADOS PARCIALMENTE ESTRUTURADOS (HashMap/JSON) ---");
        
        // Avaliação A: Completa com todos os "campos"
        Map<String, Object> avaliacaoA = new HashMap<>();
        avaliacaoA.put("id_avaliacao", "rev_001"); // Estruturado (chave)
        avaliacaoA.put("estrelas", 4);              // Estruturado (inteiro)
        avaliacaoA.put("comentario", "Chegou rápido e a qualidade é boa."); // Não Estruturado (valor)
        
        // Avaliação B: Faltando o campo 'comentario' (Flexibilidade NoSQL)
        Map<String, Object> avaliacaoB = new HashMap<>();
        avaliacaoB.put("id_avaliacao", "rev_002");
        avaliacaoB.put("estrelas", 5);
        // O campo 'comentario' é opcional no esquema NoSQL, o que o torna parcialmente estruturado.
        
        System.out.println("Avaliação A (Chaves): " + avaliacaoA.keySet());
        
        // Demonstração da leitura: Acessando dados flexíveis
        int estrelasA = (Integer) avaliacaoA.get("estrelas");
        System.out.println("Estrelas da Avaliação A: " + estrelasA);
        
        // Tentativa de obter um campo que pode não existir (tratamento de flexibilidade)
        String comentarioB = (String) avaliacaoB.getOrDefault("comentario", "N/A (Comentário Ausente)");
        System.out.println("Comentário da Avaliação B: " + comentarioB);
        System.out.println("-".repeat(50));
    }
}