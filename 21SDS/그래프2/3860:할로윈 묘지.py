import sys
input = sys.stdin.readline
INF = int(1e9)

edges = []
stone = []
hole = []
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    dist = [INF] * (w*h)
    dist[0] = 0
    g = int(input())
    for i in range(g):
        x,y = map(int,input().split())
        stone[x][y] = True
    e = int(input())
    edge_count = 0
    for i in range(e):
        x1,y1,x2,y2,t = map(int,input().split())
        edges[edge_count]