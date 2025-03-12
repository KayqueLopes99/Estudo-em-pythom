## Método especial __call__
- callable é algo que pode ser executado com parênteses.
- Em classes normais, __call__ faz a instância de uma classe callable.

+ O método __call__ permite que um objeto seja chamado como se fosse uma função. Quando você define __call__ dentro de uma classe, pode usar objeto() em vez de um método específico.

- Uma instância de uma classe é um objeto criado a partir dessa classe, contendo seus atributos e métodos definidos.

+ **OBS**: `NOMES IGUAIS A COMANDOS USAMOS: NOME_`
- Quadro:
```` py
# call.
instancia_(*args, **kwargs)
````