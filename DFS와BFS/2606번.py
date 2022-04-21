# 바이러스
# https://www.acmicpc.net/problem/2606

# 컴퓨터 수
N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 노드 간선 정보 수
M = int(input())

# 정보 입력
for i in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 # 영행렬에 이어지는 정보 추가

def dfs(v) :
    visited[v] = 1
    for i in range(N+1) :
        if graph[v][i] == 1 and visited[i] == 0 :
            dfs(i)

visited = [0]*(N+1)
dfs(1)
print(visited.count(1)-1)
