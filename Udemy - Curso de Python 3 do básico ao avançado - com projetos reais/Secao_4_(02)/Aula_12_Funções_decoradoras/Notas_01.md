## Funções decoradoras em geral
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

### 01. Funções Decoradoras e Decoradores (ou decorators)
- Funções **decoradoras** são funções que recebem outra função como argumento e **modificam seu comportamento** sem alterar diretamente seu código com uma closore. Elas permitem **adicionar, remover, restringir ou modificar** algo.  
- Funções decoradoras são funções que decoram outras funções.

```python
def decorador(funcao):
    def envoltoria():
        print("Executando algo antes da função...")
        funcao()  # Chamando a função original
        print("Executando algo depois da função...")
    return envoltoria  # Retorna a nova função modificada

# Aplicando o decorador manualmente
def minha_funcao():
    print("Sou a função original!")

minha_funcao = decorador(minha_funcao)  # Decorando manualmente
minha_funcao()
```

```
Executando algo antes da função...
Sou a função original!
Executando algo depois da função...
```
- O decorador **modifica a função original**, adicionando código antes e depois dela.

- O trabalho de uma função decoradora é receber uma função como argumento e criar uma função interna (closure). Essa função interna não será executada imediatamente, mas retornada sem execução, permitindo que o usuário a chame posteriormente.

- Quando a função decoradora é aplicada a outra função, ela pode executar ações antes ou depois da execução da função decorada, permitindo adicionar, modificar ou restringir seu comportamento sem alterar seu código original.












---

### **2️⃣ Usando `@decorador` (atalho para decorar funções)**  
O Python permite usar `@decorador` para simplificar a aplicação da função decoradora.

🔹 **Exemplo com `@decorador`:**  
```python
def decorador(funcao):
    def envoltoria():
        print("Executando algo antes...")
        funcao()
        print("Executando algo depois...")
    return envoltoria

@decorador  # Aplicando automaticamente o decorador
def minha_funcao():
    print("Sou a função original!")

minha_funcao()
```
📌 **Saída:** (mesma do exemplo anterior)  
```
Executando algo antes...
Sou a função original!
Executando algo depois...
```
✅ O `@decorador` **substitui** a necessidade de atribuir manualmente `minha_funcao = decorador(minha_funcao)`.  

---

### **3️⃣ Decoradores com funções que aceitam argumentos**  
Se a função decorada aceitar argumentos, a decoradora precisa usá-los com `*args` e `**kwargs`.

🔹 **Exemplo decorando função com argumentos:**  
```python
def decorador(funcao):
    def envoltoria(*args, **kwargs):  # Aceita qualquer argumento
        print(f"Chamando {funcao.__name__} com {args} {kwargs}")
        return funcao(*args, **kwargs)  # Executa a função original
    return envoltoria

@decorador
def soma(a, b):
    return a + b

print(soma(3, 5))
```
📌 **Saída:**  
```
Chamando soma com (3, 5) {}
8
```
✅ O decorador agora suporta **funções que recebem parâmetros**.

---

### **4️⃣ Decoradores com parâmetros personalizados**  
Podemos criar **decoradores que aceitam argumentos**, adicionando uma camada extra de funções.

🔹 **Exemplo: Criando um decorador que repete a execução da função:**  
```python
def repetir(n):
    def decorador(funcao):
        def envoltoria(*args, **kwargs):
            for _ in range(n):  # Executa a função 'n' vezes
                funcao(*args, **kwargs)
        return envoltoria
    return decorador

@repetir(3)  # Configura o decorador para repetir 3 vezes
def mensagem():
    print("Executando a função!")

mensagem()
```
📌 **Saída:**  
```
Executando a função!
Executando a função!
Executando a função!
```
✅ O decorador `@repetir(3)` **configura quantas vezes** a função será chamada.

---

### **5️⃣ Vários decoradores na mesma função**
Podemos empilhar decoradores em uma mesma função, e eles serão executados **de cima para baixo**.

🔹 **Exemplo:**  
```python
def decorador1(funcao):
    def envoltoria():
        print("Executando decorador 1")
        funcao()
    return envoltoria

def decorador2(funcao):
    def envoltoria():
        print("Executando decorador 2")
        funcao()
    return envoltoria

@decorador1
@decorador2
def minha_funcao():
    print("Função principal")

minha_funcao()
```
📌 **Saída:**  
```
Executando decorador 1
Executando decorador 2
Função principal
```
✅ O **`decorador1`** é aplicado **depois** do `decorador2` (o mais externo roda primeiro).

---

### **6️⃣ Aplicações práticas dos decoradores**  
Os decoradores são úteis para **monitorar, restringir e otimizar** o código.

#### **📌 6.1 Medindo o tempo de execução de funções**
```python
import time

def medir_tempo(funcao):
    def envoltoria(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return envoltoria

@medir_tempo
def processamento():
    time.sleep(2)
    print("Processamento concluído!")

processamento()
```
📌 **Saída:**  
```
Processamento concluído!
Tempo de execução: 2.0002 segundos
```
✅ O decorador `@medir_tempo` mede **automaticamente** quanto tempo a função leva para rodar.

---

#### **📌 6.2 Criando um decorador de autenticação**
```python
def autenticar(funcao):
    def envoltoria(usuario):
        if usuario != "admin":
            print("Acesso negado!")
            return
        return funcao(usuario)
    return envoltoria

@autenticar
def painel(usuario):
    print(f"Bem-vindo ao painel, {usuario}!")

painel("admin")  # Permite o acesso
painel("user")   # Bloqueia o acesso
```
📌 **Saída:**  
```
Bem-vindo ao painel, admin!
Acesso negado!
```
✅ O decorador `@autenticar` **bloqueia** usuários não autorizados.

---

### **Resumo**
✔️ **Decoradores** permitem modificar funções sem alterar seu código-fonte.  
✔️ O atalho `@decorador` aplica a função decoradora diretamente.  
✔️ Decoradores podem aceitar parâmetros, tornando-os mais flexíveis.  
✔️ É possível **empilhar** vários decoradores.  
✔️ Usado para **logs, autenticação, otimização e monitoramento de código**.  

Se tiver dúvidas, me avise! 🚀