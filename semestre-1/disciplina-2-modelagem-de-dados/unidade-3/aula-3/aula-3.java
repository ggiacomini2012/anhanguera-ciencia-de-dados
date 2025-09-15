// Arquivo: Pessoa.java
public class Pessoa {
    private String nome;
    private String endereco;
    private String rg;
    private String cpf;
    private String dataNascimento;
    private String nomeMae;
    private String nomePai;

    public Pessoa(String nome, String endereco, String rg, String cpf, String dataNascimento, String nomeMae, String nomePai) {
        this.nome = nome;
        this.endereco = endereco;
        this.rg = rg;
        this.cpf = cpf;
        this.dataNascimento = dataNascimento;
        this.nomeMae = nomeMae;
        this.nomePai = nomePai;
    }

    // Getters para os atributos
    public String getNome() { return nome; }
    public String getEndereco() { return endereco; }
    // ... e assim por diante para todos os atributos
    
    @Override
    public String toString() {
        return "Nome: " + nome + "\n" +
               "Endereço: " + endereco + "\n" +
               "RG: " + rg + "\n" +
               "CPF: " + cpf + "\n" +
               "Data de Nascimento: " + dataNascimento + "\n" +
               "Nome da Mãe: " + nomeMae + "\n" +
               "Nome do Pai: " + nomePai;
    }
}

// Arquivo: Funcionario.java
public class Funcionario extends Pessoa {
    private String dataAdmissao;
    private String dataDemissao;
    private double salario;

    public Funcionario(String nome, String endereco, String rg, String cpf, String dataNascimento, String nomeMae, String nomePai, String dataAdmissao, String dataDemissao, double salario) {
        super(nome, endereco, rg, cpf, dataNascimento, nomeMae, nomePai); // Chamada ao construtor da superclasse
        this.dataAdmissao = dataAdmissao;
        this.dataDemissao = dataDemissao;
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "--- Dados do Funcionário ---\n" +
               super.toString() + "\n" +
               "Data de Admissão: " + dataAdmissao + "\n" +
               "Data de Demissão: " + dataDemissao + "\n" +
               "Salário: R$" + String.format("%,.2f", salario);
    }
}

// Arquivo: Professor.java
public class Professor extends Pessoa {
    private double valorHoraAula;
    private int horasAula;

    public Professor(String nome, String endereco, String rg, String cpf, String dataNascimento, String nomeMae, String nomePai, double valorHoraAula, int horasAula) {
        super(nome, endereco, rg, cpf, dataNascimento, nomeMae, nomePai);
        this.valorHoraAula = valorHoraAula;
        this.horasAula = horasAula;
    }

    @Override
    public String toString() {
        return "--- Dados do Professor ---\n" +
               super.toString() + "\n" +
               "Valor da Hora/Aula: R$" + String.format("%,.2f", valorHoraAula) + "\n" +
               "Quantidade de Horas/Aula: " + horasAula;
    }
}

// Arquivo: Aluno.java
public class Aluno extends Pessoa {
    private String dataEntrada;
    private String dataFormatura;

    public Aluno(String nome, String endereco, String rg, String cpf, String dataNascimento, String nomeMae, String nomePai, String dataEntrada, String dataFormatura) {
        super(nome, endereco, rg, cpf, dataNascimento, nomeMae, nomePai);
        this.dataEntrada = dataEntrada;
        this.dataFormatura = dataFormatura;
    }
    
    @Override
    public String toString() {
        return "--- Dados do Aluno ---\n" +
               super.toString() + "\n" +
               "Data de Entrada na Faculdade: " + dataEntrada + "\n" +
               "Data de Formatura: " + dataFormatura;
    }
}

// Arquivo: Main.java (para rodar o exemplo)
public class Main {
    public static void main(String[] args) {
        // Criando um objeto da classe Professor
        Professor profExemplo = new Professor(
            "Carlos Martins",
            "Rua das Rosas, 123",
            "12.345.678-9",
            "123.456.789-00",
            "10/05/1980",
            "Maria Silva",
            "José Martins",
            75.00,
            20
        );

        // Criando um objeto da classe Aluno
        Aluno alunoExemplo = new Aluno(
            "Ana Souza",
            "Avenida Brasil, 456",
            "98.765.432-1",
            "987.654.321-00",
            "25/11/2000",
            "Paula Lima",
            "João Souza",
            "03/02/2020",
            "15/12/2024"
        );
        
        // Exibindo os dados
        System.out.println(profExemplo);
        System.out.println("\n" + "=".repeat(30) + "\n");
        System.out.println(alunoExemplo);
    }
}