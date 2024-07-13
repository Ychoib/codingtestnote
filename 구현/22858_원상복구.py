#D(i)[j] = i번째 카드를 j번째로 가져온다..
#S(j)[i] =
#k번 섞은 카드의 정보
import sys
n,k = map(int,input().split())

Ss = list(map(int,sys.stdin.readline().split()))

Ds = list(map(int,sys.stdin.readline().split()))
Ps = [0 for _ in range(n)]

for i in range(k):
    for Dsidx, Dsvalue in enumerate(Ds):
        Ps[Dsvalue - 1] = Ss[Dsidx]
    for Psindex, Psvalue in enumerate(Ps):
        Ss[Psindex] = Psvalue
for ps in Ps:
    print(ps, end = " ")
