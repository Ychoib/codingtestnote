import sys
"""
input = sys.stdin.readline

def podo(amount, n):
    temp = amount.copy()
    bags = []
    bag = 0
    for i in range(n):
        if i != 0:
            temp = amount[i:] + amount[:i]
        for j in range(1,n+1):
            if j % 3 == 0:
                continue
            bag += temp[j-1]
        bags.append(bag)
        bag = 0
    return bags


n = int(input())
amount = []
for i in range(n):
    amount.append(int(input()))

print(max(podo(amount,n)))
"""
n = int(input())
podo = [0]

for i in range(n):
    podo.append(int(input()))

dp = [0]
dp.append(podo[1])
dp.append(podo[1] + podo[2])
for i in range(3,n + 1):
    dp.append(max(dp[i-1],dp[i-2] + podo[i],dp[i-3] + podo[i-1] + podo[i]))
print(dp[n])
