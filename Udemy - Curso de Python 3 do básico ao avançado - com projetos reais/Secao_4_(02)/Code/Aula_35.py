def no_accept_zero(divider):
    if divider == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return True


def must_be_int_or_float(number):
    type_number = type(number)
    if not isinstance(number, (float, int)):
        raise TypeError(
            f'"{number}" deve ser int ou float. '
            f'"{type_number.__name__}" enviado.'
        )
    return True

def division(number, divider):
    must_be_int_or_float(number)
    must_be_int_or_float(divider)
    no_accept_zero(divider)
    return number / divider


print(division(8, 0))
