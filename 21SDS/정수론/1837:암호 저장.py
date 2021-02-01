p,k = map(int,input().split())

check = [True] * k

for i in range(2,int(k ** 0.5)+1):
    if check[i]:
        for j in range(i*i,k,i):
            check[j] = False

flag = True
for i in range(2,k):
    if check[i] == True:
        if p % i == 0:
            flag = False
            break
if flag:
    print("GOOD")
else:
    print("BAD",i)