from collections import deque
dx = [0,-1,0,1]
dy = [1,0,-1,0]

if __name__ == "__main__" : 
    graph =[list(map(int,input().split())) for i in range(7)]
    ch = [[0]*7 for i in range(7)]
    dq = deque()
    ch[0][0] = 1
    dq.append((0,0))
    while dq :
        if graph[6][6] != 0 :
            break
        x,y = dq.popleft()
        for i in range(4) :
            nx , ny = dx[i]+x, dy[i]+y
            if 0<=nx<7 and 0<=ny<7 and graph[nx][ny] == 0 and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                dq.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1

    print(graph[6][6] if graph[6][6]!= 0 else -1)
