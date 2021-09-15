import sys
input = sys.stdin.readline
n,m,k = list(map(int,input().split()))

A = [list(map(int,input().split())) for _ in range(n)]

from collections import deque
namu = [[deque() for _ in range(n)] for _ in range(n)] #나무
for i in range(m):
    x,y,age = list(map(int,input().split()))
    namu[x-1][y-1].append(age)
food = [[5] * n for _ in range(n)]
def spring_summer():
    for i in range(n):
        for j in range(n):
            len_tree = len(namu[i][j])
            for idx in range(len_tree): #나이가 적은 나무부터 영양분 공급
                if namu[i][j][idx] <= food[i][j]: #(i,j)땅의 양분이 부족
                    food[i][j] -= namu[i][j][idx] #양분 먹고
                    namu[i][j][idx] += 1 #나이 1먹기
                else:
                    for _ in range(idx,len_tree):
                        food[i][j] += (namu[i][j].pop() // 2)  # 죽은 나무 양분으로 바꾸기(여름)
                    break
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
def fall_winter():
    for i in range(n):
        for j in range(n):
            for age in namu[i][j]:
                if age % 5 == 0: # 번식 조건 (나이가 5의 배수)
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            namu[nx][ny].appendleft(1)
            food[i][j] += A[i][j]

for i in range(k):
    spring_summer()
    fall_winter()
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(namu[i][j])
print(answer)