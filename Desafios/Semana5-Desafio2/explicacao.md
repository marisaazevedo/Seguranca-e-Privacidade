- Começamos por copiar o ficheiro do exploit da semana 1 para a 2, e alterar a porta 4003 para 4000.

- Depois de analisar a nova main do desafio 2, vimos que havia 2 buffers e que o scanf suportava até 32 bytes (20 para o buffer 4 para o val e 8 para o meme_file).

- O nosso objetivo é que a condição do if (linha 13) seja verificada. Para satisfazer esta restrição, precisamos de escrever esse valor da condição em val.

- Ao executar o código sem provocar qualquer buffer overflow reparámos que val aparecia como ```0xdeadbeef```, ao contrário de ```\xef\xbe\xad\xde``` como está definido no código. Assim, para obter o valor pretendido ```0xfefc2223``` quando ocorre buffer overflow a sequência de carateres que foi inserida aquando da execução do programa foi ```\x23\x22\xfc\xfe```.

- Ao executar o script de python auxiliar, tendo a string ```pppppppppppppppppppp\x23\x22\xfc\xfeflag.txt``` como input, obtivémos a flag: **flag{3c43df981add5e0dc77cd3db5328b691}**.


![Desafio2](https://user-images.githubusercontent.com/123839132/229187681-1a62aede-2b23-454b-bc46-97bdf7c44b93.png)
