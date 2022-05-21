# 미로 탐색
# https://www.acmicpc.net/problem/2178
# N개의 줄에 M개의 정수 미로 : 가로길이 M 세로길이 N
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N) :
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue : # queue가 False이면 == 큐가 빈다면
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M :
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 : # 미로 길 이라면
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

    return graph[N-1][M-1] # 인덱스는 하나 작은 숫자

print(bfs(0,0))