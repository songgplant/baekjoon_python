# 단지 번호 붙이기
# https://www.acmicpc.net/problem/2667
# 아파트단지 배치도 입력
N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

cnt = 0


def dfs(x, y):
    global cnt
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        cnt += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
total_lst = []
for i in range(N):
    for k in range(N):
        if dfs(i, k) == True:
            result += 1
            total_lst.append(cnt)
            cnt = 0

total_lst.sort()
print(result)
for i in total_lst: print(i)

"""
# BFS로 풀어야 하는 권장 풀이
from collections import deque

N = int(input())
graph = []
counts = []

for _ in range(N):
  graph.append(list(map(int, input())))

def bfs(x, y):
  dx = [-1, 1, 0, 0]  
  dy = [0, 0, -1, 1]

  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0
  count = 1

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        count += 1
  
  counts.append(count)

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(i, j)

counts.sort()
print(len(counts))

for i in counts:
  print(i)
"""
