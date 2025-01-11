# 0.1 Fábrica de Decoradores - Essa função cria decoradores que podem receber parâmetros.
def factory_of_decorator(a=None, b=None, c=None):  
    def factory_of_functions(funcion):  # Essa função será o decorador real, que envolve a função alvo
        print('Decoradora 1') 
        # a, b e c podem ser usados dentro do decorador

        def nested_aninhada(*args, **kwargs):  
            print('Parâmetros do decorador, ', a, b, c)  # Mostra os valores recebidos no decorador
            print('Aninhada')  
            response = funcion(*args, **kwargs)  
            return response 
        return nested_aninhada  

    return factory_of_functions  


# 1. Aplicando o decorador com parâmetros
@factory_of_decorator(1, 2, 3) 
def f_sum(var_x, var_y):  
    return var_x + var_y  


# 2. Criando um decorador sem parâmetros e aplicando manualmente
decorators = factory_of_decorator()  
muliplication = decorators(lambda x, y: x * y)  


# 3. Chamando a função decorada `f_sum`
ten_and_five = f_sum(10, 5)  # Chama a função decorada -> `nested_aninhada(10,5)`

# 4. Chamando a função decorada `muliplication`
ten_and_five_multiplication = muliplication(10, 5)  # Chama `nested_aninhada(10,5)` para a multiplicação


# 5. Exibindo os resultados
print(ten_and_five)  # 15 (10 + 5)
print(ten_and_five_multiplication)  # 50 (10 * 5)

