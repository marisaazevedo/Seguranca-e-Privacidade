Após abrir o link para este desafio, deparamo-nos com esta página inicial:

<img width="765" alt="Screenshot 2023-06-04 at 12 32 44" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/823675da-02a5-4e58-9352-8d481948edb9">


Decidimos enviar uma mensagem para verificar o que acontece e fomos direcionados para outra página onde verificamos que ```Your request hasn't been approved... Try again later!```.

<img width="762" alt="Screenshot 2023-06-04 at 12 33 11" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/433960c7-4e3d-41d5-85ad-30644cd3ef24">

Porém na página acima existe também ```The admin will use this page to check your request```, onde ```page``` nos direciona para uma página que tem os seguintes campos ```Give the flag``` e ```Mark request as read```.

<img width="332" alt="Screenshot 2023-06-04 at 12 33 20" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/36361b5d-1d06-45b9-a715-a083c5e7aba8">

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

<img width="1040" alt="Screenshot 2023-06-04 at 12 51 21" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/4312e28e-1585-4bca-93c8-8a90d60bbd32">

Deparamo-nos com ```Forbidden: You don't have the permission to access the request resource.```

<img width="825" alt="Screenshot 2023-06-04 at 12 51 44" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/6ad973c9-0fdb-4272-a64f-4dc93fe2ea77">

Que apenas pode ser resolvido desativando o javascript para o website.

<img width="668" alt="Screenshot 2023-06-04 at 12 58 33" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/0e44570f-ae15-4f2d-99f6-e031a68dcc00">

Após o javascript estar desativado, tentamos novamente e fomos direcionados para:

<img width="756" alt="Screenshot 2023-06-04 at 13 00 33" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/6d9f4dbb-7e7d-435d-a9b3-616dcb946528">

Após darmos refresh, finalmente obtemos a flag: **flag{afc587b8e2f138c7b7405e3ba215c072}**

<img width="572" alt="Screenshot 2023-06-04 at 13 01 26" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/e168d40b-5b9c-47b4-a46d-8423cfe51f41">
