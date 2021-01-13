n = int(input())

maps = [list(map(int,input().split())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

temp = maps.copy()
def bfs(x,y,height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and maps[nx][ny] > height:
            visited[nx][ny] = 1
            bfs(nx,ny,height)

height = 0
maxcount = 0
for height in range(100):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if height < maps[x][y] and not visited[x][y]:
                count += 1
                visited[x][y] = 1
                bfs(x,y,height)
    maxcount = max(maxcount, count)
print(maxcount)

