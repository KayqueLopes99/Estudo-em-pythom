## Introdução às variáveis em Python
- Variáveis são usadas para salvar algo na memória do computador.
- PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _.
- O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável).
- Sintaxe: nome_variavel = expressão

##   Maneira profissional de declarar variáveis
- Declarações de varíaveis com o seguite sintaxe:
``` python
nome: str = 'Kayque'
idade: int = 20
peso: float = 70.5
ativo: bool = True
```


``` python
nome_completo = 'José Kayque Lima Lopes'
soma_dois_mais_dois = 2 + 2
int_um = bool('1')
print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois)
```

- Podemos aplicar uma condição em uma varíavel.
- O nome da varíavel deve refletir a descrição do comando (Regra - Código Limpo). 
``` python
nome = 'Kayque'
idade = 19
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)
```

+ 01 Exercício: variáveis e tipos de dados para treino:
- `Aula08.py`


- Observações:
- \n pular linha, ele vai servir na entrada de dados para organizar.
``` python
nome = input ('Qual e seu nome?\n')
idade = input ('Quantos anos voce tem?\n')
peso = input ('Quanto voce pesa?\n')
anime = input ('Qual e seu nome de seu anime?\n')
print(nome, idade, peso, anime)
```

- Deve obrigatoriamente começar com uma letra.
- Não deve possuir espaços em branco.
- Não pode conter símbolos especiais, exceto o sublinhado (_).


### variavel obs:
- Pode Sobrescrever uma varíavel a outra.
- Podemos definilas todas em uma mesma linha.
``` py
nome, idade = "kayque", 20
``` 

