def dfs(L) :
    global ans
    if L == m :
        ans+=1
        for i in res :
            print(i,end=' ')
        print()
    else :
        for i in range(1,n+1) :
            res[L] = i # 덮어씌운다
            dfs(L+1)
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    res = [0] * m
    ans = 0 # 개수 
    dfs(0)
    print(ans)
