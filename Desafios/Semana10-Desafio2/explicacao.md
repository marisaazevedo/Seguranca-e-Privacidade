- **Que funcionalidades é que estão acessiveis a um utilizador sem este estar autenticado?**
    
    A funcionalidades que estão acessíveis a um utilizador não autenticado são o ```login``` e o ```ping```.
    
    Para testar as funcionalidades para um utilizador não autenticado, verificamos a secção ```Check out your network status! Here```.

    Inicialmente começamos por verificar o estado da rede para a porta 5000 do servidor ctf-sp.dcc.fc.up.pt.

    ![Screenshot 2023-05-25 at 20 09 28](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/fbc02821-f2a1-4f88-a0ef-8348860eb8f7)

    ![Screenshot 2023-05-25 at 20 09 34](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/e68f93e8-db86-4756-9db2-b4d20095f275)

<br></br>

- **Das funcionalidade que identificaste e do feedback que tiveste da sua utilização, pensa como é que estas podem estar implementatadas no servidor. Será que estão a utilizar algum utilitário linux?**

    Ao observar o screenshot acima, percebemos que é muito provável que o servidor esteja a utilizar um terminal/bash para executar o comando ping no sistema Unix.

<br></br>

- **Se sim, que vulnerabilidades podem estar presentes na chamada deste utilitário?**

    A página ```ping``` possui uma vulnerabilidade podendo assim executar vários comandos no "terminal" separados por um ```;```. Para confirmar o nosso palpite, decidimos inserir a seguinte linha de código: ```; echo secret message```. Caso seja bem-sucedido, aparecerá o texto escrito a seguir ao comando ```echo```.

    ![Screenshot 2023-05-25 at 20 07 42](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/5b0f4aca-983f-4575-8147-e257b1256c5a)

    ![Screenshot 2023-05-25 at 20 07 55](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/5ecae5dd-6e44-4dea-b748-e712e6b95b62)

<br></br>

- **Capturar a Flag**

    Com isso, confirmamos a nossa hipótese.

    Como sabemos que a flag está no ficheiro ```/flags/flag.txt```, basta ler o que existe no interior desse ficheiro.

    Para visualizar o conteúdo do ficheiro temos o comando ```cat``` do Linux. Portanto, apenas precisamos de inserir a seguinte linha de código: ```; cat /flags/flag.txt```.

    ![Screenshot 2023-05-25 at 20 11 04](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/26eecc35-53ef-4c88-8546-60ef2258b86b)

    ![Screenshot 2023-05-25 at 20 11 10](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/54f448f4-9040-4e6b-9068-8624e83a4e55)

    Obtendo assim a flag: **flag{dbb0427bc0fbf77a6c4a0ef478083c1f}**
