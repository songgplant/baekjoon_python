# 토마토
# https://www.acmicpc.net/problem/7576
from collections import deque
# 가로길이 M 세로길이 N
# 좌표 : [x, y] -> x가 줄 개수니까 x=>N, y=>M
M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(N) :
    for k in range(M) :
        if tomatoes[i][k] == 1 :
            queue.append([i, k])

def bfs() : # 이미 1의 위치를 넣어놨기 때문에 변수 필요x
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0 :
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx, ny])

bfs()

# 이 아래 부분이 for문으로 비교해야 해서 느리다..
# 검색을 참고해 작성한 코드. exit(0)을 사용하지 않는 방향이 좋은 것 같다.
# flag처럼 변수를 사용하여 안익은 토마토(0)를 표기하는 게 헷갈리지 않고 좋은 것 같다.
flag = False
for i in tomatoes :
    for k in i :
        if k == 0 :
            flag = True
        answer = max(answer, k)

if flag == True :
    print(-1)
elif answer == 1 :
    print(0)
else :
    print(answer-1)

"""
실패한 코드
tomatoes = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,1]
]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
days = 0

from collections import deque
queue = deque()
searching = list()

for i in range(4) :
    for k in range(5) :
        if tomatoes[i][k] == 1 :
            queue.append((i, k))
            searching.append((i, k))

def bfs() :
    global days
    global queue
    global searching
    # queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=4 :
                continue
            if tomatoes[nx][ny] == 1 or tomatoes[nx][ny] == -1 :
                continue
            if tomatoes[nx][ny] == 0 :
                tomatoes[nx][ny] = 1
                queue.append((nx, ny))

        if set(list(queue)) - set(searching) == set(list(queue)) :
            days += 1
            searching = list(queue)

    return tomatoes

print(bfs())
"""


