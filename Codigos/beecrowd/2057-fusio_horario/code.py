s, t, f = map(int, input().split())
n = s

for _ in range(t):
    n = n + 1
    if n == 24: 
        n = 0


for i in range(abs(f)):
    if f >= 0:
        n = n + 1
        if n == 24:
            n = 0
    else:
        n = n - 1
        if n == -1: 
            n = 23

print(n)