from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

    
if __name__=="__main__" :
    graph = [list(map(int,input().split()))for _ in range(7)]
    dis = [[-1]*7 for _ in range(7)]
    dq = deque()
    dis[0][0] = 0
    dq.append((0,0))
    
    while dq :
        now = dq.popleft()
        x = now[0]
        y = now[1]
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<7 and 0<=ny<7 and dis[nx][ny] == -1 and graph[nx][ny] == 0:
                dis[nx][ny] = dis[x][y] +1 
                dq.append((nx,ny))
    print(dis[6][6])
