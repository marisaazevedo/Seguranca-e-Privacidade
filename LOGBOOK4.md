
# Semana 4

## Task 1:

printenv or env

![image](https://user-images.githubusercontent.com/124071367/226069849-53f7e94d-e1c3-4cd7-a3c5-91ca0b2202b9.png)

printenv PWD

![image](https://user-images.githubusercontent.com/124071367/226070061-0d28b74c-ad7c-4367-9389-2265112f6b67.png)

export

![image](https://user-images.githubusercontent.com/124071367/226070110-396e96ed-383d-4734-8960-244b797d3b95.png)

## Task 2:

![image](https://user-images.githubusercontent.com/124071367/226070746-99ffaa22-95bd-4104-bb85-fec1678e0f43.png)

A função printenv() é definida para percorrer e imprimir todas as variáveis de ambiente presentes na variável "environ". A função main() começa por declarar a variável childPid sendo esta do tipo pid_t e usa a função fork() para criar um novo processo filho.
Se a chamada fork() retornar 0, significa que o processo atual é o processo filho. Nesse caso, a função printenv() é chamada para imprimir todas as variáveis de ambiente presentes na variável environ, seguida pela chamada à função exit(0) para encerrar o processo filho.
Se a chamada fork() retornar um valor diferente de zero, significa que o processo atual é o processo pai. Nesse caso, o processo pai simplesmente chama a função exit(0) para encerrar o processo.
Como está na imagem, foram impressas todas as variáveis de ambiente, ou seja, o processo atual é o processo filho.
Ao trocar os comentários, o processo pai imprimirá as variáveis de ambiente presentes na variável "environ".
Não há diferenças nos ficheiros de output, pois o comando "fork()" duplica o processo atual, logo os ficheiros são iguais.

## Task 3:

![image](https://user-images.githubusercontent.com/124071367/226070474-11310419-48e8-4fb9-b68e-6516fe8c081e.png)

Quando o programa "myenv.c" é executado, executa um programa chamado /usr/bin/env, que imprime as variáveis de ambiente do processo atual. Quando o programa é executado, uma lista de variáveis  é impressa. Essas variáveis  são aquelas que estão definidas no processo que iniciou a execução do programa. Portanto concluímos que as variáveis de ambiente são herdadas pelo novo programa quando executado via execve().
Ao mudar a invocação do execve() na linha 1 para incluir o argumento "environ", o novo programa é capaz de ter acesso a todas as variáveis de ambiente da chamada do processo pai. Significa então, que as variaveis de ambiente definidas no processo pai são herdadas pelo processo filho executado por execve(). Concluimos assim que ao usar execve() com a variável "environ" como argumento, o novo programa recebe uma copia da lista de variaveis, o novo programa então herda uma copia das variaveis de ambiente do processo pai. Então o novo programa tem acesso às mesmas variáveis de ambiente que o processo pai tinha no momento em que execve() foi chamado

## Task 4:

![image](https://user-images.githubusercontent.com/124071367/226070634-847e57cb-4bf1-4b69-95b6-16387dce2d65.png)

## Task 5:

![image](https://user-images.githubusercontent.com/124071367/226071482-e913ff38-8be9-47ef-b589-66f91b579dca.png)

Ao executar o programa Set-UID a partir do shell, observamos que todas as variáveis de ambiente que eu defini no processo shell (pai) foram herdadas pelo processo filho que executou o programa Set-UID. Portanto, posso concluir que as variáveis de ambiente definidas no processo shell pai são, de facto, herdadas pelo processo filho Set-UID. O programa Set-UID mesmo sendo executado por um usuário não privilegiado, herda as variáveis de ambiente definidas no shell do usuário. Isso significa que um usuário pode alterar o comportamento do programa Set-UID, alterando as variáveis de ambiente antes de executá-lo representando uma ameaça de segurança. No entanto, a variável LD_LIBRARY_PATH não é herdada uma vez que esta é uma variável que define o caminho que o linker deve procurar ao vincular bibliotecas dinâmicas. Assim, como medida de segurança os diretórios são verificados primeiro, antes da sua localização real já que esta abordagem pode ser usada por um indivíduo mal-intencionado para executar uma versão maliciosa de uma biblioteca compartilhada. Deste modo, é necessário especificar o caminho para o qual a variável vai ser criada.

## Task 6:

![image](https://user-images.githubusercontent.com/124071367/226071027-27c93fb0-bcee-4377-8cab-afa029a67ac2.png)

Sim, é possível que este programa Set-UID execute código malicioso com privilégios root isso ocorre porque o programa utiliza o comando system que invoca o comando ls e não utiliza o caminho absoluto. Deste modo, a pessoa que pretende fazer coisas maliciosas, consegue definir o caminho para um programa executável malicioso antes do comando ls.

## Task 7:

Passo 1:

![image](https://user-images.githubusercontent.com/124071367/226071913-5700aa34-1c53-4594-8a5f-d17c85b66036.png)

Passo 2:

![image](https://user-images.githubusercontent.com/124071367/226072051-bbe046b6-1831-40db-91ce-c72a256cafcd.png)
![image](https://user-images.githubusercontent.com/124071367/226072094-42893025-a51e-4e72-b30d-f1671cc344ff.png)
![image](https://user-images.githubusercontent.com/124071367/226072114-0bb8aa4f-7b97-4628-a1d5-da9a53dbb3be.png)

sudo su ->  muda o utilizador para o root do sistema
user1 -> ao compilar o programa não apareceu o "I am not sleeping!" porque como o user1 é um processo filho este não herdou as variáveis LD_PRELOAD,como diz na dica, para evitar possíveis vulnerabilidades de segurança

## Task 8:

Passo 1:

![image](https://user-images.githubusercontent.com/124071367/226072446-e877d1e8-3758-4d92-b1dc-1a7ad03e523e.png)

Passo 2:

![image](https://user-images.githubusercontent.com/124071367/226072456-9d8ff0e4-2df9-4ddc-b96c-bf95df147dd4.png)

Sim, como é referido na questão, a chamada a system() é muito perigosa em programas que são Set-UID, que é o nosso caso, uma vez que demos previlégios de root ao Bob. Desta forma,o Bob pode comprometer a integridade do sistema, pois tem permissões de root, podendo por exemplo, remover um ficheiro que para ele não é "writable" .

A função "system()" permitem executar um comando da shell num programa em C,daí ser bastante perigoso quando é usado em programas Set-UID.Esta função retorna um inteiro que representa o estado da saída do comando executado. Se o valor de retorno for 0 quer dizer que o comando foi executado com sucesso, se der outro valor quer dizer que algo correu mal. Já a função "execev()" susbstitui o programa atual por um novo programa, que é especificado pelo caminho do arquivo do programa. Quando esta função é chamada, o programa atual é interrompido e susbstituído pelo novo. O primeiro argumento desta função deve ser um ficheiro binário executável, o segundo é um array de apontadores para strings passadas para o novo programa e o último elemento do array deve ser um apontador para NULL. O terceiro é um array de apontadores para strings, que são passados para o novo programa. Sim,como era espectável, os "attacks" foram bem sucedidos ao usar "execev()" em vez de "system()"
