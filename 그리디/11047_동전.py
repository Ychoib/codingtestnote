n,k = map(int,input().split())
token = []
for i in range(n):
    token.append(int(input()))

token.sort(reverse= True)

result = {}
for coin in token:
    coin_cnt = k // coin
    k -= coin * coin_cnt
    result[coin] = coin_cnt

print(sum(result.values()))