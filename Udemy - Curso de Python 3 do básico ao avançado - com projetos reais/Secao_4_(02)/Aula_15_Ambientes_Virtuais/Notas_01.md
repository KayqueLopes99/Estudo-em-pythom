## O que são ambientes virtuais? (venv)
## **Cada projeto deve ter um ambiente virtual.**
-  Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.
- Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
- venv é o módulo que vamos usar para criar ambientes virtuais.ome que preferir para um ambiente virtual, mas os mais comuns são:
- venv env .venv .env
- Neste local vai está as biblitecas instaladas.
- Manutenção das caracteristicas do programa. 

## Como criar o seu ambiente virtual com venv
- `python -m venv _Nome_venv`
- lib: instalações.
- Scripts: Executaveis.
- Caminho do py: Quando você acessa python o seu sistema vai buscar nos caminho path vai buscar o exe, ele vai busca o py.
## Ativando e desativando o meu ambiente virtual venv
- Muda o path enquanto tiver ativo. 
- Os caminhos mudam.
- Ativando: ambiente_virtual -> scripts -> activate
- Ativar: `_Nome_venv\Scripts\activate`.
- Desativar: `deactivate`.


### Expansão: 
## O que é um Ambiente Virtual 
- Um **ambiente virtual** (virtual environment) no Python é um **isolamento de dependências** para um projeto. Ele permite instalar pacotes específicos sem afetar outras aplicações no sistema. Isso ajuda a evitar conflitos entre versões de bibliotecas.  
- Para cada ambiente virtual temos uma sessão de bibliotecas distintas.

### Criar um Ambiente Virtual
No terminal, execute:  
```bash
python -m venv meu_ambiente
```


### Instalar Pacotes Dentro do Ambiente
```bash
pip install nome-do-pacote
```
Exemplo:  
```bash
pip install requests
```
- Os pacotes instalados ficam **apenas dentro do ambiente virtual**.

---

### Desativar o Ambiente Virtual: 
```bash
deactivate
```
- Isso restaura o ambiente global do sistema.

