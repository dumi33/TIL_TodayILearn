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
        
        for i in range(r) :
            for j in range(c) :
                if mp[i][j] >=5 :
                    each = mp[i][j]//5
                    cnt = 0
                    for k in range(4) :
                        x,y = i +dx[k], j +dy[k]
                        if 0<=x<r and 0<=y<c and mp[x][y] !=-1 :
                            new[x][y] += each 
                            cnt +=1 
                    mp[i][j] = mp[i][j] - (each*cnt)
        for i in range(r) :
            for j in range(c) :
                if new[i][j] :
                    mp[i][j] += new[i][j] 

        # 위쪽 
        tmp = mp[air[0]][c-1]
        for i in range(c-2,0,-1) :
            mp[air[0]][i+1] = mp[air[0]][i]
        mp[air[0]][1] = 0
        
        tmp2 = mp[0][c-1]
        for i in range(1,air[0]) :
            mp[i-1][c-1] = mp[i][c-1]
        mp[air[0]-1][c-1] = tmp
        
        tmp = mp[0][0]
        for i in range(1,c-1) :
            mp[0][i-1] = mp[0][i]
        mp[0][c-2] = tmp2
        
        for i in range(air[0]-2,0,-1) :
            mp[i+1][0] = mp[i][0]
        mp[1][0] = tmp
        
        # 아래쪽 
        tmp = mp[air[1]][c-1]
        for i in range(c-2,0,-1) :
            mp[air[1]][i+1] = mp[air[1]][i]
        mp[air[1]][1] = 0
        
        tmp2 = mp[r-1][c-1]
        for i in range(r-2,air[1],-1) :
            mp[i+1][c-1] = mp[i][c-1]
        mp[air[1]+1][c-1] = tmp
        
        tmp = mp[r-1][0]
        for i in range(1,c-1) :
            mp[r-1][i-1] = mp[r-1][i]
        mp[r-1][c-2] = tmp2
        
        for i in range(air[1]+2,r-1) :
            mp[i-1][0] = mp[i][0]
        mp[r-2][0] = tmp
        
    ans = sum([sum(mp[i]) for i in range(r)])
    print(ans+2)
