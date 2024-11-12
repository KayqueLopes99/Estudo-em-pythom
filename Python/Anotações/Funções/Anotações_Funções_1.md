# Funções em Python (Parte 1):
- Incluimos Funcionalidades, de forma personalizada a necessidade escolhida.
- Uma rótina de uma informação ou código que deve ser reduzido. 
- Otimização do Código.
- Sintaxe:
````py
def Nome_da_Função(Parâmetros):
    # Bloco Corespondente.
# 2 Linhas.
# 2 Linhas.
## Chamada no programa inicial:
Nome_da_Função()
````
- Deve deixar duas linhas de distância do programa principal.
## Parâmetros Nomeados:
   - As funções em Python também suportam parâmetros nomeados.
   - Exemplo:

```py
def mensagem(msg):
    print('_+_+_+_+_+_+_+_+_+_+_+_+_+_+_')
    print(msg)
    print('_+_+_+_+_+_+_+_+_+_+_+_+_+_+_')


# Essa Frase Vai Pra o Parâmetro.
mensagem('Sistema de Alunos.')

```

# Observações:
````python
def somatoria(a, b):
    soma = a + b
    print(f'A = {a}\nB = {b}\nResultado = {soma}')

# Programa Principal.
somatoria(4, 5)
somatoria(8, 9)
somatoria(2, 1)
# Maneira:
somatoria(a = 1, b = 5)
# Troca a Ordem:
somatoria(b = 1, a = 5)
````

### Empacotamento em Python
- **Empacotamento**:
   - O empacotamento permite agrupar vários valores em uma única variável (como uma lista ou tupla).
   - Você pode usar o operador `*` para empacotar valores em uma sequência.
   - Ele Cria Um Tupla em Caso de Print:
```python
def contador(* núm):
    print(núm)

contador(1,4,3,2,7)
```


   - Exemplo:
     ```python
     def minha_soma(*args):
         return sum(args)

     print(minha_soma(1, 2, 3, 4, 5))  # Saída: 15
     ```

# Observações em pratica1.
- Podemos inicializar na propria função a varíavel.
# Com Listas e Tuplas:
- Podemos manipular a Lista com Funções.
- Dobrar a Lista é um exemplo
- Exemplo em Pratica3~
