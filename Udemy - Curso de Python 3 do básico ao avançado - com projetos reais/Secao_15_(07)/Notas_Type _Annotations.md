## Type annotations - Tipagem de dados no Python
Definição: 
- bibliotecas variaveis: mypy

- Informar o tipo da variavel
`name: type = value`

- parametros e metodos

`def funcao(name: type, ...) -> retorno`

- Nas listas
`list[type]`

- Nos dicionários
`dict[type_key, type_value]`

- Nos set
`set[type]`

- dois tipos
`name: type_one | type_two = value`

- tipos opcionais
`def funcao(name: type, name1: type | None = None, ...) -> retorno`

- no isinstance
`ìf instance(y, float | int)`


- Calable() metodos e funções
- biblioteca necessária: Callable
``Callable[[parametro1, parametro2, ...], retorno]`

- TypeVar
- T pode ser um tipo qualquer desejado.
- Entra na parte do Tipos genericos.


- Tipo em classe.
``variable: nameClass`