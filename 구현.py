n,m= int(input.split())

a,b,direction = int(input.split())

data =[]
for i in range(n):
  data.append(list(map(int,input.split())))
    
def rotation():
  global direction
  direction -= 1
  if direction == -1 :
    direction = 3

  

dx = [-1,0,+1,0] #direction에 따른 x,y좌표 이동
dy = [0,+1,0,-1]

count = 0
turntime = 0

visit = [ [0] * m for i in range(n)]
visit[a][b] = 1

while True:
  rotation()
  turntime += 1
  nx = a + dx[direction] # 왼쪽 방향의 x,y 좌표
  ny = b + dy[direction]
  if data[nx][ny] == 0 and visit[nx][ny] == 0:
    a,b = dx,dy
    visit[nx][ny] = 1
    count += 1
    turntime = 0
  else:
    turntime += 1
  
  if turntime == 4 :
    nx = a - dx[direction]
    ny = b - dy[direction]
    if data[nx][ny] == 0:
      a,b = nx,ny
    else:
      break
  turntime = 0

  
