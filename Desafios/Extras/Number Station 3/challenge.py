# Python Module ciphersuite
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from binascii import unhexlify

FLAG_FILE = '/flags/flag.txt'

# Use crypto random generation to get a key with length n
def generate_key():
    random_key = bytearray(os.urandom(16))
    for i in range(16):
        random_key[i] = random_key[i] & 1
    return bytes(random_key)


# Reverse operation
def decrypt_message(key, ciphertext):
    assert len(ciphertext) % 16 == 0
    cipher = Cipher(algorithms.AES(key), modes.ECB(), default_backend())
    decryptor = cipher.decryptor()
    blocks = len(ciphertext) // 16
    message = b""
    for i in range(0, blocks):
        message += decryptor.update(ciphertext[i * 16:(i + 1) * 16])
        message = message[:-15]
    message += decryptor.finalize()
    return message


encrypted_shell = b"044cc8b0643a614ca51e3cbb7e07bac26d7ff80cb2ef9ae6bf24bc1bd28916a89325ab8e8f819c4a5dedc0dafa3fdfbc4be34ce5e4f4eefd40b5735283646b750ab97197d26bd6c95ba6a3272c22ed55ee582104f13990f941ca33011b426587c66ab910d0a2d262fc5e3faa839ef7ba2a3fc03e5ae87eeca336e1309f2471759325ab8e8f819c4a5dedc0dafa3fdfbc4873f9ac443df66cd6c60962e4c4ac603892b5df616064edac01ff179643f0cd04647ae001521c805b3c07db9ce4ca07c66ab910d0a2d262fc5e3faa839ef7bac66ab910d0a2d262fc5e3faa839ef7ba2a3fc03e5ae87eeca336e1309f24717516189f547f7547218c97b2781f427c8fcaa017b2cc80bb01d0607c5100b36d4016189f547f7547218c97b2781f427c8f2a3fc03e5ae87eeca336e1309f247175e3c7bb0f34fdb088cd20966f958749512f7036a6fda8e8ea160f0423d09e37e9044cc8b0643a614ca51e3cbb7e07bac2caa017b2cc80bb01d0607c5100b36d4004647ae001521c805b3c07db9ce4ca07bf5cf989b109ff5236459c7714be1790caa017b2cc80bb01d0607c5100b36d40caa017b2cc80bb01d0607c5100b36d40e3c7bb0f34fdb088cd20966f95874951374f952a427ac4814475029caafcd3422a3fc03e5ae87eeca336e1309f2471753892b5df616064edac01ff179643f0cdbf5cf989b109ff5236459c7714be179051a9dfacb03f069634c76efa64b487de2a3fc03e5ae87eeca336e1309f24717551a9dfacb03f069634c76efa64b487deee582104f13990f941ca33011b426587e4d4f95da883b893022fce75ee2c987ac08ce3dc67d644252a3fa27feba60c1e3f642f4d92dc390dfae15b41110af437"

for i in range(2 ** 16):
    # print(i)
    key = generate_key()
    if decrypt_message(key, unhexlify(encrypted_shell)).decode('latin-1')[0:4] == "flag":
        print(decrypt_message(key, unhexlify(encrypted_shell)).decode('latin-1'))
        break
