dic = {}


def fibonacci_2(n):
    if n in dic:
        return dic[n]
    if n == 0:
        dic[0] = 0
        return 0
    elif n ==1:
        dic[1] = 1
        return 1
    else:
        dic[n] = fibonacci_2(n-1) + fibonacci_2(n-2)
        return dic[n]