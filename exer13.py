#faça um programa qyue receba 2 numeros e informe qual numero é o maior

from os import system
import random
system('cls')


num1 = int(input('digite o primeiro valor '))
num2 = random.randint(0,100)
print (f'o numero escolhido é {num2}')

if num1 > num2:
        print (f'o numero {num1} é o maior que o {num2}')
else:
    print (f'o numero {num2} é o maior que o {num1}')

   
