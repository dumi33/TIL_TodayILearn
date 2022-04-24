def dfs(L, sum) :
    global ans
    if L == m :
        ans+=1
        for i in arr :
            print(i,end= ' ')
        print()
    else :
        for i in range(1,n+1) :
            if ch[i] == 0 :
                ch[i] = 1 
                arr[L] = i
                dfs(L+1, sum+i)
                ch[i] = 0
                
                
if __name__=="__main__" :
    n,m = map(int,input().split())
    arr = [0] * m
    ch = [0] * (n+1)
    ans = 0
    dfs(0,0)
    print(ans)
