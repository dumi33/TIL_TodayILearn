def dfs(L,sum) :
    global ans
    if L > n : return # 날짜를 넘어가버리면
    if L == n :
        if sum > ans :
            ans = sum
    else :
        dfs(L+arr[L][0], sum+arr[L][1])
        dfs(L+1, sum)
        
        
        
    
                 
if __name__=="__main__" :
    n = int(input())
    arr = []
    for i in range(n):
        d,c = map(int,input().split()) # day, cost
        arr.append((d,c))
    ans = 0
    dfs(0,0)
    print(ans)
