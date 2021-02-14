from itertools import combinations
from itertools import permutations
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

iter = [i for i in range(1,n+1)]

result = combinations(iter,k)

print(len(list(result)))

""" permuation(순열)
result_per = permutations(iter,k)

print(len(list(result_per)))

"""