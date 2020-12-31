n,m = map(int,input().split())

visited = []
for i in range(n):
    visited.append(list(map(int,input().split())))

count = 0
def dfs(x,y):
    if x <= 0 or y <= 0 or x > n or y > m:
        return False
    if visited[x][y] == False:
        visited[x][y] = True
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1
print(count)




