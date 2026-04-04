vs = int(input())

dic = {'A': 0,'E': 0, 'H': 0,'M': 0,'X': 0}


for _ in range(vs):
  nome,tipo = input().split()
  
  dic[tipo] += 1 
  
print(f'''{dic['X']} Hobbit(s)
{dic['H']} Humano(s)
{dic['E']} Elfo(s)
{dic['A']} Anao(oes)
{dic['M']} Mago(s)''')