import sys,copy
input = sys.stdin.readline

n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
op = []


sum_number = copy.deepcopy(maps)

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            sum_number[0][j] += sum_number[0][j-1]
        elif j == 0:
            sum_number[i][0] += sum_number[i-1][0]
        else:
            #슬라이싱은 end 값을 제외하므로 +=를 해준다.
            sum_number[i][j] += sum_number[i-1][j] + sum(maps[i][:j])
for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == 1 and y1 == 1:
        print(sum_number[x2-1][y2-1])
    elif x1 == 1:
        print(sum_number[x2-1][y2-1] - sum_number[x2-1][y1-2])
    elif y1 == 1:
        print(sum_number[x2-1][y2-1] - sum_number[x1-2][y2-1])
    else:
        print(sum_number[x2-1][y2-1] - sum_number[x1-2][y2-1] - sum_number[x2-1][y1-2] + sum_number[x1-2][y1-2])
