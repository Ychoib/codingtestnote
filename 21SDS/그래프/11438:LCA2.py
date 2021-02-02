
n,m,parent[][]
visit[MAX_N],depth[MAX_N]


def dfs(now,d):
    visit[now] = True
    depth[now] = d

    for next in graph[now]:
        if visit[now]: continue
        par[next][0] = now


def lca(x,y):
    #x와 y의 높리를 맞춰준다
    if depth[x] > depth[y]: swap(x,y)
    #y의 깊이가 x보다 깊다고 가정한다.
    for i in range(MAX_DEPTH, 0,-1)