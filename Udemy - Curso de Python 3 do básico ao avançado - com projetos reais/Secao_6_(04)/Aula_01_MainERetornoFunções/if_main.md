## - if __name__ == "__main__" - 
O `if __name__ == "__main__":` é uma construção comum em Python que permite que um arquivo seja executado como um script ou importado como um módulo sem executar o código dentro do bloco `if`.

- Na modularização de códigos: Evita a execução de código desnecessário quando o módulo é importado.

- A condição é necessária para verificar se o arquivo está sendo executado diretamente ou importado como um módulo.

- sintaxe:
```python
if __name__ == "__main__":
    # Código a ser executado apenas quando o arquivo é executado diretamente
    print("Este código só será executado se o arquivo for executado diretamente.")
```

- Função main(): Usada para guardar o código de execução.