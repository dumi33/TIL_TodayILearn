dx = [1,0,-1,0]
dy = [0,-1,0,1]
            
            
if __name__=="__main__" :
    n = int(input())
    mp = [[0]*101 for i in range(101)]
    for i in range(n) :
        x,y,d,g = map(int,input().split())
        curve = [d] # 방향 
        for i in range(g) :
            tmp = []
            for j in curve[::-1] :
                tmp.append((j+1)%4)
            curve.extend(tmp)
        mp[x][y] = 1
        for dir in curve: # 방향대로 돌아다니면서 1을 표시 
            nx,ny = x + dx[dir] , y + dy[dir]
            mp[nx][ny] = 1 
            x,y = nx,ny
        
    cnt = 0
    for i in range(100) :
        for j in range(100) :
            if mp[i][j] : # 한칸이 모두 1로 둘러싸인 곳 찾기 
                if mp[i+1][j] and mp[i][j+1] and mp[i+1][j+1] :
                    cnt+=1 
    print(cnt)
