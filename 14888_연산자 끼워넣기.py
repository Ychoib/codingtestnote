n = int(input())
from itertools import permutations
num_list = list(map(int,input().split()))
operation_list = list(map(int,input().split()))
ok = []
for i,v in enumerate(operation_list):
    if i == 0:
        for j in range(v):
            ok.append('+')
    elif i == 1:
        for j in range(v):
            ok.append('-')
    elif i == 2:
        for j in range(v):
            ok.append('x')
    else:
        for j in range(v):
            ok.append("/")
ok = list(permutations(ok,len(ok)))

result_list = []
for z in ok:
    result = num_list[0]
    for i in range(1,len(num_list)):
        j = z[i-1]
        if j == '+':
            result += num_list[i]
        elif j == '-':
            result -= num_list[i]
        elif j == 'x':
            result *= num_list[i]
        else:
            if result < 0:
                result = -1 * ( (-1 * result) // (num_list[i]))
            else:
                result //= num_list[i]
    result_list.append(result)
print(max(result_list))
print(min(result_list))