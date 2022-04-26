def dfs(L,val) :
    global ans 
    if L==m :
        ans+=1
        for i in res :
            print(i,end=' ')
        print()
    else :
        for i in range(1,n+1) :
            if i > val :
                res[L] = i 
                dfs(L+1, i)
    
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    ans = 0
    res = [0]*m
    dfs(0,0)
    print(ans)
