# 유기농배추
# https://www.acmicpc.net/problem/1012
test_case = int(input())

for t in range(test_case) :
    M, N, K = map(int, input().split())

    # 직사각형 가로길이M, 세로길이N, 배추위치 좌표개수
    graph = [[0 for _ in range(M+1)] for _ in range(N+1)]

    # 배추 채우기
    for i in range(K) :
        a, b = map(int, input().split())
        graph[a][b] = 1

    def dfs(x, y) :
        if x <= -1 or x >= M or y <= -1 or y >= N :
            return False
        if graph[x][y] == 1 :
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False

    result = 0
    for i in range(M) :
        for k in range(N) :
            if dfs(i, k) == True :
                result += 1
    print(result)