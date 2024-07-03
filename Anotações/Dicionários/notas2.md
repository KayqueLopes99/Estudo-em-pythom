# OBSERVAÇÕES:
1. **Lista como valor**:
- Uma lista como valor associado a uma chave. Por exemplo:
```python
pessoa = {'nome': 'Maria', 'idades': [25, 30, 35]}
```
- A chave `'idades'` tem uma lista de três valores.

2. **Dicionário aninhado**:
- Um dicionário dentro de outro dicionário. Por exemplo:
- ```python
- aluno = {'nome': 'João', 'notas': {'matematica': 8, 'portugues': 9}}
- ```
- A chave `'notas'` contém outro dicionário com as notas nas disciplinas.

# No print formatado:
- Usamos "" dentro do [] no {}.
```python
pessoas = {'Nome': 'Kayque', 'Sexo': 'M'}
print(f'O {pessoas["Nome"] tem o sexo {pessoas["Sexo"]}}')
```