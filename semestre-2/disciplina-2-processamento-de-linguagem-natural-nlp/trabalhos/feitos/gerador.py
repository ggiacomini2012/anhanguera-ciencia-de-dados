from fpdf import FPDF
import os

class PDF(FPDF):
    def footer(self):
        if self.page_no() >= 4:
            self.set_y(-20)
            self.set_font('helvetica', '', 10)
            self.cell(0, 10, str(self.page_no()), align='R')

pdf = PDF('P', 'mm', 'A4')
pdf.set_margins(30, 30, 20)
pdf.set_auto_page_break(auto=True, margin=20)

def cl(txt):
    return txt.replace('–', '-').replace('ª', 'a.')

pdf.add_page()
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'GUILHERME GIACOMINI TEIXEIRA', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(100)
pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 10, 'AULA PRÁTICA - TRADUTORES E COMPILADORES\nPROCESSAMENTO DE LINGUAGEM NATURAL', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(250)
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'BALNEÁRIO CAMBORIÚ - SC', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '2026', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.add_page()
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'GUILHERME GIACOMINI TEIXEIRA', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(80)
pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 10, 'AULA PRÁTICA - TRADUTORES E COMPILADORES', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(130)
pdf.set_x(100)
pdf.set_font('helvetica', '', 10)
txt_rosto = 'Trabalho de avaliação da disciplina Processamento de Linguagem Natural apresentado como requisito para a obtenção da média no curso Tecnólogo em Ciência de Dados.\n\nProfessor: ANDERSON INACIO SALATA DE ABREU'
pdf.multi_cell(90, 5, cl(txt_rosto), align='J', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(250)
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'BALNEÁRIO CAMBORIÚ - SC', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '2026', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.add_page()
pdf.set_y(40)
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 10, 'SUMÁRIO', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(10)
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, '1 INTRODUÇÃO .......................................................................................................... 4', align='L', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '2 DESENVOLVIMENTO ................................................................................................ 5', align='L', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '3 RESULTADOS ........................................................................................................... 8', align='L', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '4 CONCLUSÃO ............................................................................................................ 9', align='L', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '5 REFERÊNCIAS ......................................................................................................... 10', align='L', new_x='LMARGIN', new_y='NEXT')

