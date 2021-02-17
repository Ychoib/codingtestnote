import sys
input = sys.stdin.readline

d = [[-1 for i in range(101)] for i in range(101)]
arr = ""
def possiblenum(a,z):
    if a == 0 or z == 0:
        return 1
    ret = d[a][z]
    if ret != -1:
        return ret
    ret = min(possiblenum(a-1,z) + possiblenum(a,z-1),1000000000+1)
    return ret
def strarr(a,z,length):
    global arr
    if a == 0:
        for i in range(z):
            arr += "z"
            return
    elif z == 0:
        for j in range(a):
            arr += "a"
            return
    #a를 제일 앞에 두었을때 경우의 수
    idx = possiblenum(a-1,z)
    if idx >= length: #a를 제일 앞에 두었을때 나오는 경우의 수 > 순번 (제일 앞에 a가 나와야한다)
        arr += "a"
        strarr(a-1,z,length)
    else:
        arr += "z"
        strarr(a,z-1,length-idx) #z가 앞에 올때 idx만큼 순서를 건너 뛰었으므로 전체길이에서 idx제외해 순서를 건너뛴다.


temp = []
noword = 0
n,m,k = map(int,input().split())
if possiblenum(n,m) < k:
    noword = 1
else:
    strarr(n,m,k)
if noword:
    print(-1)
else:
    print(arr)