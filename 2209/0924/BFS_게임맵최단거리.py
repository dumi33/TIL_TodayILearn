from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(maps):
    q = deque([[0,0]])
    n ,m = len(maps), len(maps[0])
    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1 : return maps[x][y]
        for i in range(4) :
            nx,ny= x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] +1 
                q.append([nx,ny])
    return -1 
