## pip - instalando pacotes e bibliotecas
## **Cada projeto deve ter um ambiente virtual.**
- Lib é a localização.
- É um instalador de recursos que não estão na linguagem.
- `python -m pip install -upgrade pip` Ou `pip install pip --upgrade`.
- Desistalar: ``pip uninstall recurso` ou  `-Y`
- 1. executa o código. 2. Ambiente Virtual deve está ativo.
- Desliga o Terminal no X, para nao ficar ativando o ambiente virtual. 
- Listar: pip freeze. Ver o que está instalado.
- Gerar um arquivo chamado requirements.txt.


## Criando e usando um requirements.txt
- Criar um arquivo txt com requerimenos do programa.
- `pip freeze > Nome_do_arquivo_requirements.txt`
- pip uninstall nome_pacote
- Congelar (ver pacotes)
- pip freeze
- Criando e usando um requirements.txt
- pip freeze > requirements.txt
- Instalando tudo do requirements.txt
- pip install -r requirements.txt
- Quando você instalar algum recurso faça no ambiente virtual, pois se executar instalações no global pode-se prejudicar outros progrmas peals versões diferentes dos recursos.

- O arquivo `requirements.txt` é um **arquivo de dependências** usado em projetos Python para listar os pacotes necessários para o funcionamento do projeto. Ele permite que qualquer pessoa instale as mesmas bibliotecas com as versões corretas, garantindo a reprodutibilidade do ambiente.

---

##**Como Criar um `requirements.txt`**  
```bash
pip freeze > requirements.txt
```
- Isso cria um arquivo contendo todas as bibliotecas instaladas e suas versões.

- Para instalar todas as dependências listadas no arquivo, use:

```bash
pip install -r requirements.txt
```
- Com o ambiene virtual ativado.
- Isso garante que todas as bibliotecas necessárias serão instaladas corretamente.

---

### - **Exemplo de `requirements.txt`**
```txt
Flask==2.0.1
numpy>=1.21.0
pandas<=1.3.0
requests
```
- `==` → Exige uma versão exata.  
- `>=` → Permite versões mais recentes.  
- `<=` → Limita a versão máxima.  
- Sem versão → Instala a versão mais recente.

