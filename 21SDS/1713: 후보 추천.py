from collections import defaultdict

n = int(input())
m = int(input())

array = list(map(int,input().split()))

# 이름 (빈도 수, 순서)
photo = []
# 추천받은 빈도 수
pick = defaultdict(int)

for i in array:
    pick[i] += 1
    if i in photo:
        continue
    elif len(photo) < n:
        photo.append(i)
    elif len(photo) >= n:
        minimum = 1001
        for j in photo:
            if pick[j] < minimum:
                minimum = pick[j]
                d = j
        else:
            photo.remove(d)
            del(pick[d])
            photo.append(i)
photo.sort()
print(*photo)

