# 단지 번호 붙이기
# https://www.acmicpc.net/problem/2667
# 아파트단지 배치도 입력
N = int(input())
graph = []

for i in range(N) :
    graph.append(list(map(int, input())))

cnt = 0
def dfs(x, y) :
    global cnt
    if x <= -1 or x >= N or y <= -1 or y >= N :
        return False
    if graph[x][y] == 1 :
        graph[x][y] = 2
        cnt += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
total_lst = []
for i in range(N) :
    for k in range(N) :
        if dfs(i, k) == True :
            result += 1
            total_lst.append(cnt)
            cnt = 0

total_lst.sort()
print(result)
for i in total_lst : print(i)