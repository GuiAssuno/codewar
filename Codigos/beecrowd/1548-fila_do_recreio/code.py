casos = int(input())

for i in range(casos):
    nAlunos = int(input()) 
    notas = input().split()
    reord = [0] * nAlunos
    lugar = 0

    for a in enumerate(notas):
        reord[a[0]] = (-int(a[1]), a[0])
    
    reord.sort()

    for z in range(len(reord)):
        if z == reord[z][1]:
            lugar += 1

    print(lugar)











# casos = int(input())

# for i in range(casos):
#     nAlunos = int(input()) 
    
#     # 1. Converte tudo para inteiro de uma vez
#     notas_originais = [int(x) for x in input().split()]
    
#     # 2. Cria uma cópia da lista e já ordena de forma decrescente (reverse=True)
#     notas_ordenadas = sorted(notas_originais, reverse=True)
    
#     lugar = 0
    
#     # 3. Compara quem ficou no mesmo lugar nas duas listas
#     for z in range(nAlunos):
#         if notas_originais[z] == notas_ordenadas[z]:
#             lugar += 1

#     print(lugar)