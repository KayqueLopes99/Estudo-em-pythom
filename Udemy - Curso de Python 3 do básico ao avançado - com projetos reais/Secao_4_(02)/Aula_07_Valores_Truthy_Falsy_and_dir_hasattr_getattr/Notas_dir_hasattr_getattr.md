## dir, hasattr e getattr em Python
- Verificar os métodos dentro do objeto.
- `Debug Console` no debuger de um código.

- Elas ajudam a descobrir e manipular os atributos e métodos de um objeto de forma dinâmica.  

- Dir -> Mostra os nomes definidos dentro do objeto.
- Hasattr -> Se ele tem o atributo e pegar seu valor.
- Getattr -> de forma mais dinamica e sem erro. 


| Função | O que faz? | Quando usar? |
|--------|-----------|--------------|
| `dir(obj)`  | Lista atributos e métodos de um objeto | Para ver tudo o que o objeto tem |
| `hasattr(obj, "atributo_ou_método")` | Verifica se um atributo existe (`True` ou `False`) | Antes de acessar um atributo desconhecido |
| `getattr(obj, "atributo", padrão)` | Obtém o valor de um atributo (ou retorna um padrão se ele não existir) | Para acessar um atributo sem risco de erro |

