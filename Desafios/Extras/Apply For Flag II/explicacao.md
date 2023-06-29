Após abrir o link para este desafio, deparamo-nos com esta página inicial:
![Screenshot 2023-06-29 at 11 31 33](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/024c69b1-3a08-4a4e-8f89-33e4a848bb57)


Decidimos enviar uma mensagem para verificar o que acontece e fomos direcionados para outra página onde verificamos que ```Your request hasn't been approved... Try again later!```.

![Screenshot 2023-06-29 at 11 31 39](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/652c06a6-1f56-42cb-bb24-4dbca6dc3ec7)

Porém na página acima existe também ```The admin will use this page to check your request```, onde ```page``` nos direciona para uma página que tem os seguintes campos ```Give the flag``` e ```Mark request as read```.

![Screenshot 2023-06-29 at 11 31 44](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/82baa168-bf77-40b0-af23-f8bc90545b60)

Ao clicar em ```here``` reparamos que retornava à página anterior.

Decidimos então voltar à página inicial e notamos que após darmos refresh o id do pedido mudou.

A fim de submeter diretamente à última página, é preciso efetuar um pedido POST para o URL 'http://ctf-sp.dcc.fc.up.pt:5004/request/', seguido pelo ID exibido na página inicial. Esse ID é gerado com base num novo botão que redireciona para a página desejada.

```html
<form method="POST" action="http://ctf-sp.dcc.fc.up.pt:5004/request/dca58c915d1b02dd553a11073e129baef09e2ec1/approve" role="form">
    <div class="submit">
        <input type="submit" id="giveflag" value="Give the flag">
    </div>
</form>

<script type="text/javascript">
    document.querySelector('#giveflag').click();
</script>
```

Depois de submetermos o código acima:

![Screenshot 2023-06-29 at 11 31 51](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/51a771b8-3f48-4efa-9af4-b703d47f3475)

Deparamo-nos com ```Forbidden: You don't have the permission to access the request resource.```

![Screenshot 2023-06-29 at 11 31 57](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/2475c1b5-0c6c-4344-b46c-13172b8b5ca0)

Que apenas pode ser resolvido desativando o javascript para o website.

![Screenshot 2023-06-29 at 11 32 15](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/67e23335-1b35-4ed2-b60c-b8826c80a690)

Após o javascript estar desativado, tentamos novamente e fomos direcionados para:

![Screenshot 2023-06-29 at 11 32 22](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/82889d65-ed07-4673-b299-2ba66beb8daa)

Após darmos refresh, finalmente obtemos a flag: **flag{afc587b8e2f138c7b7405e3ba215c072}**

![Screenshot 2023-06-29 at 11 32 27](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/de1ca5ad-5e16-4e1a-b8cf-a45895c99972)
