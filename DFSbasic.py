graph = [[] for _ in range(10)] # 빈 리스트 만들기
print(len(graph))
graph[0].append((1, 7))
graph[0].append((2, 5))
print(graph)
print(type(graph[0][0]))