n = int(input())
x = list(map(int,input().split()))
x_ = sorted(set(x))
cnt_list = []

temp = {x_[i] : i for i in range(len(x_))}
for i in x:
    print(temp[i], end = " ")



