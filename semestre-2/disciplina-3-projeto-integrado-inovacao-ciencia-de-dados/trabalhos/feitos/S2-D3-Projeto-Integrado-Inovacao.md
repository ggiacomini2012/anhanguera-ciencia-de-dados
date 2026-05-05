# MODELO DE PADRÕES DE ARQUITETURA E SOLUÇÕES EM DADOS: 
# Projeto Integrado Inovação - Ciência de Dados

Trabalho de avaliação da disciplina Projeto Integrado Inovação – Ciência de Dados apresentado como requisito para a obtenção da média no curso.

**Aluno:** Guilherme Giacomini Teixeira
**Local:** Balneário Camboriú - SC
**Ano:** 2026

---

## SUMÁRIO
1. [INTRODUÇÃO](#1-introdução)
2. [DESENVOLVIMENTO](#2-desenvolvimento)
3. [RESULTADOS](#3-resultados)
4. [CONCLUSÃO](#4-conclusão)
5. [REFERÊNCIAS](#5-referências)

---

## 1 INTRODUÇÃO

Este relatório técnico apresenta o desenvolvimento do Projeto Integrado de Inovação em Ciência de Dados, cujo objetivo central é propor e demonstrar a viabilidade de uma solução tecnológica para os desafios operacionais de uma empresa nacional de varejo digital. A empresa em questão enfrenta dificuldades crescentes em seus canais de atendimento devido a altos tempos de espera, ausência de classificação automática de chamados, falta de visão estatística de performance e a necessidade latente de mitigação de riscos relacionados à Lei Geral de Proteção de Dados (LGPD).

Para suprir essa demanda, foi projetada e executada uma Prova de Conceito (POC) que unifica conhecimentos de Processamento de Linguagem Natural (NLP), Probabilidade e Estatística, Pesquisa Operacional e Segurança de Dados. O projeto simulou a chegada e o atendimento de mensagens, construiu um modelo classificador automatizado, avaliou a distribuição e frequência estatística dos contatos, e aplicou estratégias de anonimização. 

O produto final deste documento detalha a resolução prática do código proposto em ambiente Google Colab, bem como respostas técnicas e fundamentadas às disciplinas correlatas, comprovando a aplicação prática da teoria e a eficiência de uma arquitetura de dados inteligente e segura para processos de negócio do varejo.

---

## 2 DESENVOLVIMENTO

### 2.1 Análise da Prova de Conceito (Código Colab)

A seguir, apresentam-se as análises obtidas a partir da execução do código de simulação proposto para o contexto da empresa de varejo:

**A) NLP**
1. **Qual categoria teve melhor desempenho no classificador Naive Bayes?**
Todas as categorias obtiveram desempenho perfeito no relatório de classificação (Precision, Recall e F1-Score iguais a 1.00). Esse resultado ocorreu devido à forma como os dados fictícios foram gerados: uma lista muito reduzida e repetitiva de frases pré-definidas. Com isso, os dados separados para o teste eram idênticos ou perfeitamente sobrepostos aos vistos no treinamento, não apresentando desafio de generalização para o classificador.

2. **Em suas palavras, como funciona a vetorização Bag of Words?**
A vetorização "Bag of Words" (Saco de Palavras) converte textos em formatos numéricos lidos por máquinas. Ela extrai um vocabulário com todas as palavras únicas contidas nos dados e, para cada mensagem, cria um vetor contando a frequência de cada uma dessas palavras. A ordem ou sintaxe da frase é ignorada; a ferramenta se importa unicamente com *quais* palavras apareceram e *quantas* vezes.

**B) Probabilidade e Estatística**
3. **Qual categoria teve maior frequência? O que isso indica?**
Durante a execução de nossa geração de dados estocásticos, a categoria com maior frequência foi "elogio". Em um contexto real de negócios, isso indicaria uma alta satisfação com os serviços prestados, mas, dentro do modelo em questão, indica apenas a variação probabilística e a aleatoriedade (`random.choice`) selecionando essa variável uma quantidade marginalmente superior de vezes na amostra de 500 mensagens.

4. **Interprete o histograma de tempo de espera: é simétrico, assimétrico, disperso?**
O histograma gerado pela operação matemática entre as distribuições tendeu à assimetria (mais disperso à direita). Em simulações operacionais reais e em Teoria das Filas, os tempos de espera tendem a ser fortemente assimétricos à direita, concentrando a grande massa de eventos em tempos curtos, com uma cauda longa representando casos atípicos em que o cliente aguardou um período consideravelmente maior devido ao estrangulamento da capacidade do serviço.

**C) Pesquisa Operacional**
5. **O tempo médio de espera é adequado? Como poderia ser reduzido?**
O tempo médio na simulação apresentou-se por volta de 2,59 minutos. A "adequação" está sujeita aos SLAs (Acordos de Nível de Serviço) da empresa. Caso represente um problema — especialmente para a volatilidade do atendimento via chat/WhatsApp —, esse tempo pode ser reduzido otimizando-se o modelo de roteamento de filas, promovendo escalonamento do pessoal nos horários de pico previstos pelas distribuições estatísticas ou inserindo o autoatendimento prévio automatizado.

6. **Cite duas ações que podem otimizar o fluxo de atendimento.**
* **Primeira linha de defesa via Chatbot (NLP):** Inserir agentes de IA focados em resolver chamados triviais de imediato, reservando os atendentes humanos exclusivamente para as exceções complexas.
* **Roteamento Especializado:** Segmentar o tráfego da fila dinamicamente para que assuntos críticos (ex: cancelamentos e retenções) furem a fila comum ou vão diretamente para especialistas, reduzindo o trânsito total da base.

**D) Segurança de Dados**
7. **O que é anonimização?**
A anonimização, no contexto corporativo e da LGPD, é a descaracterização técnica de uma informação, removendo elementos vinculantes e impossibilitando, em caráter irreversível, que aquele dado possa identificar direta ou indiretamente uma pessoa física, mantendo entretanto o valor daquele texto como material para cálculos estatísticos.

8. **Quais dados sensíveis podem aparecer em mensagens de clientes?**
Nomes completos, CPFs, números de cartões de crédito, dados bancários completos, endereços residenciais, imagens pessoais, e-mails, senhas, além de dados potencialmente sensíveis relativos a saúde e biometria, dependendo da transação.

9. **Qual risco existe em armazenar textos sem anonimização?**
Armazenar textos na forma bruta incorre no gravíssimo risco de vazamento ou exposição indevida da privacidade. Além de destruir a credibilidade da empresa no mercado, a conduta fere as normas da LGPD, expondo a corporação a multas milionárias (de até 2% do faturamento), obrigações civis de reparação e ao bloqueio total do uso do banco de dados na companhia.


### 2.2 Resolução de Conceitos Específicos por Disciplina

**A) PROCESSAMENTO DE LINGUAGEM NATURAL (NLP)**
1. **Explique como o processo de pré-processamento textual pode influenciar o desempenho de um classificador de mensagens. Dê um exemplo prático.**
O pré-processamento elimina o ruído e reduz o vocabulário ao mínimo necessário para a extração do contexto analítico. Ele facilita o treinamento do modelo matemático. Exemplo prático: ao remover *stop words* e unificar sinônimos com *stemming*, mensagens originalmente distintas como "A minha entrega não chegou hoje!!" e "não recebi entrega" transformam-se essencialmente na mesma representação tokenizada (["não", "chegou", "entrega"]), garantindo que o algoritmo de classificação aloque ambas precisamente na mesma caixa ("Reclamação").

