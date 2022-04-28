# 답은 나오는데 틀렸습니다.. 코드
from collections import deque
visited = [0]*30

N = int(input())

def findmin() :
    queue = deque([])
    queue.append(N)

    while queue :
        # print(queue)
        x = queue.popleft()

        if x == 1 :
            print(visited[x])
            break

        if x % 5 == 0 and visited[x] :
            visited[x//5] = visited[x] + 1
            queue.append(x//5)
        if x % 3 == 0 and visited[x] :
            visited[x//3] = visited[x] + 1
            queue.append(x//3)
        if x % 2 == 0 and visited[x] :
            visited[x//2] = visited[x] + 1
            queue.append(x//2)

        visited[x-1] = visited[x] + 1
        queue.append(x-1)

findmin()

# 정상 코드
# x = int(input())
# d = [0]*30001
#
# for i in range(2, x+1) :
#     d[i] = d[i-1]+1
#     if i % 2 == 0 :
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0 :
#         d[i] = min(d[i], d[i//3]+1)
#     if i % 5 == 0 :
#         d[i] = min(d[i], d[i//5]+1)
#
# print(d[x])