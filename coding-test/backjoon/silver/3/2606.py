import sys

com = int(sys.stdin.readline().rstrip())
rep = int(sys.stdin.readline().rstrip())
graph = [[] for j in range(com+1)]
visited = [False]*(com+1)

for i in range(rep) :
    a,b = map(int,sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(n) :
    visited[n] = True
    for j in graph[n] :
        if not visited[j]:
            global cnt
            cnt+=1
            dfs(j)

dfs(1)
print(cnt)
