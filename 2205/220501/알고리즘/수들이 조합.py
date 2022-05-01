def dfs(L,V) :
    global ans 
    if L == m :
        ans+=1
        for i in res :
            print(i,end=' ')
        print()
    else :
        for j in range(V+1,n+1) :# 뒤에 저장한 값 다음부터만 for문을 돈다. 
            res[L] = j
            dfs(L+1,j)
    
    
if __name__=="__main__" :
    n,m = map(int,input().split())
    ans = 0
    res = [0]*m

    dfs(0,0)
    print(ans)
