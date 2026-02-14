## Structural Pattern Matching
**Conceito:** Uma evolução do "Switch Case" que permite verificar a **estrutura** dos dados e extrair valores simultaneamente.

- Sintaxe 
A estrutura básica substitui longas cadeias de `if/elif/else`.

```python
match sujeito:
    case padrao_1:
        # Bloco executado se o padrão_1 corresponder
    case padrao_2 if condicao:
        # "Guard": Só entra aqui se o padrão corresponder E a condição (if) for verdadeira
    case padrao_3 | padrao_4:
        # Operador OR (|): Executa se for padrão_3 OU padrão_4
    case _:
        # Wildcard: Funciona como o "default/else". Captura qualquer coisa não tratada acima.

```

- Diferenças do "Switch" Tradicional

* **Switch (C/Java/JS):** Geralmente verifica apenas igualdade de valor (`if x == 1`).
* **Match (Python):** Verifica o **tipo**, a **estrutura** (tamanho da lista, chaves do dicionário) e faz o **binding** (atribuição) de variáveis na hora.
* **Segurança:** Não precisa de `break`. Ao entrar em um `case`, ele executa e sai automaticamente (não ocorre "fall-through").

- Desempacotamento com `split()`

Esta é uma das aplicações mais poderosas para processamento de texto ou comandos. O Python divide a string e verifica se a lista resultante bate com o padrão.

**Cenário:** Um interpretador de comandos simples.

```python
comando = input("Digite o comando (ex: 'ir norte'): ").lower()

# O split() gera uma lista. Ex: "ir norte" vira ["ir", "norte"]
match comando.split():
    # Padrão: Lista com 1 item exato
    case ["sair"]:
        print("Encerrando o programa...")

    # Padrão: Lista com 2 itens, onde o primeiro é FIXO ("ir")
    # 'direcao' é uma variável nova que recebe o segundo item
    case ["ir", direcao]:
        print(f"Movendo o personagem para: {direcao}")

    # Padrão: Lista com 2 itens, primeiro fixo ("pegar")
    case ["pegar", item]:
        print(f"Item {item} adicionado ao inventário.")
    
    # Padrão: Lista com 3 itens (ex: "falar com npc")
    # Usando o coringa '_' para ignorar o "com"
    case ["falar", _, npc]:
        print(f"Iniciando diálogo com {npc}")

    # Default: Qualquer outra coisa que não bata nos padrões acima
    case _:
        print("Comando inválido ou não reconhecido.")

```

- O Wildcard (`_`)

O caractere sublinhado `_` é um coringa especial.

* **No final (`case _`):** Serve como o `default` (pega tudo).
* **No meio (`case [_, valor]`):** Serve para ignorar uma parte específica da estrutura que não interessa.

- Exemplo 

O `match` também funciona diretamente com objetos.

```python
@dataclass
class Ponto:
    x: int
    y: int

p = Ponto(0, 10)

match p:
    case Ponto(x=0, y=0):
        print("Origem")
    case Ponto(x=0, y=y):
        print(f"No eixo Y, altura {y}")
    case Ponto(x=x, y=0):
        print(f"No eixo X, distância {x}")
    case Ponto():
        print("Ponto fora dos eixos")

```

