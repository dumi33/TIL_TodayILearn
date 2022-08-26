from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def changeDir(t) :
    global dir 
    for x,c in dirList :
        if x == t : 
            if c == "L" : 
                dir = (dir-1)%4 
            elif c == "D" :
                dir  = (dir+1)%4
        


def move() :
    global dir
    time = 0
    
    while True :
        time +=1 
        # 가장 최근 위치 ( 머리 )
        cx,cy = snake[-1]
        nx,ny = cx+dx[dir], cy+dy[dir]

        # 벽에 부딫이지않고 뱀이 없다면 
        if 0<=nx<n and 0<=ny<n and mp[nx][ny] != 2 :
            # 사과가 없다면
            # 꼬리를 뺀다. 
            if mp[nx][ny]==0 : 
                fx,fy = snake.popleft()
                mp[fx][fy] = 0
            mp[nx][ny] = 2 
            snake.append([nx,ny])
        else :
            return time 
        
        # 방향 전환 
        changeDir(time)
        
        
    



if __name__=="__main__" :
    n = int(input())
    k = int(input())
    mp = [[0]*n for _ in range(n)]
    
    # 사과 자리 표시 
    for _ in range(k) :
        a, b = map(int,input().split())
        mp[a-1][b-1] = 1 
    
    # 시간에 따른 방향 변화 
    dirList = []
    l = int(input())
    for _ in  range(l) :
        x,c = input().split()
        dirList.append([int(x),c])
    
    # 첫 방향은 오른쪽 
    dir= 0 
    snake = deque()
    # 첫 위치를 넣어준다. 
    snake.append([0,0])
    
    print(move())
