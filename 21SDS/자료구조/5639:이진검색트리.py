import sys

def postorder(start,end):
    if start > end:
        return
    div = end + 1
    for i in range(start+1,end+1):
        if tree[start] < tree[i]:
            div = i
            break
    postorder(start+1,div-1)
    postorder(div,end)
    print(tree[start])



tree = []
count = 0
while count <= 100000:
    try:
        new = int(input())
    except:
        break
    tree.append(new)
    count+=1
postorder(0,len(tree)-1)


