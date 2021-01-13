from collections import deque
from sys import stdin

n = int(input())

maps = []
for i in range(n):
    maps.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0] * n for i in range(n)]

count = 0
def dfs(x,y):
    global count
    visited[x][y] = 1
    if maps[x][y] == 1:
        count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                dfs(nx,ny)

numlist = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            numlist.append(count)
            count = 0

print(len(numlist))
for i in sorted(numlist):
    print(i)