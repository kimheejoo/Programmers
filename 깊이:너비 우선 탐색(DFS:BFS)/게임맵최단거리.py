def solution(maps):
    from collections import deque
    n = len(maps)
    m = len(maps[0])
    directions_x = [1, -1, 0, 0] # 동서남북 x
    directions_y = [0, 0, 1, -1] # 동서남북 y
    q = deque()
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        for x, y in zip(directions_x, directions_y):
            if (0 <= i+x < n and 0 <= j+y < m):
                if (maps[i+x][j+y] == 1):
                    maps[i+x][j+y] = maps[i][j] + 1
                    q.append((i+x, j+y))
        
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1