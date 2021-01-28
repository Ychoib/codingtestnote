n = int(input())

board = [[0] * n for i in range(n)]
"""
count = 0
def check(r,c):
    global count
    for i in range(n):
        board[i][c] = 1
    for j in range(n):
        board[r][j] = 1
    board[r][c] = 2
    while 0 <= r+1 < n and 0 <= c+1 < n:
        r = r + 1
        c = c + 1
        board[r][c] = 1
    while 0 <= r-1 < n and 0 <= c-1 < n:
        r = r - 1
        c = c - 1
        board[r][c] = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                check(i,j)

    if board.count(2) == n:
        count += 1

for i in range(n):
    for j in range(n):
        check(i,j)
print(count)
"""


def adjacent(x):
    