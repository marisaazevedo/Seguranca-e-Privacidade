## Task 1: Becoming a Certificate Authority (CA)

 ```O objetivo desta tarefa, é tornarmo-nos uma Certificate Authority (CA) para podermos emitir um certificado digital para terceiros.```

 Começamos por copiar o openssl.cnf para o nosso diretório para que pudéssemos fazer as alterações necessárias no mesmo, e como pedido no guião, tiramos o comentário no parametro 'unique_subject'.

<img width="604" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/a5a43032-d7e7-4617-b6e4-8252cbda2e45">

Após isto, criamos a pasta 'demoCA' e adicionamos os arquivos necessários conforme referido no guião.

Após a configuração inicial, precisamos gerar um certificado self-signed para a nossa CA:

<img width="1671" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/c2342e2c-6880-4db8-9235-7f9b130587e7">

Podemos usar os seguintes comandos para ver o conteúdo decodificado do certificado X509 e a chave RSA:

 ```openssl x509 -in ca.crt -text -noout```:

```py
06/04/23]seed@VM:~/.../Crypto_PKI$ openssl x509 -in ca.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            63:c5:8d:44:74:d6:40:17:b5:52:46:c3:fc:91:a1:d3:e5:3f:ee:c1
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = www.modelCA.com, O = Model CA LTD., C = US
        Validity
            Not Before: Jun  4 17:52:02 2023 GMT
            Not After : Jun  1 17:52:02 2033 GMT
        Subject: CN = www.modelCA.com, O = Model CA LTD., C = US
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (4096 bit)
                Modulus:
                    00:b1:05:8e:2a:f7:75:ee:6d:0a:db:d4:26:90:72:
                    4b:42:97:de:47:61:bb:92:94:9f:d0:99:fe:78:d7:
                    b9:09:37:8a:54:d6:8f:50:63:11:93:6c:60:2a:01:
                    6c:f2:79:c4:f9:05:64:6a:11:4c:81:9d:a0:7c:97:
                    15:8e:bf:8c:59:c3:93:0a:1c:f0:d0:c7:ec:73:1e:
                    35:a4:d8:f7:de:60:21:90:9e:c5:dc:5c:7b:7f:62:
                    83:52:23:56:48:04:28:a9:45:0f:41:67:e4:ae:bf:
                    b3:47:0a:9d:ec:3a:05:8d:e3:de:d5:4a:97:b2:ae:
                    d6:5c:11:49:a3:a6:ff:16:87:ca:04:46:5e:79:4a:
                    e1:7a:fa:2a:98:2e:ac:3e:ec:b5:b7:5c:d8:08:a3:
                    b5:ef:0d:2c:62:9e:93:63:41:01:8d:bd:ae:b4:9c:
                    4c:52:91:ef:9e:23:be:7a:d7:56:35:bd:b0:07:e5:
                    3f:12:b5:a8:5f:30:e9:15:56:d2:69:4f:de:c6:19:
                    47:01:17:b1:62:fa:8d:04:32:5b:db:4a:b3:64:dd:
                    7e:7f:f9:86:f5:7e:40:71:f5:1b:1e:a8:a1:dd:77:
                    12:30:e6:f2:66:12:7d:3a:c8:1d:8d:d4:f5:57:f2:
                    60:a2:65:fe:b9:e0:a3:f1:e5:72:c4:6c:c4:8d:8f:
                    51:d5:4b:a3:46:a7:51:a3:0c:01:f5:73:e2:dd:63:
                    bb:10:bb:37:a9:19:3b:7b:60:1b:a5:6d:5c:84:3f:
                    e7:36:e6:db:2a:14:d8:19:04:67:40:07:29:ea:ad:
                    03:74:48:3f:5c:0a:60:57:9f:1a:a5:a9:42:29:c4:
                    32:6d:fb:3c:5d:2d:ee:50:55:a8:62:36:fc:37:a9:
                    d9:18:cb:28:7e:03:a6:fa:f8:f1:87:70:c5:15:75:
                    5d:10:a8:17:0a:f4:18:df:b6:0e:48:9b:6d:2c:24:
                    f1:50:e4:07:1c:cc:67:ff:b7:16:7e:01:9a:de:76:
                    95:01:52:b2:3d:56:7f:7f:5a:7d:0c:2a:18:33:78:
                    43:ad:cd:2d:0a:d4:52:04:41:fc:4c:64:7d:47:2c:
                    b5:65:95:22:ae:6b:33:f2:6d:e2:cf:a0:3c:8c:d7:
                    30:bd:44:a0:50:34:f4:f7:47:74:2a:c6:e4:d6:7b:
                    2b:99:fb:cc:de:32:9a:28:60:ac:99:c2:7c:c1:fc:
                    ec:55:1a:a4:0f:7b:da:f8:94:8f:2c:e2:74:df:22:
                    5b:93:a0:f1:8c:81:20:9c:02:12:d4:58:48:22:1c:
                    6d:ea:91:29:b1:7c:90:47:af:01:2a:bc:ff:38:dc:
                    2c:49:48:20:8c:57:31:c4:be:53:d7:68:9c:7c:1c:
                    66:2b:6f
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier:
                46:EB:AF:9D:50:47:7D:DA:19:29:61:C3:51:91:50:6D:C7:F8:05:A7
            X509v3 Authority Key Identifier:
                keyid:46:EB:AF:9D:50:47:7D:DA:19:29:61:C3:51:91:50:6D:C7:F8:05:A7

            X509v3 Basic Constraints: critical
                CA:TRUE
    Signature Algorithm: sha256WithRSAEncryption
         22:fa:ad:b4:54:40:40:df:59:08:06:c9:ff:de:9b:1d:af:18:
         1a:b0:80:92:34:76:e9:7f:f8:56:3d:d2:44:ce:3a:5f:dc:d4:
         71:48:9a:2e:9f:cb:76:f2:64:ea:c7:1e:aa:12:a5:43:30:2f:
         1d:fc:86:6a:e6:2d:78:01:72:8d:2f:3c:e2:cc:25:ec:81:25:
         bc:83:8b:db:4d:0b:ee:01:ba:f3:57:53:89:d1:d4:17:c8:35:
         ae:2c:95:8f:51:9e:cc:e6:36:9a:48:06:a9:b1:89:96:46:67:
         72:60:67:40:14:a8:3b:31:17:a0:8a:90:a3:f7:12:60:d4:c9:
         43:48:3e:a3:41:bf:bc:e3:6c:a9:7b:d9:16:b2:15:6f:2f:cc:
         f6:07:69:35:4a:2c:40:9d:24:d2:c3:c8:57:d4:89:4a:73:b4:
         08:c0:f4:ab:d6:89:64:e6:07:d5:11:32:f4:b4:ea:17:38:e4:
         5f:f0:d7:4e:66:33:11:42:f8:5f:a1:1a:70:3a:07:c8:15:a9:
         a6:b4:a6:ac:81:1a:39:89:ec:50:de:81:22:c8:cb:e1:18:79:
         a8:30:1f:d0:5c:da:d1:0d:16:fa:c9:42:51:fb:4b:fd:d7:48:
         d7:0f:b0:20:46:66:81:e0:1c:ce:12:ff:11:7d:c2:32:6a:8a:
         84:48:aa:75:37:ab:cd:03:19:a7:d7:49:dd:77:c0:a1:7a:1a:
         f1:81:f7:fa:df:6a:e6:b1:c9:02:27:c2:97:7a:a3:64:dc:14:
         93:b2:77:51:0c:22:c3:43:96:30:61:b1:52:ea:1c:c9:26:aa:
         81:a6:04:57:cd:45:51:c4:af:8e:dc:e7:7f:76:15:8b:d8:30:
         60:cf:27:3c:e3:68:77:4b:0d:15:b2:a3:9d:98:e8:43:86:2d:
         94:5d:09:22:37:0b:7e:13:7d:16:93:52:fd:39:0d:43:4e:7b:
         23:8c:f5:a3:34:7c:4e:69:dd:98:b9:ff:5a:f4:33:d6:55:a5:
         b6:fc:c6:7a:9d:d7:4b:bd:ed:a4:79:38:09:2c:86:21:8a:a9:
         23:9f:d4:60:47:19:dc:be:80:7b:78:97:54:76:fa:c3:6e:3a:
         36:95:34:c0:0d:1f:66:16:2c:da:de:27:54:9d:48:d3:db:8a:
         cf:64:17:8e:47:57:14:3a:c6:40:da:87:29:d2:12:31:5f:24:
         c3:30:51:fd:68:92:1f:8d:62:e5:dd:09:0f:f1:fd:ad:a7:6d:
         6e:ab:bc:00:19:34:59:42:25:3b:5a:77:a0:62:2a:a9:75:43:
         6c:88:04:08:f5:06:81:5d:03:38:0a:f3:12:ff:c5:fa:6c:8b:
         36:db:c6:3b:73:3e:c6:3e
```

 ```openssl rsa  -in ca.key -text -noout```:

 ```py
 [06/04/23]seed@VM:~/.../Crypto_PKI$ openssl rsa -in ca.key -text -noout
Enter pass phrase for ca.key:
RSA Private-Key: (4096 bit, 2 primes)

modulus:

00:b1:05:8e:2a:f7:75:ee:6d:0a:db:d4:26:90:72:
4b:42:97:de:47:61:bb:92:94:9f:d0:99:fe:78:d7:
b9:09:37:8a:54:d6:8f:50:63:11:93:6c:60:2a:01:
6c:f2:79:c4:f9:05:64:6a:11:4c:81:9d:a0:7c:97:
15:8e:bf:8c:59:c3:93:0a:1c:f0:d0:c7:ec:73:1e:
35:a4:d8:f7:de:60:21:90:9e:c5:dc:5c:7b:7f:62:
83:52:23:56:48:04:28:a9:45:0f:41:67:e4:ae:bf:
b3:47:0a:9d:ec:3a:05:8d:e3:de:d5:4a:97:b2:ae:
d6:5c:11:49:a3:a6:ff:16:87:ca:04:46:5e:79:4a:
e1:7a:fa:2a:98:2e:ac:3e:ec:b5:b7:5c:d8:08:a3:
b5:ef:0d:2c:62:9e:93:63:41:01:8d:bd:ae:b4:9c:
4c:52:91:ef:9e:23:be:7a:d7:56:35:bd:b0:07:e5:
3f:12:b5:a8:5f:30:e9:15:56:d2:69:4f:de:c6:19:
47:01:17:b1:62:fa:8d:04:32:5b:db:4a:b3:64:dd:
7e:7f:f9:86:f5:7e:40:71:f5:1b:1e:a8:a1:dd:77:
12:30:e6:f2:66:12:7d:3a:c8:1d:8d:d4:f5:57:f2:
60:a2:65:fe:b9:e0:a3:f1:e5:72:c4:6c:c4:8d:8f:
51:d5:4b:a3:46:a7:51:a3:0c:01:f5:73:e2:dd:63:
bb:10:bb:37:a9:19:3b:7b:60:1b:a5:6d:5c:84:3f:
e7:36:e6:db:2a:14:d8:19:04:67:40:07:29:ea:ad:
03:74:48:3f:5c:0a:60:57:9f:1a:a5:a9:42:29:c4:
32:6d:fb:3c:5d:2d:ee:50:55:a8:62:36:fc:37:a9:
d9:18:cb:28:7e:03:a6:fa:f8:f1:87:70:c5:15:75:
5d:10:a8:17:0a:f4:18:df:b6:0e:48:9b:6d:2c:24:
f1:50:e4:07:1c:cc:67:ff:b7:16:7e:01:9a:de:76:
95:01:52:b2:3d:56:7f:7f:5a:7d:0c:2a:18:33:78:
43:ad:cd:2d:0a:d4:52:04:41:fc:4c:64:7d:47:2c:
b5:65:95:22:ae:6b:33:f2:6d:e2:cf:a0:3c:8c:d7:
30:bd:44:a0:50:34:f4:f7:47:74:2a:c6:e4:d6:7b:
2b:99:fb:cc:de:32:9a:28:60:ac:99:c2:7c:c1:fc:
ec:55:1a:a4:0f:7b:da:f8:94:8f:2c:e2:74:df:22:
5b:93:a0:f1:8c:81:20:9c:02:12:d4:58:48:22:1c:
6d:ea:91:29:b1:7c:90:47:af:01:2a:bc:ff:38:dc:
2c:49:48:20:8c:57:31:c4:be:53:d7:68:9c:7c:1c:
66:2b:6f


publicExponent: 65537 (0x10001)

privateExponent:

58:48:58:fa:7c:a7:47:dd:01:c9:58:28:53:69:6c:
b7:2d:5e:21:63:50:54:6d:e2:b5:f9:d6:bb:15:7a:
a6:6a:18:86:ee:ea:52:40:d6:07:1b:c9:69:a9:84:
57:f8:fa:8e:e6:6d:89:a8:4e:eb:65:5d:20:45:88:
ee:c4:00:8e:d3:c6:85:08:a1:e0:bd:93:e2:65:72:
83:5f:e1:5d:f9:bb:43:90:ab:44:96:aa:d0:80:a4:
d5:55:e2:35:d0:3d:27:0d:d5:e9:dc:92:63:c4:1e:
f8:93:06:e7:44:98:78:86:e8:1e:9f:30:c0:60:09:
6f:a8:ff:7c:aa:50:15:40:6b:33:6e:94:b7:10:ed:
1a:93:a0:a2:7c:c4:52:2d:63:02:ab:3e:e2:30:23:
0f:b1:16:2d:a8:c0:00:83:ee:ee:6d:66:af:94:33:
4c:0a:93:e1:de:19:a4:d1:b7:a0:dd:94:e8:9b:1f:
b5:88:fb:0b:5e:2d:20:03:48:b4:54:ac:d9:46:c9:
ee:75:8e:75:ba:56:91:7d:3b:ea:45:7a:ea:16:bc:
7b:be:49:dc:2c:b6:9f:1e:8a:03:e4:3d:b5:61:28:
a5:52:c8:18:b7:a7:d4:a4:f0:78:47:78:83:ff:d0:
c9:ac:ec:38:6f:1b:d4:0b:86:0d:07:e1:8e:67:a7:
7b:4f:18:a9:8a:33:31:42:21:8e:fa:f9:cc:65:fc:
c4:41:b7:87:4e:67:bc:4b:ca:bc:77:82:77:cb:ce:
37:d1:db:58:88:7e:01:3e:0e:c5:63:69:98:cf:26:
7b:85:97:f1:0e:45:e2:1f:00:51:33:3c:fa:d9:bf:
cf:cc:5a:48:35:94:65:7d:2b:8d:e1:8c:30:1a:e5:
20:0f:3e:cf:7c:3d:e1:17:e4:e4:9e:5f:08:f8:94:
3f:2a:1c:81:3c:78:0a:3d:91:ed:c4:d2:4f:61:83:
00:5e:59:cf:5b:f3:b1:5a:18:76:e5:23:bf:15:27:
d7:25:52:90:ae:6e:02:d2:25:2b:e7:82:fd:39:3a:
64:74:26:f4:b8:52:39:d4:d7:51:42:17:23:ab:c3:
0e:87:e6:f7:01:ef:2f:21:15:e8:bc:8e:34:d8:66:
df:ad:2c:17:8a:44:61:b0:1e:6f:e4:5a:f7:8b:24:
b9:12:81:61:46:c3:47:a0:71:b3:29:d5:3c:c1:c8:
8b:6b:c6:31:0a:ea:6a:f0:e7:ca:cb:e8:2f:1d:ea:
3a:af:58:9e:10:23:0f:ce:f2:30:56:8a:53:5e:6a:
60:58:dc:0b:fb:3d:6a:06:ba:6d:71:83:9c:ae:73:
21:3a:92:f8:88:d3:26:36:ef:7f:f6:3c:bc:07:33:
71:e1

prime1:

00:e9:a3:3e:4d:33:1a:b4:23:91:7a:cf:f9:c5:73:
ee:2c:bb:bf:30:e2:40:ad:34:e5:b7:97:56:50:9d:
19:b0:cd:be:4b:a4:a3:eb:f6:18:fe:3d:cb:e1:eb:
a7:85:f5:67:14:73:26:5c:31:d4:20:b4:b4:c2:65:
ca:a0:07:6d:ba:3b:9f:23:42:c3:78:51:9e:78:13:
cc:76:33:7c:16:7d:12:3e:5f:61:20:94:b2:f8:e7:
01:d8:0d:6c:f9:33:f9:79:44:bb:dc:70:aa:5d:2b:
7b:19:c2:68:5c:aa:62:97:bb:cb:c9:e6:e2:bd:a3:
fb:80:3b:44:34:ed:07:a3:95:ea:be:82:26:d8:a3:
cb:64:0a:ea:82:78:d4:55:4c:6e:e9:a9:fc:39:1c:
32:ef:29:6d:6d:a2:48:3e:ef:4e:1e:0a:19:6a:17:
f6:24:0f:c1:cb:7a:c6:45:c9:b0:b0:3e:78:44:60:
55:5b:f3:ca:99:8a:18:3f:a7:ae:f7:09:53:e4:4e:
eb:e7:d5:19:de:32:ea:b1:bf:50:3a:14:33:58:93:
71:e6:63:59:d7:0b:8e:c2:d9:5d:54:81:a1:35:e1:
e3:0d:07:23:b2:9c:0c:0d:db:f9:51:31:04:45:8f:
9c:b4:aa:13:fb:6e:3a:67:17:59:6f:a1:f7:48:20:
80:33

prime2:

00:c1:f7:11:32:32:de:c5:f0:fd:f5:0e:b2:1e:38:
c4:a3:e2:63:1c:05:0e:0e:8c:d4:2e:b6:ad:ce:a8:
ac:03:9d:fd:e1:66:42:f7:6b:74:67:54:1a:96:d6:
ec:d7:30:bf:1e:29:b8:31:b0:a4:43:bb:ef:54:9d:
a9:6e:dd:ad:10:68:52:40:f5:16:cb:3e:b7:17:39:
6a:a0:18:93:ce:cb:3f:f0:41:68:4c:f6:f6:1e:1d:
b5:58:9b:e7:49:0d:a3:8d:ce:61:3c:ef:00:83:4c:
22:29:ae:f6:bf:bc:01:75:9f:ad:81:67:10:cc:f8:
52:02:22:d5:e8:77:9b:96:21:a3:b7:ba:3a:e5:8e:
8b:ab:1e:9c:44:a2:9f:cf:fa:ba:68:fe:cb:fa:78:
40:71:1b:91:b0:ba:db:16:81:62:f9:3a:ae:06:55:
e7:15:71:b8:c0:8b:7c:72:2c:0f:1a:db:69:39:cc:
b5:23:3a:63:e5:79:18:46:eb:22:a9:0c:0d:12:e7:
0f:1f:0e:c5:dc:1a:1d:06:19:8d:9d:1b:50:39:7e:
c0:5f:83:d9:0d:c4:38:4f:78:21:92:3e:ab:f1:4f:
9a:56:03:7f:ba:27:12:75:d7:de:55:65:63:69:37:
42:aa:8d:39:12:a4:2f:af:93:08:f8:b8:f5:46:31:
7b:d5
```

