"""
dp[i] = i번째 앱까지 봤을때 얻을 수 있는 최대 메모리
i번째 앱을 비활성화하는 경우
i번째 앱을 비활성화 하지 않는 경우


dp[i] = max(dp[i-1] + Mi,dp[i-1])
------------------------------------------------------------
dp[i][j] = i번째 앱까지 봤을 때, j만큼의 비용을 써서 얻을 수 있는 최대 메모리

i-1번째까지 봤을때, i번째 앱을 비활성화 or 그냥 냅둠을 선택할 수 있다

1)비활성화:
i-1 c[i]의 비용을 쓰면서 앱을 비활성화 했다.
그래서 i,j상태가 되었다.
d[i][j] <- d[i-1][j-c[i]+m[i]]

2)i번쨰 앱을 그냥 냅둠
냅둠으로써 j만큼의 비용을 사용
d[i][j] <- d[i-1][j]

d[i][j] = max(d[i-1][j-c[i]+m[i],d[i-1][j])

j < c[i] -> d[i-1][j]

i,j가 상태가 되기 위해선
1) i-1,j 상태에서 걍 아무것도 안함
2) i-1, j-c[i] 상태에서 i번째 앱을 비활성화함으로써 c[i]의 비용을 더 들이며 m[i]의 메모리를 생성
"""

n,m = map(int,input().split())

byte = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))
result = sum(cost)
d = [[0 for i in range(result+1)] for _ in range(n + 1)]

for i in range(1,n + 1):
    by = byte[i]
    co = cost[i]
    for j in range(1,sum(cost) + 1):
        if j < co:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j],by + d[i-1][j-co])

        if d[i][j] >= m:
            result = min(result, j)
if m!=0:
    print(result)
else:
    print(0)



