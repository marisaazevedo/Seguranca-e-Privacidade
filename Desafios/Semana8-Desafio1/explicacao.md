### **1. Injeção SQL**

Ao analisar o ficheiro "index.php", notamos que este é vulnerável à injeção de código. Isto significa que há uma falha no código que pode ser explorada para obter a flag que estamos a tentar descobrir.


### **2. Vulnerabilidade encontrada**

Ao examinarmos cuidadosamente o código, notamos que a falha de segurança estava na linha 40:

```$query = "SELECT username FROM user WHERE username = '".$username."' AND password = '".$password."'";```

O problema aqui é que o código simplesmente junta as entradas do utilizador numa consulta SQL sem fazer qualquer validação ou filtragem. Isto significa que um invasor pode facilmente inserir um comando SQL malicioso como parte das entradas do utilizador, como uma aspa simples (') ou um ponto-e-vírgula (;), que pode alterar a lógica da consulta SQL original e permitir o acesso indevido a informações confidenciais ou a execução de comandos maliciosos.


### **3. Código injetado para descobrir a flag**

A partir da vulnerabilidade de Injeção de SQL descoberta no código, podemos explorá-la inserindo na entrada:

- username: ```' or '1' = '1'; #```

- password: ```qualquer coisa, uma vez que fará parte do comentário```

Isto faz com que o código SQL fique assim:

```SELECT username FROM user WHERE username = '' or '1' = '1'; #' AND password = 'qualquer coisa, uma vez que fará parte do comentário'```

Antes da condição do ```or``` colocamos uma ```'``` para fechar a variável username. A cláusula ```or '1' = '1'``` é sempre verdadeira, porque ```'1' = '1'``` é uma comparação verdadeira. Além disso, o caractere ```#``` é usado para comentar o restante da consulta SQL, o que significa que a cláusula ```AND password = 'qualquer coisa já que está em comentário'``` é ignorada.


### **4. Descoberta da flag**

Colocando então nas entradas de username e password:

<img width="272" alt="Screenshot 2023-05-02 at 15 23 18" src="https://user-images.githubusercontent.com/98234753/235695433-bd75d533-3e61-4398-a712-f9b048f7b649.png">

Com isso, a flag foi descoberta:

<img width="382" alt="Screenshot 2023-05-02 at 15 21 41" src="https://user-images.githubusercontent.com/98234753/235694947-0fd32909-678d-446b-b850-3990123e1c5a.png">

Obtendo assim a flag: **flag{b6811980c0f224c56937575e56d0689b}**
