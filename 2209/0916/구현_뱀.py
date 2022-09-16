from collections import deque
from itertools import combinations as c 
import copy
from collections import defaultdict 
           
# 북 동 남 서     
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def changeDir(t) :
    global d 
    if ch_dir[t] =='D' :
        return (d+1) % 4
    else : 
        return  (d-1) % 4
def play() :
    global time , d
    # 뱀위 위치 
    mp[0][0] = 1
    snake = deque([[0,0]]) 
    while True :
        time +=1 
        x,y = snake[-1][0],snake[-1][1]
        nx,ny = x + dx[d], y + dy[d]

        if 0<=nx<n and 0<=ny<n and mp[nx][ny] != 1 :
            if mp[nx][ny] !=2 :
                sx,sy = snake.popleft()
                mp[sx][sy] = 0
            mp[nx][ny] = 1 
            snake.append([nx,ny])
        else :
            return time 
        if time in ch_dir :
            d = changeDir(time)
        
if __name__=="__main__" :
    n = int(input())
    k = int(input())
    mp = [[0]*n for _ in range(n)]
    
    # 사과 위치 저장 
    for i in range(k) :
        a,b = map(int,input().split())
        mp[a-1][b-1] = 2 
    
    l = int(input())
    ch_dir = {}
    for i in range(l) :
        a,b = input().split()
        ch_dir[int(a)] = b 
    time ,d = 0 ,1 
    print(play())
    
