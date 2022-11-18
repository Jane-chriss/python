from os import system
system('cls')
import random

titulo = 'jogo da adivinhação'
print(titulo.center(120,'*'))

num = random.randint(1,10)

tentativa = int(input('Adivinhe o numero de 1 a 10: (0 - para sair)'))

while tentativa>0:
    if tentativa>num:
        print('é menor, tente de novo')
    elif tentativa<num:
        print('é maior, tente de novo')
    else: 
        print(f'uhuuu vc acertou - {num}')
        break
    tentativa = int(input('Adivinhe o numero de 1 a 10: (0 - para sair)'))
