def dfs(L) :
    global ans
    if L==m:
        ans+=1
        for i in res :
            print(i, end=' ')
        print()
    else : 
        for i in range(1,n+1) :
            if ch[i] == 0 :
                ch[i] = 1 # i를 썻어요 
                res[L] = i #  rewrite 됨  
                dfs(L+1)
                ch[i] = 0 # 이제 i 안써요 
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    res = [0] * m
    ans = 0 
    ch = [0] * (n+1)
    dfs(0)
    print(ans)
