
# Trabalho realizado na Semana #3

## Identificação

- a página de login do SolarWinds Storage Manager Server era vulnerável a ataques de injeção de SQL
- um invasor podia aproveitar essa falha para ignorar a autenticação no aplicativo Storage Manager ou executar comandos SQL arbitrários e extrair informações confidenciais do banco de dados de back-end usando técnicas de exploração SQL padrão
- além disso, um invasor podia aproveitar essa falha para comprometer o sistema operacional do host do servidor de banco de dados
- esta vulnerabilidade ocorre em versões anteriores a 5.1.2

## Catalogação

- esta vulnerabilidade foi reportada por Javier Castro da Digital Defense no dia 24 de janeiro de 2012
- a vulnerabilidade foi descoberta através de testes de injeção de SQL realizados pelo mesmo
- ao realizar os testes no software descobriu que era possível roubar informações confidenciais ou até modificar dados
- o nível de gravidade era 10.0

## Exploit

- o nível de complexidade destes códigos/programas era baixo, o que indica que não era necessária muita técnica para o conseguir fazer
- Exploit 1:
    - Nome: SolarWinds Storage Manager 5.1.0 - Remote SYSTEM SQL Injection;
    - Tipo : EXPLOIT-DB 18818;
    - Este explpoit permitiu inserir comandos SQL maliciosos no banco de dados subjacente.
- Exploit 2:
    - Nome: Solarwinds Storage Manager 5.1.0;
    - Tipo : EXPLOIT-DB 18833;
    - Este exploit enviava uma consulta SQL maliciosa para criar um ficheiro JSP na raiz do diretório web e, de seguida, fazia o download e executava o programa malicioso no contexto do SYSTEM.

## Ataques

- ocorreram ataques bem sucedidos e não era necessária nenhuma autenticação para conseguir fazê-los, já que eram feitos no campo de 'loginName'
- os ataques mais comuns eram:
    - Blind SQL Injection
    - Object Relational Mapping Injection
    - SQL Injection through SOAP Parameter Tampering
    - SQL Injection
    - Expanding Control over the Operating System from the Database
    - Command Line Execution through SQL Injection
- algumas configurações vulneráveis eram:
    - cpe:2.3:a :solarwinds:backup_profiler:*:*:*:*:*:*:*:*
    - cpe:2.3:a :solarwinds:storage_manager:*:*:*:*:*:*:*:*
    - cpe:2.3:a :solarwinds:storage_profiler:*:*:*:*:*:*:*:*
- estas configurações comprometeram toda a integridade, o que implicava acesso a tudo o que era confidencial na página SolarWinds

##### CVE-2012-2576 -> https://www.cvedetails.com/cve/CVE-2012-2576/
