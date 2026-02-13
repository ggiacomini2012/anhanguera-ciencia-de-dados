// Aula5Exemplo.java
// Exemplo em Java da implementação do Modelo Lógico Normalizado via Classes.
// Cada Classe representa uma Tabela, e os objetos simulam os registros.

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

// ------------------------------------------
// CLASSE 1: Aluno (Entidade - Tabela)
// Representa a tabela 'Aluno' com ID_Aluno como Chave Primária.
// ------------------------------------------
class Aluno {
    private int idAluno;          // Chave Primária (PK)
    private String nome;
    private LocalDate dataMatricula;

    public Aluno(int idAluno, String nome, LocalDate dataMatricula) {
        this.idAluno = idAluno;
        this.nome = nome;
        this.dataMatricula = dataMatricula;
    }

    // Getters para acesso aos dados
    public int getIdAluno() {
        return idAluno;
    }

    public String getNome() {
        return nome;
    }
}

// ------------------------------------------
// CLASSE 2: Livro (Entidade - Tabela)
// Representa a tabela 'Livro' com ISBN como Chave Primária.
// ------------------------------------------
class Livro {
    private String isbn;          // Chave Primária (PK)
    private String titulo;
    private int anoPublicacao;

    public Livro(String isbn, String titulo, int anoPublicacao) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.anoPublicacao = anoPublicacao;
    }

    // Getters
    public String getIsbn() {
        return isbn;
    }

    public String getTitulo() {
        return titulo;
    }
}

// ------------------------------------------
// CLASSE 3: Emprestimo (Entidade de Relacionamento - Tabela)
// Utiliza referências de objeto para simular as Chaves Estrangeiras (FK).
// Em vez de IDs, usamos os próprios objetos Aluno e Livro.
// ------------------------------------------
class Emprestimo {
    private int idEmprestimo;
    private Aluno aluno;          // Objeto Aluno - Simula a Chave Estrangeira (ID_Aluno_FK)
    private Livro livro;          // Objeto Livro - Simula a Chave Estrangeira (ISBN_FK)
    private LocalDate dataEmprestimo;
    private LocalDate dataDevolucaoPrevista;

    public Emprestimo(int idEmprestimo, Aluno aluno, Livro livro, LocalDate dataEmprestimo, LocalDate dataDevolucaoPrevista) {
        this.idEmprestimo = idEmprestimo;
        this.aluno = aluno;
        this.livro = livro;
        this.dataEmprestimo = dataEmprestimo;
        this.dataDevolucaoPrevista = dataDevolucaoPrevista;
    }
    
    // Método para exibir o Empréstimo (Simula uma Consulta/JOIN)
    public void exibirDetalhes() {
        System.out.printf(
            "[ID: %d] Aluno: %s (ID: %d) | Livro: %s (ISBN: %s) | Data Empréstimo: %s\n",
            this.idEmprestimo,
            this.aluno.getNome(),
            this.aluno.getIdAluno(),
            this.livro.getTitulo(),
            this.livro.getIsbn(),
            this.dataEmprestimo.toString()
        );
    }
}

// ------------------------------------------
// CLASSE PRINCIPAL
// ------------------------------------------
public class Aula5Exemplo {
    public static void main(String[] args) {
        System.out.println("📚 Exemplo de Modelagem Lógica em Java (Arquitetura de Dados)\n");

        // 1. Criação dos Registros (Objetos) para as Entidades Normalizadas
        // Evita-se a repetição de dados, pois o Livro e o Aluno existem apenas uma vez.
        
        // Entidade Aluno
        Aluno maria = new Aluno(101, "Maria da Silva", LocalDate.of(2023, 8, 15));
        Aluno joao = new Aluno(102, "João de Souza", LocalDate.of(2024, 1, 20));

        // Entidade Livro
        Livro bdAvancado = new Livro("978-8575225409", "Banco de Dados Avançado", 2020);
        Livro linguagemC = new Livro("978-0131103627", "A Linguagem C", 1978);
        
        // 2. Criação da Lista de Empréstimos (Simula a Tabela)
        List<Emprestimo> historicoEmprestimos = new ArrayList<>();
        
        // 3. Criação dos Registros de Relacionamento (Empréstimo)
        // O objeto Emprestimo referencia os objetos Aluno e Livro.
        historicoEmprestimos.add(new Emprestimo(
            1, 
            maria, 
            bdAvancado, 
            LocalDate.of(2025, 10, 1), 
            LocalDate.of(2025, 10, 15)
        ));

        historicoEmprestimos.add(new Emprestimo(
            2, 
            joao, 
            linguagemC, 
            LocalDate.of(2025, 10, 2), 
            LocalDate.of(2025, 10, 16)
        ));

        // 4. Exibição dos Dados (Simulando uma Consulta com JOIN)
        System.out.println("📋 Lista de Empréstimos:");
        System.out.println("------------------------------------------------------------------------");
        for (Emprestimo e : historicoEmprestimos) {
            e.exibirDetalhes();
        }
        System.out.println("------------------------------------------------------------------------");
        System.out.println("\n✔️ Modelo Lógico exemplificado: Classes (Entidades) se relacionam via Referências (Chaves Estrangeiras).");
    }
}
// Para compilar e rodar:
// 1. Salve como Aula5Exemplo.java
// 2. javac Aula5Exemplo.java
// 3. java Aula5Exemplo