def add_h1(text):
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell(0, 10, cl(text), align='L', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

def add_h2(text):
    pdf.ln(5)
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell(0, 10, cl(text), align='L', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

def add_p(text, indent=True):
    pdf.set_font('helvetica', '', 12)
    if indent:
        pdf.set_x(30 + 12.5)
    pdf.multi_cell(0, 8, cl(text), align='J', new_x='LMARGIN', new_y='NEXT')

pdf.add_page()
add_h1('1 INTRODUÇÃO')
add_p('O Processamento de Linguagem Natural (NLP) é uma subárea da inteligência artificial que visa aproximar a computação estruturada da linguagem humana desestruturada. Para que algoritmos possam computar inferências estatísticas ou semânticas a partir de textos em linguagem natural, o input (texto bruto) necessita passar por um pipeline de normalização e transformação vetorial.')
add_p('Este relatório documenta a execução de um experimento prático computacional cujo objetivo foi aplicar técnicas elementares de pré-processamento textual. Utilizando a linguagem Python com o auxílio das bibliotecas NLTK e SpaCy, o projeto implementou rotinas para marcação morfossintática (Part-of-Speech Tagging), normatização (remoção de ruídos, extração de raízes e lematização) e segmentação de tokens.')
add_p('O presente documento expõe a análise técnica da prova de conceito, os recortes das execuções lógicas e a validação dos conceitos fundamentais de NLP requeridos pela proposta acadêmica.')

pdf.add_page()
add_h1('2 DESENVOLVIMENTO')

add_h2('2.1 Análise da Prova de Conceito Computacional')
add_p('O experimento foi estruturado como um pipeline sequencial aplicado sobre um texto de entrada padrão, desenvolvido em ambiente Python isolado. As respostas comportamentais das bibliotecas NLTK e SpaCy em cada etapa foram as seguintes:', False)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'A) Segmentação de Texto (Sentence Splitting e Tokenization)', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('A divisão do texto bruto em unidades processáveis foi realizada no nível de sentenças (via identificação de pontuação terminativa) e no nível de palavras (tokens). O algoritmo de tokenização demonstrou separar com precisão as unidades lexicais, mantendo a coerência em relação aos sinais de pontuação subjacentes. A segmentação computacional é o passo base, pois transforma uma string de caracteres linear em um vetor iterável que alimentará os modelos seguintes.', False)
pdf.ln(5)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'B) Marcação Morfossintática (POS Tagging)', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('Após a tokenização, o modelo pré-treinado do SpaCy para a língua portuguesa (pt_core_news_sm) foi instanciado sobre o vetor. O algoritmo realizou a classificação sintática de cada token, gerando mapeamentos no formato de chave e valor. Termos estruturais como Inteligência foram mapeados corretamente para substantivos, enquanto verbos transitivos receberam a tag correta. Essa etapa garantiu a extração da função lógica da palavra na estrutura da frase, superando a mera análise literal.', False)
pdf.ln(5)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'C) Normatização Textual (Stopwords, Stemming e Lematização)', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('Para a normalização, o pipeline foi dividido em três fluxos paralelos:', False)
add_p('1. Remoção de Stopwords: A aplicação do dicionário padrão do NLTK filtrou as palavras estruturais sem valor semântico independente (como preposições e artigos).', False)
add_p('2. Stemming: O algoritmo SnowballStemmer operou através de corte heurístico de prefixos e sufixos. Identificou-se que a técnica reduz os tokens de maneira agressiva ao seu radical.', False)
add_p('3. Lematização: Executada via motor do SpaCy, a lematização preservou a integridade linguística, transformando conjugações e plurais nas suas entradas normativas de dicionário.', False)
pdf.ln(5)

add_h2('2.2 Resolução de Conceitos Específicos')

pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 8, cl('1) Qual é a função da marcação morfossintática em NLP?'), align='L', new_x='LMARGIN', new_y='NEXT')
add_p('A marcação morfossintática (POS Tagging) tem a função de assinalar a classe gramatical de cada token (substantivo, adjetivo, verbo, advérbio) dentro do seu contexto sintático. Em NLP, isso é fundamental para a desambiguação semântica de sistemas matemáticos. Um classificador precisa distinguir algoritmicamente se a palavra canto foi usada como um substantivo (o canto da sala) ou como a flexão do verbo cantar. Sem essa marcação estrutural, a extração de sentido em análises mais profundas fica severamente comprometida.', False)
pdf.ln(3)

pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 8, cl('2) Qual é a diferença entre stemming e lematização?'), align='L', new_x='LMARGIN', new_y='NEXT')
add_p('Ambas são técnicas de redução morfológica para agrupar variações de uma mesma palavra, mas diferem no rigor algorítmico. O stemming é heurístico e reativo; ele aplica regras estáticas de corte de sufixos para chegar a um radical comum, muitas vezes gerando radicais que sequer existem como palavras válidas (ex: estudante e estudar viram estud). A lematização, por sua vez, realiza uma análise morfológica sistêmica em tempo de execução, consultando um vocabulário interno para reverter a palavra à sua raiz de dicionário correta (o lema). Por exemplo, a lematização identifica que fui e ir derivam do mesmo lema base, algo impossível de ser feito por corte de sufixos via stemming.', False)
pdf.ln(3)

pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 8, cl('3) Quais problemas podem surgir durante a segmentação de textos?'), align='L', new_x='LMARGIN', new_y='NEXT')
add_p('A etapa de segmentação sofre com ambiguidades lógicas em casos limite. Algoritmos ingênuos que utilizam o caractere de ponto como sinalizadores restritos de final de sentença tendem a falhar ou dividir strings incorretamente frente a abreviações (Sr., EUA) ou números decimais formatados (3.14). Além disso, hifenizações, URLs, hashtags e menções geram complexidade; seccioná-los puramente por caracteres de espaçamento corrompe o valor da informação semântica original contida neles. O uso de tokens padronizados e Expressões Regulares (Regex) bem definidas resolve grande parte desses impasses.', False)

