
n,m = map(int,input().split())
r,c,d = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]

#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[0] * m for i in range(n)]

count = 0
def bfs(x,y,d):
    global count
    # 0인 부분을 2로 바꾸고 청소한 횟수 증가
    if maps[x][y] == 0:
        maps[x][y] = 2
        count += 1

    # 방향의 왼쪽을 확인후 이동 가능하면 이동, 안된다면 방향 바꾸기
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if maps[nx][ny] == 0:
            bfs(nx,ny,nd)
            return
        d = nd

    #네 방향이 모두 막혔을 때 후진
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    #뒤쪽이 벽일 경우 멈춘다.
    if maps[nx][ny] == 1:
        return
    #후진하고 탐색 진행
    bfs(nx,ny,d)


bfs(r,c,d)
print(count)
