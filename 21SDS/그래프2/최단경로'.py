"""
최단경로
1) 다익스트라
- 대부분은 다익스트라
- 우선순위 큐 사용
2) 벨만포드
- 간선간 비용 중 음수가 있는 경우
3) 플로이드 워셜
- 정점갯수^3
- 코드가 제일 쉬운데, 정점갯수가 매우 적을때 사용
- 모든 지점에서 모든 지점까지 최단경로 구하기 가능
"""

"""개선된 다익스트라 알리즘"""
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


n,m = map(int,input().split())

start = int(input())


#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] *(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)


#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])