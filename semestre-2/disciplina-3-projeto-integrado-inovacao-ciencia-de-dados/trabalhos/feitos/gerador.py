from fpdf import FPDF

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
pdf.multi_cell(0, 10, 'PROJETO INTEGRADO INOVAÇÃO - CIÊNCIA DE DADOS', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(250)
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'BALNEÁRIO CAMBORIÚ - SC', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '2026', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.add_page()
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'GUILHERME GIACOMINI TEIXEIRA', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(80)
pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 10, 'PROJETO INTEGRADO INOVAÇÃO - CIÊNCIA DE DADOS', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(130)
pdf.set_x(100)
pdf.set_font('helvetica', '', 10)
txt_rosto = 'Trabalho de avaliação da disciplina Projeto Integrado Inovação - Ciência de Dados apresentado como requisito para a obtenção da média no curso Tecnólogo em Ciência de Dados.\n\nProfessora: VANICE DALTO\nMentor: JOAO HENRIQUE CORREIA DOS SANTOS'
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
pdf.cell(0, 10, '3 RESULTADOS ........................................................................................................... 9', align='L', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '4 CONCLUSÃO ............................................................................................................ 10', align='L', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '5 REFERÊNCIAS ......................................................................................................... 11', align='L', new_x='LMARGIN', new_y='NEXT')

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
add_p('Este relatório aborda a aplicação prática de técnicas de Ciência de Dados para otimização de processos de atendimento em uma empresa de varejo digital. A operação atual apresenta gargalos de processamento, como altos tempos de espera na fila e a necessidade de classificação manual dos chamados recebidos. Além disso, a empresa precisa garantir conformidade com a LGPD no tratamento dos textos dos clientes.')
add_p('O projeto consistiu na execução de uma Prova de Conceito (POC) que integra conhecimentos de Processamento de Linguagem Natural (NLP), Probabilidade e Estatística, Pesquisa Operacional e Segurança de Dados. Durante a simulação computacional, os dados de entrada foram processados e classificados utilizando Naive Bayes, enquanto os tempos de espera e atendimento foram modelados estatisticamente para posterior avaliação. O código também implementou funções básicas de desidentificação de texto.')
add_p('O presente documento apresenta os dados gerados pela execução do script em Python no ambiente Google Colab, acompanhados de uma análise técnica e objetiva sobre a viabilidade e os fundamentos matemáticos e de software do modelo desenvolvido.')

pdf.add_page()
add_h1('2 DESENVOLVIMENTO')
add_p('A seguir, apresentam-se os resultados gerados pela execução do script de simulação, divididos por área técnica:')

add_h2('2.1 Análise da Prova de Conceito (Código Colab)')
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'A) NLP', align='L', new_x='LMARGIN', new_y='NEXT')

add_p('1. Qual categoria teve melhor desempenho no classificador Naive Bayes?', False)
add_p('Conforme os dados gerados, todas as categorias atingiram F1-Score de 1.00 no relatório de classificação do Scikit-Learn. Esse resultado ocorreu porque o dataset sintético foi gerado a partir de uma lista estática e reduzida de frases. Consequentemente, as amostras do conjunto de teste eram idênticas às do conjunto de treinamento, resultando em um cenário de overfitting onde o algoritmo não foi testado quanto à sua capacidade real de generalização.', False)

add_p('2. Em suas palavras, como funciona a vetorização Bag of Words?', False)
add_p('O Bag of Words é uma técnica de extração de features que converte strings em matrizes numéricas computáveis. Ele cria um dicionário (vocabulário) contendo todas as palavras únicas do corpus. Para cada documento processado, o algoritmo retorna um vetor que contabiliza a frequência absoluta de cada palavra, ignorando completamente a ordem, a sintaxe estrutural e a semântica da frase.', False)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'B) Probabilidade e Estatística', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('3. Qual categoria teve maior frequência? O que isso indica?', False)
add_p('A execução do script registrou a categoria elogio como a de maior frequência absoluta no vetor. Do ponto de vista algorítmico, como a função de randomização da biblioteca Python utilizou uma distribuição teoricamente uniforme, essa pequena diferença aponta apenas a variabilidade estatística normal da amostragem em um N pequeno (500 interações), sem representar uma tendência de negócio estrutural.', False)

