# 토마토
# https://www.acmicpc.net/problem/7576
# 토마토 문제 고민 중
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

for i in range(4) :
    for k in range(5) :
        if tomatoes[i][k] == 1 :
            queue.append((i, k))

def bfs(x, y) :
    global days
    global queue
    # queue.append((x, y))


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
