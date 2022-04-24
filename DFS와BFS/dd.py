from collections import deque
queue = deque()
queue.append((1, 2))
queue.append((3, 4))
print(queue)
print(type(queue))
print(list(queue))
print(type(list(queue)))
test = []
test.append((1,2))
queue = list(queue)
print(type(queue))
print(test)
if set(queue) - set(test) == set(queue) :
    print("있음")
    print(test)
else :
    print("차집합 결과가 아님")
    print(set(queue)-set(test))