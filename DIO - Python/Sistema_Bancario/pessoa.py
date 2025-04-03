from datetime import datetime
import os
from random import randint
from time import sleep
from valida import valida_numero, valida_opcao

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def depositar(historico, saldo, valor):
        LIMITE_DE_DEPOSITO = 10000
        horario = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        if valor <= 0:
            print("\033[91mErro: O valor do depósito deve ser maior que zero.\033[m")
            return saldo
        

        saldo_atual = saldo
        limite_atual = LIMITE_DE_DEPOSITO
     
        if saldo_atual + valor > limite_atual:
            print(f"\033[91mErro: O saldo total não pode ultrapassar o limite do banco ({limite_atual}).\033[m")
            return saldo   
        
        saldo_atual += valor   
        saldo = saldo_atual
        historico.append(f"Depósito de R$ {valor:.2f} - Realizado em {horario}")

        print(f"\033[92mDepósito de {valor:.2f} realizado com sucesso! Novo saldo: {saldo:.2f}\033[m")
        return saldo

7

def sacar(historico, saldo, valor, saques_diarios, limite):
        LIMITE_DO_SAQUE = 1000
        horario = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        if valor > LIMITE_DO_SAQUE:
            print(f"Você não pode sacar mais que R${LIMITE_DO_SAQUE} por saque.")
            return saldo, saques_diarios, limite

        if valor <= 0:
            print("\033[91mErro: O valor do depósito deve ser maior que zero.\033[m")
            return saldo, saques_diarios, limite
        
        if saques_diarios == 0:
            print(f"\033[91mVocê atingiu o limite de saques diários.\033[m")
            return saldo, saques_diarios, limite

        saldo_disponivel = saldo + limite  

        print(f"O saldo atual: R$ {saldo:.2f} | Limite disponível: R$ {limite:.2f}")

        if valor > saldo_disponivel:
            print(f"Erro: Saldo insuficiente para realizar o saque de {valor}.")
            return saldo, saques_diarios, limite
        
        valor_sacado = valor

        if valor <= saldo:
            saldo -= valor

        else:
            diferenca = valor - saldo  
            saldo = 0  
            limite -= diferenca  

       
        historico.append(f"Saque de R$ {valor_sacado:.2f} - Realizado em {horario}")
        saques_diarios -= 1

        print(f"\033[92mSaque de R$ {valor_sacado:.2f} realizado! Novo saldo: R$ {saldo:.2f} | Novo limite: R$ {limite:.2f}\033[m")

        return saldo, saques_diarios, limite


def imprimir(historico):
    indice = 1
    print("-"*42)
    print("\033[38;5;136m============ Extrato da Conta ============\033[m")
    for extrato in historico:  
        print(f"\033[38;5;136m{indice}*: {extrato}\033[m") 
        indice += 1
    print("-"*42)
    




def menu():
    print("-"*42)
    print("\033[38;5;136m===== Bem-vindo ao Banco FinTechOne! =====\033[m")
    sleep(0.3)
    print("\033[38;5;136m===== Menu de Opções =====\033[m")
    sleep(0.3)
    print("\033[38;5;21m[1] - Sacar.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[2] - Depositar.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[3] - Extrato.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[4] - Sair do Sistema Bancário.\033[m")
    sleep(0.3)
    print("-"*42)

def executar():
    historico = [] 
    saldo = 0
    saques_diarios = 3  
    
    limite_do_saque = 1000
    
    while True:
        menu()
        opcao = valida_opcao(input("Informe uma opção do menu acima: "))
        

        if opcao is None:
            print("\033[91mErro: Opção inválida. Tente novamente.\033[m")
            continue

        match opcao:
            case 1:


                while True:
                  valor = valida_numero(input("Informe o valor a ser sacado: "))
    
                  if valor is not None:  
                      saldo, saques_diarios, limite_do_saque = sacar(historico, saldo, valor, saques_diarios, limite_do_saque)
                      break  
                  else:
                      print("\033[91mTente novamente.\033[m")   

                
                

            case 2:
                while True:
                  valor = valida_numero(input("Informe o valor a ser depositado: "))
    
                  if valor is not None:  
                      saldo = depositar(historico, saldo, valor)
                      break  
                  else:
                      print("\033[91mTente novamente.\033[m")  

                
            
                
            case 3:
                print("\033[38;5;21m[5] - Extrato.\033[m")
                imprimir(historico)

            case 4:
                print("\033[92mSaindo do Sistema Bancário. Volte Sempre!\033[m")
                sleep(5)
                limpar_tela()
                break