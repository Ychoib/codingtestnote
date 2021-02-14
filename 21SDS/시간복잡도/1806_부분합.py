n,s = map(int,input().split())

array = list(map(int,input().split()))

sum_array = [0] * (n+1)

for i in range(1,n+1):
    sum_array[i] = sum_array[i-1] + array[i-1]

start_ = 0
end_ = 1
def partial_sum(start,end):
    answer = 1000001
    while start != n:
        result = sum_array[end] - sum_array[start]
        if result >= s:
            if end - start < answer:
                answer = end - start
            start += 1
        else:
            if end != n:
                end += 1
            else:
                start += 1
    if answer != 1000001:
        print(answer)
    else:
        print(0)

partial_sum(start_,end_)