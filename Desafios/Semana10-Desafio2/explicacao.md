- **Que funcionalidades é que estão acessiveis a um utilizador sem este estar autenticado?**

    A funcionalidades que estão acessíveis a um utilizador não autenticado são o ```login``` e o ```ping```.

    Para testar as funcionalidades para um utilizador não autenticado, verificamos a secção ```Check out your network status! Here```.

    Inicialmente começamos por verificar o estado da rede para a porta 5000 do servidor ctf-sp.dcc.fc.up.pt.

    ![Screenshot 2023-06-29 at 11 23 18](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/c552be55-fd17-4238-8fe0-4c13413e492a)

<br></br>

- **Das funcionalidade que identificaste e do feedback que tiveste da sua utilização, pensa como é que estas podem estar implementatadas no servidor. Será que estão a utilizar algum utilitário linux?**

    Ao observar o screenshot acima, percebemos que é muito provável que o servidor esteja a utilizar um terminal/bash para executar o comando ping no sistema Unix.

<br></br>

- **Se sim, que vulnerabilidades podem estar presentes na chamada deste utilitário?**

    A página ```ping``` possui uma vulnerabilidade podendo assim executar vários comandos no "terminal" separados por um ```;```. Para confirmar o nosso palpite, decidimos inserir a seguinte linha de código: ```; echo secret message```. Caso seja bem-sucedido, aparecerá o texto escrito a seguir ao comando ```echo```.

    ![Screenshot 2023-06-29 at 11 23 27](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/067e203c-12af-4985-a39e-8cd8d6423c5a)

<br></br>

- **Capturar a Flag**

    Com isso, confirmamos a nossa hipótese.

    Como sabemos que a flag está no ficheiro ```/flags/flag.txt```, basta ler o que existe no interior desse ficheiro.

    Para visualizar o conteúdo do ficheiro temos o comando ```cat``` do Linux. Portanto, apenas precisamos de inserir a seguinte linha de código: ```; cat /flags/flag.txt```.

    ![Screenshot 2023-06-29 at 11 23 36](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/6ac29682-d9c9-4314-93ee-b4ef455439df)

    Obtendo assim a flag: **flag{dbb0427bc0fbf77a6c4a0ef478083c1f}**
