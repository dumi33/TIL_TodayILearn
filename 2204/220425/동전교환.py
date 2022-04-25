def dfs(L,sum) :
    global ans
    if L > ans : return # 동전의 개수가 최소보다 클경우 
    if sum > total : return  # 총 합이 금액보다 커질경우 
    if sum == total :
        if L < ans :
            ans = L
    else :
        for i in range(n) :
            dfs(L+1,  sum+arr[i])
        
                 
if __name__=="__main__" :
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    total = int(input())
    ans = sys.maxsize
    dfs(0,0)
    print(ans)
