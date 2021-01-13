from collections import deque

def bfs(a,b):
    count = 0
    q = deque([[a,count]])
    while q:
        value = q.popleft()
        a = value[0]
        count = value[1]
        if a == b:
            return count
        if not visited[a]:
            count += 1
            visited[a] = True
            for i in adj[a]:
                if not visited[i]:
                    q.append([i,count])
    return -1






total = int(input())
a, b = map(int,input().split())
connect = int(input())
visited = [False] * (total+1)
adj = [[] for _ in range(total + 1)]
for i in range(connect):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(a,b))