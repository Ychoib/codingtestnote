n = int(input())
fees = list(map(int,input().split()))
m = int(input())

s = 1
e = max(fees)
while s <= e:
    sum_num = 0
    mid = (s + e )// 2
    for i in fees:
        if i >= mid:
            sum_num += mid
        else:
            sum_num += i

    if sum_num > m:
        e = mid - 1
    else:
        s = mid + 1
print(e)