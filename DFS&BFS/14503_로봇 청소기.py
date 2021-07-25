n,m = list(map(int,input().split()))

r,c,d = list(map(int,input().split()))

import sys
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
clean = [[0 for _ in range(m)] for _ in range(n)]

#서,남,동,북
dx = [0,1,0,-1]
dy = [-1,0,1,0]

clean[r][c] = 1
if d == 1:
    d = 3
elif d == 2:
    d = 2
elif d == 3:
    d = 1
def dfs(x,y):
    global d
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 1 or clean[nx][ny] == 1:
                cnt += 1
    if cnt == 4:
        back_x, back_y = x + dx[(d + 1) % 4], y + dy[(d + 1) % 4]
        if maps[back_x][back_y] == 1:
            return
        else:
            dfs(back_x, back_y)
    else:
        left_x,left_y = x + dx[d % 4],y + dy[d % 4]

        if 0 <= left_x < n and 0 <= left_y < m:
            if maps[left_x][left_y] == 0:
                if clean[left_x][left_y] == 0:
                    d += 1
                    clean[left_x][left_y] = 1
                    dfs(left_x,left_y)
                elif clean[left_x][left_y] == 1:
                    d += 1
                    dfs(x,y)
            else:
                d += 1
                dfs(x,y)


result = 0
dfs(r,c)
for i in clean:
    result += i.count(1)

print(result)