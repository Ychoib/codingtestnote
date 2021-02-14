n,m = map(int,input().split())

array = list(map(int,input().split()))

count = 0
sum_array = [0] * (n+1)
for i in range(1,n+1):
    sum_array[i] = array[i-1] + sum_array[i-1]
def check(start,end):
    global count
    result = sum_array[end] - sum_array[start]
    if result == m:
        count += 1
    else:
        return
for i in range(n+1):
    for j in range(n+1):
        check(i,j)
print(count)