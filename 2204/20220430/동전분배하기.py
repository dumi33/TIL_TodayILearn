import sys
def dfs(L) :
    global ans
    if L == n :
        cha = max(val) - min(val)
        if cha < ans : # 비교를 나중에하면 시간초과
            s = set()
            for i in val :
                s.add(i)
            if len(s) == 3 :
                ans = cha
    else :
        for i in range(3) :
            val[i] += arr[L]
            dfs(L+1)
            val[i] -= arr[L]
            
    
            
if __name__=="__main__" :
    n = int(input())
    arr = []
    val = [0]*3
    for i in range(n) :
        tmp = int(input())
        arr.append(tmp)
    ans = sys.maxsize # 차이의 최솟값 
    dfs(0)
    print(ans) 
