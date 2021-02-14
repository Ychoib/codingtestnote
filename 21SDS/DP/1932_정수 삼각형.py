import sys
input = sys.stdin.readline


n = int(input())
d = []
for i in range(n):
    d.append(list(map(int,input().split())))
k=2
for i in range(1,n):
    for j in range(len(d[i])):
        if j == 0:# 가장 왼쪽값일 경우 현재 값과 바로 위의 값 더함
            d[i][j] = d[i][j] + d[i-1][j]
        elif j == len(d[i]) -1: # 가장 오른쪽일 경우 현재값과 바로 위랑 더함
            d[i][j] = d[i-1][j-1] + d[i][j]
        else: # 중간일 경우 대각선 왼쪽과 오른쪽 중 큰 값을 선택
            d[i][j] = max(d[i-1][j-1] + d[i][j],d[i-1][j]+ d[i][j])

print(max(d[n-1]))