pdf.add_page()
add_h1('3 RESULTADOS')
add_p('A implementação computacional permitiu observar as implicações diretas da escolha do fluxo de processamento de texto. Enquanto técnicas primitivas como a contagem frequencial sofrem com alto ruído estatístico quando expostas a stopwords, sua filtragem imediata gerou matrizes de dados (vetores) reduzidos e adensados semanticamente.')
add_p('Computacionalmente, constatou-se que a lematização consome maior recurso de processamento por exigir dicionários acoplados no motor, mas devolve dados íntegros e compatíveis linguisticamente. O stemming, por ser mais barato do ponto de vista algorítmico, tem validade em projetos onde o peso semântico exato da palavra é menos crítico do que a velocidade de indexação e recuperação no banco de dados (como arquiteturas básicas de motores de busca).')
add_p('A marcação morfossintática demonstrou alta coerência, possibilitando que um algoritmo isolasse automaticamente apenas verbos e substantivos do texto, caso o desenvolvedor desejasse extrair somente o núcleo da ação das sentenças.')

pdf.add_page()
add_h1('4 CONCLUSÃO')
add_p('O experimento validou a importância das etapas sequenciais no processamento de linguagem natural. Algoritmos mais limpos na sua entrada produzem cálculos determinísticos mais precisos na saída. A aplicação de tokenização cuidadosa e normalização inteligente reduz agressivamente a dimensionalidade espacial do processamento, evitando gasto de recursos computacionais com informações gramaticais inúteis para os modelos.')
add_p('Fica claro que não existe uma técnica de redução superior absoluta. Stemming e Lematização, embora busquem o mesmo objetivo, atendem a restrições arquiteturais diferentes: o primeiro prioriza a velocidade de execução; o segundo, o rigor de contexto e conservação semântica. A escolha do método deve sempre subordinar-se aos requisitos de desempenho e memória exigidos pela regra de negócio do projeto em questão.')

pdf.add_page()
add_h1('5 REFERÊNCIAS')

refs = [
    'ALENCAR, Ana Catarina de. Inteligência Artificial, Ética e Direito: Guia Prático para Entender o Novo Mundo. São Paulo: Expressa, 2022.',
    'Big Data Analytics. ISSN 2058-6345.',
    'GABRIEL, Martha. Inteligência Artificial: Do Zero ao Metaverso. Rio de Janeiro: Atlas, 2022.',
    'International Journal of Advanced Research in Computer Science. ISSN 0976-5697.',
    'KAUFMAN, Dora. Desmistificando a inteligência artificial. São Paulo: Autêntica Editora, 2022.',
    'MORAIS, Izabelly Soares de...[et al]. Introdução a Big Data e Internet das Coisas (IoT). Porto Alegre: SAGAH, 2018.',
    'PRADO, Magaly. Fake News e Inteligência Artificial: O poder dos algoritmos na guerra da desinformação. São Paulo: Grupo Almedina, 2022.',
    'SILVA, Fernanda Rosa da... [et al.]. Cloud computing. Porto Alegre: SAGAH, 2020.'
]

pdf.set_font('helvetica', '', 12)
for ref in sorted(refs):
    pdf.multi_cell(0, 8, cl(ref), align='L', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

output_path = r'c:\Users\G_406\Desktop\trabalho\diario-de-trabalho\metas\faculdade\ciencia-de-dados\semestre-2\disciplina-2-processamento-de-linguagem-natural-nlp\trabalhos\feitos\S2-D2-Processamento-de-Linguagem-Natural.pdf'
pdf.output(output_path)
print(f"PDF gerado com sucesso em: {output_path}")
