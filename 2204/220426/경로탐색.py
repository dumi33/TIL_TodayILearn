def dfs(v) :
    global ans
    if v == n :
        ans+=1
    else :
        for i in range(1,n+1) :
            if ch[i]==0 and g[v][i] == 1:
                ch[i] = 1 
                dfs(i)
                ch[i] = 0
        
     
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    g = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1) # 출석배열은 이차원 배열일 필요 없음 
    for i in range(m) :
        a,b = map(int,input().split())
        g[a][b] = 1 
    ans = 0
    ch[1] = 1 # 처음부터 1 들림 
    dfs(1)
    print(ans)
