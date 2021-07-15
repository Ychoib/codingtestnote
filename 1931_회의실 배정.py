n = int(input())
end = 0
flag = 0
cnt = 0
a = []
for i in range(n):
    s,e = map(int,input().split())
    a.append([s,e])
a = sorted(a,key = lambda x: x[0])
a = sorted(a,key = lambda x: x[1])

for i,j in a:
    if i >= end:
        end = j
        cnt += 1


print(cnt)