n = int(input())
k = int(input())

maps = [[0 for _ in range(n+2)] for _ in range(n+2)]
import sys
from collections import deque
for i in range(k):
    x,y = list(map(int,sys.stdin.readline().split()))
    maps[x][y] = 1

l = int(input())
head = [1, 1]
tail = [1, 1]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = deque([[1,1]])
maps[1][1] = -1

times = {}
def direction(d_cnt,c):
    if c == "D":
        d_cnt = (d_cnt + 1) % 4
    else:
        d_cnt = (d_cnt - 1) % 4
    return d_cnt
def bam():
    time = 1
    d_cnt = 0

    while True:
        head[0] = head[0] + dx[d_cnt]
        head[1] = head[1] + dy[d_cnt]
        if 0 < head[0] <= n and 0 < head[1] <= n and maps[head[0]][head[1]] != -1:
            if not maps[head[0]][head[1]] == 1:
                temp_x,temp_y = visited.popleft()
                maps[temp_x][temp_y] = 0
            maps[head[0]][head[1]] = -1
            visited.append([head[0],head[1]])
            if time in times.keys():
                d_cnt = direction(d_cnt,times[time])

            time += 1
        else:
            print(time)
            exit()

for i in range(l):
    x,c = list(map(str,sys.stdin.readline().split()))
    times[int(x)] = c
bam()
