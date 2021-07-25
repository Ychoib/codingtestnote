n,m = list(map(int,input().split()))
import sys,copy
from itertools import combinations
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def spread_dfs(maps_temp,x,y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps_temp[nx][ny] == 0:
                maps_temp[nx][ny] = 2
                spread_dfs(maps_temp,nx,ny)
zero_index = []
virus_index = []
def set_wall():
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                zero_index.append((i,j))
            elif maps[i][j] == 2:
                virus_index.append((i,j))

set_wall()
zero_combi = list(combinations(zero_index,3))

safe_num = []
def check_safe(combi):
    maps_temp = copy.deepcopy(maps)
    for i in combi:
        maps_temp[i[0]][i[1]] = 1
    for x,y in virus_index:
        spread_dfs(maps_temp,x,y)
    result = 0
    for i in maps_temp:
        result += i.count(0)
    safe_num.append(result)
for i in zero_combi:
    check_safe(i)
print(max(safe_num))