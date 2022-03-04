# 왼쪽, 오른쪽, 안놓는 경우 생각
# 음수가 나올경우 동일한 숫자로 양수로 나오므로 무시 

def dfs(L,sum) :
    if  L == n :
        if sum > 0 :
            ans.add(sum)
    else :
        dfs(L+1, sum + nums[L]) # 왼쪽 
        dfs(L+1, sum - nums[L]) # 오른쪽
        dfs(L+1, sum) # 안놓음


if __name__ == "__main__" :
    n = int(input())
    ans = set()
    nums = list(map(int,input().split()))
    dfs(0,0) # level, sum
    print(sum(nums) - len(ans) )
    
