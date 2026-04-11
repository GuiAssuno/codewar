pilha = []

num = int(input())

for _ in range(num):
    ope = input().split()
    if (len(pilha) == 0) and (ope[0] == 'MIN' or ope[0] == 'POP'):
        print('EMPTY')    
    elif ope[0] == 'PUSH':
        pilha.append(int(ope[1]))
    elif ope[0] == 'POP':
        pilha.pop()
    elif ope[0] == 'MIN':
        temp = sorted(pilha)
        print(temp[0])







# import sys

# entrada = sys.stdin.read().splitlines()

# if not entrada:
#     sys.exit()

# num = int(entrada[0])
# pilha = []
# minimos = []  # <--- AQUI ESTAVA O PROBLEMA! Faltou criar a lista auxiliar

# for i in range(1, num + 1):
#     ope = entrada[i].split()
    
#     if len(pilha) == 0 and (ope[0] == 'MIN' or ope[0] == 'POP'):
#         print('EMPTY')    
        
#     elif ope[0] == 'PUSH':
#         valor = int(ope[1])
#         pilha.append(valor)
        
#         if len(minimos) == 0 or valor <= minimos[-1]:
#             minimos.append(valor)
            
#     elif ope[0] == 'POP':
#         removido = pilha.pop()
        
#         if removido == minimos[-1]:
#             minimos.pop()
            
#     elif ope[0] == 'MIN':
#         print(minimos[-1])