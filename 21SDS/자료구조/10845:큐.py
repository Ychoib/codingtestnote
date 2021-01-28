import sys
from collections import deque
n = int(sys.stdin.readline())

queue = deque()
for i in range(n):
    order = list(map(str,sys.stdin.readline().split()))
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif order[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            result = queue.popleft()
            print(result)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)