# Função para encontrar a raiz (com compressão de caminho)
def encontrar(cidade, pai):
    if pai[cidade] == cidade:
        return cidade
    pai[cidade] = encontrar(pai[cidade], pai)
    return pai[cidade]

# Função para unir os grupos (com união por rank)
def unir(cidade1, cidade2, pai, rank):
    raiz1 = encontrar(cidade1, pai)
    raiz2 = encontrar(cidade2, pai)
    
    if raiz1 != raiz2:
        if rank[raiz1] < rank[raiz2]:
            pai[raiz1] = raiz2
        elif rank[raiz1] > rank[raiz2]:
            pai[raiz2] = raiz1
        else:
            pai[raiz2] = raiz1
            rank[raiz1] += 1
        return True
    return False

def resolver():
    # --- O SEGREDO PARA NÃO DAR RUNTIME ERROR NO BEECROWD ---
    # Este gerador lê palavra por palavra, ignorando espaços duplos e linhas em branco,
    # até o arquivo acabar (EOF - End Of File).
    def ler_numeros():
        while True:
            try:
                linha = input().split()
                for num in linha:
                    yield int(num)
            except EOFError:
                break
                
    gerador = ler_numeros()
    
    def proximo():
        return next(gerador)

    # --- INÍCIO DA LÓGICA ---
    try:
        n = proximo()
        f = proximo()
        r = proximo()
    except StopIteration:
        return # Se a entrada for completamente vazia, encerra em segurança

    conexoes = []

    # Lendo as Ferrovias (Tipo 0 - Prioridade máxima)
    for _ in range(f):
        u = proximo()
        v = proximo()
        custo = proximo()
        conexoes.append((0, custo, u, v))

    # Lendo as Rodovias (Tipo 1)
    for _ in range(r):
        u = proximo()
        v = proximo()
        custo = proximo()
        conexoes.append((1, custo, u, v))

    # Ordena: 1º pelo tipo (0 antes de 1), 2º pelo custo (menor para o maior)
    conexoes.sort()

    # Inicializando o Union-Find
    pai = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    custo_total = 0
    arestas_usadas = 0

    # Construindo a Árvore Geradora Mínima (Kruskal)
    for tipo, custo, u, v in conexoes:
        if unir(u, v, pai, rank):
            custo_total += custo
            arestas_usadas += 1
            
            # Uma rede que conecta N cidades precisa de N - 1 ligações
            if arestas_usadas == n - 1:
                break

    # Saída esperada pelo Beecrowd (apenas o número)
    print(custo_total)

# Executa o programa
resolver()