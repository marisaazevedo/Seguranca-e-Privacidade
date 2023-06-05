Inicialmente começamos por executar a linha de código fornecida ```nc ctf-sp.dcc.fc.up.pt 6002``` e obtemos uma sequência de letras e números criptografados.

PRINT

De seguida, procedemos a analisar o código em python fornecido ```challenge.py```. Verificamos que temos uma função que gera um ```k```, outra que codifica e outra que decodifica.

Na primeira função fornecida, aquela que gera o k, o número 16 é usado, ou seja, existem 2^16 possibilidades para encontrar o k que contém a flag.

Com isso, criamos então um ciclo que executa 2^16 vezes e que a cada iteração gera um ```k```, decodifica a mensagem correspondente (com a função ```decrypt_message``` fornecida) até encontrar a mensagem que começa com "flag".

Basta-nos então executar o código e obtemos a flag: **flag{5d9a0e6dd9171983f76277849e2b9b5c}**

PRINT
