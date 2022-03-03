def dfs(L,sum,time) :
    global max_score
    if time > m :
        return 
    if L == n :
        if sum > max_score :
            max_score = sum
    else :
        dfs(L+1, sum+nums[L][0] ,time+nums[L][1] )  
        dfs(L+1, sum ,time)  

if __name__ == "__main__" :
    n,m = map(int,input().split())
    nums = []
    max_score = 0 # 최대점수 
    for i in range(n) :
        score,time = map(int,input().split())
        nums.append((score,time))
    dfs(0,0,0) # level , sum , time
    print(max_score)
