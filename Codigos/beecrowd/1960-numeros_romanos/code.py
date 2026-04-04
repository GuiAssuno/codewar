uni = ['','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
dec = ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
cen = ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

ro = [cen, dec, uni]

n = input()
f = ''
if 3 == len(n):
    f += (ro[0][int(n[0])])
    f += (ro[1][int(n[1])])
    f += (ro[2][int(n[2])])

elif 2 == len(n):
    f += (ro[1][int(n[0])])
    f += (ro[2][int(n[1])])

elif 1 == len(n):
    f += (ro[2][int(n[0])])

print(f)

#print(f'{(ro[0][int(n[0])-1])}{(ro[1][int(n[1])-1])}{(ro[2][int(n[2])-1])}')
