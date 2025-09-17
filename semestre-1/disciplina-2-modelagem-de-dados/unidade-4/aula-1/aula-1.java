// aula-1.java

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

/**
 * Classe para simular a tabela original, não normalizada,
 * com dados de um formulário de registro de jogos de futebol.
 */
class RegistroJogo {
    int numeroJogo;
    String dataPartida;
    String localJogo;
    String cidadeLocal;
    String nomeOponente;
    String codigoJogador;
    String nomeJogador;
    String posicaoJogador;
    int golsMarcados;

    public RegistroJogo(int numeroJogo, String dataPartida, String localJogo, String cidadeLocal, String nomeOponente, String codigoJogador, String nomeJogador, String posicaoJogador, int golsMarcados) {
        this.numeroJogo = numeroJogo;
        this.dataPartida = dataPartida;
        this.localJogo = localJogo;
        this.cidadeLocal = cidadeLocal;
        this.nomeOponente = nomeOponente;
        this.codigoJogador = codigoJogador;
        this.nomeJogador = nomeJogador;
        this.posicaoJogador = posicaoJogador;
        this.golsMarcados = golsMarcados;
    }

    @Override
    public String toString() {
        return "RegistroJogo{" +
                "numeroJogo=" + numeroJogo +
                ", dataPartida='" + dataPartida + '\'' +
                ", localJogo='" + localJogo + '\'' +
                ", cidadeLocal='" + cidadeLocal + '\'' +
                ", nomeOponente='" + nomeOponente + '\'' +
                ", codigoJogador='" + codigoJogador + '\'' +
                ", nomeJogador='" + nomeJogador + '\'' +
                ", posicaoJogador='" + posicaoJogador + '\'' +
                ", golsMarcados=" + golsMarcados +
                '}';
    }
}

/**
 * Representa a tabela normalizada 'Jogos'.
 */
class Jogo {
    int numeroJogo;
    String dataPartida;
    String localJogo;
    String nomeOponente;

    public Jogo(int numeroJogo, String dataPartida, String localJogo, String nomeOponente) {
        this.numeroJogo = numeroJogo;
        this.dataPartida = dataPartida;
        this.localJogo = localJogo;
        this.nomeOponente = nomeOponente;
    }

    @Override
    public String toString() {
        return "Jogo{" +
                "numeroJogo=" + numeroJogo +
                ", dataPartida='" + dataPartida + '\'' +
                ", localJogo='" + localJogo + '\'' +
                ", nomeOponente='" + nomeOponente + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Jogo jogo = (Jogo) o;
        return numeroJogo == jogo.numeroJogo;
    }

    @Override
    public int hashCode() {
        return Objects.hash(numeroJogo);
    }
}

/**
 * Representa a tabela normalizada 'Jogadores'.
 */
class Jogador {
    String codigoJogador;
    String nomeJogador;
    String posicaoJogador;

    public Jogador(String codigoJogador, String nomeJogador, String posicaoJogador) {
        this.codigoJogador = codigoJogador;
        this.nomeJogador = nomeJogador;
        this.posicaoJogador = posicaoJogador;
    }

    @Override
    public String toString() {
        return "Jogador{" +
                "codigoJogador='" + codigoJogador + '\'' +
                ", nomeJogador='" + nomeJogador + '\'' +
                ", posicaoJogador='" + posicaoJogador + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Jogador jogador = (Jogador) o;
        return codigoJogador.equals(jogador.codigoJogador);
    }

    @Override
    public int hashCode() {
        return Objects.hash(codigoJogador);
    }
}

/**
 * Representa a tabela de ligação 'Atuacoes'.
 */
class Atuacao {
    int numeroJogo;
    String codigoJogador;
    int golsMarcados;

    public Atuacao(int numeroJogo, String codigoJogador, int golsMarcados) {
        this.numeroJogo = numeroJogo;
        this.codigoJogador = codigoJogador;
        this.golsMarcados = golsMarcados;
    }

    @Override
    public String toString() {
        return "Atuacao{" +
                "numeroJogo=" + numeroJogo +
                ", codigoJogador='" + codigoJogador + '\'' +
                ", golsMarcados=" + golsMarcados +
                '}';
    }
}

/**
 * Representa a tabela normalizada 'Localizacoes'.
 */
class Localizacao {
    String localJogo;
    String cidadeLocal;

    public Localizacao(String localJogo, String cidadeLocal) {
        this.localJogo = localJogo;
        this.cidadeLocal = cidadeLocal;
    }

