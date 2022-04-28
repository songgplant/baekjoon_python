## 다이나믹 프로그래밍(동적 계획법)
# 코드 자료 : 책) 이것이 취업을 위한 코딩 테스트다 with 파이썬
# 피보나치 수열 소스코드(재귀적)
d = [0]*100

def fibo(x) :
    print('fibo(', x, ')를 실행했습니다')
    if x == 1 or x == 2 :
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    # fibo(x)+fibo(x-1)이 아님을 주의
    # fibo(x-1)부터 순차적으로 함수를 실행하는 것에 주의!
    # fibo(x-1)과 fibo(x-2) 동시 실행이 아님!!

    return d[x]

print(fibo(6))
#-------------------------------------------
# 피보나치 수열 (반복적, bottom-up)
d = [0]*100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1) :
    d[i] = d[i-1]+d[i-2]
print(d[n])

