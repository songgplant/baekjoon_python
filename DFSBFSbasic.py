# graph = [[] for _ in range(10)] # 빈 리스트 만들기
# print(len(graph))
# graph[0].append((1, 7))
# graph[0].append((2, 5))
# print(graph)
# print(type(graph[0][0]))

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, "를 True로 바꿉니다")
    print(v, end=' ')

    for i in graph[v] :
        print(v, "와 연결된 노드들 반복합니다")
        if not visited[i] : # 방문하지 않았다면
            dfs(graph, i, visited) # 방문처리를 하러 갑니다

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9
dfs(graph, 1, visited)
#----------------------------------------------------

from collections import deque
def bfs(graph, start, visited) :
    queue = deque([start])
    print("큐에 start를 넣었습니다")
    visited[start] = True
    print("start노드를 방문처리합니다")
    print(visited)
    
    while queue : # queue가 Fales이면 중단
        print(visited)
        v = queue.popleft()
        print(v, end=' ')
        print(v,'랑 연결된 노드를 파악')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9
bfs(graph, 1, visited)