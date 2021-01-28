import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    order = list(map(str,sys.stdin.readline().split()))
    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            result = stack.pop()
            print(result)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)