import sys
input = sys.stdin.readline


w,h = map(int,input().split())

d = [[[0] * 2 for i in range(w)] for i in range(h) ]

for i in range(1,w):
    d[0][i][0] = 1
for j in range(1,h):
    d[j][0][0] = 1

for i in range(1,w):
    for j in range(1,h):
        d[i][j][0] = (d[i][j-1][0] + d[i][j-1][1] + d[i-1][j][0] + d[i-1][j][1]) % 100000#방향 전환 할 수 있다.
        d[i][j][1] = (d[i][j-1][0] + d[i-1][j][1]) % 100000

print(d[w][h][0] +  d[w][h][1])