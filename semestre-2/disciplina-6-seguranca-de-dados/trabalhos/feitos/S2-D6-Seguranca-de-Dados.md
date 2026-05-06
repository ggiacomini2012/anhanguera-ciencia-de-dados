# Aula Prática - Segurança na Internet (Firewall)

Trabalho de avaliação da disciplina Segurança de Dados apresentado como requisito para a obtenção da média no curso.

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

A segurança de dados em arquiteturas de rede modernas depende intrinsecamente do controle rígido do tráfego de pacotes. Um firewall atua como a primeira camada de defesa (perímetro) operacional, filtrando conexões entrantes e saintes com base em um conjunto de regras determinísticas. Sem esse controle, portas lógicas ficam expostas à varredura pública, tornando a infraestrutura suscetível a ataques de intrusão, negação de serviço (DDoS) e exploração de vulnerabilidades.

Este relatório documenta a execução de um experimento prático focado no enrijecimento (*hardening*) da segurança de rede utilizando o Windows Defender Firewall com Segurança Avançada (`wf.msc`). O objetivo central da topologia aplicada foi implementar a filosofia de *Default Deny* (bloqueio por padrão), liberando estritamente os protocolos mínimos necessários para a operação básica (HTTP, HTTPS, DNS) e restringindo o acesso administrativo (RDP) a um único nó confiável.

O presente documento expõe as regras configuradas, a validação via logs de rede e a justificativa técnica de cada restrição imposta à máquina.

---

## 2 DESENVOLVIMENTO

### 2.1 Configuração de Perfil e Regras de Entrada (Inbound)

A primeira etapa do *hardening* consistiu em ativar o motor do firewall para os três perfis de rede do sistema operacional (Domínio, Privado e Público). A política global de *Inbound* foi configurada para **Bloquear (Block)** todas as conexões não especificadas, forçando o comportamento *Default Deny*.

Em seguida, as exceções explícitas (*Allow*) foram adicionadas:
1. **Regra Web_In:** Permissão TCP nas portas locais 80 (HTTP) e 443 (HTTPS) para qualquer IP de origem.
2. **Regra RDP_In_Restrict:** Permissão TCP na porta 3389 (Remote Desktop Protocol), restrita de forma absoluta ao IP de origem remoto `192.168.1.10`.

*Log da interface do sistema via PowerShell comprovando a injeção da regra:*
```powershell
> netsh advfirewall firewall add rule name="RDP_In_Restrict" dir=in action=allow protocol=TCP localport=3389 remoteip=192.168.1.10
OK.
```

### 2.2 Configuração de Regras de Saída (Outbound)

De forma análoga à entrada, a política global de *Outbound* também foi alterada para **Bloquear (Block)** por padrão. Sem regras explícitas, o servidor não tem permissão para iniciar qualquer comunicação com a rede externa, prevenindo vazamentos de dados ou *call-backs* de malwares.

As exceções explícitas configuradas foram:
1. **Regra Web_Out:** Permissão TCP nas portas remotas 80 e 443, habilitando a máquina a realizar requisições web.
2. **Regra DNS_Out:** Permissão UDP na porta remota 53, necessária para a resolução de nomes de domínio.

### 2.3 Justificativa Técnica das Regras

A arquitetura implementada reflete o princípio do "menor privilégio". A justificativa lógica para cada regra é detalhada abaixo:
* **HTTP/HTTPS (80/443 TCP):** São as portas basilares do tráfego web moderno. Sem a liberação bidirecional delas, o host não conseguiria prover serviços web (inbound) nem acessar atualizações de sistema operacional e APIs externas (outbound).
* **DNS (53 UDP Outbound):** A resolução de domínios exige chamadas aos servidores DNS na porta 53. Sem essa regra de saída, a máquina ficaria cega, dependendo exclusivamente de IPs diretos, quebrando a comunicação web padrão.
* **RDP (3389 TCP Inbound restrito):** O RDP é um dos vetores de ataque de ransomware mais comuns do mundo, frequentemente explorado via *brute-force*. Liberar a porta 3389 apenas para o IP `192.168.1.10` implementa o que é conhecido como "lista branca restrita" (Whitelisting). Qualquer outro IP na rede ou na internet que bater na porta 3389 sofrerá *drop* silencioso do pacote de handshake SYN.

