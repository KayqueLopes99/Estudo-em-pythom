import os
from itertools import count
caminho = os.path.join('C:\\', 'Users', 'kaiqu', 'Music', 'Estudo-em-pythom')

counter = count()
for root, dirs, files in os.walk(caminho):
    theCounter = next(counter)
    print(theCounter, 'Pasta Atual: ', root)

    for dir_ in dirs:
        print("   ", theCounter, 'Dir:', dir_)
    
    for file_ in files:
        print("   ", theCounter, 'File:', file_)
