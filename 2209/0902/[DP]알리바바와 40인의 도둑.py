if __name__=="__main__" :
    n = int(input())
    mp = [list(map(int,input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    dy[0][0] = mp[0][0]
    
    # 가장 자리 
    for i in range(1,n) :
        dy[0][i] = mp[0][i] + dy[0][i-1]
        dy[i][0] = mp[i][0] + dy[i-1][0]
    
    for i in range(1,n) :
        for j in range(1,n) :
            if dy[i][j] == 0 :
                dy[i][j] = min(dy[i][j-1], dy[i-1][j]) + mp[i][j]
    
    print(dy[n-1][n-1])
