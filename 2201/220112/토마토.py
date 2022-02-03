from  collections import deque
queue = deque()
m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 : queue.append([i,j])

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs() :
    while queue:
        x,y = queue.popleft()
        for i in range(4) :
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]==0 :
                queue.append([nx,ny])
                arr[nx][ny] = arr[x][y]+1

bfs()
ans = 0

for i in arr :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans-1)