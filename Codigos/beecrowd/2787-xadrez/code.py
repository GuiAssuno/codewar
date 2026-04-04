# Lendo a quantidade de linhas e colunas
l = int(input())
c = int(input())

# Somando a linha e a coluna
soma = l + c

# O símbolo '%' (módulo) pega o resto da divisão. 
# Se o resto da divisão por 2 for zero, o número é par.
if soma % 2 == 0:
    # Se for par, a casa é branca
    print(1)
else:
    # Se for ímpar, a casa é preta
    print(0)