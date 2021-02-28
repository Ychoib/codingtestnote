import sys
"""
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
money = []
for i in range(n):
    money.append(list(map(int,input().split())))

def select():
    bag = 0
    # 첫 집의 최소값 비용 더해주기
    bag += min(money[0])
    idx = money[0].index(min(money[0]))
    # 두 번째 집부터 이전의 색을 제외한 색들 중 최소값 찾기
    for i in range(1,len(money)):
        temp = []
        # 이전에 사용했던 색을 제외한 색들 중 비용 최소값 찾기
        for j in range(len(money[i])):
            if j == idx:
                continue
            else:
                # 제외한 색들을 temp에 따로 담아준다.
                temp.append(money[i][j])
        # 이전 집의 최소 비용을 가지는 색의 인덱스 업데이트
        idx = money[i].index(min(temp))
        # 제외된 색들중 최소값을 찾아 더해주기
        print(idx)
        bag += min(temp)
    return bag
print(select())
"""

#dp사용
input = sys.stdin.readline
n = int(input())

matrix = []
dp = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    if i == 0:
        dp[i] = matrix[i]
    else:
        dp[i][0] = matrix[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = matrix[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = matrix[i][2] + min(dp[i-1][0],dp[i-1][1])
min_num = min(dp[n-1][0],dp[n-1][1],dp[n-1][2])
print(min_num)