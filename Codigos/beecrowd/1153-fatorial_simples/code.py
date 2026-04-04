n = int(input())

# O fatorial começa sempre valendo 1 (se começasse em 0, a multiplicação zeraria tudo)
fatorial = 1

# O laço 'for' vai rodar de 1 até o valor de N. 
# O '+ 1' no range é necessário porque o Python sempre para um número antes.
for i in range(1, n + 1):
    # Multiplicamos o valor atual do fatorial pelo próximo número da sequência
    fatorial = fatorial * i

# Por fim, imprimimos apenas o resultado, sem nenhum texto extra
print(fatorial)