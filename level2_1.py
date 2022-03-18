from collections import deque

def solution(maps):
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    rows = len(maps)
    cols = len(maps[0])

    graph = [[-1 for _ in range(cols)] for _ in range(rows)]

    queue = deque()
    queue.append([0,0])
    graph[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(0<=ny<rows)and(0<=nx<cols)and(maps[nx][ny]==1):
                if graph[ny][nx]==-1:
                    graph[ny][nx]=graph[y][x]+1
                    queue.append([ny,nx])
    answer = graph[-1][-1]
    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))