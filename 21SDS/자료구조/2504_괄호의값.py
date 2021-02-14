

def check_stack(new):
    stack = []
    for a in new:
        if a == "(" or a == "[":
            stack.append(a)
        elif a == ")" and stack:
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(a)
        elif a == "]" and stack:
            if stack[-1] == "[":
                stack.pop()
            else:
                stack.append(a)
        else:
            stack.append(a)
    if stack:
        return True
    else:
        return False

def calculate(new):
    stack = []
    for a in new:
        if a == "(":
            stack.append(a)
        elif a == ")":
            if stack [-1] == "(":
                stack[-1] = 2
            else:
                temp = 0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i] == "(":
                        stack[-1] = temp * 2
                        break
                    else:
                        temp += stack[i]
                        stack.pop()
        elif a == "[":
            stack.append(a)
        elif a == "]":
            if stack[-1] == "[":
                stack[-1] = 3
            else:
                temp = 0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i] == "[":
                        stack[-1] = temp * 3
                        break
                    else:
                        temp += stack[i]
                        stack.pop()
    return sum(stack)



new = input().strip()
if check_stack(new) == False:
    print(calculate(new))
else:
    print(0)