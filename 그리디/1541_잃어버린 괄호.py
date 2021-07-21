import re
expo = str(input())
num_list = []
oper_list = []
temp = []
num_list = list(map(int,re.split('[+-]',expo)))

for idx,element in enumerate(expo):
    if element == "+" or element == "-":
        oper_list.append(element)

result = num_list[0]
for i, v in enumerate(oper_list):
    if v == '+':
        result = result + num_list[i + 1]
    elif v == '-':
        result = result - sum(num_list[i + 1:])
        break
print(result)
"""
flag = 0
prev_index = 0
result = num_list[0]
for i,v in enumerate(oper_list):
    if v == '-':
        if '-' in oper_list[i+1:]:
            for j in range(i,len(oper_list)):
                if j == '-':
                    break
                elif j == '+':
                    oper_list[j] = '-'
        else:
print(oper_list)
for i in range(len(oper_list)):
    if v == '+':
        result = num_list[i] + num_list[i+1]
    elif v == '-':
        result = result - num_list[i+1]
    print(result)"""

