import sys
sys.setrecursionlimit(50000)
n = int(input())
cnt = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    non[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if non[nx][ny] == 1:
            dfs(nx,ny)


for i in range(n):
    r, c, k = map(int, input().split())
    non = [[0 for i in range(c)] for i in range(r)]
    for j in range(k):
        x, y = map(int,input().split())
        non[x][y] = 1
    for a in range(r):
        for b in range(c):
            if non[a][b] == 1:
                dfs(a,b)
                cnt += 1
    print(cnt)
    cnt = 0


