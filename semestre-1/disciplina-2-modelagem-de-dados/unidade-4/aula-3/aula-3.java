import java.util.ArrayList;
import java.util.List;

// =============================================================================
// Representando a Normalização com Classes e Objetos em Java
// =============================================================================
// Assim como em bancos de dados, podemos aplicar os princípios de normalização
// na estruturação de classes em Java para evitar duplicação de dados e manter
// a integridade. Cada classe representa uma entidade ou tabela normalizada.

public class Aula3Normalizacao {

    // =========================================================================
    // Exemplo 1: Forma Normal de Boyce-Codd (FNBC)
    // =========================================================================
    // A FNBC nos ensina a isolar dependências funcionais problemáticas.
    // Antes da FNBC, teríamos uma única classe 'Filho' que misturaria
    // dados do aluno com dados da sala/professor, gerando redundância.

    // Classe ANTES da normalização (violando a FNBC)
    public static class FilhoAntesFNBC {
        String nomeFilho;
        String enderecoFilho;
        String dataNascimento;
        String nomeEscola;
        String numeroSala;
        String nomeProfessor; // Este atributo está diretamente na classe,
                              // mas depende de 'numeroSala' e 'nomeEscola',
                              // que não são chaves primárias.
    }

    // Classes DEPOIS da normalização (na FNBC)
    public static class Filho {
        int id;
        String nomeFilho;
        String enderecoFilho;
        String dataNascimento;
        String numeroSala; // Referência para a sala
    }

    public static class Sala {
        String numeroSala;
        String nomeEscola;
        String nomeProfessor;
    }

    private static void demonstrarFNBC() {
        System.out.println("---");
        System.out.println("### Demonstração da FNBC: Aluno e Professor ###");

        // Criação de objetos para simular os dados
        Sala sala101 = new Sala();
        sala101.numeroSala = "101";
        sala101.nomeEscola = "Escola X";
        sala101.nomeProfessor = "Prof. Ana";

        Sala sala205 = new Sala();
        sala205.numeroSala = "205";
        sala205.nomeEscola = "Escola Y";
        sala205.nomeProfessor = "Prof. Carlos";

        Filho joao = new Filho();
        joao.id = 1;
        joao.nomeFilho = "João";
        joao.enderecoFilho = "Rua A";
        joao.dataNascimento = "10/01/2015";
        joao.numeroSala = sala101.numeroSala; // Relacionamento com a classe Sala

        Filho pedro = new Filho();
        pedro.id = 2;
        pedro.nomeFilho = "Pedro";
        pedro.enderecoFilho = "Rua C";
        pedro.dataNascimento = "20/09/2017";
        pedro.numeroSala = sala101.numeroSala; // Note que não há duplicação de dados do professor

        System.out.println("\nDados do aluno (classe Filho): " + joao.nomeFilho + " está na sala " + joao.numeroSala);
        System.out.println("Dados da sala (classe Sala): Sala " + sala101.numeroSala + " tem o professor " + sala101.nomeProfessor);

        System.out.println("\n--> Vantagem: Se a 'Prof. Ana' for substituída, alteramos apenas o objeto 'sala101', e a mudança reflete em todos os 'Filho' que referenciam essa sala, sem a necessidade de atualizar múltiplos registros.");
    }

    // =========================================================================
    // Exemplo 2: Quarta Forma Normal (4FN)
    // =========================================================================
    // A 4FN lida com dependências multivaloradas. Quando uma única entidade
    // contém múltiplos fatos independentes, ela deve ser dividida.

    // Classes ANTES da normalização (violando a 4FN)
    public static class CompraAntes4FN {
        int codFornecedor;
        String codProduto;
        String codComprador;
    }

    // Classes DEPOIS da normalização (na 4FN)
    public static class FornecedorProduto {
        int codFornecedor;
        String codProduto;
    }

    public static class FornecedorComprador {
        int codFornecedor;
        String codComprador;
    }

    private static void demonstrar4FN() {
        System.out.println("---");
        System.out.println("### Demonstração da 4FN: O Histórico de Compras ###");

        // Criação de objetos para simular a tabela problemática
        List<CompraAntes4FN> compras = new ArrayList<>();
        CompraAntes4FN compra1 = new CompraAntes4FN();
        compra1.codFornecedor = 101; compra1.codProduto = "BA3"; compra1.codComprador = "01";
        compras.add(compra1);
        // ... (e assim por diante com a duplicação)

        // Criando as listas normalizadas
        List<FornecedorProduto> fornecedorProdutos = new ArrayList<>();
        FornecedorProduto fp1 = new FornecedorProduto();
        fp1.codFornecedor = 101; fp1.codProduto = "BA3";
        fornecedorProdutos.add(fp1);

        List<FornecedorComprador> fornecedorCompradores = new ArrayList<>();
        FornecedorComprador fc1 = new FornecedorComprador();
        fc1.codFornecedor = 101; fc1.codComprador = "01";
        fornecedorCompradores.add(fc1);
        
        FornecedorComprador fc2 = new FornecedorComprador();
        fc2.codFornecedor = 101; fc2.codComprador = "25"; // A inclusão de um novo comprador não duplica o produto
        fornecedorCompradores.add(fc2);


        System.out.println("\nLista de Fornecedor-Produtos (na 4FN):");
        for (FornecedorProduto fp : fornecedorProdutos) {
            System.out.println("Fornecedor: " + fp.codFornecedor + ", Produto: " + fp.codProduto);
        }

        System.out.println("\nLista de Fornecedor-Compradores (na 4FN):");
        for (FornecedorComprador fc : fornecedorCompradores) {
            System.out.println("Fornecedor: " + fc.codFornecedor + ", Comprador: " + fc.codComprador);
        }

        System.out.println("\n--> Vantagem: Se o fornecedor 101 passa a ter um novo produto 'X', adicionamos apenas um objeto na lista 'fornecedorProdutos' sem precisar repetir a informação de todos os compradores.");
    }

    public static void main(String[] args) {
        demonstrarFNBC();
        System.out.println("\n\n");
        demonstrar4FN();
        System.out.println("\n---");
        System.out.println("Fim da demonstração. A normalização é a chave para classes mais limpas e modelos de dados mais robustos!");
    }
}