import sys
def dfs(L,sum) :
    if L == n :
        if sum == total-sum : # sum과 나머지가 같다면
            print("YES")
            sys.exit(0) # 종료
        else :
            return 
    if sum > (total // 2) : # cut edge
        return 
    else :
        dfs(L+1, sum+arr[L]) # 더한다면
        dfs(L+1, sum) # 더하지않는다면


if __name__ == "__main__" :
    n = int(input())
    arr = list(map(int,input().split()))
    total = sum(arr)
    dfs(0,0)
    print("NO") # sys.exit(0)을 실행하지않고 여기로 왔다는 것은 없다는 의미