#### •  What part of the certificate indicates this is a CA’s certificate?

Sabemos que é um certificado CA, pois ``` CA = True ```

```py
            X509v3 Basic Constraints: critical
                CA:TRUE
```

#### •  What part of the certificate indicates this is a self-signed certificate?

O certificado é self-signed pois o subject e a authority key identifier são iguais.

```py
        X509v3 extensions:
            X509v3 Subject Key Identifier:
                46:EB:AF:9D:50:47:7D:DA:19:29:61:C3:51:91:50:6D:C7:F8:05:A7
            X509v3 Authority Key Identifier:
                keyid:46:EB:AF:9D:50:47:7D:DA:19:29:61:C3:51:91:50:6D:C7:F8:05:A7
```

#### •  In the RSA algorithm, we have a public exponente, a private exponent d, a modulus n, and two secret numbers p and q, such that n=pq.  Please identify the values for these elements in your certificateand key files

Esses valores: ("modulus", "publicExponent", "privateExponent", "prime1" e "prime2") estão presentes no output do ```openssl rsa -in ca.key -text -noout``` como vimos anteriormente.

Podemos verificar que é possível visualizar o "publicExponent" (65537) tanto no ficheiro da chave como no ficheiro do certificado.

No entanto, o valor do "privateExponent" e dos números "prime1" e "prime2" apenas estão presentes no ficheiro da chave.

