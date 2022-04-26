def dfs(L,sum,time) :
    global ans
    if time > m : return 
    if L == n :
        if sum > ans :
            ans = sum
    else :
        dfs(L+1, sum+arr[L][0],time+arr[L][1]) # 해당 문제를 풀었을 때 
        dfs(L+1, sum,time) # 해당 문제를 풀지않았을 때 
        
        
    
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    arr = []
    for i in range(n) :
        a,b = map(int,input().split())
        arr.append((a,b))
    ans = 0
    dfs(0,0,0) #  level, score, time 
    print(ans)
