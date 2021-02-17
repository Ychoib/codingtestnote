import sys
input = sys.stdin.readline

def comb(n,k):
    parent = 1
    child = 1
    for i in range(n,n-k,-1):
        parent *= i
    for j in range(1,k):
        child *= j
    result = parent // child
    return result

m = int(input()) # 조약돌 색깔 개수
num_stone = list(map(int,input().split()))

k = int(input()) # 조약돌을 뽑는 개수

if m == 1 or k == 1:
    print(1.0)
    exit()

result = 1 # 같은 색을 뽑을 확률

# nCk + mCk // n+mCk
sum_stone = sum(num_stone)
parent = 0
for i in num_stone:
    parent += comb(i,k)
result = parent / comb(sum_stone,k)
print(result)