* Modulus:
```py
 Modulus:
                    00:b1:05:8e:2a:f7:75:ee:6d:0a:db:d4:26:90:72:
                    4b:42:97:de:47:61:bb:92:94:9f:d0:99:fe:78:d7:
                    b9:09:37:8a:54:d6:8f:50:63:11:93:6c:60:2a:01:
                    6c:f2:79:c4:f9:05:64:6a:11:4c:81:9d:a0:7c:97:
                    15:8e:bf:8c:59:c3:93:0a:1c:f0:d0:c7:ec:73:1e:
                    35:a4:d8:f7:de:60:21:90:9e:c5:dc:5c:7b:7f:62:
                    83:52:23:56:48:04:28:a9:45:0f:41:67:e4:ae:bf:
                    b3:47:0a:9d:ec:3a:05:8d:e3:de:d5:4a:97:b2:ae:
                    d6:5c:11:49:a3:a6:ff:16:87:ca:04:46:5e:79:4a:
                    e1:7a:fa:2a:98:2e:ac:3e:ec:b5:b7:5c:d8:08:a3:
                    b5:ef:0d:2c:62:9e:93:63:41:01:8d:bd:ae:b4:9c:
                    4c:52:91:ef:9e:23:be:7a:d7:56:35:bd:b0:07:e5:
                    3f:12:b5:a8:5f:30:e9:15:56:d2:69:4f:de:c6:19:
                    47:01:17:b1:62:fa:8d:04:32:5b:db:4a:b3:64:dd:
                    7e:7f:f9:86:f5:7e:40:71:f5:1b:1e:a8:a1:dd:77:
                    12:30:e6:f2:66:12:7d:3a:c8:1d:8d:d4:f5:57:f2:
                    60:a2:65:fe:b9:e0:a3:f1:e5:72:c4:6c:c4:8d:8f:
                    51:d5:4b:a3:46:a7:51:a3:0c:01:f5:73:e2:dd:63:
                    bb:10:bb:37:a9:19:3b:7b:60:1b:a5:6d:5c:84:3f:
                    e7:36:e6:db:2a:14:d8:19:04:67:40:07:29:ea:ad:
                    03:74:48:3f:5c:0a:60:57:9f:1a:a5:a9:42:29:c4:
                    32:6d:fb:3c:5d:2d:ee:50:55:a8:62:36:fc:37:a9:
                    d9:18:cb:28:7e:03:a6:fa:f8:f1:87:70:c5:15:75:
                    5d:10:a8:17:0a:f4:18:df:b6:0e:48:9b:6d:2c:24:
                    f1:50:e4:07:1c:cc:67:ff:b7:16:7e:01:9a:de:76:
                    95:01:52:b2:3d:56:7f:7f:5a:7d:0c:2a:18:33:78:
                    43:ad:cd:2d:0a:d4:52:04:41:fc:4c:64:7d:47:2c:
                    b5:65:95:22:ae:6b:33:f2:6d:e2:cf:a0:3c:8c:d7:
                    30:bd:44:a0:50:34:f4:f7:47:74:2a:c6:e4:d6:7b:
                    2b:99:fb:cc:de:32:9a:28:60:ac:99:c2:7c:c1:fc:
                    ec:55:1a:a4:0f:7b:da:f8:94:8f:2c:e2:74:df:22:
                    5b:93:a0:f1:8c:81:20:9c:02:12:d4:58:48:22:1c:
                    6d:ea:91:29:b1:7c:90:47:af:01:2a:bc:ff:38:dc:
                    2c:49:48:20:8c:57:31:c4:be:53:d7:68:9c:7c:1c:
                    66:2b:6f
                Exponent: 65537 (0x10001)
```

