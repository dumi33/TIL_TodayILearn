import sys
from collections import deque
q = deque()
input = sys.stdin.readline
n,m =  map(int ,input().split())

arr = [list(map(int,input().strip())) for _ in range(n)]
vis = [[[0]*2 for _ in range(m)] for __ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    q.append([0,0,1])
    vis[0][0][1] = 1
    while q :
        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return vis[x][y][z]
        for i in range(4) :
            nx , ny= dx[i]+x,  dy[i]+y
            if 0<=nx<n and 0<=ny<m: # 어처구니없게 여기에 n,m대신 x,y를 넣음
                if arr[nx][ny]==1 and z == 1 :
                    vis[nx][ny][0] = vis[x][y][1] +1
                    q.append([nx,ny,0])
                elif arr[nx][ny]==0 and vis[nx][ny][z]==0 :
                    q.append([nx,ny,z])
                    vis[nx][ny][z] = vis[x][y][z] +1
    return -1

    
print(bfs())
