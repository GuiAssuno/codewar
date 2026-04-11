TAM = 12
m = [[0]*TAM] * TAM
con = suma = 0

op = input()

for i in range((TAM*TAM)):    
    n = float(input())
    m[(i//TAM)][(i%TAM)] = n

    if ((i//TAM)+(i%TAM)) > (TAM-1):
        suma += n
        con += 1

if op == "S":
    print(f'{suma:.1f}')
else:
    print(f'{(suma/con):.1f}')




#TAM = 12
#m = [[0]*12] * 12
#som = cont = 0

#opc = input()

#for i in range ((TAM * TAM)):
#    m[(i//TAM)][(i%TAM)] = float(input())

#    if ((i//TAM)+(i%TAM)) > (TAM):
#        som += m[(i//TAM)][(i%TAM)]
#        cont += 1

#if opc == 'S':
#    print(f'{som:.1f}')
#elif opc == 'M':    
#    print(f'{(som/cont):.1f}')


# List Comprehension

# linhas = 3
# colunas = 4

# # Cria uma matriz 3x4 preenchida com zeros
# matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

# print(matriz)
# # Resultado: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



# Passo a Passo

# linhas = 3
# colunas = 4
# matriz = []

# for i in range(linhas):
#     linha_vazia = [0] * colunas   # Cria uma lista com 4 zeros
#     matriz.append(linha_vazia)    # Guarda essa lista dentro da matriz principal





# Usando NumPy

# import numpy as np

# # Cria uma matriz 3x4 cheia de zeros automaticamente
# matriz = np.zeros((3, 4))


