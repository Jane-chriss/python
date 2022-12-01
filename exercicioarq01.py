from os import system
import os.path, datetime

arquivo = 'produtos.csv'

if os.path.isfile(arquivo):
    produtos = open(arquivo, 'r', encoding='utf-8')
    tamanho = os.path.getsize(arquivo)
    datamodificacao = os.path.getatime(arquivo)
    print(f'data de modificação: {datetime.datetime.fromtimestamp(datamodificacao)}')
    print(f'tamanho do arquivo(bytes): {tamanho}')

    listaprodutos = []
    for linha in produtos:
        colunas = linha.strip().split(";")
        print(colunas)
        colunas[0] = int(colunas[0])
        colunas[2] = int(colunas[2])
        colunas[4] = int(colunas[4])
        colunas[5] = int(colunas[5])
        colunas[6] = int(colunas[6])
        colunas[7] = int(colunas[7])
        colunas[8] = float(colunas[8])
        colunas[9] = float(colunas[9])

        listaprodutos.append(colunas)
    produtos.close()
    for prod in listaprodutos:
        print(prod)

#calculando total de custo
    totaldecusto = 0
    for prod in listaprodutos:
        totaldecusto += prod[9]
    print(f'total de custo: {totaldecusto}')

#calcular valor total de venda apenas das cerevejas

    totalvenda = 0
    for prod in listaprodutos:
        if 'cerveja' in str(prod[1]).lower():
            totalvenda += prod[8]
    print(f'total de venda: {totalvenda}')

    #exibe apenas os produtos inativos
    for prod in listaprodutos:
        if prod[7] ==1:
            print(prod)
    
    produtos.close()





