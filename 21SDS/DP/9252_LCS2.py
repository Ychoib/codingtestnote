

a = list(map(str,input().rstrip()))
b = list(map(str,input().rstrip()))

d = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j],d[i][j-1])
result = []
now = d[-1][-1]
i = len(d) - 1 #row
j = len(d[0]) - 1 #column

while now != 0:
    if d[i-1][j] == (d[i][j] -1) and d[i][j-1] == (d[i][j] - 1):
        result.append(a[i-1])
        now -= 1
        i -= 1
        j -= 1
    else:
        if d[i-1][j] > d[i][j-1]:
            i -= 1
        else:
            j -= 1
result.reverse()
if len(result) == 0:
    print(d[-1][-1])
else:
    print(d[-1][-1])
    for i in result:
        print(i,end ="")