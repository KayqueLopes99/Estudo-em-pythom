# C:\Users\kaiqu\Music\Estudo-em-pythom\Udemy 
#caminho = r'C:\\Users\\kaiqu\\Music\\Estudo-em-pythom\\Udemy'

import os

caminho = os.path.join('C:\\', 'Users', 'kaiqu', 'Music', 'Estudo-em-pythom')
if os.path.exists(caminho):
    for item in os.listdir(caminho):
        # print(item)
        caminhoCompleto = os.path.join(caminho, item)
        print(item)
        if not os.path.isdir(caminhoCompleto):
            continue
        for conteudo in os.listdir(caminhoCompleto):
            print("   ", conteudo)

else:
    print(f'O caminho não existe: {caminho}')