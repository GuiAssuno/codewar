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
