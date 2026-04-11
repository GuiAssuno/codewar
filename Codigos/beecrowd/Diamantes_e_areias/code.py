casos = int(input())
soma = 0
for _ in range(casos):
    mina = input()

    cont = ant = 0
    final = bag = ponto = ''
    
    while True:
        for x in mina:
            if x == '.':
                ponto += x
                continue
                
            if x == '<' and bag == '<':
                bag = x
                final += bag + ponto
                ponto = ''
                continue

            elif x == '<' and bag == '':
                bag = x
                final += ponto
                continue

            if x == '>' and bag == '<':
                cont += 1
                soma += 1
                bag = ''
                ponto = ''
                continue
            elif x == '>' and bag == '':
                final += ponto + x
                ponto = ''
                continue
        
        if cont == ant:
            break
        else:
            mina = final 
            ant = cont
            final,cont = '', 0

    print(soma)
    soma = 0