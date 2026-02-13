import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Representa um item no banco de dados.
 * Simula o dado persistente no Servidor/Nuvem.
 */
class Produto {
    private String nome;
    // Usamos AtomicInteger para simular a thread-safety (Isolamento/Consistência)
    // necessária em um ambiente de sistema distribuído (múltiplos acessos simultâneos).
    private AtomicInteger estoque; 

    public Produto(String nome, int estoqueInicial) {
        this.nome = nome;
        this.estoque = new AtomicInteger(estoqueInicial);
    }

    public String getNome() {
        return nome;
    }

    public int getEstoque() {
        return estoque.get();
    }

    /**
     * Tenta decrementar o estoque. 
     * Simula a transação e garante Atomicidade e Consistência (ACID).
     * @param quantidade A ser vendida.
     * @return true se a venda foi bem-sucedida (commit), false se falhou (rollback).
     */
    public boolean tentarVenda(int quantidade) {
        int estoqueAtual;
        int novoEstoque;
        
        // Loop de verificação otimista para garantir que 
        // nenhuma outra thread alterou o valor entre a leitura e a escrita.
        do {
            estoqueAtual = estoque.get(); // Leitura (Isolamento)
            if (estoqueAtual < quantidade) {
                return false; // Falha na Consistência
            }
            novoEstoque = estoqueAtual - quantidade;
        // O compareAndSet garante que a operação só será escrita se o estoqueAtual 
        // for o mesmo que lemos inicialmente, garantindo a Atomicidade.
        } while (!estoque.compareAndSet(estoqueAtual, novoEstoque));
        
        // Durabilidade: O valor foi persistido (no AtomicInteger, simulando o DB)
        return true; 
    }
}

/**
 * Simula o Servidor de Banco de Dados na Nuvem (Back-end).
 * Centraliza o gerenciamento de dados e a lógica transacional.
 */
class ServidorInventario {
    private Map<String, Produto> inventarioDB;

    public ServidorInventario() {
        // Simulação do Banco de Dados Central (Nuvem)
        inventarioDB = new HashMap<>();
        inventarioDB.put("SKU-100", new Produto("Camiseta Básica", 500));
        inventarioDB.put("SKU-201", new Produto("Calça Jeans Premium", 250));
    }

    /**
     * Simula a consulta de um Cliente. 
     * É a base da Arquitetura Cliente-Servidor.
     */
    public int consultarEstoque(String sku) {
        if (inventarioDB.containsKey(sku)) {
            return inventarioDB.get(sku).getEstoque();
        }
        return -1; // Produto não encontrado
    }

    /**
     * Processa o pedido de venda de um Cliente (Nó Distribuído).
     */
    public String realizarVenda(String sku, int quantidade, String nomeCliente) {
        System.out.println(String.format("[SERVIDOR]: Processando pedido de %s: Vender %d de %s.", nomeCliente, quantidade, sku));
        
        Produto produto = inventarioDB.get(sku);

        if (produto == null) {
            return "[SERVIDOR] ❌ Erro: SKU não existe.";
        }

        if (produto.tentarVenda(quantidade)) {
            // Sucesso na transação ACID.
            return String.format("[SERVIDOR] ✅ SUCESSO! %d un. vendidas. Novo Estoque Global: %d", 
                                 quantidade, produto.getEstoque());
        } else {
            // Falha na transação.
            return String.format("[SERVIDOR] ⛔ FALHA! Estoque insuficiente para %s. Atual: %d", 
                                 nomeCliente, produto.getEstoque());
        }
    }
}

/**
 * Simula um Cliente (Loja ou E-commerce) fazendo requisições ao Servidor.
 * Reforça o conceito de Sistema Distribuído (múltiplos pontos de acesso).
 */
class ClienteVarejo implements Runnable {
    private ServidorInventario servidor;
    private String nomeCliente;
    private String sku;
    private int quantidade;

    public ClienteVarejo(ServidorInventario servidor, String nomeCliente, String sku, int quantidade) {
        this.servidor = servidor;
        this.nomeCliente = nomeCliente;
        this.sku = sku;
        this.quantidade = quantidade;
    }

    @Override
    public void run() {
        // 1. Cliente consulta o estoque (Requisição GET)
        int estoqueAntes = servidor.consultarEstoque(sku);
        System.out.println(String.format("\n[CLIENTE %s]: Estoque antes: %d", nomeCliente, estoqueAntes));
        
        // Simula o tempo de processamento/comunicação
        try {
            Thread.sleep((long) (Math.random() * 100)); 
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // 2. Cliente realiza a venda (Requisição POST/Transação)
        String resultado = servidor.realizarVenda(sku, quantidade, nomeCliente);
        System.out.println(String.format("[CLIENTE %s]: Resposta: %s", nomeCliente, resultado));
    }
}


public class aula_3 {
    public static void main(String[] args) throws InterruptedException {
        
        System.out.println("===================================================================");
        System.out.println("      SIMULAÇÃO JAVA: ARQUITETURA DISTRIBUÍDA EM NUVEM (THREADS)     ");
        System.out.println("===================================================================");
        
        ServidorInventario servidorCentral = new ServidorInventario();

        System.out.println("\n--- ESTOQUE INICIAL (SKU-100) ---");
        System.out.println("Estoque Total: " + servidorCentral.consultarEstoque("SKU-100"));

        // 1. Criando Clientes (Nós) que acessam o Servidor (Nuvem) simultaneamente (Threads)
        Thread t1 = new Thread(new ClienteVarejo(servidorCentral, "Loja-SP", "SKU-100", 200));
        Thread t2 = new Thread(new ClienteVarejo(servidorCentral, "E-commerce (Pico)", "SKU-100", 250));
        Thread t3 = new Thread(new ClienteVarejo(servidorCentral, "Loja-RJ", "SKU-100", 100)); // Deve falhar

        System.out.println("\n--- INICIANDO TRANSAÇÕES SIMULTÂNEAS (Sistema Distribuído) ---");
        
        // 2. Executando as transações
        t1.start();
        t2.start();
        t3.start();

        // Espera todas as threads terminarem para verificar o resultado final
        t1.join();
        t2.join();
        t3.join();

        // 3. Verificação final do estoque global sincronizado
        System.out.println("\n--- ESTOQUE FINAL SINCRONIZADO (Consistência) ---");
        int estoqueFinal = servidorCentral.consultarEstoque("SKU-100");
        System.out.println("Estoque Total Remanescente: " + estoqueFinal);
        
        // 500 (Inicial) - 200 (SP) - 250 (E-comm) = 50.
        // A transação de 100 da Loja-RJ deve falhar, demonstrando a Integridade (ACID).
        
        System.out.println("\n===================================================================");
        System.out.println(" O Java simula como o Servidor garante a integridade (AtomicInteger)");
        System.out.println("  e a sincronização de dados entre múltiplos Clientes/Nós.");
        System.out.println("===================================================================");
    }
}