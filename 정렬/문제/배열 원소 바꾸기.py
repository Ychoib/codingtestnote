n,m = map(int,input().split())

array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))

array_a.sort()
array_b.sort(reverse= True)


min_a = min(array_a)
max_b = max(array_b)


for i in range(m):
    if array_a[i] < array_b[i]:
        array_a[i],array_b[i] = array_b[i],array_a[i]
    else:
        break
print(sum(array_a))