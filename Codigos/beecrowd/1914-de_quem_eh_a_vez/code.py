n = int(input())


for _ in range((n)):
    try:
        a = input().split()
        b,c = map(int,input().split())

        x = (b + c)%2

        if x == 0:
            if a[1] == 'PAR':
                print(a[0])
            else: 
                print(a[2])
        else:
            if a[1] == 'IMPAR':
                print(a[0])
            else:
                print(a[2])
    except:
        break