    @Override
    public String toString() {
        return "Localizacao{" +
                "localJogo='" + localJogo + '\'' +
                ", cidadeLocal='" + cidadeLocal + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Localizacao that = (Localizacao) o;
        return localJogo.equals(that.localJogo);
    }

    @Override
    public int hashCode() {
        return Objects.hash(localJogo);
    }
}

public class aula_1 {

    public static void main(String[] args) {
        System.out.println("--------------------------------------------------");
        System.out.println("    EXEMPLO DE NORMALIZAÇÃO DE DADOS EM JAVA    ");
        System.out.println("--------------------------------------------------");

        // Passo 1: Criação da tabela original não normalizada
        List<RegistroJogo> tabelaOriginal = criarTabelaOriginal();
        System.out.println("\n[Tabela Original - Formulário do Clube]");
        tabelaOriginal.forEach(System.out::println);

        // Passo 2: Normalização para 2FN (já que a 1FN é atendida)
        System.out.println("\n--- Normalização para 2ª Forma Normal (2FN) ---");
        System.out.println("Separando as dependências parciais de 'CodigoJogador' e 'NumeroJogo'.");

        // Cria a tabela de Jogos e remove duplicatas (com base no numeroJogo)
        List<Jogo> tabelaJogos = tabelaOriginal.stream()
                .map(r -> new Jogo(r.numeroJogo, r.dataPartida, r.localJogo, r.nomeOponente))
                .distinct()
                .collect(Collectors.toList());

        // Cria a tabela de Jogadores e remove duplicatas (com base no codigoJogador)
        List<Jogador> tabelaJogadores = tabelaOriginal.stream()
                .map(r -> new Jogador(r.codigoJogador, r.nomeJogador, r.posicaoJogador))
                .distinct()
                .collect(Collectors.toList());

        // Cria a tabela de Atuações (tabela de ligação)
        List<Atuacao> tabelaAtuacoes = tabelaOriginal.stream()
                .map(r -> new Atuacao(r.numeroJogo, r.codigoJogador, r.golsMarcados))
                .collect(Collectors.toList());

        System.out.println("\n[Tabela JOGOS]");
        tabelaJogos.forEach(System.out::println);
        System.out.println("\n[Tabela JOGADORES]");
        tabelaJogadores.forEach(System.out::println);
        System.out.println("\n[Tabela ATUACOES]");
        tabelaAtuacoes.forEach(System.out::println);

        // Passo 3: Normalização para 3FN
        System.out.println("\n--- Normalização para 3ª Forma Normal (3FN) ---");
        System.out.println("Separando a dependência transitiva de 'CidadeLocal' de 'LocalJogo'.");

        // Cria a tabela de Localizacoes e remove duplicatas (com base no localJogo)
        List<Localizacao> tabelaLocalizacoes = tabelaOriginal.stream()
                .map(r -> new Localizacao(r.localJogo, r.cidadeLocal))
                .distinct()
                .collect(Collectors.toList());
        
        // A tabela de Jogos original, agora com a dependência transitiva removida, já foi criada.

        System.out.println("\n[Tabela LOCALIZACOES]");
        tabelaLocalizacoes.forEach(System.out::println);
        System.out.println("\n[Tabela JOGOS (após a 3FN)]");
        tabelaJogos.forEach(System.out::println);

        System.out.println("\n--------------------------------------------------");
        System.out.println("          PROCESSO DE NORMALIZAÇÃO FINALIZADO       ");
        System.out.println("--------------------------------------------------");
    }

    private static List<RegistroJogo> criarTabelaOriginal() {
        List<RegistroJogo> registros = new ArrayList<>();
        registros.add(new RegistroJogo(101, "2023-10-25", "Estádio Municipal", "Santa Catarina", "Time A", "J001", "João Silva", "Atacante", 2));
        registros.add(new RegistroJogo(102, "2023-11-02", "Arena Olímpica", "Rio de Janeiro", "Time B", "J002", "Maria Santos", "Meio-campo", 1));
        registros.add(new RegistroJogo(103, "2023-11-10", "Estádio Municipal", "Santa Catarina", "Time C", "J001", "João Silva", "Atacante", 0));
        registros.add(new RegistroJogo(104, "2023-11-18", "Estádio do Morumbi", "São Paulo", "Time D", "J003", "Pedro Rocha", "Defensor", 3));
        registros.add(new RegistroJogo(105, "2023-11-25", "Arena Olímpica", "Rio de Janeiro", "Time E", "J002", "Maria Santos", "Meio-campo", 1));
        return registros;
    }
}