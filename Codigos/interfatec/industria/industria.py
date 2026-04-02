while True:
    try:
        a,b = map(int,input().split())

        
        arr = list(range(1, a+1))
        n = len(arr)
        i = b

        while n > 1:
            while i > n:
                i = i-n

            del arr[i-1]
            i += b-1
            n -= 1

        print(arr[0])

    except EOFError:
        break