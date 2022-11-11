import sys
input = sys.stdin.readline

money = int(input())

chart = list(map(int,input().split()))

cnt = 0
jun = []
jun_money = money
# 매수 주식수, 총 자산
for i in chart:
    if chart[-1] == i:
        jun_money += i * cnt
        break
        #print(chart[-1] * cnt) #마지막날의 주식 가격 * 산 주식 수 
        
    #돈이 있을때 매수
    if jun_money > 0:
        cnt += jun_money // i #매수한 주식 수 
        jun_money -= i * (jun_money // i)  #풀매수한 주식만큼 총자산에서 빼기
        #print("jun_cnt", cnt)
        
#print("jun money: ",jun_money)
    
# 10 20 23 34 55 30 22 19 12 45 23 44 34 38
sung_money = money
upcnt,dncnt =0,0
sung = []
cnt = 0
for i in range(len(chart)):
    #print("day", i + 1)
    #print("chart : ", chart[i])
    
    if chart[-1] == chart[i]:
        sung_money += chart[i] * cnt
        break
        #print(chart[-1] * cnt) #마지막날의 주식 가격 * 산 주식 수 
        
    if i > 0 :
        if chart[i] > chart[i-1]:
            upcnt += 1
            dncnt = 0
        elif chart[i] < chart[i-1]:
            dncnt += 1
            upcnt = 0
    #print("upcnt : ",upcnt)   
    #print("dncnt : ",dncnt)
    
    #3번 떨어지면 풀매수
    if dncnt >= 3:
        if sung_money > 0:
            cnt += sung_money // chart[i] #매수한 주식 수 
            sung_money -= chart[i] * (sung_money // chart[i]) #풀매수한 주식만큼 총자산에서 빼기

    #3번 오르면 풀매도
    if upcnt >= 3:
        if cnt > 0:
            sung_money += chart[i] * cnt
            cnt = 0

        
    #print("cnt : ",cnt)
    #print("sung_money :",sung_money)
    #print()
    
#print("jun_money :",jun_money)
       
#print("sung money: ",sung_money)
#print()

if sung_money > jun_money: print("TIMING")
elif jun_money > sung_money: print("BNP")
else: print("SAMESAME") 