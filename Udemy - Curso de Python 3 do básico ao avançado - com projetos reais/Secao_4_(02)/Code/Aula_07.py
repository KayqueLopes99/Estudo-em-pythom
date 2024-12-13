def multiplication(*args):
    result = 1
    for number in args:
        result *= number

    return result


tuple_number = (1,2,3,4,5)
result = multiplication(*tuple_number)
print(result)




def impar_or_par(numero):
    if numero % 2 == 0:
        return (f"\033[92mO Número {numero} é Par\033[m")
    else:
        return (f"\033[mO Número {numero} é Ímpar\033[m")


inform_number = int(input("\033[92mInforme um número Par saber se ele é Par ou Ímpar: \033[m"))

par_or_impar_funcion = impar_or_par(inform_number)
print(par_or_impar_funcion)
