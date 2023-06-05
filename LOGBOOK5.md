## Semana 5

### Task 1 - 3.4

![3 4T1](https://user-images.githubusercontent.com/123839132/226573313-4cbd1ee3-241e-4adc-bc2a-0d70ff299108.png)
![3 4T1b](https://user-images.githubusercontent.com/123839132/226573348-c1aa0daa-d5c5-4d33-a4b5-cd2a25d3a52e.png)
![3 4T1a](https://user-images.githubusercontent.com/123839132/226573337-510136e8-488a-4cd2-88ee-581da9f5d6be.png)

Ao utilizar o comando make verificamos que os ficheiros a32.out e a64.out estão a ser compilados utilizando o execstack, o que permite que o código seja executado a partir da pilha.
Ao executar os ficheiros, percebemos que a shell é aberta em ambos os casos, permitindo ao usuário executar comandos do sistema, podendo comprometer a integridade do sistema. (usamos os comando ls e cat como exemplo)

### Task 2

A função auxiliar definida neste programa armazena até 100 caracteres e quando esta é chamada, é-lhe passada um argumento com 517 caracteres. Assim e como a função strcpy() não verifica limites, vai ocorrer um buffer overflow o que pode ser muito perigoso uma vez que estamos perante um programa Set-UID.

``gcc -DBUF_SIZE=100 -m32 -o stack -z execstack -fno-stack-protector stack.c``

"-DBUF_SIZE = 100": isto define uma macro do pré-processador denominada BUF_SIZE com um valor de 100.
"-m32": isto especifica que o código compilado deve ser para uma arquitetura de sistema de 32 bits.
"-o stack": isto especifica o nome do ficheiro de saída como "stack".
"-z execstack":  isto marca a stack como executável, o que é necessário para alguns tipos de exploits.
"-fno-stack-protector": isto desativa o mecanismo de proteção de pilha incorporado do compilador, que pode impedir certos tipos de exploits, mas também pode interferir em certos tipos de código.

Em geral, este comando de linha de shell compila um ficheiro de código em C com determinadas opções e sinalizadores para gerar um ficheiro executável denominado "stack" que pode executar código na pilha e não utiliza o mecanismo de proteção de pilha incorporado.

``sudo chown root stack``

Esta linha de comando altera o proprietário do ficheiro ´stack´ para o utilizador root.

``sudo chmod 4755 stack``

Esta linha de comando torna o ficheiro ´stack´ num SET-UID.

![T2_sem_conteudo](https://user-images.githubusercontent.com/123839132/228690902-3d54fd60-b798-4e27-ba19-b17514202665.png)


### Task 3 - 5.1

`` O comando touch badfile foi feito no 5.1 ``

![1](https://user-images.githubusercontent.com/123839132/228990021-17743910-2b16-420b-8bef-5fdff8201b47.png)
![2](https://user-images.githubusercontent.com/123839132/228989994-e8c1beb8-8965-446b-9325-95c2d8e1ef94.png)


gdb é um pacote de debugging que nos permite ver o que está a acontecer dentro do programa. Podemos percorrer o código, definir breakpoints, examinar e alterar variáveis e assim por diante.

Quando gdb pára dentro da função bof(), ele pára antes que o registo ebp aponte para o stack frame atual e assim não perdemos a informação de onde o array buffer começa. Assim é retornado o endereço da variável buffer que indica o endereço de memória onde o array, que é usado para armazenar o atributo passado à função bof(), começa.

Temos de usar o comando next para executar algumas instruções e parar depois que o ebp for modificado para apontar para o stack frame da função bof(). Assim, é-nos retornado o endereço de memória do ebp atual que será utilizado como return address.

### Task 3 - 5.2

![Screenshot from 2023-03-31 01-45-53](https://user-images.githubusercontent.com/123839132/228995075-bfb4f257-375e-47aa-ab86-1e55879c6a13.png)

conteúdo do exploit.py:

![Screenshot from 2023-03-31 01-47-21](https://user-images.githubusercontent.com/123839132/228995307-5b650a85-5491-4e95-8e20-58f63c1e9c32.png)


![Screenshot from 2023-03-31 01-38-47](https://user-images.githubusercontent.com/123839132/228994375-a66cf148-fee1-4389-9007-1016f69168f5.png)

Start = colocamos o shellcode no final do array criado na variável content (bytearray)

Offset =  É a distancia entre o ínicio do buffer e o endereço de retorno. Como temos esses dados (print do 5.1) fizemos diretamente no "debbuger" que nos deu 108, adicionamos +4 pois estamos a trabalhar num programa de 32bits.

Ret = Utilizamos o nosso valor do "buffer", que obtivemos a partir do "gdb" e adicionamos 120 uma vez que o buffer é capaz de alocar 100 caracteres, assim execedemos o tamanho do buffer provocando um buffer-overflow

L = 4 = Deixamos o 4 porque estamos a usar um 32-bit adress
