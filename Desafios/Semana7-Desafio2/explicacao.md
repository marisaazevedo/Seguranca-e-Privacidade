**CheckSec**

O comando "checksec programa" é usado para verificar as medidas de segurança implementadas num programa.
Com base na saída apresentada, podemos inferir que o programa é para um sistema operacional de 32 bits.
<br/><br/>
As proteções ativadas são:
- Stack Canary: o programa tem uma proteção contra ataques de buffer overflow, que consiste em verificar se a integridade da pilha foi comprometida durante a execução. Se for detetado que a pilha foi corrompida, o programa irá terminar imediatamente.
- NX: a área de memória designada para o código não pode ser executada como se fosse um espaço de dados, tornando mais difícil para um invasor explorar vulnerabilidades no programa por meio da injeção de código malicioso.
<br/><br/>
![image](https://user-images.githubusercontent.com/98234753/232121517-75e5842e-48c8-41c3-ae15-a9d891c6ecc2.png)
<br/><br/>

**Análise do Programa**

- Qual é a linha do código onde a vulnerabilidade se encontra? E o que é que a vulnerabilidade permite fazer? \
Encontra-se na linha 14: "print(buffer)". Permite crashar o programa e aceder à memória, permitindo assim alterar valores e injetar código malicioso.
<br/><br/>
- A flag é carregada para memória? Ou existe alguma funcionalidade que podemos utilizar para ter acesso à mesma? \
É possível ter acesso e alterar o valor da variável "key", que é carregada na memória. 
<br/><br/>
- Para desbloqueares essa funcionalidade o que é que tens de fazer? \
Para explorar esta vulnerabilidade e alterar o valor de "key" para 0xbeef, utilizamos a técnica de "Format String", que permite inserir comandos específicos para alterar valores de variáveis na string de formatação.
<br/><br/>

**Script**

Para solucionar este segundo desafio, utilizamos o script em Python que foi disponibilizado no primeiro desafio desta semana.
<br/><br/>

**gdb**

 Executamos o debugger no programa para encontrar o endereço da variável key.
- Obtendo então o seguinte endereço 0x804c034. 
<br/><br/>
![image](https://user-images.githubusercontent.com/98234753/232124343-3a4e116f-0931-4cc3-8e39-7a4936a11c11.png)
<br/><br/>

**Catch the Flag**

Com acesso ao endereço da variável key, convertemos o mesmo para little endian. \
Para o ataque ser feito com sucesso:
1. Adicionamos antes do endereço representado em formato little endian uma sequência de quatro "@" que são usados como um buffer para o ataque.
2. Adicionamos depois do endereço representado em formato little endian a instrução de formatação de string "%48871x%n". \
Como a key pretendida é 0xbeef (em decimal 48879), será necessário então imprimir 48879 caracteres antes de se chamar "%n".
Porém, "\x34\xc0\x04\x08" já corresponde a 4 caracteres, então fica-se com 48875 caracteres antes de se chamar "%n". \
No entanto, quando o "%48875x" é lido durante a formatação da string, o apontador da stack avança para a próxima posição, fazendo com que ele deixe de apontar para o endereço 0x804c034, que era o endereço da variável "key". \
Para resolver o problema mencionado anteriormente, optamos por remover mais 4 caracteres. Com essa mudança, durante a formatação da string, o apontador da stack passou a apontar para o endereço correto da variável "key".

Finalmente, adicionamos a linha de código ```p.sendline(b"@@@@\x34\xc0\x04\x08%.48871x%n")``` no script Python.
<br/>
- Obtendo assim a flag: **flag{f8d2c2ba615bd7a2dc1813f1759aadd}**
<br/><br/>
![image](https://user-images.githubusercontent.com/98234753/232134388-edb0803b-8049-427d-9047-6dbe09ec01c1.png)
<br/><br/>
