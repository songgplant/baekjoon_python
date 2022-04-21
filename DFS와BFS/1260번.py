# DFS와 BFS
# https://www.acmicpc.net/problem/1260

N, M, V = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v) :
    visited[v] = 1
    print(v, end=' ')
    for i in range(N+1) :
        if graph[v][i] == 1 and visited[i] == 0 :
            dfs(i)

from collections import deque
def bfs(v) :
    myqueue = deque()
    myqueue.append(v)
    visited[v] = 1

    while myqueue :
        v = myqueue.popleft()
        print(v, end=' ')
        for i in range(1, N+1) :
            if graph[v][i] == 1 and visited[i] == 0 :
                myqueue.append(i)
                visited[i] = 1

dfs(V)
visited = [0]*(N+1)
print()
bfs(V)