* Exponents:
```py
publicExponent: 65537 (0x10001)
privateExponent:
    58:48:58:fa:7c:a7:47:dd:01:c9:58:28:53:69:6c:
    b7:2d:5e:21:63:50:54:6d:e2:b5:f9:d6:bb:15:7a:
    a6:6a:18:86:ee:ea:52:40:d6:07:1b:c9:69:a9:84:
    57:f8:fa:8e:e6:6d:89:a8:4e:eb:65:5d:20:45:88:
    ee:c4:00:8e:d3:c6:85:08:a1:e0:bd:93:e2:65:72:
    83:5f:e1:5d:f9:bb:43:90:ab:44:96:aa:d0:80:a4:
    d5:55:e2:35:d0:3d:27:0d:d5:e9:dc:92:63:c4:1e:
    f8:93:06:e7:44:98:78:86:e8:1e:9f:30:c0:60:09:
    6f:a8:ff:7c:aa:50:15:40:6b:33:6e:94:b7:10:ed:
    1a:93:a0:a2:7c:c4:52:2d:63:02:ab:3e:e2:30:23:
    0f:b1:16:2d:a8:c0:00:83:ee:ee:6d:66:af:94:33:
    4c:0a:93:e1:de:19:a4:d1:b7:a0:dd:94:e8:9b:1f:
    b5:88:fb:0b:5e:2d:20:03:48:b4:54:ac:d9:46:c9:
    ee:75:8e:75:ba:56:91:7d:3b:ea:45:7a:ea:16:bc:
    7b:be:49:dc:2c:b6:9f:1e:8a:03:e4:3d:b5:61:28:
    a5:52:c8:18:b7:a7:d4:a4:f0:78:47:78:83:ff:d0:
    c9:ac:ec:38:6f:1b:d4:0b:86:0d:07:e1:8e:67:a7:
    7b:4f:18:a9:8a:33:31:42:21:8e:fa:f9:cc:65:fc:
    c4:41:b7:87:4e:67:bc:4b:ca:bc:77:82:77:cb:ce:
    37:d1:db:58:88:7e:01:3e:0e:c5:63:69:98:cf:26:
    7b:85:97:f1:0e:45:e2:1f:00:51:33:3c:fa:d9:bf:
    cf:cc:5a:48:35:94:65:7d:2b:8d:e1:8c:30:1a:e5:
    20:0f:3e:cf:7c:3d:e1:17:e4:e4:9e:5f:08:f8:94:
    3f:2a:1c:81:3c:78:0a:3d:91:ed:c4:d2:4f:61:83:
    00:5e:59:cf:5b:f3:b1:5a:18:76:e5:23:bf:15:27:
    d7:25:52:90:ae:6e:02:d2:25:2b:e7:82:fd:39:3a:
    64:74:26:f4:b8:52:39:d4:d7:51:42:17:23:ab:c3:
    0e:87:e6:f7:01:ef:2f:21:15:e8:bc:8e:34:d8:66:
    df:ad:2c:17:8a:44:61:b0:1e:6f:e4:5a:f7:8b:24:
    b9:12:81:61:46:c3:47:a0:71:b3:29:d5:3c:c1:c8:
    8b:6b:c6:31:0a:ea:6a:f0:e7:ca:cb:e8:2f:1d:ea:
    3a:af:58:9e:10:23:0f:ce:f2:30:56:8a:53:5e:6a:
    60:58:dc:0b:fb:3d:6a:06:ba:6d:71:83:9c:ae:73:
    21:3a:92:f8:88:d3:26:36:ef:7f:f6:3c:bc:07:33:
    71:e1
```
* Prime1:

