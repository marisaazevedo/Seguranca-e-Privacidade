###  Task 1
 ```O objetivo desta tarefa, é tornarmo-nos uma Certificate Authority (CA) para podermos emitir um certificado digital para terceiros.```
 
 Começamos por copiar o openssl.cnf para o nosso diretório para que pudéssemos fazer as alterações necessárias no mesmo e como pedido no guião tiramos o comentário no parametro 'unique_subject'.
 
 ![uncomment](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/2bf9ebce-a6ac-4ca3-b3ba-d05488b85043)

Após isto, criamos a pasta 'demoCA' e adicionamos os arquivos necessários de acordo com o guião.

![demoCAfiles](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/47957b2c-3942-4ff3-8d69-d12ccd820eaa)

Após a configuração inicial, precisamos gerar um certificado self-signed para a nossa CA:

![create_certificate](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/ff8aee23-1508-471b-81d2-af720aab8e5d)

Podemos usar os seguintes comandos para ver o conteúdo decodificado do certificado X509 e a chave RSA:

 ```openssl x509 -in ca.crt -text -noout``` 
 
 ![view_publickey1](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/8d165e66-28e1-4fc7-bcdf-6f535c3a79a3)
 
 ![view_publickey2](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/2e091b0a-fd64-46e1-a1ce-09a9f0c12d62)

 ```openssl rsa  -in ca.key -text -noout```
 
![view_privatekey1](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/6525841a-bae6-49e3-92fe-551cd177fc28)

![view_privatekey2](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/f5ef4805-9e07-4242-9ede-ccaf780a00aa)

![view_privatekey3](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/bedfa333-4a78-4d44-a49b-fc743b4b88f1)

#### •  What part of the certificate indicates this is a CA’s certificate?
Sabemos que é um certificado CA, pois ``` CA = True ```

![proofCAcert](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/269f7b18-f404-463f-8937-3a753101fa3c)

#### •  What part of the certificate indicates this is a self-signed certificate?
O certificado é self-signed pois o subject e a authority key identifier são iguais. 

![proof_selsigncert](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/d0c42aca-830e-4daa-9b02-7f78e93393e4)

#### •  In the RSA algorithm, we have a public exponente, a private exponent d, a modulus n, and two secret numbers p and q, such that n=pq.  Please identify the values for these elements in your certificateand key files
Esses valores: ("modulus", "publicExponent", "privateExponent", "prime1" e "prime2") estão presentes no output do ```openssl rsa -in ca.key -text -noout``` como vimos anteriormente.

Podemos verificar que é possível visualizar o "publicExponent" (65537) tanto no ficheiro da chave como no ficheiro do certificado.

No entanto, o valor do "privateExponent" e dos números "prime1" e "prime2" apenas estão presentes no ficheiro da chave.

**n = "modulus"**

**p = "prime1"**

**q = "prime2"**

Modulus | Exponents
:---------:|:---------:
<img width="518" alt="Screenshot 2023-05-30 at 11 49 48" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/7f9eba9f-1fca-4d76-b211-dba1a1b5ad13"> | <img width="391" alt="Screenshot 2023-05-30 at 11 50 30" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/ecd2e87a-495d-45b1-8204-eb7a43aa3b4a">

Prime1 | Prime2
:--------:|:--------:
<img width="406" alt="Screenshot 2023-05-30 at 11 54 50" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/8016ce7b-a343-43b9-b0d3-30b333b28f5c"> | <img width="414" alt="Screenshot 2023-05-30 at 11 55 07" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/b461602a-04a5-4ab0-ab43-0d3ca1897472">

### Task 2

Inicialmente, começamos por gerar o "Certificate Signing Request" para o nosso servidor (www.pereira2003.com)

```
openssl req -newkey rsa:2048 -sha256
            -keyout server.key
            -out server.csr 
            -subj "/CN=www.pereira2003.com/O=Pereira2003 Inc./C=US" -passout pass:dees
```

![CSR_command](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/c8b80736-0972-4212-a909-d30c95201955)

De seguida, utilizamos os seguintes comandos:

```openssl req -in server.csr -text -noout``` : permite visualizar com mais detalhes as informações de solitação do certificado

![decoded_public_key](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/91fbdaf1-08b6-4453-998c-54a74f64db2c)

```openssl rsa -in server.key -text -noout``` : permite visualizar o conteúdo da chave privada RSA em formato de texto
 
![decoded_private_key1](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/b6f6b0d2-6d9b-4dba-8a9c-f5d2d18f2273)

![decoded_private_key2](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/d44a7f83-1837-41ef-9e82-4c3fbda0f9af)

Por fim, utilzamos o seguinte comando que permite adicionar nomes alternativos ao nosso "certificate signing request".

```
openssl req -newkey rsa:2048 -sha256
            -keyout server.key
            -out server.csr 
            -subj "/CN=www.pereira2003.com/O=Pereira2003 Inc./C=US" -passout pass:dees
            -addext "subjectAltName = DNS:www.pereira2003.com, \
                                      DNS:www.pereira2003A.com, \
                                      DNS:www.pereira2003B.com"
```

![adding_alternatives_names](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/f340c6e9-e1a2-4408-ac34-0bb3cb0725aa)

### Task 3

Nesta tarefa, vamos gerar o certificado solicitado pelo CSR criado na tarefa anterior. 

Primeiramente:

* Abrimos o arquivo ```opennssl.cnf```, e como pedido no enunciado descomentamos a seguinte linha:
```py
# Extension copying option: use with caution.
copy_extensions = copy
```

* Depois disso utilizamos o seguinte comando para transformar o **CSR** num certificado **X509**, usando o seguinte comando:

```py
openssl ca -config opennssl.cnf -policy policy_anything \
           -md sha256 -days 3650 \
           -in server.csr -out server.crt -batch \
           -cert ca.crt -keyfile ca.key
```

![tas3_1](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/6b79afc7-ab6b-4b4b-a3a6-51cb78fd0d7e)

Depois de termos o certificado, utilizamos o seguinte comando:

```py
openssl x509 -in server.crt -text -noout

```
![task3_2](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/7d41bd8b-84dc-4881-8331-1fc7a41f2b09)

![task3_3](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/123839132/09ac71e2-8c47-4d50-9d78-857e3e2de213)

* Conseguimos imprimir o contéudo do certificado e verificamos que os nomes "alternativos" que adicionamos na task anterior estão presentes.
