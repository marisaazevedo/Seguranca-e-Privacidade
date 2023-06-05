Inicialmente começamos por executar a linha de código fornecida ```nc ctf-sp.dcc.fc.up.pt 6002``` e obtemos uma sequência de letras e números criptografados.

<img width="837" alt="Screenshot 2023-06-04 at 19 17 33" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/6bf81b53-943d-4a67-a188-244008fe83e7">

De seguida, procedemos a analisar o código em python fornecido ```challenge.py```. Verificamos que temos uma função que gera um ```k```, outra que codifica e outra que decodifica.

Na primeira função fornecida, aquela que gera o k, o número 16 é usado, ou seja, existem 2^16 possibilidades para encontrar o k que contém a flag.

Com isso, criamos então um ciclo que executa 2^16 vezes e que a cada iteração gera um ```k```, decodifica a mensagem correspondente (com a função ```decrypt_message``` fornecida) até encontrar a mensagem que começa com "flag".

Basta-nos então executar o código e obtemos a flag: **flag{5d9a0e6dd9171983f76277849e2b9b5c}**

<img width="689" alt="Screenshot 2023-06-04 at 19 17 39" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/38969d05-f0c1-4961-860a-640e1b8c6b34">
