n,f,r = map(int,input().split())

# fer = [0]*f
# rod = [0]*r

# for i in range((f+r)):
#     a, b, c = map(int,input().split())
#     if i < f:
#         fer[i] = (a, b, c, 'F')    
#     else:
#         rod[i-f] = (a, b, c, 'R')


# esc = []

nf = ( (n-1)//2 + 1 if (n-1)//2 + 1 < f else f )   
nr = (n -1) - nf 

g= 1
y = 1
print(nf)
print(nr)

for k in range((((f-nf)*nf)+1), f+1):
    x = k * g
    g += 1
    print(k)
g= 1

for k in range((((r-nr)*nr)+1), r+1):
    y = k * g
    g += 1
    print(k)

w = x*y

#for i in range():
    







print(w)
#print(nf)
#print(nr)
#print(fer[2][2])
#print(rod)
#print(((n//2) + (n%2)))


