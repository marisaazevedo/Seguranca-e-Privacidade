Neste desafio, começamos por fazer o comando "checksec program" para verificar as medidas de segurança implementadas no programa.

![Screenshot from 2023-06-03 12-06-01](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/124071367/ada593c9-be72-4458-99ed-8d5d9ad43a82)

Depois disso, testamos se existia uma vulneravilidade do formato de string.

![Screenshot from 2023-06-03 12-46-11](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/124071367/5c5066d5-651f-4dba-9ae8-d97597a3e54b)

Em seguida usamos o gbd no programa atraves do comando ``` gdb program ```  e em seguida usamos o comando ``` info functions ``` para listar todas as funcoẽs presente no codigo.

![Screenshot from 2023-06-03 12-56-23](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/124071367/aa844ca5-3088-4066-ab52-81b315e313a5)

Uma das funções mais cruciais presentes no codigo era a ```old_backdoor```, pois, ao analisarmos essa função com o comando ```disas```, descobrimos uma chamada de sistema que permitiria abrir um shell. 

Para conseguirmos escrver o exploit para esta vulnerabilidade, tivemos de encontar o endereço onde ocrre um jump (0x0804c010), para redirecionamos o programa para essa a funçao ```old_backdoor```.

![Screenshot from 2023-06-04 19-15-50](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/124071367/1c08e631-10ac-400b-880d-b7e31a7c9ae2)

Depois de termos escrito o exploit, executamos-o com o comando:
               ```python3 exploit.py```
               
 ![Screenshot from 2023-06-04 19-23-54](https://github.com/DCC-FCUP-SP/sp2223-t01g06/assets/124071367/2d9addd1-1293-4ab0-be94-81da42302467)

