Inicialmente começamos por executar a linha de código fornecida ```nc ctf-sp.dcc.fc.up.pt 6002``` e obtemos uma sequência de letras e números criptografados.

![Screenshot 2023-06-29 at 11 35 44](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/4c5e8aa1-cc05-4af2-bc75-4b1770a53cfb)

De seguida, procedemos a analisar o código em python fornecido ```challenge.py```. Verificamos que temos uma função que gera um ```k```, outra que codifica e outra que decodifica.

Na primeira função fornecida, aquela que gera o k, o número 16 é usado, ou seja, existem 2^16 possibilidades para encontrar o k que contém a flag.

Com isso, criamos então um ciclo que executa 2^16 vezes e que a cada iteração gera um ```k```, decodifica a mensagem correspondente (com a função ```decrypt_message``` fornecida) até encontrar a mensagem que começa com "flag".

Basta-nos então executar o código e obtemos a flag: **flag{5d9a0e6dd9171983f76277849e2b9b5c}**

![Screenshot 2023-06-29 at 11 35 50](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/1e8ef15b-9987-4d08-8a74-f1096737f44f)
