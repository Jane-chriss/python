from recibo import Recibo
from os import system
system('cls')

novoRecibo = Recibo('jhoão')
novoRecibo.valor = 1258.20
novoRecibo.descricao('desenvolvimento de sistemas em python')

#print(novoRecibo.nome, novoRecibo.valor, novoRecibo._descricao)

print(novoRecibo)

