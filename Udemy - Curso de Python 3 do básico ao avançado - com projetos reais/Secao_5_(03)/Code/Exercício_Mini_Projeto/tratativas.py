from datetime import datetime
import re

def valida_cpf(cpf):
    # Remover formatações e garantir apenas números
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", '')
    
    if not cpf.isdigit() or len(cpf) != 11:
        print("\033[91mO CPF deve ter exatamente 11 dígitos e conter apenas números.\033[m")
        return False
    
    # Verifica se todos os números são iguais (ex: 00000000000 ou 11111111111)
    if cpf == (cpf[0] * 11):
        print("\033[91mFormato inválido! CPF não pode ter todos os números iguais.\033[m")
        return False

    # Cálculo do primeiro dígito verificador
    lista_com_9_digitos_cpf = []
    contador_regressivo_1 = 10
    for digito in cpf[:9]:
        lista_com_9_digitos_cpf.append(int(digito) * contador_regressivo_1)
        contador_regressivo_1 -= 1
    
    soma_valores_1 = sum(lista_com_9_digitos_cpf)
    resultado_primeiro_digito = (soma_valores_1 * 10) % 11
    resultado_primeiro_digito = resultado_primeiro_digito if resultado_primeiro_digito <= 9 else 0

    # Cálculo do segundo dígito verificador
    lista_com_10_digitos_cpf = []
    contador_regressivo_2 = 11
    for digito in cpf[:10]:  # Inclui o primeiro dígito verificador
        lista_com_10_digitos_cpf.append(int(digito) * contador_regressivo_2)
        contador_regressivo_2 -= 1
    
    soma_valores_2 = sum(lista_com_10_digitos_cpf)
    resultado_segundo_digito = (soma_valores_2 * 10) % 11
    resultado_segundo_digito = resultado_segundo_digito if resultado_segundo_digito <= 9 else 0

    # Verificação final
    if resultado_primeiro_digito == int(cpf[9]) and resultado_segundo_digito == int(cpf[10]):
        cpf_padronizado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        print(f"\033[92mSucesso! CPF: {cpf_padronizado} é válido.\033[m")
        return cpf_padronizado
    else:
        print("\033[91mErro! CPF inválido.\033[m")
        return False

def valida_opcao_inteiro(variavel):
    if isinstance(variavel, int) or (isinstance(variavel, str) and variavel.isdigit()):
        var_int = int(variavel)
        if 1 <= var_int <= 12:
            return var_int
        else:
            print("\033[91mOpção selecionada não está no intervalo [1-12].\033[m")
    else:
        print("\033[91mA opção escolhida deve ser um número inteiro.\033[m")

def valida_inteiro(variavel):
    if isinstance(variavel, int):
        return variavel
    elif isinstance(variavel, str) and variavel.isdigit():
        return int(variavel)
    else:
        print("\033[91mPor favor, insira um valor numérico inteiro válido.\033[m")
        return None
    

class Validar:
    def valida_nome(self, nome):
        if not nome.replace(" ", "").isalpha():
            print("\033[91mNome do Usuário Invalido!\nPor favor, informe um Nome Válido.\033[m")
            return None
    
        nome_formatado = nome.title()
        return nome_formatado
    
    def valida_data_de_nascimento(self, dia, mes, ano):
        try:
            data = datetime(year=ano, month=mes, day=dia)
            if not (1900 <= ano <= 2025):
                print("Erro: Ano Invalido!")
                return False
            return True
        except ValueError:
            print("\033[91mData Inválida! Verifique dia ou mês.\033[m")
            return False
       
    def validacao_cpf(self, cpf):
        resultado = valida_cpf(cpf)
        return resultado
    def valida_email(self, email):
        # Expressão regular para validar formato de e-mail básico
        padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        # Verificando se o e-mail segue o padrão
        if re.match(padrao_email, email):
            return email
        else:
            print("\033[91mErro: Email não é válido.\033[m")
            return None

           