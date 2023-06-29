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


<br></br>

### **Descobrir expoente privado ```d``` utilizando ```p``` e ```q```**

![Screenshot 2023-06-29 at 11 24 52](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/2fe7175e-e454-475e-9893-933f6d05b42d)

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

![Screenshot 2023-06-29 at 11 24 59](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/6bb2bc15-e8f3-4b43-80c6-d0f4298a0f34)

Agora apenas é necessário descobrir a flag encriptada. Executando o seguinte código no terminal:

```nc ctf-sp.dcc.fc.up.pt 6000```

Obtendo a seguinte sequência de números e letras criptografadas.

![Screenshot 2023-06-29 at 11 25 05](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/0eb2bb6f-79ec-4d7e-89f6-dc3a7a87b8af)

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

![Screenshot 2023-06-29 at 11 25 13](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/6507a95a-3ecf-4429-aef8-04d756bce396)
