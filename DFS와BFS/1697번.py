# 숨바꼭질
# https://www.acmicpc.net/problem/1697
from collections import deque

N, K = map(int, input().split())
# N은 출발, K는 동생위치=도착점
max_num = 100000
visited = [0]*(max_num+1)

def bfs() :
    queue = deque()
    queue.append(N)
    while queue :
        x = queue.popleft()

        if x == K :
            print(visited[x])
            break

        for j in (x-1, x+1, x*2) :
            if 0 <= j <= max_num and not visited[j] :
                visited[j] = visited[x]+1
                queue.append(j)
bfs()