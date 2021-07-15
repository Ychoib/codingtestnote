n,m = input().split()
arr = list(map(int,input().split()))

result = 0
count = 0
sum_arr = [0] * (n+1)
for i in range(1,n+1):
    sum_arr[i] = sum_arr
print(sum_arr)
for i in range(len(arr)):
    for j in range(i,len(arr)):
        result = sum_arr[j] - sum_arr[i]
        if result == int(m):
            count += 1
print(count)
