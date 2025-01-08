# Este é um arquivo que não está dentro do pacote Aula_38, ele é chamado main, ou seja, ele é o local oficial
# onde vai ocorrer a importação dos módulos daquele pacote.

# import Aula_38_package.modulo 2. Maneira

# 1, maneira from Aula_38_package.modulo import sum_the_variables_modules

# 3. Maneira 
from Aula_38_package import modulo
from sys import path 
print(__name__)
# print(*path, sep='\n')

x = float(input("Informe o primeiro algarismo: "))
y = float(input("Informe o segundo algarismo: "))

        
print(f"{modulo.division_the_variables_modules(x, y):.2f}")
print(f"{modulo.multiplication_the_variables_modules(x, y):.0f}")
print(f"{modulo.diference_the_variables_modules(x, y):.0f}")
print(f"{modulo.sum_the_variables_modules(x, y):.0f}")