add_p('4. Interprete o histograma de tempo de espera: é simétrico, assimétrico, disperso?', False)
add_p('O histograma gerado exibe uma distribuição fortemente assimétrica à direita. Na teoria de filas aplicadas a servidores reais, os dados de espera tendem a esse formato: a maior densidade dos dados concentra-se nos tempos mais baixos (atendimentos normais), mas a presença de uma cauda longa indica ocorrências de chamados que ficaram parados no sistema por um tempo exponencialmente maior.', False)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'C) Pesquisa Operacional', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('5. O tempo médio de espera é adequado? Como poderia ser reduzido?', False)
add_p('A simulação apontou uma média de espera de 2,59 minutos. A validação técnica desse número depende estritamente dos parâmetros de SLA do negócio. Para otimizar essa métrica sem aplicar um aumento linear de custos (contratação direta de hardware ou pessoal), sugere-se a implementação de um filtro de roteamento via algoritmo de NLP que direcione as entradas para filas de processamento paralelas e escalonadas de acordo com a predição da carga.', False)

add_p('6. Cite duas ações que podem otimizar o fluxo de atendimento.', False)
add_p('Processamento assíncrono automatizado: Utilizar modelos de linguagem (chatbot) para interceptar chamados padrão na entrada do pipeline (Nível 1), realizando a baixa do ticket antes que ele aloque capacidade humana. Adicionalmente, Escalonamento estocástico de servidores: Alocar recursos humanos de forma variável ao longo do dia, dimensionando a capacidade exatamente em função da distribuição das taxas de chegada calculadas no sistema.', False)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'D) Segurança de Dados', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('7. O que é anonimização?', False)
add_p('Anonimização é a aplicação de técnicas computacionais que destroem o vínculo entre um registro de dados e o indivíduo que o produziu. Uma vez executado, o processo precisa ser irreversível (não permitindo reidentificação), de modo que o dado passe a ter utilidade estritamente como número estatístico, fora do escopo penal da LGPD.', False)

add_p('8. Quais dados sensíveis podem aparecer em mensagens de clientes?', False)
add_p('Na camada de input textual, é comum a ocorrência de Personally Identifiable Information (PII) estruturada ou não estruturada, como: CPFs, RGs, números e códigos de segurança de cartões bancários, dados de login, localização (endereço), entre outros.', False)

add_p('9. Qual risco existe em armazenar textos sem anonimização?', False)
add_p('A persistência de dados em texto plano (plaintext) num banco relacional ou Data Lake expõe a infraestrutura a vazamentos de dados por parte de invasores ou acesso interno não autorizado. Em nível corporativo, isso acarreta sanções severas sob a LGPD (multas administrativas) e possíveis passivos judiciais cíveis.', False)

add_h2('2.2 Resolução de Conceitos Específicos por Disciplina')

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'A) PROCESSAMENTO DE LINGUAGEM NATURAL (NLP)', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('1. Explique como o processo de pré-processamento textual pode influenciar o desempenho de um classificador de mensagens.', False)
add_p('A limpeza reduz a dimensionalidade do vetor e padroniza as features para o treinamento matemático. Ao aplicar técnicas como remoção de stop words, conversão para lowercase e stemming, o modelo processa strings originalmente distintas como A entrega NÃO chegou e entrega não chegava em vetores idênticos. Isso potencializa o treinamento, garantindo que o classificador relacione as palavras raízes à label correta.', False)

add_p('2. Compare Bag of Words e TF-IDF. Em que situações TF-IDF produz resultados melhores e por quê?', False)
add_p('Enquanto o BoW conta apenas a frequência absoluta dos termos no vetor, o TF-IDF (Term Frequency - Inverse Document Frequency) aplica um cálculo logarítmico para penalizar termos que são comuns em todos os documentos e bonificar termos que são raros no sistema geral, mas frequentes num texto específico. O TF-IDF é superior na classificação de chamados onde vocabulários genéricos criam ruído matemático, permitindo que a variável de decisão real ganhe peso estatístico.', False)

