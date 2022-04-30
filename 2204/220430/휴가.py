def dfs(L, sum) :
    global ans
    if L > n : return 
    if L == n :
        if sum > ans : ans = sum
    else :
        dfs(L+arr[L][0], sum+arr[L][1]) # 해당 상담을 한 경우
        dfs(L+1, sum) # 상담을 안한경우, 날짜만 지나간다
        
    
            
if __name__=="__main__" :
    n = int(input())
    arr = []
    ans = 0 # 최대 이익
    for i in range(n) :
        a,b = map(int,input().split())
        arr.append((a,b))
    dfs(0,0)
    print(ans)