2. **Compare Bag of Words e TF-IDF. Em que situações TF-IDF produz resultados melhores e por quê?**
Enquanto o "Bag of Words" atua com contagem burra e bruta das aparições de palavras, o "TF-IDF" (Term Frequency-Inverse Document Frequency) promove uma penalização estratégica a palavras que aparecem repetitivamente em todos os documentos e não diferenciam os textos. O TF-IDF brilhará na identificação de "features" em domínios densos, como os dados varejistas do caso. Ele entenderá que "pedido" pode ser frequente em quase toda mensagem da loja, reduzindo seu peso preditivo, enquanto exalta o peso definidor do termo ocasional "estorno" que é altamente relevante para a classificação "Cancelamento".

3. **O Naive Bayes assume independência entre as palavras. Em mensagens curtas de atendimento, essa suposição pode impactar negativamente os resultados? Justifique com base no contexto real do problema.**
Sim. Essa premissa "ingênua" (Naive) pode destruir o significado pragmático na análise de sentimento e intensões curtas. Como ele ignora o encadeamento das palavras (ordem), para ele as frases "Não quero devolução, adorei" e "Quero devolução, não adorei" contêm o exato mesmo vetor matemático, o que na vida real representa situações radicalmente opostas (Elogio vs Cancelamento).

