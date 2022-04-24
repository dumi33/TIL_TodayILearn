def dfs(L) :
    global cnt
    if L == m : # m까지 다 채우면
        cnt+=1
        for i in res :
            print(i,end=' ')
        print()
    else :
        for i in range(1,n+1) : # for 문을 돌며 숫자를 채우기 
            res[L] = i
            dfs(L+1)
        
    
if __name__=="__main__" :
    cnt = 0 
    n,m = map(int,input().split())
    res = [0] * (m) # m 만큼만 있으면 된다. 
    dfs(0)
    print(cnt)
