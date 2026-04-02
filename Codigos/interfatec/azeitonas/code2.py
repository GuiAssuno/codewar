x,y = map(int,input().split() )


if (x != y) and ((x > 1 )and (x < 101)) and ((y > 1 )and (y < 101)):
    print(f"{x} {y}")
    print(f"{y} {x}")
    print(f"{y} -{x}")
    print(f"{x} -{y}")
    print(f"-{x} -{y}")
    print(f"-{y} -{x}")
    print(f"-{y} {x}")
    print(f"-{x} {y}")

else:
    print('ERRO')