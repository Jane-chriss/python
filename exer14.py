
import random


num1 = random.randint(0,100)
print(f'o numero é {num1}')
num2 = random.randint(0,100)
print(f'o numero é {num2}')
num3 = random.randint(0,100)
print(f'o numero é {num3}')


if num1 > num2 and num1> num3:
        print (f'o numero {num1} é o maior')

elif num2 > num1 and num2> num3:
           print (f'o numero {num2} é o maior')
else:
    print (f'o numero {num3} é o maior que o {num1} e que {num2}')

