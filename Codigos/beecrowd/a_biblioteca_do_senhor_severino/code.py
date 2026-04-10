while True:
    try:
        total = int(input())
        livros = []
        for i in range(total):
            livros.append(int(input()))

        livros.sort()

        for x in range((len(livros))):
            print(str(livros[x]).zfill(4))
    except :
        break
