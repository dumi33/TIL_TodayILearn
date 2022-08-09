from collections import deque
from itertools import combinations as c 

dx = [0,1,0,-1]
dy = [1,0,-1,0]

if __name__=="__main__" :
    n,q = map(int,input().split())
    board_size = 2**n
    mp = [list(map(int,input().split())) for i in range(board_size)]
    List= list(map(int,input().split()))
    
    for L in List : # q번 반복 
        r_size = 2**L
        new = [[0]*board_size for i in range(board_size)]
        
        # 90도로 회전 
        for x in range(0, board_size, r_size) :
            for y in range(0, board_size, r_size) :
                for i in range(r_size) :
                    for j in range(r_size) :
                        new[x+j][y+r_size-1-i] = mp[x+i][y+j]
        
        mp = new 
        melt_list = []
        for i in range(board_size) :
            for j in range(board_size) :
                ice = 0
                for dir in range(4) :
                    nx,ny= i + dx[dir], j + dy[dir]
                    if 0<=nx<board_size and 0<=ny<board_size and mp[nx][ny]>0 :
                        ice+=1 
                if ice < 3 and mp[i][j] >0 :
                    melt_list.append([i,j])
        
        for x,y in melt_list :
            mp[x][y] -=1 
            
            
    vis = [[0]*board_size for i in range(board_size)]
    max_ice = 0
    
    for i in range(board_size) :
        for j in range(board_size) :
            if mp[i][j] > 0 and vis[i][j] == 0 :
                ice_cnt = 0
                d = deque([[i,j]])
                vis[i][j] =1 
                
                while d :
                    x,y = d.popleft()
                    ice_cnt+=1 
                    for dir in range(4) :
                        nx,ny= dx[dir]+x , y + dy[dir]
                        if 0<=nx<board_size and 0<=ny<board_size and mp[nx][ny] >0 and vis[nx][ny]==0 :
                            vis[nx][ny] =1 
                            d.append([nx,ny])
                            
                max_ice = max(ice_cnt,max_ice)
    
    print(sum(sum(mp,[])))
    print(max_ice)
