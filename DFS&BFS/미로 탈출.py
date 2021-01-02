from collections import deque
n,m = map(int,input().split())

miro = []
for i in range(n):
    miro.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                continue
            if miro[next_x][next_y] == 0:
                continue
            if miro[next_x][next_y] == 1:
                miro[next_x][next_y] = miro[x][y] + 1
                queue.append((next_x,next_y))
    for i in range(n):
        print(miro)
    return miro[n-1][m-1]

print(bfs(0,0))