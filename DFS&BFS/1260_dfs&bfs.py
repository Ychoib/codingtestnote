
n,m,v = map(int,input().split())
maps = [[0 for i in range(n+1)] for i in range(n+1)]
visited = [0 for i in range(n+1)]

def dfs(v):
    print(v,end = ' ')
    visited[v] = 1
    for i in range(1,n+1):
        if visited[i] == 0 and maps[v][i] == 1:
            dfs(i)

def bfs(v):
    q = [v]
    visited[v] = 0
    while q:
        v = q.pop(0)
        print(v,end = ' ')
        for i in range(1,n+1):
            if visited[i] == 1 and maps[v][i] == 1:
                q.append(i)
                visited[i] = 0


for i in range(m):
    x,y = map(int,input().split())
    maps[x][y] = 1
    maps[y][x] = 1
dfs(v)
print()
bfs(v)

