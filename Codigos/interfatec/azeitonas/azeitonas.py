x,y = map(int, input().split())

if x < 1 or x > 100 or y < 1 or y > 100 or x == y:
    print("ERRO")
else:
    print(x,y) 
    print(y,x) 
    print(y,-x)
    print(x,-y)
    print(-x,-y)
    print(-y,-x)
    print(-y,x)
    print(-x,y) 