```py
prime1:
    00:e9:a3:3e:4d:33:1a:b4:23:91:7a:cf:f9:c5:73:
    ee:2c:bb:bf:30:e2:40:ad:34:e5:b7:97:56:50:9d:
    19:b0:cd:be:4b:a4:a3:eb:f6:18:fe:3d:cb:e1:eb:
    a7:85:f5:67:14:73:26:5c:31:d4:20:b4:b4:c2:65:
    ca:a0:07:6d:ba:3b:9f:23:42:c3:78:51:9e:78:13:
    cc:76:33:7c:16:7d:12:3e:5f:61:20:94:b2:f8:e7:
    01:d8:0d:6c:f9:33:f9:79:44:bb:dc:70:aa:5d:2b:
    7b:19:c2:68:5c:aa:62:97:bb:cb:c9:e6:e2:bd:a3:
    fb:80:3b:44:34:ed:07:a3:95:ea:be:82:26:d8:a3:
    cb:64:0a:ea:82:78:d4:55:4c:6e:e9:a9:fc:39:1c:
    32:ef:29:6d:6d:a2:48:3e:ef:4e:1e:0a:19:6a:17:
    f6:24:0f:c1:cb:7a:c6:45:c9:b0:b0:3e:78:44:60:
    55:5b:f3:ca:99:8a:18:3f:a7:ae:f7:09:53:e4:4e:
    eb:e7:d5:19:de:32:ea:b1:bf:50:3a:14:33:58:93:
    71:e6:63:59:d7:0b:8e:c2:d9:5d:54:81:a1:35:e1:
    e3:0d:07:23:b2:9c:0c:0d:db:f9:51:31:04:45:8f:
    9c:b4:aa:13:fb:6e:3a:67:17:59:6f:a1:f7:48:20:
    80:33
```

