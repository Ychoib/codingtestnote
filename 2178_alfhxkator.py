n,m = map(int,input().split())
maps = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
check = [[0 for _ in range(m)] for _ in range(n)]
def bfs(x,y):
    q = [[x,y]]
    check[x][y] = 1
    while q:
        temp = q.pop(0)

        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1 and check[nx][ny] == 0:
                q.append([nx,ny])
                check[nx][ny] = check[temp[0]][temp[1]] + 1

bfs(0,0)
print(check[n-1][m-1])