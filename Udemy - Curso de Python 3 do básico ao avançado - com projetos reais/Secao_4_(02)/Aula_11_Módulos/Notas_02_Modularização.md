
## Modularização - Entendendo os seus próprios módulos e sys.path no Python
- **Módulos** são arquivos `.py` individuais.
+ Uso:
```python
from meu_pacote import modulo1
import modulo1
```
- O ideal é import meu_pacote nesta questão.
- Vantagens:
> Organização.
> Manutenção.
> Ocultação.
> Reutilização em outros arquivos. 

- O primeiro módulo executado chama-se __main__.
- É um arquivo central tudos os modulos ligados a ele, mantenha junto com este. 
- Deve-se está na mesmo diretório.

- Você pode importar outro módulo inteiro ou parte do módulo
- O python conhece a pasta onde o __main__ está e as pastas abaixo dele. *Uma pasta fora da pasta*.
- Ele não reconhece pastas e módulos acima do __main__ por padrão. O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path


## O que é `sys.path`   
- É uma lista que contém os diretórios onde o Python procura por módulos e pacotes quando você faz uma importação (`import`).  

```python
import sys
print(sys.path)
```
- Isso imprimirá uma **lista de diretórios** onde o Python está procurando por módulos.

## Como importar coisas do seu próprio módulo (ponto de vista do __main__)
- A importação funciona primeiro.
- Uso da variável: `mudulo_importado.variavel`
- Uso das funcionalidades dentro dele `from modulo_importado import funcion_01, variavel_do_modulo`.
- Arquivos modularizados próximos

## Recarregando módulos, importlib e singleton
- *singleton*: Só pode existir uma coisa no programa. A importação de um módulo mais de uma vez só é realizada uma única vez, pois já está salvo na memória. 
- Uma instância é um objeto real criado a partir de uma classe, ou seja, quando usamos uma classe como modelo e criamos algo concreto baseado nela. 🎯

- Exemplo simples:
*Se "Carro" for uma classe, então "meu carro vermelho da Toyota" é uma instância dessa classe.* 

- **garante que uma classe tenha apenas uma única instância**.  

---

### Recarregando Módulos, `importlib`
- - Atualiza um módulo sem reiniciar o Python | `importlib.reload(meu_modulo)`.
- Quando importamos um módulo com `import`, ele só é carregado **uma vez**.  
- Se fizermos mudanças no código do módulo depois da importação, **o Python não vai atualizar automaticamente**.  
- Para **recarregar um módulo sem reiniciar o Python**, usamos **`importlib.reload()`**.



## Introdução aos packages (pacotes) em Python
- **Pacotes** são diretórios que contêm vários módulos. Um pacote é identificado pela presença de um arquivo `__init__.py` dentro da pasta. Esse arquivo pode estar vazio ou conter código de inicialização para o pacote.

- Separar as funções por assunto. 
- Um pacote com varias funções separadas por ações no projeto.
+ Estrutura de exemplo de um pacote:

    ```
Pasta_python/  
│── meu_pacote_01/  
│   ├── __init__.py  
│   ├── modulo1.py  
│   ├── modulo2.py  
│  
│── meu_pacote_02/  
│   ├── __init__.py  
│   ├── pasta_cor/  
│   └── pasta_calculos/  
│  
│── Arquivo_main.py  
    ```

- Temos duas maneiras de importar os ódulos com pacotes
- 1. Maneira: `import pacote.modulo` - Você vai ter que colocar este nome na chamada das funções na main que estão neste modulo.
- 2. Maneira: `from pacote.modulo import função_do_modulo` - Aqui você so vai colocar o nome da função normalmente na main.

- **3. Maneira:** ``from pacote import modulo``: Na chamada `modulo.função_dele`.
`````py
import Aula_38_package.modulo

# 1, maneira from Aula_38_package.modulo import sum_the_variables_modules
from sys import path # 2. Maneira

print(__name__)
print(*path, sep='\n')

x = float(input("Informe o primeiro algarismo: "))
y = float(input("Informe o segundo algarismo: "))

        
print(f"{Aula_38_package.modulo.division_the_variables_modules(x, y):.2f}")
print(f"{Aula_38_package.modulo.multiplication_the_variables_modules(x, y):.0f}")
print(f"{Aula_38_package.modulo.diference_the_variables_modules(x, y):.0f}")
print(f"{Aula_38_package.modulo.sum_the_variables_modules(x, y):.0f}")
```