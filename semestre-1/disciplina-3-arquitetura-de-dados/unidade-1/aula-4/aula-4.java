// Nome do arquivo: aula-4.java
// Exemplo de Modelagem Lógica e Física em Java (Representação Estruturada)

import java.util.ArrayList;
import java.util.List;
import java.time.LocalDate;

// -------------------------------------
// 1. CLASSE EDITORA (Entidade Forte)
// -------------------------------------
class Editora {
    // Atributos privados simulam as colunas da tabela e garantem o Encapsulamento.
    private int codEditora; // Chave Primária (PK)
    private String nome;     // Tipo de dado: VARCHAR

    public Editora(int codEditora, String nome) {
        this.codEditora = codEditora;
        this.nome = nome;
    }

    // Getters para acesso aos dados
    public int getCodEditora() {
        return codEditora;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Editora [PK=" + codEditora + ", Nome=" + nome + "]";
    }
}

// -------------------------------------
// 2. CLASSE LIVRO (Entidade Relacionada)
// -------------------------------------
class Livro {
    private int codLivro;       // Chave Primária (PK)
    private String titulo;      // Tipo de dado: VARCHAR
    private int anoPublicacao;  // Tipo de dado: INT
    private int codEditoraFk;   // Chave Estrangeira (FK) -> Editora

    public Livro(int codLivro, String titulo, int anoPublicacao, int codEditoraFk) {
        this.codLivro = codLivro;
        this.titulo = titulo;
        this.anoPublicacao = anoPublicacao;
        this.codEditoraFk = codEditoraFk;
    }

    // Getters
    public int getCodLivro() {
        return codLivro;
    }

    public int getCodEditoraFk() {
        return codEditoraFk;
    }

    public String getTitulo() {
        return titulo;
    }

    @Override
    public String toString() {
        return "Livro [PK=" + codLivro + ", Título=" + titulo + ", FK_Editora=" + codEditoraFk + "]";
    }
}

// -------------------------------------
// 3. CLASSE PEDIDO (Chave Composta e FKs)
// -------------------------------------
class Pedido {
    private int numPedido;        // Chave Primária (PK)
    private LocalDate dataPedido; // Tipo de dado: DATE
    private double valorTotal;    // Tipo de dado: DECIMAL
    private int codClienteFk;     // Chave Estrangeira (FK) -> Cliente (Assumida, mas não implementada aqui)

    public Pedido(int numPedido, LocalDate dataPedido, double valorTotal, int codClienteFk) {
        this.numPedido = numPedido;
        this.dataPedido = dataPedido;
        this.valorTotal = valorTotal;
        this.codClienteFk = codClienteFk;
    }

    // Getters
    public int getNumPedido() {
        return numPedido;
    }

    public int getCodClienteFk() {
        return codClienteFk;
    }

    @Override
    public String toString() {
        return "Pedido [PK=" + numPedido + ", Data=" + dataPedido + ", FK_Cliente=" + codClienteFk + ", Total=" + valorTotal + "]";
    }
}

// -------------------------------------
// 4. CLASSE ITENSPEDIDO (Tabela Associativa N:N)
// -------------------------------------
class ItensPedido {
    // A chave composta é representada pela combinação dos dois atributos FKs
    private int numPedidoFk;  // Chave Primária (PK) e Estrangeira (FK) -> Pedido
    private int codLivroFk;   // Chave Primária (PK) e Estrangeira (FK) -> Livro
    private int quantidade;
    private double precoUnitario;

    public ItensPedido(int numPedidoFk, int codLivroFk, int quantidade, double precoUnitario) {
        this.numPedidoFk = numPedidoFk;
        this.codLivroFk = codLivroFk;
        this.quantidade = quantidade;
        this.precoUnitario = precoUnitario;
    }

    // Getters
    public int getNumPedidoFk() {
        return numPedidoFk;
    }

    public int getCodLivroFk() {
        return codLivroFk;
    }

    @Override
    public String toString() {
        return "ItemPedido [PK_Composta=(" + numPedidoFk + ", " + codLivroFk + "), Qtd=" + quantidade + "]";
    }
}


public class aula_4 {
    public static void main(String[] args) {
        System.out.println("--- SIMULANDO AS TABELAS (MODELO LÓGICO) EM JAVA ---\n");

        // Simulação do Repositório/Banco de Dados (Tabelas)
        List<Editora> tabelaEditora = new ArrayList<>();
        List<Livro> tabelaLivro = new ArrayList<>();
        List<Pedido> tabelaPedido = new ArrayList<>();
        List<ItensPedido> tabelaItensPedido = new ArrayList<>();

        // Inserção de Dados na Tabela EDITORA
        tabelaEditora.add(new Editora(101, "Atlas Publishing"));
        tabelaEditora.add(new Editora(102, "Tech Books Inc."));
        System.out.println("Tabela Editora (2 registros): " + tabelaEditora);

        // Inserção de Dados na Tabela LIVRO (Uso da FK)
        tabelaLivro.add(new Livro(1, "Aventura em Python", 2023, 102));
        tabelaLivro.add(new Livro(2, "SQL Avançado", 2022, 102));
        tabelaLivro.add(new Livro(3, "Modelagem de Dados", 2021, 101));
        System.out.println("Tabela Livro (3 registros): " + tabelaLivro);

        // Inserção de Dados na Tabela PEDIDO (Uso da FK)
        tabelaPedido.add(new Pedido(1000, LocalDate.of(2024, 10, 1), 150.00, 500)); // Cliente 500
        System.out.println("Tabela Pedido (1 registro): " + tabelaPedido);

        // Inserção de Dados na Tabela ITENS_PEDIDO (Chave Composta e FKs)
        tabelaItensPedido.add(new ItensPedido(1000, 1, 1, 80.00)); // Pedido 1000, Livro 1
        tabelaItensPedido.add(new ItensPedido(1000, 3, 1, 70.00)); // Pedido 1000, Livro 3
        System.out.println("Tabela ItensPedido (2 registros): " + tabelaItensPedido);

        System.out.println("\n--- DEMONSTRAÇÃO DO RELACIONAMENTO N:1 (LIVRO -> EDITORA) ---");
        // Buscando um livro e seu respectivo nome de editora (Simulação de JOIN)
        Livro livroExemplo = tabelaLivro.get(0);
        Editora editoraCorrespondente = tabelaEditora.stream()
            .filter(e -> e.getCodEditora() == livroExemplo.getCodEditoraFk())
            .findFirst()
            .orElse(null);

        if (editoraCorrespondente != null) {
            System.out.println("O livro '" + livroExemplo.getTitulo() + "' (FK: " + livroExemplo.getCodEditoraFk() + ")");
            System.out.println("É da editora: " + editoraCorrespondente.getNome());
        }
    }
}