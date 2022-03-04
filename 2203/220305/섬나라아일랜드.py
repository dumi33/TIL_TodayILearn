from collections import deque
dx = [0,-1,0,1,1,-1,-1,1]
dy = [1,0,-1,0,1,1,-1,-1]




if __name__ == "__main__" : 
    n = int(input())
    graph = [list(map(int,input().split())) for i in range(n)]
    dq = deque()
    cnt=0
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] == 1 :
                dq.append((i,j))
                graph[i][j] = 0
                while dq :
                    x,y = dq.popleft()
                    for k in range(8) :
                        nx,ny = dx[k]+x, dy[k]+y
                        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1 :
                            graph[nx][ny] = 0 
                            dq.append((nx,ny))
                cnt+= 1
    print(cnt)
