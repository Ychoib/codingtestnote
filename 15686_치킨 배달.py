n,m = list(map(int,input().split()))
import sys
from collections import deque
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

from itertools import combinations
import copy
house = []
chicken_house = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken_house.append((i,j))
        elif maps[i][j] == 1:
            house.append((i,j))

minv = float('inf')
for ch in combinations(chicken_house, m):
    sumv = 0

    for home in house:
        sumv += min(abs(home[0] - i[0]) + abs(home[1] - i[1]) for i in ch)
        if minv <= sumv: break
    if sumv < minv: minv = sumv

print(minv)
"""

dx = [0,0,-1,1]
dy = [-1,1,0,0]
result_list = []
def bfs(fx,fy,chicken):
    cnt = 0
    q = deque([(fx,fy)])
    chicken[fx][fy] = cnt
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] != 2 and chicken[nx][ny] == -1:
                    q.append((nx,ny))
                    chicken[nx][ny] = chicken[x][y] + 1
                elif maps[nx][ny] == 2:
                    result.append(chicken[x][y] + 1)
                    return
house = []
chicken_house = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken_house.append((i,j))
        elif maps[i][j] == 1:
            house.append((i,j))

chic = list(combinations(chicken_house,len(chicken_house) - m))
result_maps = []
for i in chic:
    temp_maps = copy.deepcopy(maps)
    for j in i:
        temp_maps[j[0]][j[1]] = 0
    result_maps.append(temp_maps)

for maps in result_maps:
    result = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                chicken = [[-1] * n for _ in range(n)]
                bfs(i,j,chicken)
    result_list.append(sum(result))
print(min(result_list))
"""