**B) PROBABILIDADE E ESTATÍSTICA PARA ANÁLISE DE DADOS**
4. **Em um teste A/B aplicado ao tempo de resposta, o grupo A teve média 6,2 min e o grupo B 5,1 min. Explique como você verificaria estatisticamente se essa diferença é significativa.**
Executaríamos um Teste de Hipóteses (tal qual o Teste T de Student para amostras independentes). A Hipótese Nula (H0) assumiria que as duas médias representam as mesmas realidades, sendo a diferença observada puro acaso. Caso o cálculo do *p-valor* do Teste T fosse menor do que o nível de significância estabelecido (o habitual alfa de 5%, ou 0,05), rejeitaríamos a Hipótese Nula e inferiríamos de fato que a implantação que gerou os 5,1 min. representam um salto estrutural (estatisticamente significativo) em eficiência frente ao cenário anterior.

5. **Dado um histograma de tempo de espera assimétrico à direita, descreva qual medida de tendência central (média, mediana ou moda) é mais apropriada para representar esse conjunto. Justifique.**
A **Mediana**. Como a assimetria à direita indica que há poucas ocorrências que puxam a cauda com valores elevadíssimos de tempo (outliers de clientes que esperaram horas na fila), a Média aritmética seria contaminada, parecendo falsamente muito maior do que a realidade experimentada pela enorme maioria dos clientes. A Mediana, indicando o percentil 50, demonstraria mais honestamente o tempo aguardado pelo cliente central, independentemente do teto superior extremo na amostra.

6. **O tempo entre chegadas no call center segue uma distribuição exponencial. Explique o que isso significa em termos de probabilidade e por que esse modelo é amplamente usado em filas.**
Isso traduz a famosa "Falta de Memória" (Markoviana) da distribuição exponencial. Para os cálculos operacionais de filas, isso garante que o fato de ninguém ter contatado a central há 10 minutos não torna mais provável ou improvável que o próximo contato vá ocorrer nos próximos 3 segundos. É altamente utilizada em pesquisa operacional por representar o caráter naturalmente intermitente, contínuo e orgânico da chegada de demandas externas.

**C) OTIMIZAÇÃO E PESQUISA OPERACIONAL**
7. **Explique como um modelo de simulação de eventos discretos poderia ajudar a decidir entre contratar mais atendentes ou investir em um chatbot inicial.**
O gestor poderia instanciar no software dois cenários distintos espelhando os parâmetros estatísticos do caso real: no Cenário 1, os servidores paralelos (atendentes) aumentam de X para X+Y; no Cenário 2, as taxas de chegada são filtradas por um funil anterior ("chatbot") que elimina, por exemplo, 30% da carga estatística que chegaria à base da fila humana. Simular ambas e analisar a métrica final (redução de fila vs aumento de custo) permitiria tomar a decisão corporativa fundamentada financeiramente sem expor a empresa em operação *live*.

8. **O tempo de chegada e atendimento no sistema foram modelados por distribuições estatísticas. Justifique por que essa modelagem é essencial para simulação e otimize uma sugestão de melhoria no processo.**
Se a empresa adotasse parâmetros de médias estáticas (1 chegada por 2 minutos, demorando 5 minutos), jamais veria enfileiramento na simulação (afinal, a matemática cartesiana rodaria lisa e imutável). As distribuições estocásticas reproduzem estritamente as imprevisibilidades do mundo fático — as flutuações e picos geradores dos afunilamentos e gargalos em sistema de filas que a empresa varejista precisa otimizar.
**Sugestão de otimização:** Aproveitar os painéis da simulação para identificar gargalos e dimensionar turnos "pulmão".

**D) SEGURANÇA DE DADOS**
10. **Mensagens de atendimento podem conter dados pessoais e até dados sensíveis. Explique como identificar esses elementos automaticamente e os riscos de mantê-los em texto puro.**
Com arquiteturas de IA, as empresas constroem ou conectam rotinas de *Named Entity Recognition (NER)* (que compreendem contexto do termo na frase identificando Nomes ou Organizações) unidas a RegEx (Expressões Regulares - varreduras algorítmicas imbatíveis para capturar padrões sintáticos como de CPFs ou numeração de RG/Boleto). Se expostas no Data Lake bruto da empresa, uma única engenharia social e exploração de banco poderia expor todo o compliance, acarretando punições drásticas.

