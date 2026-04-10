entradas = int(input())
impar = []
par = []
for i in range(entradas):
    n = int(input())

    if (n % 2):
        impar.append(((n*-1)))
    else:
        par.append(n)

par.sort()
impar.sort()


for z in par:
    print(i)
for z in impar:
    print(z)