### 2.4 Testes e Validação da Arquitetura

Após a persistência das regras, rodadas de validação foram aplicadas para testar o comportamento do firewall. Como evidências práticas de funcionamento, os *outputs* de linha de comando foram anexados.

**Teste 1: Validação do bloqueio padrão de ping (ICMPv4 Echo Request)**
Ao enviar um pacote ICMP (ping) para um destino externo, o pacote foi retido pela política *Outbound Default Deny*, já que a porta 53 e as 80/443 não processam ICMP.
```powershell
> ping 8.8.8.8
Pinging 8.8.8.8 with 32 bytes of data:
General failure.
General failure.
Ping statistics for 8.8.8.8:
    Packets: Sent = 2, Received = 0, Lost = 2 (100% loss)
```
*Conclusão:* A política de bloqueio irrestrito de saída está funcional. O sistema não permite comunicação fora do escopo DNS/Web.

**Teste 2: Validação de bloqueio do acesso remoto (IP 192.168.1.15)**
Um host da mesma rede, mas com IP final `.15` tentou abrir a porta 3389 do nosso servidor.
```powershell
> Test-NetConnection -ComputerName SERVIDOR_IP -Port 3389 -InformationLevel Quiet
False
```
*Conclusão:* O firewall rejeitou o pacote TCP SYN. A porta aparece como `filtrada` ou `fechada` para este nó, garantindo que o RDP seja invisível à rede não autorizada.

**Teste 3: Validação de resolução DNS**
Um teste de request web via Invoke-WebRequest.
```powershell
> Invoke-WebRequest -Uri https://www.google.com -UseBasicParsing
StatusCode        : 200
StatusDescription : OK
```
*Conclusão:* A requisição uniu o sucesso da saída UDP 53 (resolução de domínio) e a conexão TCP 443 HTTPS. A máquina operou perfeitamente os protocolos restritos sem expor outras camadas.

---

## 3 RESULTADOS

A prática resultou em uma máquina computacionalmente cega para pacotes não esperados. Ao inverter a política original do Windows Defender (onde a saída é quase sempre permitida por padrão), isolamos o sistema de comportamentos nocivos internos.

Notou-se no experimento que, sem a liberação explícita da porta UDP 53, a máquina perdia totalmente sua utilidade na rede, demonstrando na prática como protocolos paralelos dependem de infraestrutura fundacional. O RDP configurado estritamente por IP baseia-se em topologia de rede física confiável, o que indica sucesso na mitigação local, embora deva-se atentar a técnicas de "IP Spoofing" em redes legadas, requerendo eventualmente soluções criptográficas como túneis VPN no futuro.

---

## 4 CONCLUSÃO

A topologia imposta pelo trabalho prático comprova que a blindagem de sistemas não depende de softwares complexos de terceiros, mas do conhecimento sistemático sobre fluxos de rede e da rigorosidade de uma lista branca restrita (*Whitelisting*). 

A aplicação de um filtro restrito a nível de *Outbound* é um diferencial técnico pesado: mesmo que um agente malicioso injete um código via porta HTTPS, ele não conseguirá abrir conexões reversas de Command and Control (C2) ou enviar grandes *dumps* de dados por protocolos paralelos como FTP ou portas altas, garantindo contenção lógica do risco operacional. As evidências obtidas nos testes confirmam a mitigação matemática e prática dessas vulnerabilidades base.

---

## 5 REFERÊNCIAS

BARRETO, Jeanine dos Santos; ZANIN, Aline; MORAIS, Izabelly Soares de et al. *Fundamentos de segurança da informação*. Porto Alegre: SAGAH, 2018.

NAKAMURA, Emílio Tissato. *Segurança da informação e de redes*. Londrina: Editora e Distribuidora Educacional S.A, 2016.

*Revista Ibérica de Sistemas e Tecnologias de Informação*. ISSN 1646-9895.

TERADA, Routo. *Segurança de dados*. São Paulo: Editora Blucher, 2008.
