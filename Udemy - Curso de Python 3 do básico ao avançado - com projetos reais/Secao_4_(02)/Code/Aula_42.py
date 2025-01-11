# Dificuldade para nomear a função pelas alterações. Para isso vamos criar outras funções que vão decorar ela (Ajustar).
# 03. com uma closore vamos decorar ajustando isso. Podendo fazer coisas antes e depois.
# Função decoradora. 
def create_funcion(funcion):
    def intern(*args, **kwargs):
        print("Vou te decorar:")
        # Ver se todos são str
        for arg in args:
            is_string(arg)

        result = funcion(*args, **kwargs)
        print(f'O seu resultado foi {result}.')
        print('Ok, agora você foi decorada')
        return result
    return intern

# 01. Temos uma função mas queremos tratar um erro.
@create_funcion
def invert_string(string):
    return string[::-1]

# 02. Criamos uma função para atender o erro com uma mensagem.
def is_string(parameters):
    if not isinstance(parameters, str):
        raise TypeError('Parametro deve ser string')
    
invert = invert_string('123')
print(invert)
