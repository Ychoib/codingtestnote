import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(m)]

dist = [INF] * (n + 1)

def belman_ford():
    minus = False
    dist[1] = 0
    for i in range(n):
        for j in range(m):
            v = graph[j][0]
            nv = graph[j][1]
            w = graph[j][2]
            if dist[v] != INF and dist[nv] > dist[v] + w:
                dist[nv] = dist[v] + w
                if i == n-1:
                    minus = True
    if minus:
        print(-1)
    else:
        for j in range(2,n+1):
            if dist[j] != INF:
                print(dist[j])
            else:
                print(-1)
belman_ford()