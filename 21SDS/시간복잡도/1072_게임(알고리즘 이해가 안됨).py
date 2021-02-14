from math import floor
x,y = map(int,input().split())
start, end = 0, 1000000000

new = floor(y*100/x)

if new >= 99: print(-1)
else:
    while start <= end:

        mid = (start + end) // 2

        if floor((y + mid) * 100 / (x + mid)) <= new: start = mid + 1
        else: end = mid - 1
    print(end + 1)