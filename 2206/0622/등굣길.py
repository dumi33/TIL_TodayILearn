def solution(m, n, puddles):
    answer = 0
    mp = [[0]*(m+1) for i in  range(n+1)]
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if i==1 and j== 1 :
                mp[i][j] = 1
            elif [j,i] not in puddles :
                mp[i][j] = mp[i-1][j] + mp[i][j-1]
    
    return mp[n][m] % 1000000007
