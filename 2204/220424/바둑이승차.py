def dfs(L, sum ,tsum) :
    global ans
    if sum > c : return # 무게를 넘었다면
    if  total - tsum + sum < ans : return # 나머지 다 태워도 ans보다 가볍다면
    if L == n:
        if sum > ans :
            ans = sum
    else :
        dfs(L+1, sum + arr[L], tsum + arr[L]) # 태운다면
        dfs(L+1, sum , tsum + arr[L]) # 태우지않는다면
        
    
if __name__=="__main__" :
    c,n = map(int,input().split())
    arr = []
    ans = 0
    for i in range(n) :
        tmp = int(input())
        arr.append(tmp)
    total = sum(arr)
    dfs(0,0,0)
    print(ans)
