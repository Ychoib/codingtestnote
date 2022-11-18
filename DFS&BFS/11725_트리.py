

N = int(input())
visited = [0] * (N + 1)

dict_ = dict()
for i in range(N + 1):
    dict_[i] = []
def dfs(v):
    visited[v] = 1
    #print(v, end = " ")
    for i in range(N+1):
        if visited[i] == 0 and maps[v][i] == 1:
            dict_[v].append(i)
            dfs(i)
    #print(dict_)
maps = [[0 for i in range(N + 1)] for i in range(N+1)]
for i in range(N - 1 ):
    x,y = map(int,input().split())
    maps[x][y] = maps[y][x] = 1
    
dfs(1)
for i in range(2,N+1):
    print([key for key, value in dict_.items() if i in value][0])
    
    