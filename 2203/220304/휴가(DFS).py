def dfs(day, money) :
    global profit 
    if day > n : return 
    if day == n :
        if profit < money :
            profit = money
    else :
        dfs(day+nums[day][0], money+nums[day][1]) # level으로 하는것이 아니라 day로 올려준다. 
        dfs(day+1,money)


if __name__ == "__main__" :
    n = int(input())
    nums = []
    profit = 0
    for i in range(n) :
        day,money = map(int,input().split())    
        nums.append((day,money))
    dfs(0,0) # day, money
    print(profit)
