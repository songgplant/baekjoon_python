#테스트케이스 무한
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break # while문 중단
    if b % a == 0 :
        print("factor")
    elif a % b == 0 :
        print("multiple")
    else :
        print("neither")