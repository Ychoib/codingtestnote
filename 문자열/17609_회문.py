def firstcheck(word,left,right):
    while left < right :
        if word[left] != word[right]:
            move_left = secondcheck(word,left + 1, right)
            move_right = secondcheck(word,left,right-1)
            if move_left or move_right:
                return 1
            else:
                return 2
        else:
            left += 1
            right -= 1
    return 0
            
def secondcheck(word,left,right):
    while left < right : 
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
        
N = int(input())
for i in range(N):
    str_ = input()
    left,right = 0,len(str_) -1
    print(firstcheck(str_,left,right))
    
            
                
            