11. **Diferencie pseudonimização de anonimização e explique qual delas é mais adequada para sistemas de chatbot.**
A Anonimização destrói a origem (a chave) de forma irreversível; ninguém mais rastreará que a reclamação Y pertenceu ao João. Já a Pseudonimização mascara ("embaralha") o identificador original usando tokens criptográficos que podem, eventualmente, ser rastreados para as bases de perfis da empresa de posse das chaves. Em processamentos com Chatbots, a **anonimização** dos *logs textuais soltos e treinamentos de IA NLP* garante a paz fiscal/legal, mas os dados estruturados paralelos das sessões que fecham pedidos ainda devem utilizar pseudonimização para permitir a cobrança no sistema transacional de pagamentos da corporação.

12. **Em um pipeline de NLP, em que etapa a criptografia deve ser aplicada? Explique sua resposta com foco em segurança, desempenho e arquitetura.**
Na camada arquitetural "in flight" (em trânsito) — quando trafega entre o Whatsapp e os servidores corporativos via protocolos criptografados (ex: HTTPS / TLS) — e também "at rest" (em repouso) quando inseridas provisoriamente num Data Lake. Contudo, as arquiteturas computacionais de NLP demandam o carregamento textual na memória RAM do pipeline já não criptografado, para evitar esgotamento computacional maciço. Neste exato ponto (na memória), o correto a atuar, via código de ingestão, é o pré-processamento em tempo real promovendo de imediato a Anonimização antes que os dados continuem correndo via processos computacionais ou persistam e retroalimentem os vetores do classificador matemático. 

---

## 3 RESULTADOS

Com a execução da Prova de Conceito baseada no código estipulado de simulação Python, assim como do estudo teórico, validou-se a extrema utilidade do emprego da Ciência de Dados na operação central de relacionamento ao consumidor da referida rede de Varejo Digital. 

Destacam-se três conclusões principais extraídas e confirmadas na operação:
1. **Poder de Interceptação da IA (NLP):** A viabilidade de triagem inteligente via Naive Bayes e NLP confirma que a classificação automática é barata e madura, permitindo ao gestor alocar tempo e recursos humanos exclusivamente naquilo em que a máquina não transita.
2. **Previsibilidade e Dimensionamento Matemático (Simulação e Filas):** A compreensão de padrões estocásticos (probabilísticos de chegado e serviço, analisados em Pesquisa Operacional) destrói as estratégias primitivas de apenas "contratar para diminuir filas". Validou-se a viabilização de testes em Modelos Discretos de Simulação para encontrar o cenário ideal de operação do serviço.
3. **Resiliência e Higiene Jurídica nos Dados:** O isolamento e a descaracterização criptografada e anonimizada na modelagem protege os ativos financeiros da organização e respeitam a intimidade e dados garantidos à sociedade civil pela LGPD.

---

## 4 CONCLUSÃO

A realização prática e teórica do Projeto Integrado demonstrou claramente a essência holística do perfil do Cientista de Dados e as responsabilidades adjacentes a ele: não basta construir ou codificar um classificador estatisticamente perfeito se ele colidir com as normas legais de compliance na manipulação daquele dado. A integração proposta nesta Prova de Conceito demonstrou-se robusta. Modelou-se logicamente o negócio para expandi-lo não usando mera intuição gerencial, mas sim ciência fundamentada em previsibilidade matemática da Pesquisa Operacional e Segurança de Informação perimetral ao algoritmo de IA NLP.

Este trabalho reforça a competência do cientista de dados em prover otimização, escalabilidade inteligente aos processos corporativos sem perder de vista a integridade da arquitetura dos serviços organizacionais.

---

## 5 REFERÊNCIAS

ANHANGUERA. Projeto Integrado Inovação – Ciência de Dados: Roteiro de Aula Prática e Simulações Operacionais. Balneário Camboriú: Anhanguera, 2026. Material de curso.

BRASIL. Lei Geral de Proteção de Dados Pessoais (LGPD). Lei nº 13.709, de 14 de agosto de 2018. Brasília, DF: Presidência da República, 2018.

TAHA, H. A. Pesquisa Operacional: Uma Visão Geral. 8. ed. São Paulo: Pearson Prentice Hall, 2008.

JURAFSKY, D.; MARTIN, J. H. Speech and Language Processing. 3. ed. Draft. Stanford: Stanford University, 2023.
