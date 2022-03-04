def dfs(L,sum) :
    global cnt
    if sum > T : return
    if L == k :
        if sum == T : cnt +=1 
    else :
        for i in range(nums[L][1]+1) : # 있는 동전의 개수를 돌면서 
            dfs(L+1, sum+ (nums[L][0]*i))

if __name__ == "__main__" :
    cnt = 0
    T = int(input())
    k = int(input())
    nums = []
    for i in range(k) :
        val,count = map(int,input().split())
        nums.append((val,count))
    dfs(0,0)
    print(cnt)
