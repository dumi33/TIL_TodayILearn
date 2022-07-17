dx = [1,0,-1,0] 
dy = [0,-1,0,1]


        
if __name__=="__main__" :
    r,c,t = map(int,input().split())
    mp = [list(map(int,input().split())) for i in range(r)]
    
    
    for i in range(r) :
        if mp[i][0] == -1 : 
            air = (i,i+1)
            break
    
    for _ in range(t) :

        new = [[0]*c for i in range(r)]
        # 확산 
        for i in range(r) :
            for j in range(c) :
                if mp[i][j] >= 5 :
                    tmp = mp[i][j]//5
                    cnt = 0
                    for k in range(4) :
                        x,y = i+dx[k], j + dy[k]
                        if 0<=x <r and 0<=y<c and mp[x][y] != -1  : 
                            new[x][y] += tmp
                            cnt +=1 
                    mp[i][j] = mp[i][j] - (tmp*cnt)
        for i in range(r) :
            for j in range(c) :
                mp[i][j] += new[i][j]
                
        # 공기청정기 
        
        # 위쪽 [반시계]
        
        # 오른쪽으로 
        tmp = mp[air[0]][c-1]
        for i in range(c-1, 1,-1) :
            mp[air[0]][i] = mp[air[0]][i-1]
        mp[air[0]][1] = 0 
        
        # 위쪽으로 
        tmp2 = mp[0][c-1]
        for i in range(air[0]-1) :
            mp[i][c-1] = mp[i+1][c-1]
        mp[air[0]-1][c-1] = tmp
        
        # 왼쪽으로 
        tmp = mp[0][0]
        for i in range(c-1) :
            mp[0][i] = mp[0][i+1]
        mp[0][c-2] = tmp2 
        
        # 아래쪽으로 
        for i in range(air[0]-2,0,-1) :
            mp[i+1][0] = mp[i][0]
        mp[1][0] =tmp
        
        
        
        # 공기청정기의 아래쪽 
        
        tmp = mp[air[1]][c-1]
        for i in range(c-2,0,-1) :
            mp[air[1]][i+1] = mp[air[1]][i]
        
        tmp2 = mp[r-1][c-1]
        for i in range(r-1,air[1],-1) :
             mp[i][c-1] = mp[i-1][c-1]
        mp[air[1]+1][c-1] = tmp
        
        
        tmp = mp[r-1][0]
        for i in range(c-1) :
            mp[r-1][i] = mp[r-1][i+1]
        mp[r-1][c-2] = tmp2
        
        for i in range(air[1]+1, r-1) :
            mp[i][0] = mp[i+1][0]
        mp[air[1]][1] = 0
        mp[r-2][0] = tmp
        
    ans = sum([sum(mp[i]) for i in range(r)])
    print(ans+2)
