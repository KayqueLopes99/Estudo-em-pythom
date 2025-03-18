
# Se caso @Multiplication() pode-se: 
class Multiplication:
    def __init__(self, multiplicador):
        self._multiple = 10

    def __call__(self, func):
        # Função interna do decorator
        def intern(*args, **kwds):
            # Retornando / Guardando a função executada.
            result = func(*args, **kwds)
            return result * self._multiple
        # Retornando a função interna.
        return intern # Adiando a execução 
    

@Multiplication(10) # Chamando a classe e passando o multiplicador.

def operation_the_multiplication(x, y):
    return x * y

operation = operation_the_multiplication(2, 4)
print(operation)

