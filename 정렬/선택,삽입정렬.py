
#선택 정렬( O(n^2) )
array1 = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array1)):
    min_index = i
    for j in range(i+1, len(array1)):
        if array1[min_index] > array1[j]:
            min_index = j
    array1[i],array1[min_index] = array1[min_index], array1[i]
print(array1)

#삽입 정렬( O(n^2) )
array2 = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array2)):
    for j in range(i,0,-1):
        if array2[j] < array2[j-1]:
            array2[j],array2[j-1] = array2[j-1],array2[j]
        else:
            break
print(array2)