* Prime2:

```py
prime2:
    00:c1:f7:11:32:32:de:c5:f0:fd:f5:0e:b2:1e:38:
    c4:a3:e2:63:1c:05:0e:0e:8c:d4:2e:b6:ad:ce:a8:
    ac:03:9d:fd:e1:66:42:f7:6b:74:67:54:1a:96:d6:
    ec:d7:30:bf:1e:29:b8:31:b0:a4:43:bb:ef:54:9d:
    a9:6e:dd:ad:10:68:52:40:f5:16:cb:3e:b7:17:39:
    6a:a0:18:93:ce:cb:3f:f0:41:68:4c:f6:f6:1e:1d:
    b5:58:9b:e7:49:0d:a3:8d:ce:61:3c:ef:00:83:4c:
    22:29:ae:f6:bf:bc:01:75:9f:ad:81:67:10:cc:f8:
    52:02:22:d5:e8:77:9b:96:21:a3:b7:ba:3a:e5:8e:
    8b:ab:1e:9c:44:a2:9f:cf:fa:ba:68:fe:cb:fa:78:
    40:71:1b:91:b0:ba:db:16:81:62:f9:3a:ae:06:55:
    e7:15:71:b8:c0:8b:7c:72:2c:0f:1a:db:69:39:cc:
    b5:23:3a:63:e5:79:18:46:eb:22:a9:0c:0d:12:e7:
    0f:1f:0e:c5:dc:1a:1d:06:19:8d:9d:1b:50:39:7e:
    c0:5f:83:d9:0d:c4:38:4f:78:21:92:3e:ab:f1:4f:
    9a:56:03:7f:ba:27:12:75:d7:de:55:65:63:69:37:
    42:aa:8d:39:12:a4:2f:af:93:08:f8:b8:f5:46:31:
    7b:d5
```

## Task 2: Generating a Certificate Request for Your Web Server

Neste exercicio vamos criar um Certificate Signing Request (CSR), sendo gerado pelo CA que criamos na Task 1.

* Usamos o seguinte comando:

```py
openssl req -newkey rsa:2048 -sha256  \
            -keyout server.key   -out server.csr  \
            -subj "/CN=www.bank32.com/O=Bank32 Inc./C=US" \
            -passout pass:dees
```

<img width="1674" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/beb2275a-416d-48a5-8b91-f6b4087af819">

Como pedido no enunciado, devemos adicionar nomes alternativos, pois muitos sites têm URLs diferentes que fazem parte do mesmo "servidor":

* **Nota:** Este comando vai criar dois arquivos no nosso dirétorio (```server.crs``` e ```server.key```) e também vai gerar um par de chaves públicas e privadas. Em seguida vai criar então uma solicitação de CSR a partir da chave pública.

```py
openssl req -newkey rsa:2048 -sha256  \
            -keyout server.key -out server.csr  \
            -subj "/CN=www.bank32.com/O=Bank32 Inc./C=US"  \
            -passout pass:dees  \
            -addext "subjectAltName = DNS:www.bank32.com, DNS:www.bank32A.com, DNS:www.bank32B.com"

```

<img width="1672" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/bdd98ab7-eeff-469a-a39b-ebac2593eb3a">


Usamos os seguinte comandos para **examinar o conteúdo decodificado do CSR** e dos arquivos da chave privada:

````py
openssl req -in server.csr -text -noout
openssl rsa -in server.key -text -noout
````

<img width="746" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/2069eb0d-1805-442a-a93f-1434726586d9">

