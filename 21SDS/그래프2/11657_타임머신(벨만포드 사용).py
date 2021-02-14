
""" 음의 코스트가 있다면 벨만 포드 최단 경로 사"""

import sys
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
            v = graph[j][0] #시작 지점
            nv = graph[j][1] #도착 지점
            w = graph[j][2] #소요 시간
            if dist[v] != INF and dist[nv] > dist[v] + w:
                dist[nv] = dist[v] + w
                if i == n-1: #n번째 루트에 접근을 한다면 음의 사이클을 도는 것이다.
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

