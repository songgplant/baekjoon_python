graph = []
for i in range(3) :
    graph.append(list(map(int, input())))
print(graph)

def dfs(x, y) :
    print(x, y,'에서 dfs를 실행')
    if x <= -1 or x >= 3 or y <= -1 or y >= 3 :
        print(x,y,'가범위를 벗어남 false반환')
        return False
    if graph[x][y] == 0 :
        print(x,y,'가 0이라서 바꾸기')
        graph[x][y] = 1
        print(graph)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        print('상하좌우 확인하고 True를 리턴')
        return True
    print('false를 리턴')
    return False
result = 0
for i in range(3) :
    for k in range(3) :
        if dfs(i, k) == True :
            result += 1
print(result)