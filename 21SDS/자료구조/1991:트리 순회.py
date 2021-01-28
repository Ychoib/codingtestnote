import sys
tree = {}
def preorder(node):
    if node == ".":
        return
    print(node, end = "")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == ".":
        return
    inorder(tree[node][0])
    print(node, end = "")
    inorder(tree[node][1])

def postorder(node):
    if node == ".":
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = "")

n = int(sys.stdin.readline())

for i in range(n):
    result = list(map(str,sys.stdin.readline().split()))
    root, left, right = result[0], result[1], result[2]
    tree[root] = (left,right)

preorder("A")
print()
inorder("A")
print()
postorder("A")