def dfs(L,s) :
    global ans
    if L == k :
        total = sum(res)
        if total % m == 0 :
            ans+=1
    else :
        for i in range(0,n) :
            if arr[i] > s:
                res[L] = arr[i]
                dfs(L+1, arr[i])
        
                 
if __name__=="__main__" :
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    m = int(input())
    res = [0]*(k)
    ans = 0
    dfs(0,0)
    print(ans)
