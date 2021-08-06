n,m = list(map(int,input().split()))
import sys
total_maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
from collections import deque
def dfs(cnt):
    global check,area
    if cnt == len(cctv):
        tmp = 0
        for i in range(n):
            for j in range(m):
                if total_maps[i][j] == 0 and check[i][j] == 0:
                    tmp += 1
        return tmp
    x,y = cctv[cnt]
    for i in range(4):
        new_dir = []
        if total_maps[x][y] == 1:
            new_dir.append(i)
        elif total_maps[x][y] == 2:
            new_dir.append(i)
            new_dir.append((i+2)%4)
        elif total_maps[x][y] == 3:
            new_dir.append(i)
            new_dir.append((i-1)%4)
        elif total_maps[x][y] == 4:
            new_dir.append(i)
            new_dir.append((i-1)%4)
            new_dir.append((i+2)%4)
        elif total_maps[x][y] == 5:
            new_dir.append(i)
            new_dir.append((i+1)%4)
            new_dir.append((i - 1) % 4)
            new_dir.append((i + 2) % 4)
        q = deque()
        for d in new_dir:
            nx = x + dx[d]
            ny = y + dy[d]
            while 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == 0 and total_maps[nx][ny] != 6:
                    check[nx][ny] = 1
                    q.append((nx,ny))
                elif total_maps[nx][ny] == 6:
                    break
                nx += dx[d]
                ny += dy[d]
        area = min(area,dfs(cnt + 1)) #다음 cctv확인

        #maps 초기화해주기
        while q:
            qx,qy = q.popleft()
            if total_maps[qx][qy] == 0:
                check[qx][qy] = 0
        if total_maps[x][y] == 5: break
    return area
cctv = []

check = [[0 for _ in range(m)] for _ in range(n)]
area = 0
for i in range(n):
    for j in range(m):
        if total_maps[i][j] and total_maps[i][j] != 6:
            cctv.append([i,j])
            check[i][j] = 1
        if not total_maps[i][j]:
            area += 1
dfs(0)