### **Explorar a vulnerabilidade como um utilizador comum**

Inicialmente fizemos um teste apenas para verificar como o servidor web interage com um input inserido por um utilizador.

<img width="820" alt="Screenshot 2023-05-16 at 12 36 45" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/b6f0ca1f-486e-4814-9952-9c91d69a8373">

<img width="820" alt="Screenshot 2023-05-16 at 12 36 51" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/2622512b-bfe9-4d26-9d4c-50b084d39e29">

<img width="815" alt="Screenshot 2023-05-16 at 12 36 56" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/dbc8ed9f-088c-4f62-8575-0e95a7726679">

### **Vulnerabilidade no formulário de submissão**

Decidimos explorar o formulário de submissão e começamos por experimentar inserir um alerta que abriria uma janela com uma mensagem.

<img width="776" alt="Screenshot 2023-05-16 at 13 25 47" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/6caa8a3d-7a98-4d3f-b8d8-da40018fcbb5">

<img width="550" alt="Screenshot 2023-05-16 at 13 25 55" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/9d23a752-28e5-4575-af64-0c1b7095c37d">


De seguida, decidimos inspecionar o servidor web para descobrir como poderíamos interagir e encontrar uma maneira de capturar a flag.
Após submetermos o formulário, descobrimos que a área de seleção ```Give the flag``` tinha o ID = 'giveflag'. Isso permitiu que com um certo input ser possível obter acesso à flag e, consequentemente, descobri-la.

<img width="453" alt="Screenshot 2023-05-16 at 14 31 11" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/8f16cd28-b59e-41f2-814c-9cdcde8d1544">

### **Capturar a Flag**

Utilizando o ID descoberto, 'giveflag', inserimos um código JavaScript que simula um clique nesse elemento. Esta ação desencadeia um evento de clique associado ao elemento, o que nos permite executar a função desejada e com isso descobrir a flag.

```<script> document.getElementById('giveflag').click() </script>```

<img width="769" alt="Screenshot 2023-05-16 at 14 35 25" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/15a151ce-66e5-4f6c-9b62-e8b367dd1867">

<img width="766" alt="Screenshot 2023-05-16 at 14 35 30" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/5d061c43-2e70-42dc-8249-a826cdc0aad8">

Como indicado a página faz refresh de 5 em 5 segundos e a resposta do administrador ao pedido pode demorar até 2 minutos. Após um certo tempo a flag acabou por aparecer no ecrã.

<img width="756" alt="Screenshot 2023-05-16 at 14 35 36" src="https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/98234753/43053576-8bdd-4657-8dfd-4d85c6ba6640">

Obtendo assim a flag: **flag{af526321748ba275e4d593bed9c50c88}**
