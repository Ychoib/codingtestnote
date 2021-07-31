n = int(input())
import sys
schedule = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]

result_list = []

result = 0
def dfs(day,i,v):
    global result
    if day > n:
        return
    next_schedule = v[0]
    for j in range(i,len(schedule)):
        if j == next_schedule + 1:
            print(j,v[1])
            result += schedule[j][1]
            dfs(day,j,schedule[j])

for i,v in enumerate(schedule):
    day = 1
    result += v[1]
    dfs(day,i,v)
    print()
    result_list.append(result)
    result = 0
print(result_list)
print(max(result_list))
