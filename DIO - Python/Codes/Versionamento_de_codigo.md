## Versionamento de Código com Git e GitHub
- O Git é um Sistema de Controle de Versão Distribuído (DVCS), enquanto o GitHub é uma plataforma de hospedagem de código que utiliza o Git para controle de versão.
- O Git é um sistema de controle de revisão rápido, escalável e distribuído, com um conjunto
de comandos excepcionalmente rico que fornece operações de alto nível e acesso total aos componentes internos.
- Servidor que hospeda od códigos.
### 1. Configuração Inicial do Git
- Antes de começar a usar o Git, é necessário configurar
o nome e o e-mail para associar os commits ao seu usuário:
```sh
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```
- Para verificar a configuração:
```sh
git config --list
```

### 2. Comandos Básicos do Git

#### 2.1 Verificar versão e ajuda
```sh
git --version  # Mostra a versão do Git instalada
git --help  # Exibe a ajuda do Git
```

#### 2.2 Criar ou clonar um repositório
```sh
git init  # Cria um repositório Git vazio
git clone <link-do-repositório>  # Clona um repositório remoto
```

#### 2.3 Adicionar e confirmar mudanças
```sh
git add <arquivo>  # Adiciona um arquivo específico
```
```sh
git add .  # Adiciona todos os arquivos modificados ao staging
```
```sh
git commit -m "Mensagem do commit"  # Registra as mudanças no repositório
```

#### 2.4 Status e diferenças
```sh
git status  # Exibe o estado dos arquivos no diretório de trabalho
git diff  # Mostra as diferenças entre os arquivos modificados e o último commit
```

#### 2.5 Trabalhando com branches
```sh
git branch  # Lista as branches disponíveis
git branch -m main  # Renomeia a branch atual para "main"
```
```sh
git merge <nome-da-branch>  # Mescla outra branch com a branch atual
```

#### 2.6 Atualizar e enviar alterações
```sh
git pull  # Atualiza o repositório local com mudanças do repositório remoto
git push  # Envia as mudanças locais para o repositório remoto
```

### 3. Sequência Padrão de Comandos:
```sh
git init

git status

git add .

git status

git commit -m "Mensagem do commit"

git branch -m main

git push
```


## Instalação do Git:
- Site e seleção da versão. 
- Nome da ramificação: main. 
- Comandos:
```sh
# Configurações no Git bash:
$ git config ## --global , --system ou --local
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
$ git config user.name  # Mostrar
$ git config user.email 
$ git config init.defaultBranch # branch padrão < - mostrar o nome.
$  git config --global init.defaultBranch "Nome"
$ git config --global --list # configurações globais mostradas
```
## Autenticando via Token: 
```sh
#
$ git clone link do git hub
$ Token
$ git config --gloabal credentioal.helper store
```

## Criando e Clonando Repositórios
- Captura do link do repositório existente. 
``` sh
git init # inicializa
git remote add origin url # Esse é diferente é adicionar a origem. 
# Ou
git clone url_do_repositorio nome_do_repo_caso_deseje_mudar
git clone URL --branch name --sing... # Clonar branck especiififca.

git add .
git status # Mostrar o status da área de preparação. Verde -> Ok.

git commit -m "Name"
git log 
touch name/name.md # adicionar arquivos.


mkdir name # criar um diretórios

git commit -m "Mensagem do commit"

```

## Desfazer
- Em projetos em grupo é complexo, por isso cuidado. 
``` sh 
git init # na pasta errada
rm -rf .git
git status
git restore name_file # descartando suas mudanças todas  CUIDADO!

# Alterar a mensagem

git commit --amend -m"New Name" # Alterar o Nome do Ultimo commit feito. 


# desfazer o commit
git log # Historico de commit
git reset --soft hash do commit do git log. # PEGAR OS ARQUIVOS E adicionalos a preparação
git log

git reset --mixed hash do ultimo commit # Pegou os files e adicionou na área anterior.
git reset --hard hash do ultimo commit # apaga a ultima alteração.
git log


```

## Envio: Local -> Remoto

```sh
git remote add origin url 
git push -u origin main 

```

- Via interface: +, commit_name, push. 
- Atualização: Local <- Remoto: `git pull`


## Trabalhando com Branches - Criando, Mesclando, Deletando e Tratando Conflitos
- Uma Barnch é uma ramificação do seu projeto, para teste de funcionalidades.
- Um universo paralelo.
- Trabalham de forma independente. 
- Conversão de nome e commits

````sh
# Criando:
git log
git checkout -b new_branch # Alterar para outra branch.
git checkout main # Retorna para branch main
# Commits não se interligam.

# Mesclando:
git merge nome_da_branck_que_será_mesclada
git branch # listar as branchs

# Deletando:
git branch -d branch_para_deletar
git branch # listar as branchs

# Tratando Conflitos: 
# De Merge: envio duplo em equipe. Ex: (envio pelo github e pelo vscode). 
git pull
git add .
# faz o commit
git push origin main


````