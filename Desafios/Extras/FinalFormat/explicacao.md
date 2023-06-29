Neste desafio, começamos por fazer o comando "checksec program" para verificar as medidas de segurança implementadas no programa.

![Screenshot 2023-06-29 at 11 29 24](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/f7b38598-cbd6-488c-86b2-36f769f0478a)

Depois disso, testamos se existia uma vulneravilidade do formato de string.

![Screenshot 2023-06-29 at 11 29 30](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/583f059a-c822-485a-9d57-02da942e2913)

Em seguida usamos o gbd no programa atraves do comando ``` gdb program ```  e em seguida usamos o comando ``` info functions ``` para listar todas as funcoẽs presente no codigo.

![Screenshot 2023-06-29 at 11 30 03](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/0ecd3a68-fcd7-4602-906e-f5d7addf25bd)

Uma das funções mais cruciais presentes no codigo era a ```old_backdoor```, pois, ao analisarmos essa função com o comando ```disas```, descobrimos uma chamada de sistema que permitiria abrir um shell.

Para conseguirmos escrver o exploit para esta vulnerabilidade, tivemos de encontar o endereço onde ocrre um jump (0x0804c010), para redirecionamos o programa para essa a funçao ```old_backdoor```.

![Screenshot 2023-06-29 at 11 30 11](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/5e574c28-70fe-4580-b485-82d5aad13661)

Depois de termos escrito o exploit, executamos-o com o comando:
               ```python3 exploit.py```

![Screenshot 2023-06-29 at 11 30 19](https://github.com/marisaazevedo/Seguranca-e-Privacidade/assets/98234753/3af54903-96df-4025-a464-2fcf4341d7c1)
