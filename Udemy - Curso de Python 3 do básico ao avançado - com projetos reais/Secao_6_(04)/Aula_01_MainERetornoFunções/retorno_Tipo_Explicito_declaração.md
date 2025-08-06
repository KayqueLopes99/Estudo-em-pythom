## Sintaxe 2.0 de funções || métodos
- Podemos definir um retorno explicito na prorpia função com o *(->)*.
- Sintaxe:
```python
def nome_da_funcao(parametros: tipo) -> tipo_de_retorno:
    # corpo da função
    return valor_de_retorno
```
- Em métodos , o tipo de retorno é usado para indicar o tipo de valor que a função deve retornar.
- Exemplo:
```python
def soma(a: int, b: int) -> int:
    return a + b
resultado = soma(5, 3)
print(resultado)  # Saída: 8
```


##   Maneira profissional de declarar variáveis
- Declarações de varíaveis com o seguite sintaxe:
``` python
nome: str = 'Kayque'
idade: int = 20
peso: float = 70.5
ativo: bool = True
```

