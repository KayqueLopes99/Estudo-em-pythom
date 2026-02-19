## Flyweight
> Flyweight é um padrão usado para economizar memória quando você tem muitos objetos parecidos.

> Em vez de criar milhares de objetos iguais, você cria poucos objetos e compartilha eles.
> Exemplo

Imagine um jogo com **1 milhão de árvores**.

Cada árvore tem:

*  Tipo (carvalho, pinheiro, etc.)
*  Cor
*  Textura
*  Posição (x, y)

Agora:

* Tipo, cor e textura **não mudam**.
* A posição **muda para cada árvore**.

Se você criar 1 milhão de objetos completos, vai gastar muita memória.

Com Flyweight você faz assim:

* Cria **um objeto para cada tipo de árvore** (carvalho, pinheiro…)
* A posição você passa por fora

Ou seja:

* O que **não muda** → fica dentro do objeto
* O que **muda** → fica fora

Pronto. Você reduziu drasticamente o consumo de memória.

> Estado Extrínseco

É o que **muda dependendo do contexto**.
Fica **fora** do Flyweight.
É passado como parâmetro.

Exemplo:

* Posição da árvore
* Tamanho individual
* Vida restante

---


Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.