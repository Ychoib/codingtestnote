import sys
sys.setrecursionlimit(10000)
n,m = map(int,input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)]
def dfs(y):
    visited[y] = 1
    for i in range(1,n+1):
        if graph[y][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)