```py
[06/04/23]seed@VM:~/.../Crypto_PKI$ openssl rsa -in server.key -text -noout
Enter pass phrase for server.key:
RSA Private-Key: (2048 bit, 2 primes)
modulus:
    00:bb:27:79:53:6d:89:93:cd:d4:f1:c1:ff:7a:53:
    77:be:81:01:df:92:7c:53:cb:d9:9f:4b:eb:4e:50:
    84:2d:0d:62:19:5b:53:f3:d1:44:5b:15:d3:15:d9:
    1a:80:a1:97:8b:73:aa:31:b1:7f:e3:56:17:04:21:
    ac:15:ab:bb:7f:a7:0c:cd:e7:34:c4:7a:d6:ab:4f:
    13:a4:6b:da:dd:53:55:07:60:43:66:13:f0:4f:ea:
    16:c4:f1:7a:51:77:32:e5:bc:bf:a2:ee:5f:6e:33:
    f4:b6:a8:34:bc:ef:93:c4:e8:7c:28:5f:54:ab:77:
    10:90:0a:8a:58:f3:4b:bb:9b:df:c4:ce:47:83:55:
    d3:ad:73:b5:9e:50:4b:43:45:5d:af:fb:47:f7:ff:
    91:8e:c8:4d:d9:fd:84:08:4d:c8:91:94:77:71:db:
    1c:b0:a2:70:cd:9a:36:26:6b:73:a9:f3:1d:dc:be:
    58:cb:9b:28:59:df:8b:99:7e:9b:9e:58:7a:36:92:
    29:99:1a:d8:e4:ae:a3:80:6d:cb:d8:81:4b:e9:d1:
    64:16:c7:ba:a7:d9:36:c4:a3:9f:15:d8:98:33:72:
    43:fa:c2:17:35:6c:c9:f2:30:78:73:6e:46:4f:7e:
    d7:23:60:93:0b:a9:a5:d2:f9:a1:56:62:b1:f3:32:
    4c:77
publicExponent: 65537 (0x10001)
privateExponent:
    27:78:b5:cf:f0:a4:39:76:09:d9:4b:2f:14:9f:91:
    fb:ad:bd:b5:67:71:ad:42:ab:0d:3b:b7:ce:f6:90:
    49:e8:2e:ae:66:62:98:63:a4:65:09:7f:51:76:4e:
    6e:9e:a6:15:95:39:69:ed:a3:a9:50:b8:dd:f8:34:
    11:05:fd:2f:79:0d:ec:47:3d:0b:cb:54:87:20:d0:
    65:b7:11:9b:e8:3d:60:a6:de:d0:22:98:66:62:5a:
    97:02:ce:e7:6b:9a:62:75:a2:7d:3c:85:07:fb:11:
    3b:8c:d2:42:9e:cc:ad:94:d2:ca:b9:00:64:81:62:
    0e:df:0a:3a:a4:65:6e:95:9e:59:1c:cf:8f:bb:d0:
    58:99:6a:6e:40:0a:2b:34:c7:f7:69:ae:a9:e0:b4:
    8d:3d:f4:5c:60:d2:c2:56:c2:4e:ca:e5:05:77:c6:
    ed:a0:b7:45:a5:cc:9e:66:5c:d0:e6:82:7c:82:8c:
    fe:78:c4:a7:12:88:aa:35:42:69:22:c3:94:29:34:
    98:da:01:53:07:79:e4:16:e5:3a:89:a2:97:ac:4f:
    b1:04:8b:45:51:69:fe:ec:3d:6b:4d:e5:50:c0:d0:
    91:8a:47:e6:9f:af:4f:80:bd:c6:90:30:70:8e:79:
    d2:dd:2c:9f:99:67:bc:cb:d2:e6:52:d2:ed:21:b1:
    f1
prime1:
    00:f8:03:17:bb:cb:02:d0:5e:77:da:79:19:2f:a5:
    a1:76:b0:52:0a:61:77:bd:c4:35:3f:18:e4:05:3d:
    bf:b8:22:50:ab:00:41:04:69:94:03:7e:04:a3:9c:
    0f:e6:96:93:3a:33:f8:e2:91:91:b4:55:ca:cc:c4:
    1d:b6:e7:6b:cf:c0:38:24:10:4d:a2:38:97:e8:67:
    23:95:53:53:25:28:11:ae:40:40:75:85:6b:d0:13:
    e4:6a:73:f3:1d:d2:56:f4:f8:71:d6:b1:65:75:94:
    7d:8c:08:be:cd:6b:56:91:8f:fe:e5:68:80:b5:3b:
    0c:32:d7:a9:fa:0b:8f:4f:5b
prime2:
    00:c1:2e:98:a3:dc:90:34:9a:b3:f0:0b:20:f2:e2:
    13:b6:2c:57:3a:30:31:b2:1e:e9:1d:4e:48:84:9f:
    55:db:e1:38:d6:66:c5:50:e3:ad:9e:59:28:8d:3d:
    5d:87:62:82:76:11:a7:fc:3a:27:07:7c:13:90:a0:
    be:1e:1f:79:31:05:2c:2f:a6:89:16:de:e5:69:0e:
    d4:51:d4:bb:39:96:51:85:5c:a7:90:d0:8d:0c:4c:
    fc:c3:83:6c:56:82:a0:ac:7f:5a:56:80:8d:e7:e2:
    45:cf:59:f1:63:9d:76:a5:7d:9e:82:e9:c3:1f:5f:
    d0:fd:1b:02:2f:f5:c6:7e:15
exponent1:
    00:e7:9a:73:c2:72:3d:a9:7a:5e:b0:8d:e0:00:47:
    cb:75:bc:08:91:1b:1e:27:ff:9f:bd:d1:af:b6:59:
    48:bd:5a:86:3c:7a:5b:3d:14:9f:1d:77:c4:3b:49:
    54:eb:ff:f7:73:25:ef:a9:1d:49:94:bf:7d:48:25:
    68:9e:52:94:b2:88:8d:a4:d7:f8:b7:a1:e3:f2:2a:
    c6:e6:fe:ce:29:67:b6:c3:23:cb:4e:34:0f:4f:5c:
    14:35:79:1c:32:e0:27:46:52:f0:74:0e:6b:72:16:
    fd:fb:14:7b:a1:f7:37:fb:6d:1e:1a:fb:b1:1e:0d:
    0b:42:3b:75:c7:44:9e:4a:fb
exponent2:
    60:55:45:26:c9:71:5b:da:1d:8a:c1:71:ef:cc:8f:
    39:d4:08:b7:6a:9b:0d:90:de:7c:8f:b2:17:f8:80:
    cf:42:13:9e:ce:e6:ec:7c:6c:f2:be:d1:3b:05:73:
    e3:74:5b:4c:57:67:a6:9e:b5:21:c5:5c:d8:4d:60:
    21:13:5e:d2:f4:1a:61:b4:b1:3e:27:6e:cd:21:e8:
    fc:d9:91:77:99:1f:13:da:ed:70:88:9f:1d:98:32:
    9f:a8:a4:d8:cb:11:26:93:e7:4f:a5:91:9e:25:b6:
    dc:3c:a4:e4:20:fc:ae:6f:e3:20:b3:43:6b:1c:d3:
    d1:b3:ab:36:91:60:27:35
coefficient:
    33:23:98:2f:b3:d6:24:c2:9c:db:e0:41:5c:c0:53:
    29:00:0b:1f:c0:ad:55:22:c8:41:28:bc:63:36:08:
    f3:b5:0f:f0:fb:e1:24:3d:8c:63:56:63:f0:50:38:
    71:55:c5:ff:8b:53:a7:2e:d3:94:fc:1d:e6:42:80:
    30:35:81:a5:8e:d4:53:2d:8a:3f:e7:72:15:2a:39:
    61:21:ed:f8:07:85:b5:a9:12:fd:e9:14:31:b3:3f:
    58:f6:8e:69:c6:0e:3f:e1:e8:0b:d3:bc:cc:d0:85:
    66:c9:4e:4b:8c:a8:09:56:d1:a5:3a:2e:3c:81:30:
    ad:ba:40:1f:8c:0d:14:69
```

