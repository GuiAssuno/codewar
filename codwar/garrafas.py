def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    while idx < len(input):
        A, B = int(input[idx]), int(input[idx + 1])
        idx += 2
        res = 0
        for i in range(2, A + 1):
            print("Valor de i: {}".format(i))
            print(f"Valor de (res+B): {res + B}")
            res = (res + B) % i
            
            print(f"valor de res == >  {res}")
        print("ultimo : " + str(res + 1))

if __name__ == "__main__":
    main()