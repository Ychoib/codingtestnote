import sys
n,m = list(map(int,input().split()))
trees = list(map(int,sys.stdin.readline().split()))

s = min(trees)
e = max(trees)
while True:
    sum = 0
    mid = (e + s) // 2
    for i in range(len(trees)):
        if trees[i] - mid >= 0:
            sum += (trees[i] - mid)
    if s > e:
        print(e)
        break
    if sum >= m:
        s = mid + 1
    else:
        e = mid - 1
