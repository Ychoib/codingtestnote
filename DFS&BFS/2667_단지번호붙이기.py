n = int(input())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

total = 0
cnt = 1
maps = []

for i in range(n):
    maps.append(list(map(int,input())))
visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x,y):
    global total
    if maps[x][y] == 1:
        total += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if maps[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx,ny)

num_list = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            dfs(i,j)
            num_list.append(total)
            total = 0
print(len(num_list))
num_list.sort()

for i in num_list:
    print(i)