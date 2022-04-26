def dfs(L,val) :
    global ans
    if L == k :
        if (sum(res)%m) == 0 :
            ans+=1
    else :
        for i in arr : # 배열을 돌면서 
            if i > val : 
                res[L] = i # 크다면 해당 숫자를 답에 넣는다. 
                dfs(L+1,i)
                 
if __name__=="__main__" :
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    m = int(input())
    ans = 0
    res = [0]*k
    dfs(0,0)
    print(ans)
