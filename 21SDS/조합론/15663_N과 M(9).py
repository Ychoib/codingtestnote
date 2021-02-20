from itertools import permutations

n,m = map(int,input().split())

num = list(map(int,input().split()))

result = []

res = permutations(num,m)
sort_res = sorted(list(set(res)))


for i in sort_res:
    for j in i:
        print(j,end = " ")
    print()