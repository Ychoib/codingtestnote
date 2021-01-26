from collections import deque

r,c = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
maps = [list(map(str,input())) for i in range(r)]
count = [[0] * c for i in range(r)]
q,wq = deque(),deque()
def dfs(x,y):
    q.append((x,y))
    count[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if maps[nx][ny] == "." and count[nx][ny] == 0:
                        count[nx][ny] = count[x][y] + 1
                        q.append((nx,ny))
                    elif maps[nx][ny] == "D":
                        print(count[x][y])
                        return
            qlen -= 1
        water()
    print("KAKTUS")
    return
def water():
    qlen = len(wq)
    while qlen:
        x,y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny] == ".":
                    maps[nx][ny] = "*"
                    wq.append((nx,ny))
        qlen -= 1


for i in range(r):
    for j in range(c):
        if maps[i][j] == "S":
            x,y = i,j
        if maps[i][j] == "*":
            wq.append((i,j))

water()
dfs(x,y)
