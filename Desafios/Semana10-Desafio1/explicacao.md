### **Explorar a vulnerabilidade como um utilizador comum**

Inicialmente fizemos um teste apenas para verificar como o servidor web interage com um input inserido por um utilizador.

![Screenshot 2023-06-29 at 11 20 18](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/ebea6458-c2f3-4544-8ac2-485da29c2e1e)

### **Vulnerabilidade no formulário de submissão**

Decidimos explorar o formulário de submissão e começamos por experimentar inserir um alerta que abriria uma janela com uma mensagem.

![Screenshot 2023-06-29 at 11 20 34](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/06f8ec2b-fbb7-4d59-afe3-6f7ec0897ce7)

De seguida, decidimos inspecionar o servidor web para descobrir como poderíamos interagir e encontrar uma maneira de capturar a flag.
Após submetermos o formulário, descobrimos que a área de seleção ```Give the flag``` tinha o ID = 'giveflag'. Isso permitiu que com um certo input ser possível obter acesso à flag e, consequentemente, descobri-la.

![Screenshot 2023-06-29 at 11 20 48](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/cce189e9-b03e-43d7-9d40-5b98424850ae)

### **Capturar a Flag**

Utilizando o ID descoberto, 'giveflag', inserimos um código JavaScript que simula um clique nesse elemento. Esta ação desencadeia um evento de clique associado ao elemento, o que nos permite executar a função desejada e com isso descobrir a flag.

```<script> document.getElementById('giveflag').click() </script>```

![Screenshot 2023-06-29 at 11 21 02](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/d895a0c1-dd46-46bb-b718-92e2b6349452)

Como indicado a página faz refresh de 5 em 5 segundos e a resposta do administrador ao pedido pode demorar até 2 minutos. Após um certo tempo a flag acabou por aparecer no ecrã.

![Screenshot 2023-06-29 at 11 21 10](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/eea72aeb-7676-4626-a6da-f231d7a32f98)

Obtendo assim a flag: **flag{af526321748ba275e4d593bed9c50c88}**
