def solution(common):
    answer = 0
    for i in range(len(common)):
        if common[i+2] - common[i+1] == common[i+1] - common[i]:
            return common[-1] + (common[i+2] - common[i+1])
        else:
            return common[-1] * (common[i+2] / common[i+1])
        
    return answer

print(solution([1,2,3,4]))