#최대값 찾기

def bs(low,high):
    mid = 0
    while low <= high :
        mid = (low + high) / 2
        if check(mid) : low = mid + 1;
        else:   high = mid - 1;
    return low - 1

#최소값 찾기
def bs(low,high):
    mid = 0
    while low <= high:
        mid = (low + high) / 2