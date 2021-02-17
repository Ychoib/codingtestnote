import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
num = []
for i in range(n):
    num.append(str(input().rstrip()))

result = permutations(num,k)
pre_result = set() #set로 설정하면 중복이 들어오면 제외하고 추가된다.
for i in result:
    # 문자열 합치는 방법 ex) {('1','2')} -> {'12'}
    pre_result.add(''.join(i))
print(len(pre_result))