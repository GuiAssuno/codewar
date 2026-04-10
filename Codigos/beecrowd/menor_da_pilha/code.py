pilha = []

num = int(input())

for _ in range(num):
    ope = input().split()
    if (pilha is None) and (ope[0] == 'MIN' or ope == 'POP'):
        print('EMPTY')    
    elif ope[0] == 'PUSH':
        pilha.append(int(ope[1]))
    elif ope[0] == 'POP':
        pilha.pop()
    elif ope[0] == 'MIN':
        print(min(pilha))
