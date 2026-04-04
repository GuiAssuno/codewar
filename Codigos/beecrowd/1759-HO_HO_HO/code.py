# Lendo a quantidade de vezes que o Papai Noel vai falar "Ho"
n = int(input())

# Um laço de repetição que vai rodar (N - 1) vezes.
# Se N for 5, esse laço vai rodar 4 vezes.
for i in range(n - 1):
    # O segredo está no end=" "
    # Ele impede que o Python pule de linha e já coloca o espaço necessário
    print("Ho", end=" ")

# O último "Ho" fica de fora do laço para receber a exclamação colada
# Como é o último print, ele pula a linha normalmente no final
print("Ho!")