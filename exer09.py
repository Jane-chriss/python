#vamos trabalhar com dados de texto, usando varios metiodos para verificar e modificar o valor de uma variavel de clss srt

from os import system
system('cls')
nomecompleto = input ('informe seu nome completo ')

#tamanho da minha string | tamanho de caracteres

print ('1. total de caracteres:', len(nomecompleto))

#acessando caracter a partir da posição
print ('2. o caracter da posição 2 é: ' ,nomecompleto [2])

#transformando maiuscula | minuscula
print ('3. texto em maiuscula', nomecompleto.upper())
print ('4. texto em maiuscula', nomecompleto.lower())
print ('5. texto em maiuscula', nomecompleto.capitalize())

#apurar a posi~çao de um determinado caracter
print ('6. posição do caracter espaço ' , nomecompleto.find (' '))

#fatiar uma string ate uma determinada posição
espaco = nomecompleto.find (' ')
print ('7. somente o primeiro nome: ' , nomecompleto[0:espaco])

#substituir um caracter por outro
print ('8. nome sem espaço: ' , nomecompleto.replace(' ', ''))

#verificar somente letra e numeros
print ('9. tem somente letras?' , nomecompleto.replace (' ', '').isalpha())
print ('10. é alfa numerico?' , nomecompleto.replace (' ', '').isalnum())

#quebrar o texto em partes especificas retornando array
print ('11. quebrar o texto a cada espaço em branco' , nomecompleto.split(" "))

#centralizar texto usando * para completar as laterais
print ('12. centralizar o texto entre *' , nomecompleto.center(80,"*"))





