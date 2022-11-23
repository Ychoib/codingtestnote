import sys
sys.setrecursionlimit(10 ** 4)

        
move = [(0,1),(0,-1),(1,-1),(1,0),(-1,-1),(-1,0),(-1,1),(1,1)]            
def dfs(a,b):
    maps[a][b] = 0
    for x,y in move:
        dx = a + x
        dy = b + y
        if 0 <= dx < H and 0 <= dy < W and maps[dx][dy] == 1:
            #방문하지 않았고, 땅이면 방문
            dfs(dx,dy)
    
while 1:
    W,H = map(int,input().split())
    if W == 0 and H ==0:
        break
    maps = []
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    for x in range(H):
        maps.append(list(map(int,input().split())))
    for i in range(H):
        for j in range(W):
            if maps[i][j] != 0:
                dfs(i,j)
                cnt += 1
    print(cnt)
