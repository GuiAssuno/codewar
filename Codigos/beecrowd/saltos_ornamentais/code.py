<<<<<<< HEAD
n = int(input())


for i in range(n):
    nome  = input()
    gd    = float(input())
    notas = input().split()
    notas = sorted(notas)


    print(notas[1])
=======
casos = int(input())

for _ in range(casos):
    filt = []
    nota = 0
    
    nome = input()
    gd = float(input())
    notas = input().split()

    for n in notas:
        filt.append(float(n))
        nota += float(n)

    filt.sort()
   
    print (f'{nome} {((nota-(filt[0]+filt[6]))*gd):.2f}')



>>>>>>> c770c3145bab8a0b471ed7523d2633629de738df
