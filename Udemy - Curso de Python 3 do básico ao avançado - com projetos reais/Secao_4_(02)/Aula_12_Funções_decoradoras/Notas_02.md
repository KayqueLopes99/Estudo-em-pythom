## Decoradores com parâmetros - (`@decorador(param)`)
- ``@funcao_decoradora`` Já executa a função decoradora. 
- Para que um decorador aceite parâmetros, é necessário adicionar **mais um nível de função**. O decorador agora terá **três níveis**:  
- **Uma função externa** que recebe os parâmetros(pegar os parametros do decorador).  
- **Uma função intermediária** (o próprio decorador) pegar a função.  
- **Uma função interna** que será a função decorada que vai subsituir a função real e vai executa-la.  
---
````py
# 0.1 Fábrica de Decoradores - Essa função cria decoradores que podem receber parâmetros.
def factory_of_decorator(a=None, b=None, c=None):  # Parâmetros opcionais do decorador
    def factory_of_functions(funcion):  # Essa função será o decorador real, que envolve a função alvo
        print('Decoradora 1')  # Executado assim que o decorador é aplicado
        # a, b e c podem ser usados dentro do decorador

        def nested_aninhada(*args, **kwargs):  # Função interna (wrapper) que executa lógica adicional
            print('Parâmetros do decorador, ', a, b, c)  # Mostra os valores recebidos no decorador
            print('Aninhada')  # Indica que o wrapper foi chamado
            response = funcion(*args, **kwargs)  # Chama a função original com seus argumentos
            return response  # Retorna o resultado da função original
        return nested_aninhada  # Retorna a função wrapper sem executá-la ainda

    return factory_of_functions  # Retorna a função decoradora


# 1. Aplicando o decorador com parâmetros
@factory_of_decorator(1, 2, 3)  # Chama a fábrica, que retorna `factory_of_functions`
def f_sum(var_x, var_y):  # Função que será decorada
    return var_x + var_y  # Soma os valores recebidos


# 2. Criando um decorador sem parâmetros e aplicando manualmente
decorators = factory_of_decorator()  # Cria um decorador sem passar parâmetros (a, b, c = None)
muliplication = decorators(lambda x, y: x * y)  # Aplica esse decorador a uma função de multiplicação


# 3. Chamando a função decorada `f_sum`
ten_and_five = f_sum(10, 5)  # Chama a função decorada -> `nested_aninhada(10,5)`

# 4. Chamando a função decorada `muliplication`
ten_and_five_multiplication = muliplication(10, 5)  # Chama `nested_aninhada(10,5)` para a multiplicação


# 5. Exibindo os resultados
print(ten_and_five)  # 15 (10 + 5)
print(ten_and_five_multiplication)  # 50 (10 * 5)
````

## Ordem de aplicação dos decoradores
- Quando usamos mais de um decorador. 
- Ordem de baixo para cima é a ordem.

```py
@decorador(name='03') # Terceiro
@decorador(name='02') # Segundo.
@decorador(name='01') # Primeiro.
```

```py
# Ordem dos decoradores
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

# De baixo para cima é a ordem.
@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')

def soma(x, y):
    return x + y
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
```