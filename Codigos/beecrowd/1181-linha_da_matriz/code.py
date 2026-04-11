TAM = 12
m = [[0]*12] * 12
som = cont = 0


linha = int(input())
opc = input()

for i in range ((TAM * TAM)):
    m[(i//TAM)][(i%TAM)] = float(input())

    if ((i//TAM)) == linha:
        som += m[(i//TAM)][(i%TAM)]
        cont += 1

if opc == 'S':
    print(f'{som:.1f}')
elif opc == 'M':    
    print(f'{(som/cont):.1f}')
