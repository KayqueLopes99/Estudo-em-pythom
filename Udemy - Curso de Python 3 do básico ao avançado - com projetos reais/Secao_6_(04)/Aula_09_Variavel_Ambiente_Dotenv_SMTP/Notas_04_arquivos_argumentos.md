## sys.argv - Executando arquivos com argumentos no sistema
- O módulo `sys` em Python fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com ele. Uma dessas variáveis é `sys.argv`, que é uma lista em Python que contém os argumentos da linha de comando passados para o script Python.
- `sys.argv[0]` é o nome do script Python.
- `sys.argv[1]` é o primeiro argumento passado para o script, `sys.argv[2]` é o segundo, e assim por diante.
- Exemplo de uso:
```python
import sys
print('Nome do script:', sys.argv[0])
print('Primeiro argumento:', sys.argv[1])
print('Segundo argumento:', sys.argv[2])
print('Todos os argumentos:', sys.argv)

```

## argparse.ArgumentParser - Criando scripts com argumentos nomeados
- O módulo `argparse` facilita a escrita de interfaces de linha de comando amigáveis. O programa define quais argumentos são necessários, e o `argparse` cuida de analisar esses argumentos da linha de comando.
- Exemplo de uso:
```python
import argparse
parser = argparse.ArgumentParser(description='Processa alguns inteiros.')  # Cria o parser e define a descrição do programa
parser.add_argument(
    '-b', '--basic',  # Define o argumento -b ou --basic
    help='exibe uma mensagem básica',  # Mensagem de ajuda para o argumento
    # type=str,  # Tipo do argumento (comentado)
    metavar='string',  # Nome exibido na ajuda para o valor esperado
    # default='Mensagem básica'  # Valor padrão (comentado)
    # nargs='+',  # Aceita múltiplos valores (comentado)
    action='append'  # Adiciona cada ocorrência do argumento em uma lista
)

args = parser.parse_args()  # Faz o parsing dos argumentos da linha de comando
print(args.soma(args.inteiros))  # Exemplo de uso dos argumentos (pode estar incorreto dependendo dos argumentos definidos)
```
> parsing: processamento dos argumentos da linha de comando.

Beleza, José. Vou te explicar **`argparse.ArgumentParser`** no Python de forma direta, sem rodeio, e com exemplo para fixar.


Com ele, você consegue rodar um programa assim:
```bash
python meu_script.py --nome José --idade 21
```

```python
import argparse

# 1. Criar o parser
parser = argparse.ArgumentParser(description="Exemplo com argumentos nomeados")

# 2. Adicionar argumentos
parser.add_argument("--nome", type=str, required=True, help="Informe o seu nome")
parser.add_argument("--idade", type=int, required=True, help="Informe a sua idade")

# 3. Ler os argumentos
args = parser.parse_args()

# 4. Usar os argumentos
print(f"Olá, {args.nome}! Você tem {args.idade} anos.")
```

- rodar no terminal
```bash
python exemplo.py --nome José --idade 21
```
```
Olá, José! Você tem 21 anos.
```

> Argumentos nomeados x posicionais

* **Nomeados** → usam `--` e você pode passar em qualquer ordem (`--nome José --idade 21`).
* **Posicionais** → não usam `--` e devem estar na ordem certa (`python exemplo.py José 21`).
