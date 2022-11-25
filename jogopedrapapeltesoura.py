from optparse import OptionContainer
from os import system
import random
system('cls')



titulo = 'Pedra | Papel | Tesoura'
print(titulo.center(60,'#'))


opcao = 's'
contadorjogadas = 0
contadorjogador = 0
contadorcomputador = 0
while opcao.upper() == 'S':
    system('cls')
    computador = random.randint(0,2)
    jogador = int(input('''escolha uma opção para se jogar
    [0] Pedra 
    [1] Papel 
    [2] tesoura
    Digite a sua escolha: '''))

    if jogador>=3:
        resultado = f'voce nao escolheu uma opção valida!'
        
    else:
        contadorjogadas += 1
        pecas = ('Pedra', 'Papel', 'Tesoura')
        print(f'voce escolheu {pecas[jogador]}')
        print(f'computador escolheu {pecas[computador]}')
        tabela = ((0,1,-1), (-1,0,1), (1,-1,0))
        jogada = tabela[computador] [jogador]
        if jogada ==0:
            resultado = f'deu empate'
        elif jogada == 1:
            resultado = f'voce ganhou'
            contadorjogador +=1
        elif jogada == -1:
            resultado = f'o computador ganhou'
            contadorcomputador +=1
    print (resultado)

    opcao = input('jogar novamente (S) para sim')

system('cls')

print('resumo do jogo'.center(60,'#'))
print(f'Quantidade de jogas: {contadorjogadas}')
print(f'você ganhou {contadorjogador} jogadas')
print(f'computador ganhou {contadorcomputador} jogadas')