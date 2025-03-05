## Encapsulamento e Modificadores de Acesso em Python
- Encapsulamento é um princípio da Programação Orientada a Objetos (POO) que restringe o acesso direto aos atributos e métodos de uma classe. 
+ Modificadores de acesso:
- **Público**: pode ser acessado livremente em qualquer local.  
- **Protegido** (`_`): deve ser usado apenas dentro da classe ou em subclasses(uso interno).  
- **Privado** (`__`): só deve ser acessado dentro da própria classe que ele foi definido.  

+ **Python não possui modificadores de acesso explícitos**, mas segue convenções para indicar diferentes níveis de acesso:

1. **Público (sem underline)**  
   ```python
   class Exemplo:
       def metodo_publico(self):
           print("Método público")

   obj = Exemplo()
   obj.metodo_publico()  # Pode ser acessado de qualquer lugar
   ```
   - Pode ser acessado dentro e fora da classe normalmente.

2. **Protegido (um underline `_` antes do nome)**  
   ```python
   class Exemplo:
       def _metodo_protegido(self):
           print("Método protegido")

   obj = Exemplo()
   obj._metodo_protegido()  # Ainda pode ser acessado, mas NÃO é recomendado
   ```
- Indica que **não deve** ser acessado fora da classe ou suas subclasses, mas **não impede** o acesso.
- Pode acessar mas não deve.

3. **Privado (dois underlines `__` antes do nome)**  
   ```python
   class Exemplo:
       def __metodo_privado(self):
           print("Método privado")

   obj = Exemplo()
   obj.__metodo_privado()  # ERRO! Não pode ser acessado diretamente
   ```
   - O Python aplica **name mangling** (desfiguração de nome), tornando o atributo acessível apenas dentro da própria classe.
   - O nome real do método fica assim: `_Exemplo__metodo_privado`
   - Para acessar manualmente:
     ```python
     obj._Exemplo__metodo_privado()  # Funciona, mas NÃO é recomendado
     ```
