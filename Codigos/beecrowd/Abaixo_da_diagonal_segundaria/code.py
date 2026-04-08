TAM = 12
m = [[0]*TAM] * TAM
con = sum = 0


op = input()



for i in range((TAM*TAM)):    
    n = float(input())
    m[(i//TAM)][(i%TAM)] = n



    if ((i//TAM)+(i%TAM)) > (TAM-1):
        sum += n
        con += 1



if op == "S":
    print(f'{sum:.1f}')
else:
    print(f'{(sum/con):.1f}')