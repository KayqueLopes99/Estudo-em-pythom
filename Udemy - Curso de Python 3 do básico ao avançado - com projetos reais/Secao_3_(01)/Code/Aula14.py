variavel_a = "Kay"
variavel_b = 'Isa'
variavel_c = 'Let'

formato = 'A = {} B = {} C = {}'.format(variavel_a, variavel_b, variavel_c)

print(formato)

a = 'AA'
b = 'BB'
c = 'CC'
d = 20.1

string = 'a= {} b= {} c= {} d= {:.2f}' # out of range = variavel que já acabou e não achou.

format = string.format(a, b, c, d)
print(format)

# Com índices 0,1,2,3 = Ordem de varíaveis. 
string = 'a= {0} b= {1} c= {2} d= {3:.2f}' 

format = string.format(a , b, c, d)
print(format)

# Parâmetros Nomeados.
# Com índices 0,1,2,3 = Ordem de varíaveis. 
string = 'a= {nome1} b= {nome2} c= {nome3} d= {idade1:.2f}' 

# Deve nomear todos
format = string.format(
    nome1=a , nome2=b, nome3=c, idade1=d
)
print(format)