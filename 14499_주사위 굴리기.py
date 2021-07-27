import sys
n,m,x,y,k = list(map(int,input().split()))
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

side = [0,0,0,0] #상하좌우
updown = [0,0] #위아래

move = [list(map(int,sys.stdin.readline().split()))]

start = [x,y] #주사위의 지도 위치

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def moving(move):
    if move == 1:
        #동쪽으로 굴리고 주사위의 위치 정렬
        side[2], side[3] = updown[0], updown[1]

        start[0] = start[0] + dx[move-1]
        start[1] = start[1] + dy[move-1]
        if 0 <= start[0] < n or 0 <= start[1] < m:
            if maps[start[0]][start[1]] == 0:
                maps[start[0]][start[1]] = updown[1]
            else:
                updown[1] = maps[start[0]][start[1]]

for i in move:

