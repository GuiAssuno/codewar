casos = int(input())

dic = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for _ in range(casos):
    infixa = input().strip()
    pilha = []
    saida = ''
    
    for x in infixa:
        if x.isalnum():
            saida += x
            
        elif x == '(':
            pilha.append(x)
            
        elif x == ')':
            while pilha and pilha[-1] != '(':
                saida += pilha.pop()
            if pilha and pilha[-1] == '(':
                pilha.pop() 
                
        else:
            while pilha and pilha[-1] != '(' and dic[x] <= dic.get(pilha[-1], 0):
                saida += pilha.pop()
            pilha.append(x)
            
    while pilha:
        saida += pilha.pop()
        
    print(saida)