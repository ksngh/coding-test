from collections import deque

def bfs():
    queue = deque([(0, 0, 1)])  # (x, y, 이동 거리)
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        if x == columns - 1 and y == rows - 1:  # 목적지 도착 시 거리 반환
            return dist

        # 4방향 탐색 (좌, 우, 상, 하)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < columns and 0 <= ny < rows and graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, dist + 1))

    return -1  # 도달 불가능한 경우

# 입력 예시
rows, columns = map(int, input().split())  # 예제: 4 6
graph = [list(map(int, input().strip())) for _ in range(rows)]
visited = [[False] * columns for _ in range(rows)]

# BFS 실행
result = bfs()
print(result)
