# -*- coding: utf-8 -*-

entrada = []
while True:
    try:
        linha = input().split()
        for pedaco in linha:
            entrada.append(int(pedaco))
    except EOFError:
        break

if len(entrada) > 0:
    n = entrada[0]
    f = entrada[1]
    r = entrada[2]
    posicao_atual = 3
    
    conexoes = []
    for i in range(f):
        cidade_u = entrada[posicao_atual]
        cidade_v = entrada[posicao_atual + 1]
        custo = entrada[posicao_atual + 2]
        conexoes.append([0, custo, cidade_u, cidade_v])
        
        posicao_atual = posicao_atual + 3

    for i in range(r):
        cidade_u = entrada[posicao_atual]
        cidade_v = entrada[posicao_atual + 1]
        custo = entrada[posicao_atual + 2]
        
        conexoes.append([1, custo, cidade_u, cidade_v])
        posicao_atual = posicao_atual + 3

    conexoes.sort()

    pai = []
    for i in range(n + 1):
        pai.append(i)

    def acha_chefe(cidade):
        if pai[cidade] == cidade:
            return cidade
        chefe_de_verdade = acha_chefe(pai[cidade])
        pai[cidade] = chefe_de_verdade
        return chefe_de_verdade

    custo_total = 0
    estradas_construidas = 0

    for conexao in conexoes:
        tipo = conexao[0]
        custo = conexao[1]
        cidade1 = conexao[2]
        cidade2 = conexao[3]

        chefe1 = acha_chefe(cidade1)
        chefe2 = acha_chefe(cidade2)

        if chefe1 != chefe2:
            pai[chefe1] = chefe2
            
            custo_total = custo_total + custo
            estradas_construidas = estradas_construidas + 1
            
            if estradas_construidas == n - 1:
                break

    print(custo_total)