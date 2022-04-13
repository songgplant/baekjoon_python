# 시간초과, 답은 맞음
num = int(input("총 지역 개수 : "))
liters = list(map(int, input().split()))
moneys = list(map(int, input().split()))
totallist = []

def stepsum(n, money, liter) :
    sum = 0
    for i in range(n+1) :
        sum += money[i] * liter[i]
    return sum

# moneys[0]*liters[0:2] # 0,1
# moneys[0]*liters[0:3] # 0,1,2
# moneys[0]*liters[0:4] # 0,1,2,3
for x in range(num-1) :
    frontsum = moneys[0]*sum(liters[0:x])
    needmoney = moneys[x:]
    needliter = liters[x:]

    for k in range(len(needmoney)) :
        if k == 0 :
            total = needmoney[0]*sum(needliter[0:])
        else :
            total = stepsum(k-1, needmoney, needliter) + needmoney[k]*sum(needliter[k:])
        totallist.append(frontsum+total)

# for k in range(num) :
#     if k == 0 :
#         total = moneys[0]*sum(liters[0:])
#     else :
#         total = stepsum(k-1, moneys, liters) + moneys[k]*sum(liters[k:])
#     totallist.append(total)

print(min(totallist))

# 실행시간 생각하기
n = int(input())
roads = list(map(int, input().split())) # 지역 간 거리
costs = list(map(int, input().split())) # 지역 개수n만큼

res = roads[0]*costs[0]
m = costs[0]
dist = 0
for i in range(1, n-1) : # 첫지역 건너뛰기
    if costs[i] < m :
        res += m*dist
        dist = roads[i]
        m = costs[i]
    else :
        dist += roads[i]
    if i == n-2 :
        res += m*dist
print(res)