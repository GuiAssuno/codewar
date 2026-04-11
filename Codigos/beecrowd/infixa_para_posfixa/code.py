casos = int(input())

dic = {'^': 3, ['*','/',]:2 , ['+', '-']:1}

for _ in range(casos):
    infixa = input()
    pilha = []
    saida = ''
    for x in infixa:
        if x in op:
             
        else:
            saida += x