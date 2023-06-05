### Lab Environment Setup

Utilizamos o previlégio de root para alterar o arquivo /etc/hosts e adicionamos o IP mencionado no guião.

![configurarr](https://user-images.githubusercontent.com/123839132/234608719-6be43736-19f7-4678-8dd2-0d6854bd167f.png)
![AddHost](https://user-images.githubusercontent.com/123839132/234608746-76827bea-c474-46c6-a324-89c003c8c9e0.png)

Após executar o servidor descrito no guião, utilizamos os comandos "docker" para descobrir o ID do container e iniciar uma shell.
![configurar](https://user-images.githubusercontent.com/123839132/234599446-51974012-be34-44b5-9721-2723437390a0.png)

### Task 1

```O objetivo desta task é familiarizamo-nos com os comandos SQL e ganhar experiência com as SQL Queries. Como dito no enunciado a base de dados que iremos utilizar é MySQL.```

Começamos por fazer login utilizando root como username e pdees como password, após isto, para aceder à base de dados pretendida executamos o seguinte comando:
``` use sqllab_users; ```

De modo a termos conhecimento de todas as tabelas nesta base de dados, executamos o comando ```show tables; ```. Com isto, percebemos que apenas existe a tabela credential.
![Task1_a](https://user-images.githubusercontent.com/123839132/234599022-0854241d-1b8b-49f1-9eab-60fc410ad3b8.png)
Para acedermos a toda a informação da funcionária Alice, começamos por visualizar o conteúdo da tabela credential e, uma vez conhecida a variável que guarda os nomes dos funcionários, executamos o comando ``` select * from credential where Name = 'Alice'; ``` de modo a obter toda a informação desta funcionária.
![Task1_b](https://user-images.githubusercontent.com/123839132/234599037-6ef3121c-c2f5-49b9-b180-acb1d6fd104b.png)

### Task 2

#### Task 2.1

```O objetivo deste exercício é realizarmos um ataque de Injection SQL, para isso, temos de fazer login na página web como admin para termos as informações de todos os funcionários, como consta no código fornecido no guião. ```

Para isto, precisamos apenas de preencher o campo de username com a seguinte string: ```admin'#```. Desta forma,conseguimos fazer com que o comando SELECT utilize apenas o campo do username e não da password uma vez que ao usar " ' " terminamos a string do username e ao colocar "#" estamos a comentar os próximos campos desta clausúla, no caso, a password. (Em SQL o "#" serve para escrever um comentário)

![Task2 1login](https://user-images.githubusercontent.com/123839132/234617106-76b23367-53d8-420c-b646-7b909e9cfd92.png)
![Task2 1results](https://user-images.githubusercontent.com/123839132/234617115-04929f37-a2be-41e1-b312-9ea5d67e0d21.png)

Outra forma de realizar o que é pedido é utilizar a clausúla ```OR 1=1```, assim o que for comparado com 1 tem como resultado 1 (true).

![outra_res](https://user-images.githubusercontent.com/123839132/234623910-43d2c359-a5ae-44cd-9f1b-3b75752d813d.png)
![Task2 1results](https://user-images.githubusercontent.com/123839132/234617115-04929f37-a2be-41e1-b312-9ea5d67e0d21.png)

#### Task 2.2

```O objetivo desta tarefa é conseguirmos fazer um ataque igual ao da tarefa anterior fazendo um HTTP GET REQUEST.```

Na execução do comando temos de fazer com que a shell interprete ```admin'#``` (como realizado anteriormente para obter acesso), assim temos de converter os caracteres especiais em ASCII.

Como dito no enunciado, o " ' " é representado por %27 e após uma pequena pesquisa verificamos que o "#" é representado por %23.

Com a execução do seguinte comando ``` curl www.seed-server.com/unsafe_home.php?username=admin%27%23 ``` tivemos acesso às informações dos funcionários como pretendido.

![Tas2 2a](https://user-images.githubusercontent.com/123839132/234628121-6030f62e-5b3a-4a44-bb2e-124b8ad989a6.png)

Por curiosidade, decidimos testar este HTTP GET REQUEST no URL do browser e observamos que obtivemos o pretendido.

![Task2 2b](https://user-images.githubusercontent.com/123839132/234628286-a2e87c69-fda3-4e66-bd80-598e91359b75.png)

#### Task 2.3

```O objetivo desta tarefa é usar o ataque de Injection SQL para transformar uma instrução de SQL em duas, sendo a última uma declaração de UPDATE ou DELETE.```

Como pedido, tentamos executar duas instruções de SQL na página de login: ```admin';DELETE * FROM credential WHERE Name = "Alice";#```

![Task2 3](https://user-images.githubusercontent.com/123839132/234634089-acd2d86b-cea5-4edb-8eae-850df9b3197f.png)

![Task2 3results](https://user-images.githubusercontent.com/123839132/234634159-12608385-27d1-44bf-a2e5-5347516ab912.png)

Como esperado, não conseguimos executar duas instruções de SQL Injection pois existe uma função que previne a injeção de duas queries dentro de uma que é a [mysqli_query](https://www.w3schools.com/php/func_mysqli_query.asp).

### Task 3

```Pelas informações dadas no guião, sabemos que existe uma página onde é possível editar algumas informações de cada funcionário, isto é,o nickname, o email,o address, a password e o phonenumber. Quando uma alteração é feita num perfil é executado o código PHP dado no guião ```

### Task 3.1

Como referido anteriormente, cada funcionário pode alterar certas informações, sendo que não é possível um funcionário alterar o seu próprio salário, apenas o chefe "Boss" possui esta capacidade.

1º- começamos por fazer login na conta da Alice da mesma forma que fizemos na Task 2.1, não sendo assim necessário por a password.
![Task3a](https://user-images.githubusercontent.com/123839132/234719096-8dc7c96d-e5d3-43ee-96af-adde7a285aca.png)

2º- verificamos que o salário da Alice é de 20000, como consta na tabela.
![Task3a_2](https://user-images.githubusercontent.com/123839132/234719104-d61b4b85-33fe-4e16-a83a-abdba995d0dc.png)

3º- como o nosso objetivo é alterar o valor do salário, colocamos a seguinte instrução no campo do nickname: ``` ',salary='120007';#```. Como não é do nosso interesse alterar o nickname da Alice, apenas colocamos a " ' " de modo a "preencher" a variável referente ao mesmo. Como é possível visualizar no código "unsafe_edit_backend.php" e como era de esperar, não existe uma variável referente ao salário que é possível ser alterada por parte do funcionário, desta forma é necessário criar uma com um valor arbitrário, daí o " ,salary='120007' ". De forma a terminar a cláusula e a comentar o resto da mesma pusemos " ;# ", conseguindo assim alterar o salário da Alice, como se verifica na última imagem.

![Task3b](https://user-images.githubusercontent.com/123839132/234721009-a404cc20-a3f1-4009-8ee3-f4032f597d0f.png)

![Task3c](https://user-images.githubusercontent.com/123839132/234719223-32335d54-1417-40f4-b902-4edd8bac27b4.png)

### Task 3.2

Para alterar o salário de outro funcionário ou até mesmo do chefe, Boby, basta repetir o que foi feito na Task 3.1 e adicionar uma cláusula where de forma a assegurar o nome, ou o EID da pessoa a alterar o salário. Resultando isto na seguinte instrução:

``` ',salary='1' where EID='20000';#  ```.

![Task3 2a](https://user-images.githubusercontent.com/123839132/234723930-12faf63c-52c9-48da-a1eb-f13fc53d7c23.png)
![Task3 2](https://user-images.githubusercontent.com/123839132/234723939-a3eea306-6723-4a1c-8310-0bd21c71a160.png)

### Task 3.3

Como é dito no guião, a base de dados armazena a password em valor Hash em vez do texto exato, e por isso utilizamos um Sha1 online generator para obtermos o valor em Hash da password para a qual pretendemos alterar.

![Task3 3](https://user-images.githubusercontent.com/123839132/234725583-2975d634-7336-4611-bbee-dc0d37d0cdd3.png)

Desta forma, após darmos login na conta da Alice, conseguimos alterar a password do Boby utilizando a seguinte instrução:

``` ',Password='6adfb183a4a2c94a2f92dab5ade762a47889a5a1' where EID='20000';# ```

![Task3 3a](https://user-images.githubusercontent.com/123839132/234725596-48ea30f9-3429-4ec2-96c4-3af754d1dde8.png)

Ao utilizar esta instrução no campo do nickname conseguimos alterar a password do Boby para "helloworld". O print abaixo confirma a alteração bem sucedida da password.

![Task3 3b](https://user-images.githubusercontent.com/123839132/234725601-649b57cf-8d82-4234-a6b6-041cfa61d837.png)
