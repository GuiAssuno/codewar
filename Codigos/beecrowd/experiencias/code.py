n=int(input())
dic = {'C': 0,'R': 0,'S': 0}
total = 0

for _ in range(n):
    inp = input().split()   
    total = total + int(inp[0])
    dic[inp[1].upper()] = dic[inp[1].upper()] + int(inp[0])
    

msg = f"""Total: {total} cobaias
Total de coelhos: {dic['C']}
Total de ratos: {dic['R']}
Total de sapos: {dic['S']}
Porcentual de coelhos: {((dic['C']/total)*100):.2f} %
Porcentual de ratos: {((dic['R']/total)*100):.2f} %
Porcentual de sapos: {((dic['S']/total)*100):.2f} %
"""

print(msg)
