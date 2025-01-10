# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenation(string_inicial):
    end_value = string_inicial

    def intern(value_the_concatenation=''):
        nonlocal end_value
        end_value += value_the_concatenation
        return end_value
    return intern


c = concatenation('K')
print(c('a'))
print(c('y'))
print(c('q'))
print(c('u'))
print(c('e'))
end = c()
print(end)