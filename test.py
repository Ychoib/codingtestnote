from collections import*
d=deque()
n,m=map(int,input().split())
a=[[*map(int,input())]for i in" "*n]
x=y=0
l=1
while (x,y)!=(n-1,m-1):
    print(x,y)
    if 0<=x<n and 0<=y<m and a[x][y] and (a[x][y]==1 or a[x][y]>l):
        a[x][y]=l
        d.extend(((x-1,y,l+1),(x,y-1,l+1),(x+1,y,l+1),(x,y+1,l+1)))

    x,y,l=d.popleft()
print(l)