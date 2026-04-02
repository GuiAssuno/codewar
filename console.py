saida1 =''
saida2 =''
flag = 0


entrada = input()


for y in entrada:
    if y == "[":
        y = ''
        flag = 1
    
    if y == "]":
        y = ''
        flag = 0        

    if flag:
        saida1 += y
    else:
        saida2 += y

print(f"{saida1}{saida2}", end = "")
saida1 = saida2 = ''