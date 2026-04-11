casos = int(input())
soma = 0
for _ in range(casos):
    mina = input()

    cont = 0
    final = ''
    bag = ''
    ponto = ''
    
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
        
        if cont == 0:
            break
        else:
            mina = final 
            cont = 0
            bag=ponto=final= ''


    print(soma)
    soma = 0















# casos = int(input())

# for _ in range(casos):
#     mina = input()
    
#     diamantes = 0
#     metades_abertas = 0 # Conta quantos '<' estão esperando um '>'
    
#     for pedaco in mina:
#         if pedaco == '<':
#             metades_abertas += 1 # Guarda a metade do diamante
            
#         elif pedaco == '>' and metades_abertas > 0:
#             diamantes += 1       # Fechou o diamante!
#             metades_abertas -= 1 # Tira a metade que foi usada da espera
            
#     print(diamantes)