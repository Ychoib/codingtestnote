from collections import deque


n,m = map(int,input().split())


indegree = [0] * (n+1)
adjlist = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    indegree[b] += 1
    adjlist[a].append(b)

## 위상정렬 함수
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0: q.append(i)

while q:
    tmp = q.popleft()
    print(tmp,end = ' ')
    for i in adjlist[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

