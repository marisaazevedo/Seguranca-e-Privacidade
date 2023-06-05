### **Existe algum ficheiro que é aberto e lido pelo programa?**

Sim, o programa abre o ficheiro mem.txt e lê seu conteudo pois a função fopen é utilizada para abrir o ficheiro em modo "r", read, e o seu conteudo é lido através da função fgets.

O nome do ficheiro é armazenado na variável "mem_file" definida na 1ª linha da função main.

Depois que o ficheiro é aberto, o programa faz um loop lendo o conteudo do ficheiro linha a linha.
<br></br>
### **Existe alguma forma de controlar o ficheiro que é aberto?**

Sim, podemos alterar o valor da variável "meme_file" antes do programa ser executado.
<br></br>
### **Existe algum buffer-overflow? Se sim, o que é que podes fazer?**

Sim, pois o scanf é utilizado para ler um input de até 28 caracteres, mas o buffer tem espaço para alocar 20 caracteres. Assim, um utilizador malicioso pode inserir mais caracteres do que os que o buffer suporta.

Após analisar o código do programa, percebemos que para causar buffer-overflow temos de escrever mais de 20 caracteres, depois destes podemos escrever o ficheiro que queremos abrir, neste caso o flag.txt

Ao executar o script de python auxiliar, tendo a string ppppppppppppppppppppflag.txt como input, obtivémos a flag: **flag{c27e11234fbef14d08c42ca64d22ddce}**.

![checksecc](https://user-images.githubusercontent.com/123839132/229186326-4214e277-a3a2-424e-a1e5-49229ef3b38d.png)
