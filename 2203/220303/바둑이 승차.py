def dfs(L,sum,tsum) :
    global ans
    if sum > c : return
    if (total - tsum) + sum < ans : # cut edge 
        return   
    if L == n : # 모든 바둑이들을 돌았들 때
        ans = max(ans,sum)
    else :
        dfs(L+1, sum+ch[L],tsum+ch[L])
        dfs(L+1, sum,tsum+ch[L])


if __name__ == "__main__" :
    c,n = map(int,input().split())
    ch = []
    for i in range(n) :
        ch.append(int(input()))
    total = sum(ch)
    ans = 0
    dfs(0,0,0) # level, sum ,tsum(더했건 더하지않았건 지나쳐온 무게들 ) 
    print(ans)
