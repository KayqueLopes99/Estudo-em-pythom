# `center()`

- O método `center()` é usado para centralizar uma string dentro de uma nova string com um comprimento total definido. Você pode especificar o comprimento total e, opcionalmente, o caractere de preenchimento que será usado para preencher o espaço extra.

### Sintaxe

```python
string.center(largura * 2 , caractere_de_preenchimento)
```

- `largura`: O comprimento total da nova string (a string original será centralizada dentro dessa largura).
- A * 2 é para melhor centralização ou  qualificar a largura.
- `caractere_de_preenchimento` (opcional).

### Exemplos

```py
def escreva(mensagem):
    tamanho = len(mensagem)
    print("--"*tamanho)
    print(f"{mensagem.center(tamanho * 2)}")
    print("--"*tamanho)


print(" === Sistema De Tamanho de Mensagens === ")

escreva("Olá, Mundo!")
escreva("Pokémon é legalllll")
```
