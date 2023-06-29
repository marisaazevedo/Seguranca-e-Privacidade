Neste desafio, começamos por tentar perceber onde poderia haver uma vulnerabilidade na página, fazendo login sem sucesso. Com isto pesquisamos exploits que existem em sites WordPress e encontramos o seguinte, [https://www.exploit-db.com/exploits/50299](https://www.exploit-db.com/exploits/50299).


Desta forma e como é referido no site acima mencionado, executamos o comando:

```python3 exploit.py http://ctf-sp.dcc.fc.up.pt:5001/ 1 ```

O primeiro argumento é o url e o segundo é o id de um utilizador. Decidimos utilizar o id 1 porque se refere ao id do admin.

Com isto, obtemos 3 links e um deles abriu a página do admin.

![Screenshot 2023-06-29 at 11 28 11](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/2aa71ffd-c90e-4ca7-8750-a5dc237c3a4a)

Após isto, exploramos a página e encontramos a flag na seccção ```Posts```.

![Screenshot 2023-06-29 at 11 28 25](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/d3be653b-1a18-4670-b451-b3b484585b18)
