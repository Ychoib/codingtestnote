import sys
input = sys.stdin.readline
"""
메모리초과

n = int(input())
arr = list(map(int,input().split()))


d = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        d[i][j] = sum(arr[i:j+1])
j = 0
max_rst = d[0][0]
for i in range(len(d)):
    k = d[i][j:]
    max_rst = max(max(k),max_rst)
    j += 1
print(max_rst)
"""
n = int(input())
arr = list(map(int,input().split()))
d = [0 for i in range(n)]
result = -1001
for i in range(n):
    d[i] = max(d[i-1] + arr[i],arr[i])
    result = max(result,d[i])
print(result)

