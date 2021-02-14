import sys

sys.setrecursionlimit(10**5)
#uniofind 알고리즘

##각 노드의 루트노드를 가져온다.
def getparent(a):
    if par[a] == a: return a
    par[a] = getparent(par[a])
    return par[a]

##두 노드를 같은 집합에 합집합을 시킨다.
def union(x,y):
    a = getparent(x)
    b = getparent(y)
    if a < b:
        par[b] = a
    else:
        par[a] = b
##두 노드가 같은 집합에 있는 노드인지 판별한다.
def check(x,y):
    a = getparent(x)
    b = getparent(y)
    if a == b: return 1
    else: return 0

n,m = map(int,input().split())


par = [0] * (n+1)
adj = [[] for i in range(n)]

result = []
for i in range(n):
    par[i+1] = i+1
for i in range(m):
    o,a,b = map(int,input().split())
    if o == 0:
        union(a,b)
    elif o == 1:
        if check(a,b):
            print("YES")
        else:
            print("NO")