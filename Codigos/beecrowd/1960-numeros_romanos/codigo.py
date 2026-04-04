# Adicionamos uma string vazia no índice 0 de cada lista
uni = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
dec = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
cen = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

n = input()
n = n.zfill(3)

f = cen[int(n[0])] + dec[int(n[1])] + uni[int(n[2])]

print(f)