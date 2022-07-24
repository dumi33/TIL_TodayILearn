dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque 

def changedir(dir,t) :
    if times[t] == 'L' :
        return (dir-1)%4
    if times[t] == 'D' :
        return (dir+1)%4

def game() :
    t = 0
    snake = deque([[0,0]])
    mp[0][0] = 2 # 뱀이 있어요 
    dir = 0 # 첫 방향은 오른쪽 
    while True :
        t+=1 
        nx,ny  = snake[-1][0] + dx[dir], snake[-1][1] + dy[dir]
        if 0<=nx<n and 0<=ny<n and mp[nx][ny] != 2 :
            if mp[nx][ny] !=1 : # 사과가 없다면 
                px,py=snake.popleft()
                mp[px][py] = 0 # 뱀이 빠져나감 
            mp[nx][ny] = 2  # 뱀이 들어옴 
            snake.append([nx,ny])
            if t in times.keys() :
                dir=changedir(dir,t)
        else :
            break 
    return t 
        
    
if __name__=="__main__" :
    n = int(input())
    k = int(input())
    mp = [[0]*n for i in range(n)]
    for i in range(k) :
        x,y = map(int,input().split())
        mp[x-1][y-1] = 1 # 사과 
    L = int(input())
    times = {}
    for i in range(L) :
        x,c = input().split()
        times[int(x)] = c
    print(game()) 
