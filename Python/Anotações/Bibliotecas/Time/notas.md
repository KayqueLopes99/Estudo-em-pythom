# A biblioteca time 
- Oferece funcionalidades relacionadas ao tempo.
- O comando `sleep()` é especialmente útil para introduzir atrasos ou pausas na execução de um programa. Aqui estão os detalhes:

1. **`time.sleep(segundos)`**: Pausa a execução do programa por um número especificado de segundos. Por exemplo:
   ```python
   import time
   time.sleep(2)  # Pausa por 2 segundos
   ```
# O comando FLUSH:
`- Serve para ajustar a contagem, usei ele no exercício 98.

```python
from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
       passo *= -1
    if passo == 0:
       passo = 1
    print("=== Começando ===")
    print(f"Contagem de {inicio} até {fim} em {passo} em {passo}:") 
    if inicio < fim:
       contador = inicio
       while contador <= fim:
          print(f"{contador} ", end='', flush=True)
          sleep(0.5)
          contador += passo

    else: 
       contador = inicio
       while contador >= fim:
        print(f"{contador} ", end='', flush=True)
        sleep(0.5)
        contador -= passo

    print("Fim!")
    print("-=-" * 15)



    
print("= Sistema de Contador =")
contador(1, 10, 1)
contador(1, 10, 2)

print(" === Personalizar === ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
```