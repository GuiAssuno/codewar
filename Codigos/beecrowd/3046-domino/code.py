n = int(input())

# Aplicando a fórmula exata que o problema nos deu: ((N + 1) * (N + 2)) / 2
# Usamos '//' para garantir que a divisão seja inteira, sem o '.0' no final
quantidade_pecas = ((n + 1) * (n + 2)) // 2

# Imprimindo apenas o número do resultado
print(quantidade_pecas)