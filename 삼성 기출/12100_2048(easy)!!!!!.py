import sys

N = int(input())

maps = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

import copy
from collections import deque
q = deque()
answer = 0

def get(i,j): #해당 열이나 행의 보드 값만 가져오기 0이 아니면 저장 후 0 으로 바꾸기(다시 채우기 위함)
    if maps[i][j]:
        q.append(maps[i][j])
        maps[i][j] = 0 #
def move(direct):
    if direct == 0: #위
        for j in range(N): #열
            for i in range(N): #행
                get(i,j) #열고정
            merge(0,j,1,0) # col 고정, row를 1씩 증가하면서 합치고 블록 쌓기
    elif direct == 1: #아래
        for j in range(N):
            for i in range(N-1,-1,-1): # 행 이동
                get(i,j)
            merge(N-1,j,-1,0) # col 고정, row를 -1씩 감소하면서 합치고 블록 쌓기
    elif direct == 2: #오른쪽
        for i in range(N):
            for j in range(N): # 열 이동
                get(i,j)
            merge(i,0,0,1) # row 고정, col을 +1씩 오른쪽으로 쌓기
    elif direct == 3: #왼쪽
        for i in range(N):
            for j in range(N-1,-1,-1): # 열 이동
                get(i,j)
            merge(i,N-1,0,-1)
def merge(i,j,di,dj): #합치려는 블록 비교해 합치기
    while q:
        temp = q.popleft()
        if maps[i][j] == 0: #0이면 그대로 이동
            maps[i][j] = temp
        elif maps[i][j] == temp: #같으면 2배
            maps[i][j] = temp * 2
            i, j = i + di, j + dj
        else:
            i, j = i + di, j + dj
            maps[i][j] = temp

def solve(cnt):
    global maps,answer
    if cnt == 5:
        for i in range(N):
            answer = max(answer, max(maps[i])) #트리 구조에서 lv5가 될때 만들어진 map의 최대값
        return
    m = copy.deepcopy(maps)
    for i in range(4):
        move(i)
        solve(cnt+1)
        maps = copy.deepcopy(m) #방향마다 maps를 원래 상태로 초기화

solve(0)
print(answer)