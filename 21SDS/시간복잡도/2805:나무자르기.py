n,m = map(int,input().split())

trees = list(map(int,input().split()))

result = []

start = 1
end = max(trees)

while start <= end:
    result_v = 0
    mid = ( start + end ) // 2
    for i in range(n):
        if trees[i] >= mid:
            result_v = result_v + trees[i] - mid
    if result_v >= m :
        start = mid + 1
    elif result_v < m :
        end = mid -1

print(end)