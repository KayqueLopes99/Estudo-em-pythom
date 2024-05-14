# Estrutura de repetição while
- Seu conceito:
- Enquanto não satifazer a Condição o loop continua.
-  Usada para repetir um bloco de código enquanto uma condição for verdadeira 
- Sintaxe:
````python
while condicao:
    # bloco de código Dentro.
# Bloco de código fora.
````
# If
- Usamos vários if e não elif, pois são condições independentes.

## OBS:
- Na condição:
- Se não for nenhum desses caracteres.
- Eles podem ser Juntos.
```python
while genero not in 'MmFf':
     # Bloco.
```

## While true:
- O loop while True é um loop infinito. Ele continuará a executar o bloco de código dentro dele até que uma instrução break seja chamada.
- Exemplo:
```` python
while True:
    resposta = input("Digite 'sair' para terminar o loop: ")
    if resposta == 'sair':
        print("Saindo do loop.")
        break

````
## While False:
-  Ele nunca será executado porque False é uma constante que sempre avalia como falsa. Portanto, o código dentro do loop nunca será alcançado. 
- Exemplo:
```` python
while False:
    print("Este código nunca será executado.")


````

