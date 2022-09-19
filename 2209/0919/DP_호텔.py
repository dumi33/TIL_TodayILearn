if __name__=="__main__" :
    c,n = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans  = int(1e9)
    dp = [int(1e9)]*(c+100)
    dp[0] = 0
    for cost,custo in arr :
        for i in range(custo,len(dp)) :
            dp[i] = min(dp[i-custo]+cost,dp[i])
            if i >=c : ans = min(ans,dp[i])
    print(ans)
