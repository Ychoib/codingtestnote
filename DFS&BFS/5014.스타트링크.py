from collections import deque
f,s,g,u,d = map(int,input().split())

def bfs(i):
    q = deque()
    q.append(i)
    visit = [0 for i in range(f)]
    visit[i] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + direct[i]
            if 0 <= nx < f and visit[nx] == 0:
                q.append(nx)
                apart[nx] = apart[x] + 1 #count를 리스트에 넣는다.

apart = [-1 for i in range(f)]
direct = [u,-d]
apart[s-1] = 0
bfs(s-1)
print(apart[g-1] if apart[g-1] != -1 else "use the stairs")