### **Descobrir a mensagem de cada pessoa**

Como sabemos, foi-nos fornecido um servidor onde duas pessoas comunicam entre si usando a cifra RSA. Elas partilham o mesmo valor de módulo "n", mas têm dois valores diferentes para o expoente "e" (e1 e e2).

Começamos por executar o código para obter a informação do servidor: ```nc ctf-sp.dcc.fc.up.pt 6001```

<img width="746" alt="Screenshot 2023-05-29 at 16 03 40" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/35ba3776-c1d2-4e88-8efe-5f9b7bf419ab">

Após recebermos os valores do servidor, podemos utilizá-los num programa Python que encontramos na internet e adaptá-lo para o cenário deste desafio.

```python
import gmpy2

class RSAModuli:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.m = 0
        self.i = 0

    def gcd(self, num1, num2):
        # Encontra o maior divisor comum (GCD) entre num1 e num2
        if num1 < num2:
            num1, num2 = num2, num1
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

    def extended_euclidean(self, e1, e2):
        # Aplica o algoritmo de Euclides estendido para encontrar os valores 'a' e 'b'
        self.a = gmpy2.invert(e1, e2)
        self.b = (float(self.gcd(e1, e2) - (self.a * e1))) / float(e2)

    def modular_inverse(self, c1, c2, N):
        # Calcula o inverso modular de c1 e c2 em relação a N
        i = gmpy2.invert(c2, N)
        mx = pow(c1, self.a, N)
        my = pow(i, int(-self.b), N)
        self.m = mx * my % N

    def print_value(self):
        # Imprime o texto original descriptografado
        print("Plain Text: ", self.m)


def main():
    c = RSAModuli()
    N = 29802384007335836114060790946940172263849688074203847205679161119246740969024691447256543750864846273960708438254311566283952628484424015493681621963467820718118574987867439608763479491101507201581057223558989005313208698460317488564288291082719699829753178633499407801126495589784600255076069467634364857018709745459288982060955372620312140134052685549203294828798700414465539743217609556452039466944664983781342587551185679334642222972770876019643835909446132146455764152958176465019970075319062952372134839912555603753959250424342115581031979523075376134933803222122260987279941806379954414425556495125737356327411
    c1 = 0xdddbbff1c72999946ae11de4ea4ff5476243cf62c33dbd93c5407b7fee7b8c7042d2feec709e5909632ad0c92475b4b4729ea02993c1c7dc23516c2f2201141a04ede5f61f5ac51ff8aaede0d1d8ec8908950a37d2b680b2b5b9b6ee1e5248956108c4a7330bdcc160feef383310a99982a0b8c33d247091efec64bd7006835a7218752645115ed15debe29bdfe50c6573398993359efd89eaf16fd3bcd91d306b6c15f3dfc035f49dd6fe3a4cace6dddbe63a16f981fd8519d9639e7eca2627cfbac81e21e3d949a49ab0ff741bbe3ba27a066cd8eb14459d02ef9a9d13857dccb8c165add75df6ab4b4e50bb32210ab417fb9bf9c1bdfc6a182c440cb266d1
    c2 = 0x6676c9a87a2e0cb83ed49ff277fdb7f9efa38c3ae103f4dac887c43e6e3fd2fb04f85b4a7d5d6561b7533ef2a77afa824aaa885b057fdd45eac23fe4f7d31a0e5c42b361b714a3f4ada58540198d26a64b44623f662f7c55035fe37319e2a44a74753006daee77b98ef9c126eb76207357a200432b7f10162a78aed78b91f0201a05bcfd14fa66919b682e35c55f195dfe3f8195f9383e9ea2012dcf24513b952b0d8fe77fa4ea77cfa175b2f4b20fbd495a3d3931cd8390b3c703d195d83b71c9ac6035488f285dcec240edf1b035311555bf4c2a059a602d8e2b1b0e73d030c34840877723e36d9c7275cf7712feaa8ff849e88abfe92954ec3e7e3c7609c4
    e1 = 65537
    e2 = 65539
    c.extended_euclidean(e1, e2)
    c.modular_inverse(c1, c2, N)
    c.print_value()


if __name__ == '__main__':
    main()
```

De seguida executamos o código: ```python3 rsa_decrypt.py```. Obtendo o seguinte output em decimal:

<img width="1256" alt="Screenshot 2023-05-29 at 16 04 06" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/7f2872e2-1632-4536-a2c5-c6f75c641356">

Com o resultado obtido, passamos o ```PlainText``` de decimal para hexadecimal:

<img width="744" alt="Screenshot 2023-05-29 at 16 04 21" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/dfdff173-a058-4d0e-8c0d-f75c3ea1240f">

<br></br>

### Capturar a flag

E finalmente, convertemos de hexadecimal para texto e a flag foi descoberta: **flag{c6b0e5eeea16112e8be35f1780ab3a37}**

<img width="1198" alt="Screenshot 2023-05-29 at 16 04 45" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/3e3e5bc3-e546-4da9-971a-a2cfeed562d7">
