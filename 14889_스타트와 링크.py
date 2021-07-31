n = int(input())
import sys
from itertools import combinations
s = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
member = [i for i in range(n)]
temp_member = [i for i in range(n)]
start = list(combinations(range(n),n//2))
link = []


for i in start:
    temp_member = [z for z in range(n)]

    for j in i:
        temp_member.remove(j)
    link.append(temp_member)

result_list = []
for i in range(len(start)):
    start_score = 0
    link_score = 0
    temp_start = list(combinations(start[i],2))
    for j in temp_start:
        start_score += s[j[0]][j[1]] + s[j[1]][j[0]]
    temp_link = list(combinations(link[i], 2))
    for j in temp_link:
        link_score += s[j[0]][j[1]] + s[j[1]][j[0]]


    if start_score - link_score < 0:
        result_list.append(link_score - start_score)
    else:
        result_list.append(start_score - link_score)
print(min(result_list))