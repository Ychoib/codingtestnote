from collections import deque

N = int(input())

dq = deque([i for i in range(1, N+1)])
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])
    
# 123456
# 23456
# 34562
# 4562
# 5624
# 624
# 246
# 46
# 64
# 4