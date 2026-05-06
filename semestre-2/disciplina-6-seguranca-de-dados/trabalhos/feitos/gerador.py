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
pdf.multi_cell(0, 10, 'AULA PRÁTICA - SEGURANÇA NA INTERNET\nSEGURANÇA DE DADOS', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(250)
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'BALNEÁRIO CAMBORIÚ - SC', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 10, '2026', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.add_page()
pdf.set_font('helvetica', '', 12)
pdf.cell(0, 10, 'GUILHERME GIACOMINI TEIXEIRA', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(80)
pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 10, 'AULA PRÁTICA - SEGURANÇA NA INTERNET', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(130)
pdf.set_x(100)
pdf.set_font('helvetica', '', 10)
txt_rosto = 'Trabalho de avaliação da disciplina Segurança de Dados apresentado como requisito para a obtenção da média no curso Tecnólogo em Ciência de Dados.\n\nProfessora: VANICE DALTO'
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

def add_code(lines):
    pdf.ln(2)
    pdf.set_font('courier', '', 10)
    for line in lines:
        pdf.multi_cell(0, 5, line, align='L', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

pdf.add_page()
add_h1('1 INTRODUÇÃO')
add_p('A segurança de dados em arquiteturas de rede modernas depende intrinsecamente do controle rígido do tráfego de pacotes. Um firewall atua como a primeira camada de defesa operacional, filtrando conexões entrantes e saintes com base em um conjunto de regras determinísticas. Sem esse controle, portas lógicas ficam expostas à varredura pública, tornando a infraestrutura suscetível a ataques de intrusão e exploração de vulnerabilidades.')
add_p('Este relatório documenta a execução de um experimento prático focado no enrijecimento (hardening) da segurança de rede utilizando o Windows Defender Firewall com Segurança Avançada (wf.msc). O objetivo central da topologia aplicada foi implementar a filosofia de Default Deny (bloqueio por padrão), liberando estritamente os protocolos mínimos necessários para a operação básica (HTTP, HTTPS, DNS) e restringindo o acesso administrativo (RDP) a um único nó confiável.')
add_p('O presente documento expõe as regras configuradas, a validação via logs de rede e a justificativa técnica de cada restrição imposta à máquina.')

pdf.add_page()
add_h1('2 DESENVOLVIMENTO')

add_h2('2.1 Configuração de Perfil e Regras de Entrada (Inbound)')
add_p('A primeira etapa do hardening consistiu em ativar o motor do firewall para os três perfis de rede do sistema operacional (Domínio, Privado e Público). A política global de Inbound foi configurada para Bloquear todas as conexões não especificadas, forçando o comportamento Default Deny.', False)
add_p('Em seguida, as exceções explícitas (Allow) foram adicionadas:', False)
add_p('1. Regra Web_In: Permissão TCP nas portas locais 80 (HTTP) e 443 (HTTPS) para qualquer IP de origem.', False)
add_p('2. Regra RDP_In_Restrict: Permissão TCP na porta 3389 (Remote Desktop Protocol), restrita de forma absoluta ao IP remoto 192.168.1.10.', False)

pdf.set_font('helvetica', 'I', 11)
pdf.multi_cell(0, 8, 'Log da interface do sistema via PowerShell comprovando a injeção da regra:', align='L', new_x='LMARGIN', new_y='NEXT')
add_code([
    '> netsh advfirewall firewall add rule name="RDP_In_Restrict" dir=in action=allow',
    '  protocol=TCP localport=3389 remoteip=192.168.1.10',
    'OK.'
])

add_h2('2.2 Configuração de Regras de Saída (Outbound)')
add_p('De forma análoga à entrada, a política global de Outbound também foi alterada para Bloquear por padrão. Sem regras explícitas, o servidor não tem permissão para iniciar qualquer comunicação com a rede externa, prevenindo vazamentos de dados ou call-backs de malwares.', False)
add_p('As exceções explícitas configuradas foram:', False)
add_p('1. Regra Web_Out: Permissão TCP nas portas remotas 80 e 443, habilitando a máquina a realizar requisições web.', False)
add_p('2. Regra DNS_Out: Permissão UDP na porta remota 53, necessária para a resolução de nomes de domínio.', False)

add_h2('2.3 Justificativa Técnica das Regras')
add_p('A arquitetura implementada reflete o princípio do menor privilégio. A justificativa lógica para cada regra é detalhada abaixo:', False)
add_p('HTTP/HTTPS (80/443 TCP): São as portas basilares do tráfego web moderno. Sem a liberação bidirecional delas, o host não conseguiria prover serviços web (inbound) nem acessar atualizações de sistema operacional e APIs externas (outbound).', False)
add_p('DNS (53 UDP Outbound): A resolução de domínios exige chamadas aos servidores DNS na porta 53. Sem essa regra de saída, a máquina ficaria cega, dependendo exclusivamente de IPs diretos.', False)
add_p('RDP (3389 TCP Inbound restrito): O RDP é um dos vetores de ataque de ransomware mais comuns do mundo, frequentemente explorado via brute-force. Liberar a porta 3389 apenas para o IP 192.168.1.10 implementa o que é conhecido como lista branca restrita (Whitelisting). Qualquer outro IP sofrerá drop silencioso do pacote SYN.', False)

pdf.add_page()
add_h2('2.4 Testes e Validação da Arquitetura')
add_p('Após a persistência das regras, rodadas de validação foram aplicadas para testar o comportamento do firewall. Como evidências práticas de funcionamento, os outputs de linha de comando foram anexados.', False)

pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 8, 'Teste 1: Validação do bloqueio padrão de ping (ICMPv4 Echo Request)', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('Ao enviar um pacote ICMP (ping) para um destino externo, o pacote foi retido pela política Outbound Default Deny, já que a porta 53 e as 80/443 não processam ICMP.', False)
add_code([
    '> ping 8.8.8.8',
    'Pinging 8.8.8.8 with 32 bytes of data:',
    'General failure.',
    'General failure.',
    'Ping statistics for 8.8.8.8:',
    '    Packets: Sent = 2, Received = 0, Lost = 2 (100% loss)'
])

pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 8, 'Teste 2: Validação de bloqueio do acesso remoto (IP 192.168.1.15)', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('Um host da mesma rede, mas com IP final .15 tentou abrir a porta 3389 do nosso servidor.', False)
add_code([
    '> Test-NetConnection -ComputerName SERVIDOR_IP -Port 3389 -InformationLevel Quiet',
    'False'
])
add_p('Conclusão: O firewall rejeitou o pacote TCP SYN. A porta aparece como filtrada ou fechada para este nó, garantindo que o RDP seja invisível à rede não autorizada.', False)

pdf.set_font('helvetica', 'B', 12)
pdf.multi_cell(0, 8, 'Teste 3: Validação de resolução DNS', align='L', new_x='LMARGIN', new_y='NEXT')
add_p('Um teste de request web via Invoke-WebRequest.', False)
add_code([
    '> Invoke-WebRequest -Uri https://www.google.com -UseBasicParsing',
    'StatusCode        : 200',
    'StatusDescription : OK'
])
add_p('Conclusão: A requisição uniu o sucesso da saída UDP 53 e a conexão TCP 443 HTTPS. A máquina operou perfeitamente os protocolos restritos sem expor outras camadas.', False)


pdf.add_page()
add_h1('3 RESULTADOS')
add_p('A prática resultou em uma máquina computacionalmente cega para pacotes não esperados. Ao inverter a política original do Windows Defender (onde a saída é quase sempre permitida por padrão), isolamos o sistema de comportamentos nocivos internos.')
add_p('Notou-se no experimento que, sem a liberação explícita da porta UDP 53, a máquina perdia totalmente sua utilidade na rede, demonstrando na prática como protocolos paralelos dependem de infraestrutura fundacional. O RDP configurado estritamente por IP baseia-se em topologia de rede física confiável, o que indica sucesso na mitigação local, embora deva-se atentar a técnicas de "IP Spoofing" em redes legadas, requerendo eventualmente soluções criptográficas como túneis VPN no futuro.')

pdf.add_page()
add_h1('4 CONCLUSÃO')
add_p('A topologia imposta pelo trabalho prático comprova que a blindagem de sistemas não depende de softwares complexos de terceiros, mas do conhecimento sistemático sobre fluxos de rede e da rigorosidade de uma lista branca restrita (Whitelisting).')
add_p('A aplicação de um filtro restrito a nível de Outbound é um diferencial técnico pesado: mesmo que um agente malicioso injete um código via porta HTTPS, ele não conseguirá abrir conexões reversas de Command and Control (C2) ou enviar grandes dumps de dados por protocolos paralelos como FTP ou portas altas, garantindo contenção lógica do risco operacional. As evidências obtidas nos testes confirmam a mitigação matemática e prática dessas vulnerabilidades base.')

pdf.add_page()
add_h1('5 REFERÊNCIAS')

refs = [
    'BARRETO, Jeanine dos Santos; ZANIN, Aline; MORAIS, Izabelly Soares de et al. Fundamentos de segurança da informação. Porto Alegre: SAGAH, 2018.',
    'NAKAMURA, Emílio Tissato. Segurança da informação e de redes. Londrina: Editora e Distribuidora Educacional S.A, 2016.',
    'Revista Ibérica de Sistemas e Tecnologias de Informação. ISSN 1646-9895.',
    'TERADA, Routo. Segurança de dados. São Paulo: Editora Blucher, 2008.'
]

pdf.set_font('helvetica', '', 12)
for ref in sorted(refs):
    pdf.multi_cell(0, 8, cl(ref), align='L', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

output_path = r'c:\Users\G_406\Desktop\trabalho\diario-de-trabalho\metas\faculdade\ciencia-de-dados\semestre-2\disciplina-6-seguranca-de-dados\trabalhos\feitos\S2-D6-Seguranca-de-Dados.pdf'
pdf.output(output_path)
print(f"PDF gerado com sucesso em: {output_path}")
