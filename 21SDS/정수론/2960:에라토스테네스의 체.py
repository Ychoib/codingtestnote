




n,k = map(int,input().split())

array = [True] * (n+1)

count = 0
for i in range(2,len(array)+1):
    for j in range(i,n+1,i):
        if array[j] == True:
            array[j] = False
            count += 1
            if count == k:
                print(j)
                break

"""
check = [True] * p
for i in range(2,int(p ** 0.5)+1):
    if check[i]:
        for j in range(i*i,p,i):
            check[j] = False
"""