n = int(input())

array = []
for i in range(n):
    info = input().split()
    array.append((info[0],int(info[1])))

def setting(data):
    return data[1]

result = sorted(array, key= setting)

for i in result:
    print(i[0],end=" ")

