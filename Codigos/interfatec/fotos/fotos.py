arr = []
n = 0

while True:
    try:
        nk = int(input())
        arr.append(nk)
        n += nk        

    except EOFError:
        break

for nk in arr:
    prk = nk/n
    print(f'{prk:.3f}')