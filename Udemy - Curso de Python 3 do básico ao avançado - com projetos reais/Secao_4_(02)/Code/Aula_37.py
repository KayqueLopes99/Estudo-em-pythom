import importlib
import Aula_35
print(Aula_35.variavel_modulo)
for i in range(10):
    importlib.reload(Aula_35)
    print(i)
print('Fim')