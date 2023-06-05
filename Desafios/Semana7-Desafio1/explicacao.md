**CheckSec**

O comando "checksec programa" é usado para verificar as medidas de segurança implementadas num programa.
Com base na saída apresentada, podemos inferir que o programa é para um sistema operacional de 32 bits.
<br/><br/>
As proteções ativadas são:
- Stack Canary: o programa tem uma proteção contra ataques de buffer overflow, que consiste em verificar se a integridade da pilha foi comprometida durante a execução. Se for detetado que a pilha foi corrompida, o programa irá terminar imediatamente.
- NX: a área de memória designada para o código não pode ser executada como se fosse um espaço de dados, tornando mais difícil para um invasor explorar vulnerabilidades no programa por meio da injeção de código malicioso.
<br/><br/>
![image](https://user-images.githubusercontent.com/98234753/232104216-7889c7cb-885d-4138-85c1-dcc73d0c9ce4.png)
<br/><br/>

**Análise do Programa**

- Qual é a linha do código onde a vulnerabilidade se encontra?
<br/> Encontra-se na linha 27: "print(buffer)". Permite que se imprima uma string sem formatação.
<br/><br/>
- O que é que a vulnerabilidade permite fazer?
<br/> Esta vulnerabilidade permite crashar o program e aceder à memória. Com isso é possível alterar valores e injetar código malicioso.
<br/><br/>
- Qual é a funcionalidade que te permite obter a flag?
<br/> Ao utilizarmos uma string de formatação no próprio "print". É possível imprimir o conteúdo da memória, incluindo o valor da flag.
<br/><br/>

**gdb**

 Executamos o debugger no programa para encontrar o endereço do buffer da flag. Como não existe a proteção PIE (randomização de endereço), os endereços são mantidos através das execuções.
- Obtendo então o seguinte endereço 0x804c060.
<br/><br/>
![image](https://user-images.githubusercontent.com/98234753/232111677-92b7ae35-8d5a-4536-8127-82e58f44697a.png)
<br/><br/>

**Catch the Flag**

Com acesso ao endereço do buffer da flag, convertemos o mesmo para little endian e em seguida, adicionamos a linha de código ```p.sendline(b"\x60\xc0\x04\x08%s")``` no script Python.
<br/>
- Obtendo assim a flag: **flag{c77ae9b368c35edac4c1d3dde7c466f4}**
<br/><br/>
![image](https://user-images.githubusercontent.com/98234753/232118475-708cec4a-2e6f-49dc-a084-afff00e934e5.png)
