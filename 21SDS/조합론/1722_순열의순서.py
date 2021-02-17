import sys
import math
input = sys.stdin.readline

cache = {}
def factorial_recursive(n):
    global cache
    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * factorial_recursive(n-1)
        return cache[n]

    return n * factorial_recursive(n-1) if n > 1 else 1

n = int(input())

sec = list(map(int,input().split()))

if sec[0] == 1:
    k = sec[1]
    ans = []
    nums = list(range(1,n+1))
    key = k

    for i in range(n):
        step = (key -1) // factorial_recursive(n-1-i)
        ans.append(nums[step])
        nums.remove(nums[step])
        key -=  factorial_recursive(n-1-i)* step
    print(" ".join(map(str,ans)))
elif sec[0] == 2:
    num = sec[1:]
    sort_num = list(sorted(num))
    ans = 1 # 해당 수열이 몇번째 수열인지 저장
    for i in range(n):
        step = sort_num.index(num[i]) # 제일 앞에 수를 가져와 step을 결정한다.
        sort_num.remove(num[i])
        x = factorial_recursive(n-1-i)
        ans += (x*step)
    print(ans)
