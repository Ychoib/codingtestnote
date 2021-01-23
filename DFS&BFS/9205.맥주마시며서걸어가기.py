t = int(input())

def dfs(start):
    visited[start] = 1
    for i in range(n+2):
        if graph[start][i] == 1 and visited[i] == 0:
            dfs(i)
while t:
    n = int(input())
    s = [list(map(int,input().split())) for i in range(n+2)]
    graph = [[0] * (n+2) for i in range(n+2)]
    visited = [0 for i in range(n)]
    #양방향 그래프 만들어주기
    for i in range(n+2):
        for j in range(n+2):
            # 각 좌표의 x,y좌표가 1000보다 적다면 서로 이어주기
            if abs(s[i][0] - s[j][0]) + abs(s[i][1] -s[j][1]) <= 1000:
                graph[i][j] = 1
                graph[j][i] = 1
    dfs(0)
    if visited[n+1] == 1: print("happy")
    else: print("sad")