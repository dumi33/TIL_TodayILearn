from collections import deque


dx = [1,0,-1,0] 
dy = [0,1,0,-1]


def change(dir,c) :
    if c == "L" :
        return (dir+1)%4
    else :
        return (dir-1)%4


def move() :
    snake = deque([[0,0]])
    x,y = 0,0 
    dir = 1 
    time = 1 
    while True :
        x,y = x + dx[dir], y + dy[dir]
        if 0<=x<n and 0<=y<n and mp[x][y] !=2 :
            if mp[x][y] != 1 :
                tmp_x,tmp_y = snake.popleft()
                mp[tmp_x][tmp_y] = 0
            snake.append([x,y])
            mp[x][y] = 2
            if time in times.keys() :
                dir = change(dir, times[time])
            time +=1 
        else : 
            return time 

                        
if __name__=="__main__" :
    n = int(input())
    mp = [[0]*(n) for i in range(n)]
    for i in range(int(input())) :
        a,b = map(int,input().split()) 
        mp[a-1][b-1] = 1
    times = {}
    for i in range(int(input())) :
        x,c = input().split()
        times[int(x)] = c
    print(move())
