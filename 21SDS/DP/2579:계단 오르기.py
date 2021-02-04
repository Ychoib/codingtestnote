import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)
num = [0] * (n+1)
for i in range(1,n+1):
    num[i] = int(input())


for i in range(1,n+1):
    if i == 1:
        d[i] = num[i]
    elif i == 2:
        d[i] = max(num[i],d[i-1] + num[i])
    else:
        d[i] = max(num[i] + num[i-1] + d[i-3], num[i] + d[i-2])

print(d[n])

