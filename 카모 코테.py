answer = 0
def solution(N, S):
    # write your code in Python 3.8.10
    seat = list(map(str,S.split()))
    alpa = ["A","B","C","D","E","F","G","H","J","K"]
    maps = [[0 for _ in range(10)] for _ in range(N)] 
    for n in seat:
        print(n)
        maps[int(n[0:-1])-1][int(alpa.index(n[-1]))] = -1
    
    for x in range(N):
        seatstatus = maps[x]
        for y in range(10):
            if seatstatus[y] == 0:
                print("y : ",y)
                chkseat(seatstatus,y)
    print(maps)
    print(answer)
                
    pass
def chkseat(seatstatus,y):
    global answer
    if y == 1:
        if seatstatus[1:5].count(0) == 4:
            seatstatus[1],seatstatus[2],seatstatus[3],seatstatus[4] = 1,1,1,1
            answer += 1
    elif y == 3:
        if seatstatus[3:7].count(0) == 4:
            seatstatus[3],seatstatus[4],seatstatus[5],seatstatus[6] = 1,1,1,1
            answer += 1 
    elif y == 5:
        if seatstatus[5:9].count(0) == 4:
            seatstatus[5],seatstatus[6],seatstatus[7],seatstatus[8] = 1,1,1,1
            answer += 1
[-1,0,-1,-2,0,0,0,0,-2,0,0,0]

#solution(2,"1A 2F 1C")
solution(22,"1A 3C 2B 20G 5A")