

stack = []
orders = []
while True:
    order = input().split()
def gostack(num):
    stack.append(num)
    while True:
        if order[0] == "NUM":
            stack.append(order[1])
        elif order[0] == "END":
            num = int(input())
            for i in range(num):
                stack.append(input())
            break

print(gostack())