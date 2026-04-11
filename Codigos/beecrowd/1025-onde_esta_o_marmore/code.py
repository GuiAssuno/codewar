import sys

# Lemos toda a entrada de uma vez só, ignorando espaços e linhas em branco
entrada = sys.stdin.read().split()

if not entrada:
    sys.exit()

idx = 0
caso = 1

while idx < len(entrada):
    n = int(entrada[idx])
    q = int(entrada[idx+1])
    idx += 2
    
    # Condição de parada do problema (N e Q iguais a zero)
    if n == 0 and q == 0:
        break
        
    print(f'CASE# {caso}:')
    
    marbles = []
    # Guarda os N mármores na lista
    for _ in range(n):
        marbles.append(int(entrada[idx]))
        idx += 1
        
    # Raju organiza os mármores em ordem crescente
    marbles.sort()
    
    # O Pulo do Gato: Dicionário para memorizar a primeira posição de cada mármore
    posicoes = {}
    
    for i in range(n):
        numero = marbles[i]
        # Se o número ainda não está no dicionário, nós o guardamos.
        # Isso garante que apenas a PRIMEIRA aparição dele seja salva!
        if numero not in posicoes:
            posicoes[numero] = i + 1 # +1 porque o problema conta a partir do 1 (e não do 0)
            
    # Respondendo às Q consultas da Meena
    for _ in range(q):
        consulta = int(entrada[idx])
        idx += 1
        
        # A busca no dicionário é imediata (O(1))
        if consulta in posicoes:
            print(f'{consulta} found at {posicoes[consulta]}')
        else:
            print(f'{consulta} not found')
            
    caso += 1

    