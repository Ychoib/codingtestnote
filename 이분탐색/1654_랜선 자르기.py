import sys

k, n = map(int,input().split())
lans = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(lans)
while start <= end:
    cnt = 0

    mid = (start + end) // 2
    #print("mid = ", mid)
    for lan in lans:
     #   print("lan // mid = ", lan // mid)
        cnt += (lan // mid)

    if cnt >= n :
        start = mid + 1
    elif cnt < n:
        end = mid - 1
print(end)

