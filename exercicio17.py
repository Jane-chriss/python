nota1 = float(input('digite a nota  '))
nota2 = float(input('digite a nota 2 '))
nota3 = float(input('digite a nota 3 '))

media = (nota1+nota2+nota3)/3

if media < 7:
    print('reprovado')
elif media >=7:
    print('aprovado')