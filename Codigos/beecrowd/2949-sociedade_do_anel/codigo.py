n = int(input())

comitiva = {'X': 0, 'H': 0, 'E': 0, 'A': 0, 'M': 0}

for _ in range(n):
    # A entrada tem o formato: "Nome Raca"
    entrada = input().split()
    raca = entrada[1]  # A raça é o segundo elemento
    
    # Incrementamos a contagem da raça
    if raca in comitiva:
        comitiva[raca] += 1

# Saída formatada na ordem exigida pelo problema
print(f"{comitiva['X']} Hobbit(s)")
print(f"{comitiva['H']} Humano(s)")
print(f"{comitiva['E']} Elfo(s)")
print(f"{comitiva['A']} Anao(oes)")
print(f"{comitiva['M']} Mago(s)")