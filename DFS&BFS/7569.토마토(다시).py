from collections import deque




dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

count = 0
def bfs():
    while q:
        a,b,c = q.popleft()
        visit[c][a][b] = 1
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < n and 0 <= y < n and 0 <= z < n:
                q.append([x,y,z])
                box[z][x][y] = box[c][a][b] + 1
                visit[z][x][y] = 1


m,n,h = map(int,input().split())

box = [[] for i in range(h)]
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        box[i].append(list(map(int,input().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 1:
                q.append([x,y,z])
bfs()
max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num,box[z][x][y])
if isTrue == True:
    print(-1)
else:
    print(max_num-1)

