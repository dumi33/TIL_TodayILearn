def dfs(L,sum,tsum) :
    global ans
    if sum > c : return 
    if (total - tsum) + sum < ans : return   
    if L == n :
        if sum > ans :
            ans = sum
    else :
        dfs(L+1, sum + arr[L],tsum+arr[L]) # L번째 바둑이 태우기
        dfs(L+1, sum ,tsum+arr[L]) # L번째 바둑이 안태우기
        
    
if __name__=="__main__" : 
    c,n = map(int,input().split())
    arr = []
    ans = 0
    for i in range(n) :
        temp = int(input())
        arr.append(temp)
    total = sum(arr)
    dfs(0,0,0)
    print(ans)
