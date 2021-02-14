import sys

# n의 범위를 생각을 못해 많이 시도 했던 문제
# 에라토스테네스의 체 제대로 외우기
n = 1000000
array = [False,False] + [True] * n
for i in range(2,n+1):
    if array[i]:
        for j in range(i * i,n+1,i):
            array[j] = False

t = []
while True:
    temp = int(sys.stdin.readline())
    if temp == 0:
        break
    for i in range(3, len(array)):
        if array[i] == True and array[temp-i] == True:
            print("%d = %d + %d" %(temp,i, temp-i))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
