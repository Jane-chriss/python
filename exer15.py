#faça um programa que informe 3 numero, e indique qual o maior e qual o menor

import random

num1 = int(input('digite o numero 1º '))
num2 = int(input('digite o numero 2º '))
num3 = random.randint (0,100)
print(f'o terceiro numero é {num3}')


if num1 > num2 and num1> num3:
        print (f'o numero {num1} é o maior, os numeroa {num2} e {num3} são menores')

elif num2 > num1 and num2> num3:
           print (f'o numero {num2} é o maior, os numeros {num1} e {num3}, são menores')
else:
    print (f'o numero {num3} é o maior que o {num1} e {num2}, são menores')