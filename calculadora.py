from os import system
system('cls')

def soma(v1,v2):
    return v1+v2

def subtracao(v1,v2):
    return v1-v2

def multiplicacao(v1,v2):
    return v1*v2

def divisao(v1,v2):
    if v1==0 or v2==0:
        return False
    return v1/v2

opcao=1
while opcao:
    v1 = float(input('informe o valor 1: '))
    v2 = float(input('informe o valor 2: '))
    
    operador = int(input('''
    1. somar
    2.subtrair
    3.multiplicar
    4.dividir
    '''))
    
    if operador ==1:
        print(f'soma: {soma(v1,v2)}')
        
    if operador ==2:
        print(f'subtração: {subtracao(v1,v2)}')

    if operador ==3:
        print(f'multiplicação: {multiplicacao(v1,v2)}')

    if operador ==4:
        print(f'divisao: {divisao(v1,v2)}')
    
    opcao = input(f'\n Aperte 0 para sair ou Enter para continuar')
    if opcao == '0':
        opcao=int(opcao)
    else:
        opcao=1
        system('cls')

