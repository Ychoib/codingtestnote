s = int(input())
sum_num = 0
n = 1
while True:
    sum_num += n
    if sum_num > s:
        break
    n += 1
print(n-1)