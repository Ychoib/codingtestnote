from math import gcd
child1,parent1 = map(int,input().split())

child2,parent2 = map(int,input().split())

rst_child = child1 * parent2 + child2 * parent1
rst_parent = parent1 * parent2

div = gcd(rst_child,rst_parent)

rst_child = rst_child // div
rst_parent = rst_parent // div

print("%d %d" %(rst_child,rst_parent))
