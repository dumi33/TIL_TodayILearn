from collections import deque
s = int(input())
vis = [[-1]*(s+1) for _ in range(s+1)]

q = deque()

def bfs() :
    vis[1][0] = 0
    q.append([1,0])
    while q :
        x,y = q.popleft()
        if vis[x][x] == -1 :
            vis[x][x] = vis[x][y]+1
            q.append([x,x])
        if x+y <= s and vis[x+y][y]==-1 :
            vis[x+y][y] = vis[x][y]+1
            q.append([x+y,y])
        if x-1 >=0 and vis[x-1][y]==-1 :
            vis[x-1][y] = vis[x][y]+1
            q.append([x-1,y])
    
bfs()
ans = -1
for i in range(s+1):
    if ans==-1 or ans > vis[s][i] :
        ans = vis[s][i]

print(ans)