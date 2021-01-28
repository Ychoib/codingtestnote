n = int(input())

a = list(map(int,input().split()))

m = int(input())

check = list(map(int,input().split()))

exist = [0] * m

for i in check:
    if i in a:
        check[check.index(i)] = 1
    else:
        check[check.index(i)] = 0
for i in check:
    print(i)
