casos = int(input())
ordem = []
msg = ''
index = 0

for i in range(casos):
    frase = input().split()
    for x in frase:
        ordem.append((-(len(x)),index,x,))
        index += 1

ordem.sort()   

for a in ordem:
    msg += a[2] + ' '

print(msg.strip())
