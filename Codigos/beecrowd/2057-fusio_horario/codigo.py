s, t, f = map(int, input().split())

# Soma saída, tempo de viagem e o fuso, depois ajusta pro ciclo de 24h
chegada = (s + t + f) % 24

# Imprime o resultado
print(chegada)