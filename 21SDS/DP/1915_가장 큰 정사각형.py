import sys,copy
input = sys.stdin.readline


n,m = map(int,input().split())
k = list(map(int,list(input().rstrip())))
print(k)
maps = [list(map(int,list(input().rstrip()))) for _ in range(n)]
print(maps)
d = copy.deepcopy(maps)
ans = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and i > 0 and j > 0:
            d[i][j] += min(d[i-1][j],d[i][j-1],d[i-1][j-1])
        if d[i][j] >= ans:
            ans = d[i][j]
print(ans)
