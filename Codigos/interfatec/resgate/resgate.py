n, r, s = map(int,input().split())

t = int(input())
t_loc = list(map(int,input().split()))

g = {} # graph
visited = [False]*(n+1)

p = int(input())
for _ in range(p):
    a,b = map(int, input().split())

    if a not in t_loc and b not in t_loc:
        if a not in g:
            g[a] = []
        
        if b not in g:
            g[b] = []

        g[a].append(b)
        g[b].append(a)

def dfs(current:int , target: int, g: dict, visited: list[bool]) -> bool:
    if current not in g:
        return False
    
    visited[current] = True
    
    if current == target:
        return True
    
    for next in g[current]:
        if not visited[next]:
            if dfs(next, target, g, visited):
                return True
        
    return False


if dfs(r,s,g, visited):
    print("PROSSEGUIR")
else:
    print("ABORTAR")




