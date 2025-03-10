import sys
sys.setrecursionlimit(10000)

rep = int(sys.stdin.readline().rstrip())


def dfs(x, y):

    graph[y][x] = False
    if y - 1 >= 0 and graph[y - 1][x] == True:
        dfs(x, y - 1)

    if y + 1 < rows and graph[y + 1][x] == True:
        dfs(x, y + 1)

    if x - 1 >= 0 and graph[y][x - 1] == True:
        dfs(x - 1, y)

    if x + 1 < columns and graph[y][x + 1] == True:
        dfs(x + 1, y)



for i in range(rep):
    bugs = 0
    columns, rows, crops = map(int, sys.stdin.readline().rstrip().split(' '))
    graph = [[False for num in range(columns)] for _ in range(rows)]
    for j in range(crops):
        a, b = map(int, sys.stdin.readline().rstrip().split(' '))
        graph[b][a] = True

    for k in range(rows):
        for m in range(columns):
            if graph[k][m]:
                bugs += 1
                dfs(m, k)
    print(bugs)
