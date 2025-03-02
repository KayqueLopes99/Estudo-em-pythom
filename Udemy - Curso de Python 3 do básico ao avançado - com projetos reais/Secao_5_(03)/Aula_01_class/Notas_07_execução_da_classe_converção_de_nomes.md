## `if __name__ == '__main__'` para evitar execuções indesejadas:  

- Quando importamos uma classe ou função de outro arquivo Python, todo o código desse arquivo é executado automaticamente. Para evitar que partes indesejadas sejam executadas ao importar um módulo, usamos:  

```python
if __name__ == '__main__':
    # Código que só será executado se este arquivo for rodado diretamente
```

### **Como funciona?**  
- `__name__` contém o nome do módulo.  
- Se o arquivo for executado diretamente, `__name__` será `'__main__'`, e o bloco dentro do `if` será rodado.  
- Se o arquivo for importado, `__name__` terá o nome do módulo, e o bloco `if` não será executado.  

### **Exemplo prático:**  
#### **Arquivo: `modulo.py`**
```python
class Exemplo:
    def mensagem(self):
        print("Olá do módulo!")

print("Este print sempre aparece!")  # Será executado ao importar

if __name__ == '__main__':
    print("Este print só aparece se rodar diretamente o módulo.py")
```

## Curiosidades sobre convenções de nomes
- Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, funções, classes e assim por diante. Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso programa: *PascalCase, camelCase e snake_case.*

+ **PascalCase** - ``significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;``

+ **snake_case** - ``este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.``

- Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.