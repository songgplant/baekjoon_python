# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
# 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

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
