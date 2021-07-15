n = int(input())
lst = list(map(int,input().split()))
new_lst = []
for i in range(len(lst)):
    new_lst.append((i + 1,lst[i]))
new_lst = sorted(new_lst,key = lambda x : x[1])
result = 0
result_lst = []
for i in new_lst:
    result_lst.append(i[1])
for i in range(len(result_lst)):
    result += sum(result_lst[:i+1])
print(result)
