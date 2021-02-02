import sys

par = {}
edgelist = []


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

def getparent(par, a):
    if par[a] == a: return a
    par[a] = getparent(par,par[a])
    return par[a]
def unionparent(par, x,y):
    p_x = getparent(par,x)
    p_y = getparent(par,y)
    if p_x < p_y: par[p_y] = p_x
    else: par[p_x] = p_y
def findparent(par,x,y):
    a = getparent(par,x)
    b = getparent(par,y)
    if a==b: return 1
    else: return 0

for i in range(n):
    par[i+1] = i+1

for i in range(m):
    a,b,c = map(int,input().split())
    edgelist.append([c,a,b])
edgelist.sort(key = lambda val: val[0])

mst = []
for e in edgelist:
    w,v,u = e
    if findparent(par,v,u) == 0:
        unionparent(par,v,u)
        mst.append(e)
print(sum([w for w,v,u in mst]))

