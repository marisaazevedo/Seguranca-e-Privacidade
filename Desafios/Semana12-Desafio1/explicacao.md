### **Descobrir o valor de ```p``` e ```q```**


Ao analisarmos o código fornecido, notamos que ```p``` e ```q``` seriam os números primos maiores que 2^512 e 2^513, respetivamente.

Para os descobrir, utilizamos um código em Python que calculasse o próximo número primo.

```python
import random

def isMillerRabinPassed(number):
    # Encontra o maior valor de divisões por dois
    maxDivisionsByTwo = 0
    ec = number - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2 ** maxDivisionsByTwo * ec == number - 1)

    def trialComposite(round_tester):
        # Verifica se o número é composto por meio do teste de Miller-Rabin
        if pow(round_tester, ec, number) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** i * ec, number) == number - 1:
                return False
        return True

    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, number)
        if trialComposite(round_tester):
            return False
    return True

def nextPrime(N):
    if N <= 1:
        return 2

    prime = N
    found = False

    while not found:
        prime += 1

        if isMillerRabinPassed(prime):
            found = True

    return prime
```

Obtendo então:

<img width="1258" alt="Screenshot 2023-05-29 at 13 32 07" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/d1aafd66-f52a-45e7-9fc3-8f7237ce4d2c">

<br></br>

### **Descobrir expoente privado ```d``` utilizando ```p``` e ```q```**


Utilizamos um algoritmo em python encontrado na internet para descobrir o valor de ```d```.

```python
def mod_inverse(x, y):
    # Função para calcular o inverso modular de x em relação a y

    def extended_euclidean_algorithm(a, b):
        # Implementação do algoritmo de Euclides estendido

        if b == 0:
            return (1, 0)

        # Divide a por b e obtém o quociente q e o resto r
        (q, r) = (a // b, a % b)

        # Chama recursivamente o algoritmo de Euclides estendido para (b, r)
        (s, t) = extended_euclidean_algorithm(b, r)

        # Retorna o resultado da recursão e realiza os cálculos necessários para obter os coeficientes s e t corretos
        return (t, s - (q * t))

    inv = extended_euclidean_algorithm(x, y)[0]

    if inv < 1:
        inv += y  # Queremos apenas valores positivos

    return inv
```

Obtendo entao para ```d = mod_inverse(e, (p - 1) * (q - 1))``` o seguinte:

<img width="1257" alt="Screenshot 2023-05-29 at 13 32 46" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/774b9de6-6de0-4913-b9f7-1c374e8e4db5">

Agora apenas é necessário descobrir a flag encriptada. Executando o seguinte código no terminal:

```nc ctf-sp.dcc.fc.up.pt 6000```

Obtendo a seguinte sequência de números e letras criptografadas.

<img width="1260" alt="Screenshot 2023-05-29 at 13 33 07" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/5eebaec6-d497-4df0-b821-1c0507c726a7">

<br></br>

### **Capturar a flag**

Com os valores necessário descobertos, agora temos de os adicionar todos ao ficheiro fornecido ```template.py```.

```python
from binascii import hexlify, unhexlify
from calculate_prime import nextPrime
from find_d import mod_inverse

p = nextPrime(2 ** 512)
q = nextPrime(2 ** 513)
n = p * q
e = 0x10001 # a constant
d = mod_inverse(e, (p - 1) * (q - 1))

enc_flag = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000023ddceba2c6e9209ead7434cc615b02eae15067765ebaf0a15b17234a300acee84ac1ddedefddc03d36d2f2bb16b6f9895e760f6f1a365c9487d3928630ecce9f12c0019ff66f02cce2b2715175b2aee2a3fc997bdaabc8d6d54b0b73972af8dfdc3b25c4e8b17c4c5729c5195c9f3586f5ee607a53418575362b2e06c065d32"

def enc(x):
    int_x = int.from_bytes(x, "big")
    y = pow(int_x, e, n)
    return hexlify(y.to_bytes(256, 'big'))

def dec(y):
    int_y = int.from_bytes(unhexlify(y), "big")
    x = pow(int_y, d, n)
    return x.to_bytes(256, 'big')

y = dec(enc_flag)
print(y.decode())
```

Ao executar o código, obtemos então a flag: **flag{7a638f2651ad8057a9897f85f983a062}**

<img width="1189" alt="Screenshot 2023-05-29 at 13 33 33" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/ddec6a1b-3ecc-4ae7-8a76-e26c58cef7b3">
