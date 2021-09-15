n = int(input())
s = 0
e = n
while True:
    mid = (s + e) // 2
    if s > e:
        break
    if mid**2 < n:
        s = mid + 1
    else:
        e = mid - 1
print(mid + 1)