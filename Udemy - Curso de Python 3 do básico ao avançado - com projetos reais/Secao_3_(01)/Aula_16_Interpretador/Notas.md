## Detalhes sobre o interpretador do Python
- Funcionameto da esquerda para direita.
- `python --version`: Versão.
- `python nome_modulo.py`: Executar o módulo.py.
- `python -u`: (unbuffered) Joga direto na tela.
- `python -m mod`: (lib mod como script). -> Ambiente virtual.
- `python -c` 'cmd' (comando): executa esse comando.

## Interativo
- `python -i mod.py`: interativo com mod executando.
- saída com exit()
- visualizar as operações realizadas.

## Comando dir():
-  Sem argumentos, retorna a lista de nomes no escopo local atual. 
- Com um argumento, retorna uma lista de atributos válidos para o objeto.

``` python
dir(math) # mostra tudo relacionado a ele.
```
## Comando help():
- invoca o sistema de ajuda integrado. É posssível fazer buscas em modo interativo ou informar parâmetros qual o nome do módulo, função, classe método ou varíavel. 
``` python
helf(math) # mensagem explicativa e você pode pesquisar todas suas funcionalidades.
```

- The Zen of Python, por Tim Peters. 
```` python
""" 
Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)

The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""
```