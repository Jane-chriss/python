from os import system
system('cls')

titulo = ' calculadora Simples '
print(titulo.center(60, '#'))

print('escolha uma das opções do menu')
print('(+) - adicao\n(-) - subtração\n(*) - multiplicação \n(/) - divisão')
opcao = input('Opção: ')


while opcao != 's' :
      
    num1 = float(input('informe o valor'))
    num2 = float(input('informe o valor'))

    if opcao == '+':
        resultado = num1+num2
    if opcao =='-':
        resultado = num1-num2
    if opcao =='*':
        resultado = num1*num2
    if opcao =='/':
        resultado = num1/num2
    print(f'voce escolheu a operação de {opcao} o resultado é: {resultado}')

    print('escolha uma das opções do menu')
print('(+) - adicao\n(-) - subtração\n(*) - multiplicação \n(/) - divisão')
opcao = input('Opção: ')





