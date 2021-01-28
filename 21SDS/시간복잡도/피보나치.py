d = []
def dp(n):
    if n == 0: return 0
    elif n == 1: return 1

    # memoization
    if d[n] > 0: return d[n]

    # 점화식
    d[n] = dp(n-1) + dp(n-2)
    return d[n]

