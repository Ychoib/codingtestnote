from itertools import combinations


#라이브러리를 쓰면 메모리 초과가 나기 때문에 반복문으로 사용한다.
n,k = map(int,input().split())

iter = [i for i in range(1,n+1)]

m = n-k

parent = 1
child = 1
while n > m:
    parent *= n
    n-=1
for j in range(1,k+1):
    child *= j
print((parent // child)%10007)