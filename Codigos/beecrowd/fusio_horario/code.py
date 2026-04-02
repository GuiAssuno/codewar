m,p,c = 0

for _ in range(100):
    x = int(input())
    c += 1
    if c == 1:
        m = x
        p = c 
    
    if(x > m):
        m = x
        p = c

print(p)
print(m)