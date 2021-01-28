def init(a, tree, node, start, end):
    if start == end:
        tree[node-1] = start
    else:
        init(a,tree,node*2,start,(start+end)//2)
        init(a,tree,node*2+1,(start+end)//2+1,end)
        if a[tree[node*2-1]]<a[tree[node*2]]:
            tree[node-1] = tree[node*2-1]
        else:
            tree[node-1] = tree[node*2]

def query(a,tree,node,start,end,i,j):
    if i>end or j<start: # 주어진 범위가 전체 범위에 완전히 속하지 않는다면
        return -1
    if i<=start and end<=j: # 주어진 범위가 전체 범위를 완전히 포함한다면
        return tree[node-1] # 해당 범위의 최소값 index를 return 함

    # 주어진 범위가 전체 범위에 속해있다면
    # ex_) 0~4 index의 값이 주어졌을 때, 1~3 index에 대한 최소값을 구하고 싶음
    m1 = query(a,tree,2*node,start,(start+end)//2,i,j) # 전체 범위를 반으로 자른 범위를 넘기고 왼쪽 노드 값을 넘김
    m2 = query(a,tree,2*node+1,(start+end)//2+1,end,i,j) # 전체 범위를 반으로 자른 범위를 넘기고 오른쪽 노드 값을 넘김
    if m1==-1:
        return m2
    elif m2==-1:
        return m1
    else:
        if a[m1]<=a[m2]:
            return m1
        else:
            return m2