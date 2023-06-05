**CheckSec**

O comando "checksec programa" é usado para verificar as medidas de segurança implementadas num programa.
Com base na saída apresentada, podemos inferir que o programa é para um sistema operacional de 32 bits.
<br/><br/>
As proteções ativadas são:
- PIE (Position Independent Executable): o binário é carregado em um endereço aleatório na memória a cada execução, dificultando a exploração de vulnerabilidades baseadas em endereços fixos.
- RWX:  existem segmentos de memória com permissões de leitura, escrita e execução. Isso significa que essas áreas de memória podem ser escritas e executadas, o que permite ataques de injeção de código e exploração de vulnerabilidades em binários.
<br/><br/>
  <img width="703" alt="Screenshot 2023-05-04 at 14 49 18" src="https://user-images.githubusercontent.com/98234753/236226651-bf130982-d719-4229-a4e0-2d8ebe863f83.png">
<br/><br/>

**Análise do Programa**

- Qual é a linha do código onde a vulnerabilidade se encontra?
<br/> A vulnerabilidade encontra-se na linha 12: ```gets(buffer)```
<br/><br/>
- O que é que a vulnerabilidade permite fazer?
<br/>  A função **gets** não limita o tamanho dos dados lidos e, portanto, permite que se insira mais dados do que o buffer pode armazenar. Isso faz com que a memória adjacente ao buffer seja sobrescrita, permitindo que o fluxo do programa possa ser controlado.
<br/><br/>

**Exploit**
<br/>

Tendo como base os scripts de exploits dos desafios anteriores, começamos por adicionar uma seleção no código para determinar se o programa em questão deve ser executado localmente ou remotamente.

O passo seguinte consiste em obter o endereço de memória do buffer a partir da saída recebida pelo programa. Para isso, é utilizado o Python com a biblioteca re (expressões regulares), que procura por uma sequência de caracteres que começa com "0x" e extrai o valor hexadecimal subsequente. Esse endereço é necessário para **sobrescrever a memória adjacente ao buffer**.

O código a ser injetado é definido como um array de bytes (bytearray) contendo a sequência de instruções assembly necessárias para o ataque de transbordo de buffer. Essas instruções fazem o seguinte:

- ```31 c0``` : define o valor zero no registro eax
- ```50``` : empurra o valor de eax na pilha
- ```68 2f 2f 73 68``` : empurra os caracteres //sh na pilha, na ordem inversa
- ```68 2f 62 69 6e``` : empurra os caracteres /bin na pilha, na ordem inversa
- ```89 e3``` : move o ponteiro de pilha para ebx
- ```50``` : empurra o valor de eax na pilha
- ```53``` : empurra o valor de ebx na pilha
- ```89 e1``` : move o ponteiro de pilha para ecx
- ```b0 0b``` : define o valor 11 no registro al
- ```cd 80``` : chama a interrupção do sistema (system call) para executar o código com os privilégios necessários

Depois disso, criamos um array de bytes contendo 77 caracteres "a" (poderia ser qualquer caracter) seguidos de um ponteiro de 8 bytes. Esse ponteiro é utilizado para sobrescrever o endereço de retorno da função principal do programa, fazendo com que a execução retorne para a instrução de chamada de sistema. Isso resultará na abertura de uma shell.
<br/><br/>

**Catch the Flag**

- Obtendo assim a flag: **flag{29fe1f9b4d5951867ccf327de41b53b6}**
<br/><br/>

  <img width="698" alt="Screenshot 2023-05-04 at 14 49 53" src="https://user-images.githubusercontent.com/98234753/236226934-fd56c819-6e11-4cf9-96fd-f964d9c7bde6.png">
