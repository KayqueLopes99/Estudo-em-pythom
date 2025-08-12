## Configurando o SMTP e senhas de apps no GMAIL para enviar e-mails com Python
- Para enviar e-mails com Python usando o Gmail, você precisa configurar o SMTP e permitir o acesso de aplicativos menos seguros. Aqui estão os passos:
1. **Ativar o SMTP no Gmail**:
   - Acesse sua conta do Gmail.
   - Vá para "Configurações" (ícone de engrenagem) > "Ver todas as configurações".
   - Na aba "Encaminhamento e POP/IMAP", ative o "Acesso IMAP".

2. **Permitir aplicativos menos seguros**:
    - Acesse [Permitir aplicativos menos seguros](https://myaccount.google.com/lesssecureapps).
    - Ative a opção "Permitir aplicativos menos seguros".

3. **Gerar senha de aplicativo** (opcional, mas recomendado):



    - Acesse [Segurança da Conta Google](https://myaccount.google.com/security).
    - Na seção "Como fazer login no Google", clique em "Senhas de app".
    - Siga as instruções para gerar uma senha de aplicativo específica para o seu script Python.
4. **Instalar a biblioteca `python-dotenv`**:
   - Use o comando `pip install python-dotenv` para instalar a biblioteca que permite carregar
variáveis de ambiente de um arquivo `.env`.

5. **Criar um arquivo `.env`**:
   - Crie um arquivo chamado `.env` no mesmo diretório do seu script Python.
   - Adicione as seguintes linhas ao arquivo `.env`:

```
EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''
```

   - Substitua os valores entre aspas pelos seus dados de e-mail e senha (ou senha de aplicativo).
