## Context Manager com classes - Criando e Usando gerenciadores de contexto
- Um **Context Manager** é um recurso que gerencia a **abertura e fechamento** de recursos automaticamente, como arquivos e etc. Ele garante que, independentemente do que acontecer dentro do bloco de código, o recurso seja fechado corretamente.  

- Para criar um **Context Manager personalizado**, devemos implementar dois métodos especiais (**Dunder Methods**):  
- `__enter__()`: Define o que acontece quando o contexto é iniciado.  
- `__exit__(exc_type, exc_value, traceback)`: Define o que acontece quando o contexto termina, mesmo que ocorra uma exceção.  

- Se o método `__exit__()` retornar **True**, ele suprime qualquer exceção que tenha ocorrido dentro do bloco `with`.

---

###  O Conceito de Duck Typing  
- **não importa de que tipo um objeto é**, mas **se ele possui os métodos corretos** para ser usado no contexto esperado.  
_"Se um objeto caminha como um pato, nada como um pato e grasna como um pato, então ele deve ser um pato."_  

- Ou seja, **se um objeto implementa `__enter__()` e `__exit__()`**, o Python o trata como um **Context Manager**, **independentemente** de sua classe base.  

- Isso significa que, **não precisamos explicitamente herdar de uma classe específica** para implementar um gerenciador de contexto. Basta que os métodos corretos existam na classe.

---

- Exemplo:
```` py
# Ex:
# with open("aula21.txt", "w") as arquivo:
# ...

CAMINHO = "C:\\Users\\kaiqu\\Music\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_5_(03)\\Code\\Aula_23.txt"


class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print("Abrindo Arquivo.")
        self._arquivo =  open(self.caminho_arquivo, self.modo, encoding='utf8')   
        return self._arquivo
    

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()
        

with MyOpen(CAMINHO, "w") as arquivo: # algo: Do enter
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
````

## Context Manager com contextlib.contextmanager
- Context Manager com função - Criando e Usando gerenciadores de contexto. 
- 