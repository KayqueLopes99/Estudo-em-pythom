from random import randint
from datetime import datetime
import re

## Prontas! 
def valid_number(variable):
    if isinstance(variable, (int, float)): 
        return variable

    if isinstance(variable, str):  
        variable = variable.strip()  # Remove espaços extras
    
        if not variable:  # Se estiver vazio (Enter)
            print("\033[91mErro: Entrada vazia. Insira um número válido.\033[m")
            return None
        
        if variable.isdigit():  
            return int(variable)
        
        try:
            return float(variable)  
        except ValueError:
            print("\033[91mErro: Entrada inválida. Insira um número válido.\033[m")
            return None
    
    print("\033[91mErro: Tipo de dado inválido.\033[m")
    return None


def valid_option(variable):
    if isinstance(variable, int) or (isinstance(variable, str) and variable.isdigit()):
        integer_type_variable = int(variable)
        if 1 <= integer_type_variable <= 6:
            return integer_type_variable
        else:
            print("\033[91mOpção selecionada não está no intervalo [1-6].\033[m")
    else:
        print("\033[91mA opção escolhida deve ser um número inteiro.\033[m")





########################
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
                print("\033[91mErro: Ano Invalido!\033["
                "m")
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
