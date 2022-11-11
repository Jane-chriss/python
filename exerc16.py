#programa que pergunte em que turno você estuda
#peça para digitar M matutino | V vespertino | N noturno
#imprima a mensagem "bom dia", "boa tarde" ou "boa noite"

periodo = input('digite o periodo que você estuda, Digite M para matutino | V para vespertino ou N para noturno ')


if periodo.lower() == 'm' :
    print('Bom dia')

elif periodo.lower() == 'v' :
    print ('boa tarde')

elif periodo.lower() == 'm' :
    print ('boa noite')

else:
    print('turno não existe')




