import sys

n,m = map(int,input().split())
namelist = []
powerlist = []
for i in range(n):
    name, power = sys.stdin.readline().split(' ')
    namelist.append(name)
    powerlist.append(int(power))
plist = []


for j in range(m):
    p = int(sys.stdin.readline())
    start = 0
    end = len(powerlist) - 1
    while start <= end :
        mid = (start + end) // 2
        if p > powerlist[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(namelist[end + 1])
