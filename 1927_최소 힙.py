import heapq
import sys
n = int(input())
l = []

flag = 0
for i in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if len(l) == 0:
            print(0)
        else:
            print(heapq.heappop(l))
    else:
        heapq.heappush(l,temp)