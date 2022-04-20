a, b = map(int, input().split())
# min(a, b) 까먹음
for i in range(min(a, b), 0, -1) :
    if a%1 == 0 and b%1 == 0 :
        print(i)
    break
for i in range(max(a, b), (a*b)+1) :
    if i%a == 0 and i%b==0 :
        print(i)
    break

import math
print(math.gcd(a, b)) # Greatest Common Divisor
print(math.lcm(a, b)) # Least Common Multiple