add_p('3. O Naive Bayes assume independência entre as palavras. Em mensagens curtas de atendimento, essa suposição pode impactar negativamente os resultados?', False)
add_p('Sim. Essa premissa de independência estrita significa que o algoritmo computa as probabilidades isoladamente e ignora a ordem sintática da frase. Em mensagens de suporte, a sequência dos tokens altera totalmente a polaridade: quero reembolso, não gostei tem os exatos mesmos vetores de não quero reembolso, gostei, mas são demandas opostas. O classificador pode falhar nessas ambiguidades lógicas.', False)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'B) PROBABILIDADE E ESTATÍSTICA PARA ANÁLISE DE DADOS', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('4. Em um teste A/B aplicado ao tempo de resposta, o grupo A teve média 6,2 min e o grupo B 5,1 min. Como verificar estatisticamente se a diferença é significativa?', False)
add_p('O procedimento indicado é a aplicação de um Teste T de Student para duas amostras independentes. Formula-se a Hipótese Nula (H0) de que as médias populacionais de A e B são estatisticamente iguais e que a redução no grupo B foi apenas uma variação amostral. Calcula-se o p-valor da distribuição; caso o valor resultante seja inferior ao nível de significância (alfa) de 0,05, rejeitamos a H0 e inferimos que a implementação que resultou nos 5,1 min tem validação estatística estrutural.', False)

add_p('5. Dado um histograma assimétrico à direita, qual medida de tendência central (média, mediana ou moda) é mais apropriada?', False)
add_p('A mediana. Uma assimetria à direita significa que um pequeno volume de outliers no conjunto de dados possui tempos muito elevados, arrastando o cálculo da média para cima. A mediana, por refletir o percentil 50 do vetor, não é sensível a valores extremos e expressa com mais exatidão o tempo real percebido pela maior parte do volume processado.', False)

add_p('6. O tempo entre chegadas no call center segue uma distribuição exponencial. O que isso significa em termos de probabilidade?', False)
add_p('A distribuição exponencial é caracterizada pela propriedade de falta de memória (Markov property). Isso garante que a probabilidade matemática do tempo decorrido até a chegada do próximo input é totalmente independente do tempo que já se passou desde a chegada anterior. Essa premissa é o modelo canônico da Teoria das Filas pois descreve sistemas de chegadas aleatórias, contínuas e independentes do mundo real.', False)

pdf.add_page()
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'C) OTIMIZAÇÃO E PESQUISA OPERACIONAL', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('7. Explique como um modelo de simulação de eventos discretos ajudaria a decidir entre contratar mais atendentes ou investir num chatbot.', False)
add_p('O uso do modelo permitiria codificar as equações matemáticas que simulam os dois cenários rodando em paralelo sem impacto na produção. Para a contratação, testa-se o aumento do nó servidores; para o chatbot, adiciona-se um nó na entrada modelado para descartar um percentual probabilístico do tráfego. Analisar os logs de output de ambas as simulações entrega uma visão determinística para alocação de recursos com base na melhor taxa de redução do gargalo vs custo operacional.', False)

add_p('8. Por que modelar com distribuições estatísticas é essencial para simulação e qual a sugestão de melhoria?', False)
add_p('Se o processo fosse imputado na simulação usando variáveis constantes de tempo (médias estáticas), o sistema não simularia interações simultâneas de clientes gerando fila, resultando em um throughput perfeitamente previsível e irreal. As funções de distribuição introduzem estocasticidade e refletem os estrangulamentos verdadeiros de serviço causados pela variação do ambiente. Sugestão: usar as medições dos picos da simulação para reescalonar os turnos logísticos.', False)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 8, 'D) SEGURANÇA DE DADOS', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('10. Como identificar elementos pessoais automaticamente e os riscos de mantê-los puros?', False)
add_p('O processamento automático de PII exige a criação de pipes lógicos utilizando Named Entity Recognition (NER) para classificação contextual aliado a bibliotecas avançadas de Expressões Regulares (Regex) para validação exata de sequências numéricas (como CPF). Manter esses dados sem filtragem em bases relacionais constitui vulnerabilidade técnica crítica que viola explicitamente o framework legal da LGPD.', False)

