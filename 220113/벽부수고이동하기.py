from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs() :
    q= deque()
    vis = [[[0] * 2 for _ in range(m)] for __ in range(n)]
    q.append([0,0,1])
    vis[0][0][1] = 1
    while q :
        x,y,z = q.popleft()
        if x==n-1 and y == m-1 : 
            return vis[x][y][z]
        for i in range(4) :
            nx, ny = dx[i] + x,  dy[i] + y
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny] == 1 and z == 1 : # 벽을 안뚫은 상태 
                    q.append([nx,ny,0])
                    vis[nx][ny][0] = vis[x][y][1]+1
                elif arr[nx][ny] == 0 and vis[nx][ny][z]==0: # arr에 갈 수 있고 간적없다면
                    vis[nx][ny][z] = vis[x][y][z]+1
                    q.append([nx,ny,z])
    return -1


n,m = map(int ,input().split())

arr = [(list(map(int,list(input().strip()))))for _ in range(n)]
print(bfs())
