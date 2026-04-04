# Lê a linha inteira digitada e corta nos espaços em branco
valores = input().split()

# Pega o primeiro pedaço (índice 0), converte para inteiro e guarda no H (Cachorros-quentes)
h = int(valores[0])

# Pega o segundo pedaço (índice 1), converte para inteiro e guarda no P (Participantes)
p = int(valores[1])

# Calcula a média (usamos a divisão normal com '/' porque queremos um número decimal)
media = h / p

# Imprime o resultado com exatamente 2 casas decimais
print(f"{media:.2f}")