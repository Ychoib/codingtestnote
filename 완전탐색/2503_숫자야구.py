from itertools import permutations
n = int(input())
per_arr = list(permutations(range(1,10),3))

for i in range(n):
    test,s,b = map(int,input().split())
    test =list(str(test))
    rv = 0
    for j in range(len(per_arr)):
        s_num,b_num =0,0
        j -= rv

        for z in range(3):
            test[z] = int(test[z])
            if test[j] in per_arr[j]:
                if j == per_arr.index(test[j]):
                    s_num += 1
                else:
                    b_num += 1
        if s != s_num or b != b_num:
            per_arr.remove(per_arr[j])
            rv += 1

