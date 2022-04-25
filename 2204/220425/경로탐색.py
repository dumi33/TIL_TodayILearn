def dfs(v) :
    global cnt
    if v == n :
        cnt+=1
    else :
        for i in range(1,n+1) :
            if ch[i] == 0 and g[v][i] == 1 : # 왔었는지 확인 그리고 길이 있는지 확인 
                ch[i] = 1  #  이 길으로 갈거야 
                dfs(i)
                ch[i] = 0  #  다시 back할거야 
     
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    g = [[0]*(n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    for i in range(m) :
        a,b = map(int,input().split())
        g[a][b] = 1
    cnt = 0 
    ch[1] = 1
    dfs(1)
    print(cnt)
