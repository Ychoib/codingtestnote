from collections import deque
n,k = map(int,input().split())

dx = [-1,1,n]
node = 0
visited = []
def bfs(x):
    global node
    q = deque([[node,x]])
    while q:
        temp= q.popleft()
        location = temp[1]
        node = temp[0]

        if location == k:
            print(node)
            return
        for i in range(3):
            if i == 2:
                nx = location * 2
            else:
                nx = location + dx[i]
            if 0 <= nx < 100001 and nx not in visited:
                q.append([node + 1,nx])
                visited.append(nx)

bfs(n)