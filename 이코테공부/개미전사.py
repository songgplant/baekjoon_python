# 다이나믹 프로그래밍(동적 계획법)
n = int(input())

array = list(map(int, input().split()))

d = [0]*100 #N의 조건 범위 만큼

d[0] = array[0] # 첫 번째거는 비교할 대상이 없음

d[1] = max(array[0], array[1]) # 비교 대상이 한 칸밖에 없음

for i in range(2, n) :
    d[i] = max(d[i-1], d[i-2]+array[i])
    # d라는 숫자합 저장 칸 개념을 이용한다고 생각
    # i-1칸까지의 합은 다 고려됨
    # i-2칸까지 합을 가져온다면 현재 array위치 숫자 덧셈 가능

print(d[n-1])