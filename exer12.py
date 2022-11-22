from os import system
import random
system('cls')

#print(random.randint (0,100))
num = random.randint(0,100)

#numero escolhido é par ou impar

resto = num % 2
if resto == 0:
    print('o numero escolhido é par')
else:
    print('o numero escolhido é impar')
    #print(f'o numero escolhido é impar ')

#o numero escolhido é maior que 50 ou menos
#mais perto do 100 ou do 0
if num < 50:
    print ('numero esta mais perto do 0')
else:
    print ('numero esta mais perto do 100')

#numero escolhido é primo
#para escolher precisa de uma estrutura de repetição