add_p('11. Diferencie pseudonimização de anonimização e explique qual delas é mais adequada para sistemas de chatbot.', False)
add_p('A anonimização utiliza supressão para cortar definitivamente qualquer associação do dado ao usuário real. Na pseudonimização, a associação direta é substituída por um token de identificação (UUID) que, mediante uma base criptográfica externa, permite que a empresa faça o processo reverso. Para treinamento de modelos de chatbot, a anonimização nos logs é a abordagem arquitetural recomendada, uma vez que textos contínuos treinados pela rede neural devem estar inertes legalmente.', False)

add_p('12. Em um pipeline de NLP, em que etapa a criptografia deve ser aplicada?', False)
add_p('A criptografia deve ser aplicada aos dados em trânsito (redes TLS) e dados em repouso (armazenamento em disco). Entretanto, o carregamento das rotinas na memória RAM (preprocessamento e classificação do modelo NLP) exige que o dado seja lido descriptografado para não inviabilizar os cálculos de CPU. É nessa camada lógica, no momento da injeção para a memória, que as funções de limpeza Regex e remoção de texto sensível devem rodar de forma síncrona.', False)

pdf.add_page()
add_h1('3 RESULTADOS')
add_p('A implementação computacional do script e a análise teórica da Prova de Conceito validaram a pertinência da aplicação da Ciência de Dados na estruturação das operações sistêmicas da empresa.')
add_p('Observa-se que a classificação via algoritmo de Naive Bayes e processamento de NLP apresenta viabilidade técnica para triagem estática das bases, o que otimiza o pipeline do atendimento. Da mesma forma, a tabulação estatística baseada em Teoria das Filas comprovou a eficiência de modelos de Eventos Discretos na previsibilidade estocástica, impedindo que a empresa opere de forma subdimensionada baseada em médias empíricas. Por fim, a desidentificação via Regex se provou rotina crucial no processamento in-memory, blindando o modelo de armazenar informações sujeitas à LGPD.')

pdf.add_page()
add_h1('4 CONCLUSÃO')
add_p('A execução deste Projeto Integrado demonstrou a ligação entre modelagem estatística preditiva e governança de dados. Comprovou-se que a análise exploratória e a posterior tabulação analítica fornecem direcionamento seguro de arquitetura, provando que o trabalho do cientista de dados excede a implementação isolada de rotinas de Machine Learning.')
add_p('A integração final apresentou uma estrutura na qual o tempo médio e a previsão computacional fundamentam a tomada de decisão para minimizar gargalos, enquanto a higienização do texto atende aos requisitos de compliance. O trabalho validou a estruturação pragmática de soluções de processamento para a organização segura dos dados.')

pdf.add_page()
add_h1('5 REFERÊNCIAS')

refs = [
    'KOCH, Ingedore Villaça; ELIAS, Vanda Maria. Ler e escrever: estratégias de produção textual. 2a. ed. - São Paulo: Contexto, 2010',
    'LA TAILLE, Yves de. Moral e ética: dimensões intelectuais e afetivas. Porto Alegre: Artmed, 2007',
    'METCALF, Peter. Cultura e sociedade. (Col. Homem, cultura e Sociedade). São Paulo: Saraiva, 2015',
    'Gestão & Planejamento. FACS Servicos Educacionais S.A. 1999 - ISSN 1516-9103',
    'Revista de Gestão e Projetos 2236-0972'
]

pdf.set_font('helvetica', '', 12)
for ref in refs:
    pdf.multi_cell(0, 8, cl(ref), align='L', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

pdf.output(r'c:\Users\G_406\Desktop\trabalho\diario-de-trabalho\metas\faculdade\ciencia-de-dados\semestre-2\disciplina-3-projeto-integrado-inovacao-ciencia-de-dados\trabalhos\feitos\S2-D3-Projeto-Integrado-Inovacao.pdf')
