def dfs(day,pay) :
    global ans 
    if day > n : return 
    if day == (n) :
        ans = max(ans,pay)
        return 
    else :
        # 오늘 (day)의 상담을 안한다.
        dfs(day+1, pay)
        # 오늘 (day)의 상담을 한다. 
        dfs(day+arr[day][0],pay + arr[day][1])


if __name__=="__main__" :
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    
    dfs(0,0)
    print(ans)
