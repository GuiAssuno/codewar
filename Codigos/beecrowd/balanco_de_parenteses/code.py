pilha = []

try:
    expre = input().strip()
    pilha = []
    for c in expre:

        if c == ')' and ('(' not in pilha):
            pilha.append(')')
        elif c == ')' and '(' in pilha:
            pilha.pop()
        
        elif c == '(':
            pilha.append('(')


    if not pilha:
        print('correct')
    else:
        print('incorrect')

except EOFError:
    None
