import sys

N = int(input())
A = list(map(int,input().split()))
B,C = list(map(int,input().split()))

total_student = sum(A)
answer = 0
for i in A:
    answer += 1  # 총감독
    if i > B :
        temp = ( (i - B) % C ) #부감독
        if temp != 0:
            answer += ((i - B) // C) + 1
        else:
            answer += ((i - B) // C)
print(answer)