## Task 3: Generating a Certificate for your server

Nesta tarefa, geramos o certificado solicitado pelo CSR criado na tarefa anterior.

Para isso:

1. Modificamos o arquivo `openssl.cnf` e descomentamos a linha que contém o ``copy_extensions```:

   ![image](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/2b3ff8d9-f159-4267-bb7e-59a9a36be33d)

2. Em seguida, transformamos o **CSR** (Certificate Signing Request) em um certificado **X509**:

   ![image](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/898197b1-8d6b-4e40-985a-a12ecc4d0762)

3. Com o certificado X509 gerado, verificamos o seu conteúdo para garantir que os nomes "alternativos" adicionados na tarefa anterior estão presentes. Isso confirma que a modificação do arquivo `openssl.cnf` foi aplicada corretamente.

   ![image](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/c0466f4c-5b28-4e65-b6a4-e1c47978bc88)

## Task 4: Deploying Certificate in an Apache-Based HTTPS Website

Nesta tarefa, vamos ver como os certificados de chave pública são usados por sites para proteger a "navegação" web, começando por configurar um site HTTPS baseado no Apache.

Começamos por configurar o nosso arquivo ```bank32_apache_ssl.conf```, que é responsável por definir o diretório onde os arquivos de cada site estão armazenados no servidor Apache e os nossos hosts.

<img width="1207" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/bb468944-dce6-4739-acf8-f47a89189a77">


* Desta forma, garantimos que o servidor sabe como gerir múltiplos sites em simultâneo.

De seguida, precisamos de configurar o nosso site:

1. Inicialmente, utilizamos o comando `docker ps` para mostrar todos os containers em execução.

2. Em seguida, executamos o comando `docksh <container_id>`, substituindo `<container_id>` pelo ID do container encontrado no passo anterior. Com este comando, acedemos à shell dentro do container.

3. Dentro do container, habilitamos o módulo SSL do Apache e ativamos o site como pedido no enunciado.

<img width="886" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/2f4b5a12-2ef3-44f1-9611-748fadf0bebf">

* Quando acedemos ao nosso website , o navegador exibe um erro que o nosso website está a ser reconhecido por uma CA não confiavel, uma vez que ele é self-signed:

<img width="896" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/c7194314-7933-45bb-b439-faf5211cd071">
<img width="783" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/ba5b8854-8e6d-440e-93f5-7be7a3bbb221">

* Como dito no enunciado, para corrigir esse aviso adicionamos manualmente a nossa CA na lista de CAs confíaveis no Firefox:

<img width="898" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/6a765ea0-66d2-4be2-9904-132203d2c897">

* Após inserirmos, conseguimos verificar que já temos acesso ao nosso website:

<img width="887" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/f8b5e4f8-1083-42e0-8408-0df8c6fa84a0">

## Task 5: Launching a Man-In-The-Middle Attack

Nesta tarefa, mostraremos como a PKI pode derrotar ataques Man-In-The-Middle (MITM).

Primeiro, selecionamos o site `www.zara.com` como alvo e configuramos o nosso servidor para se passar por esse site. Modificámos o nosso arquivo `bank32_apache_ssl.conf` e alteramos o **ServerName** para `www.zara.com`.

![Configuração do ServerName](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/3f0202e3-8e73-407a-b412-94457fa94f7b)

Em seguida, editamos o arquivo `/etc/hosts` e criamos uma entrada associando o nome de domínio `www.zara.com` a um endereço IP específico.

![Edição do arquivo /etc/hosts](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/b1e6cfe8-9980-4f10-832e-d7225ae932b2)

* Reiniciamos o nosso APACHE , utilizando o comando `sudo service apache2 restart`.

Ao tentar aceder ao site `www.zara.com`, recebemos um erro de certificado:

![Erro de certificado](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/4c905b78-d306-46f2-8372-431959eb4dd8)

Este erro ocorre porque estamos a tentar aceder ao site utilizando um certificado que não é válido para o domínio em questão. O nosso certificado é válido apenas para os seguintes sites:

- www.bank32.com
- www.bank32A.com
- www.bank32B.com

Como o nosso certificado não corresponde ao domínio `www.zara.com`, o navegador (neste caso, Firefox) não confia no site e exibe um erro. Isso indica que o nosso ataque MITM não teve sucesso.

## Task 6: Becoming a Certificate Authority (CA)

Nesta tarefa, exploramos um cenário em que a Autoridade Certificadora (CA) raiz é comprometida e sua chave privada é roubada. Vamos fazer um ataque MITM bem-sucedidos num sites HTTPS, sem levantar suspeitas no navegador da vítima.

Primeiramente, criamos o certificado para o site alvo, no caso utilizamos o site utilizado no exercicio anterior, ```zara.com```.

Utilizamos o comando que executamos da Tarefa 2 para criar o nosso certificado, temos que trocar a parte de  "www.bank32.com" pelo nosso site alvo "www.zara.com".

<img width="979" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/41d8d549-346e-461e-8eee-03cb5d1963e2">

De seguida, assinamos o nosso certificado:

<img width="1265" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/745fa50e-269a-41f2-8d60-f5c0e9ae0dfe">

* Como geramos o novo certificado (zara_server.crt) e possuimos a chave privada (zara_server.key), precisamos copiá-los para a pasta image_www/certs para substituir os arquivos de certificado usados na tarefa anterior e executamos os seguintes comandos:

<img width="788" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/514389b3-c148-4d32-b9de-b6349cc3be00">

* Tivemos também que modificar o ficheiro ```Dockerfile```:

<img width="814" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/fd53de62-af22-47ab-bc99-bd807a2050ae">

* Depois de reiniciar o nosso docker container e inicializar o nosso apache, conseguimos entrar no nosso site e realizar com sucesso o ataque MITM:

<img width="1261" alt="image" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/42e75c44-0869-4e11-8d3a-6b76515c5b3b">
