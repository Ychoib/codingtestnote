from collections import defaultdict
import sys
input = sys.stdin.readline
array = defaultdict(int)

count_ = 0
while True:
    temp = input().rstrip()
    if not temp:
        break
    array[temp] += 1
    count_ += 1

tree_list = list(array.keys())
tree_list.sort()
for i in tree_list:
    print("%s %.4f" %(i, array[i]/count_ * 100))