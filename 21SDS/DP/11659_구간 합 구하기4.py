import sys
input = sys.stdin.readline

n,m = map(int,input().split())

num = list(map(int,input().split()))
sum_numbers = [0] * n

for i in range(n):
    if i == 0:
        sum_numbers[i] = num[i]
    else:
        sum_numbers[i] = sum_numbers[i-1] + num[i]

for i in range(m):
    n,m = map(int,input().split())
    if n == 1:
        print(sum_numbers[m-1])
    else:
        print(sum_numbers[m-1]-sum_numbers[n-2])