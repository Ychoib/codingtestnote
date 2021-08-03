from collections import deque
c = [deque(input()) for _ in range(4)]
cycle_num = int(input())
def clock_rolling(select):
    global c
    temp = c[select].pop()
    c[select].appendleft(temp)
def banclock_rolling(select):
    global c
    temp = c[select].popleft()
    c[select].append(temp)
def rolling(select,direction):
    global c
    print(c)
    if direction == 1:
        clock_rolling(select)
        if 0 <= select + 1 < len(c):
            if c[select][2] != c[select+1][6]: #오른쪽 바퀴 돌아가야하는 상황
                rolling(select+1,direction * -1)
        else:
            return
        if 0 <= select - 1 < len(c):
            if c[select][6] != c[select-1][2]: #왼쪽 바퀴 회전
                rolling(select-1,direction * -1)
        else:
            return

    else:
        banclock_rolling(select)
        if 0 <= select + 1 < len(c):
            if c[select][2] != c[select+1][6]: #오른쪽 바퀴 돌아가야하는 상황
                rolling(select+1, (-1 *direction))
        else:
            return
        if 0 <= select - 1 < len(c):
            if c[select][6] != c[select-1][2]:
                rolling(select-1,(direction * -1))
        else:
            return



import sys
for i in range(cycle_num):
    c_select,direction = list(map(int,sys.stdin.readline().split()))
    rolling(int(c_select)-1,direction)
    print(c)
    print("next")

print(c)
result = 0
for i in range(4):
    if i == 0 and c[i][0] == '1':
        result += 1
    elif i == 1 and c[i][0] == '1':
        result += 2
    elif i == 2 and c[i][0] == '1':
        result += 4
    elif i == 3 and c[i][0] == '1':
        result += 8
print(result)